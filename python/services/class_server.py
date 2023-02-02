import grpc
from python.proto_files.class_files import class_pb2
from python.proto_files.class_files import class_pb2_grpc
from concurrent import futures
from dotenv import load_dotenv
import os
from python.working_files.decorators import database_connect

load_dotenv()


class ClassCall(class_pb2_grpc.ClassCallServicer):
    @database_connect
    def AddClass(self, db, request, context):
        teacher_username, class_name, hour = request.teacher_username, request.class_name, request.hour
        try:
            # Grab user_id from username
            sql = "SELECT user_id FROM user WHERE username = '%s'" % teacher_username
            db.execute(sql)
            user_id = db.fetchall()[0]

            # If valid id
            if user_id:
                # Check to see if that user is in fact a teacher
                sql = "SELECT teacher_id FROM teacher WHERE user_id = %s" % user_id["user_id"]
                db.execute(sql)
                teacher_id = db.fetchall()
                if not teacher_id:
                    raise ValueError("That user is not a teacher")

                # If user is a teacher
                else:
                    teacher_id = teacher_id[0]["teacher_id"]

                    # Make sure teacher is not already teaching at that hour
                    sql = "SELECT * FROM class WHERE hour = '%s' AND teacher_id = '%s'" % (hour, teacher_id)
                    db.execute(sql)
                    if db.fetchall():
                        raise ValueError("That teacher is already teaching a class at that hour!")

                    # If they have that hour free
                    else:
                        # Add class for that teacher
                        sql = "INSERT INTO class(teacher_id, class_name, hour) VALUES(%s, '%s', %s)" % (
                        teacher_id, class_name, hour)
                        db.execute(sql)
                        return class_pb2.RemoveClassReply(message="Class Created", status_code=200)
            else:
                raise ValueError("The username provided for the teacher does not exist")
        except ValueError as error:
            return class_pb2.RemoveClassReply(error=str(error), status_code=404)
        except Exception as error:
            return class_pb2.RemoveClassReply(error=str(error), status_code=400)

    @database_connect
    def RemoveClass(self, db, request, context):
        class_id = request.class_id
        try:
            # See if the class exists
            sql = "SELECT * FROM class WHERE class_id = '%s'" % class_id
            db.execute(sql)

            # If class exists
            if db.fetchall():
                # Delete class from student classes
                sql = "DELETE FROM student_classes WHERE class_id = '%s'" % class_id
                db.execute(sql)

                # Delete class from class table
                sql = "DELETE FROM class WHERE class_id = '%s'" % class_id
                db.execute(sql)
                return class_pb2.RemoveClassReply(message="Class has been removed", status_code=200)
            else:
                raise ValueError("That class does not exist")
        except ValueError as v:
            return class_pb2.RemoveClassReply(error=str(v), status_code=404)
        except Exception as error:
            return class_pb2.RemoveClassReply(error=str(error), status_code=400)

    @database_connect
    def AddUserToClass(self, db, request, context):
        class_id, username = request.class_id, request.username
        try:
            # Getting user id from username
            sql = "SELECT user_id FROM user WHERE username = '%s'" % username
            db.execute(sql)
            user_id = db.fetchall()

            # If it's valid
            if user_id:
                user_id = user_id[0]["user_id"]

                # Get student_id from user_id
                sql = "SELECT student_id FROM student WHERE user_id = %s" % user_id
                db.execute(sql)
                student_id = db.fetchall()
                if not student_id:
                    raise ValueError("That user is not a student")

                # If valid
                else:
                    # Check class validity
                    sql = "SELECT class_id FROM class WHERE class_id = %s" % class_id
                    db.execute(sql)
                    if not db.fetchall():
                        raise ValueError("That class does not exist")

                    # If valid, check to make sure hour isn't occupied by another class
                    # Start by getting hour for class provided
                    student_id = student_id[0]["student_id"]
                    grab_hour_for_class_id = "SELECT hour FROM class WHERE class_id = %s" % class_id
                    db.execute(grab_hour_for_class_id)
                    hour = db.fetchall()[0]["hour"]

                    # Now we grab all classes for that user
                    grab_all_classes_for_the_student = "SELECT * FROM student_classes WHERE student_id = %s" % student_id
                    db.execute(grab_all_classes_for_the_student)
                    classes = db.fetchall()
                    has_hour = False

                    # For each of those classes, we will check the hour against hour for class provided
                    for clas in classes:
                        grab_hour_for_class_id = "SELECT hour FROM class WHERE class_id = %s" % clas["class_id"]
                        db.execute(grab_hour_for_class_id)
                        class_hour = db.fetchall()[0]["hour"]
                        if class_hour == hour:
                            has_hour = True

                    # If hour occupied
                    if has_hour:
                        raise ValueError("That student already has a class at that hour!")
                    else:
                        # Finally run query
                        put_student_in_student_classes_table = "INSERT INTO student_classes VALUES(%s, %s)" % (student_id, class_id)
                        db.execute(put_student_in_student_classes_table)
                        return class_pb2.AddUserToClassReply(message="User has been added to class", status_code=200)
            else:
                raise ValueError("That username is not attached to a valid user")
        except ValueError as v:
            return class_pb2.AddUserToClassReply(error=str(v), status_code=404)
        except Exception as error:
            return class_pb2.AddUserToClassReply(error=str(error), status_code=400)

    @database_connect
    def RemoveUserFromClass(self, db, request, context):
        class_id, username = request.class_id, request.username
        try:
            # Grab user id from username
            sql = "SELECT user_id FROM user WHERE username = '%s'" % username
            db.execute(sql)
            user_id = db.fetchall()

            # If user_id exists
            if user_id:
                user_id = user_id[0]["user_id"]

                # Grab student_id from user_id
                sql = "SELECT student_id FROM student WHERE user_id = %s" % user_id
                db.execute(sql)
                student_id = db.fetchall()
                if not student_id:
                    raise ValueError("That user is not a student")

                # If user is a student
                else:
                    student_id = student_id[0]["student_id"]

                    # Make sure class is valid
                    sql = "SELECT class_id FROM class WHERE class_id = %s" % class_id
                    db.execute(sql)
                    if not db.fetchall():
                        raise ValueError("That class does not exist")

                    # If valid, remove user from that class
                    remove_user_from_table = "DELETE FROM student_classes WHERE student_id = %s" % student_id
                    db.execute(remove_user_from_table)
                    return class_pb2.AddUserToClassReply(message="User has been removed from the class", status_code=200)
        except ValueError as v:
            return class_pb2.AddUserToClassReply(error=str(v), status_code=404)
        except Exception as error:
            return class_pb2.AddUserToClassReply(error=str(error), status_code=400)



def serve():
    # General service setup
    port = '3'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    class_pb2_grpc.add_ClassCallServicer_to_server(ClassCall(), server)
    server.add_insecure_port(os.getenv("IP") + ':' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
