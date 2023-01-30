import os
import smtplib
import ssl
from concurrent import futures
from email.mime.text import MIMEText

import grpc
from dotenv import load_dotenv

from python.proto_files.email import email_pb2
from python.proto_files.email import email_pb2_grpc
from python.working_files.decorators import database_connect

load_dotenv()
password = os.getenv("EMAIL_PASSWORD")
context = ssl.create_default_context()


def send_email(email, message):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(os.getenv("MOREBOARD_EMAIL"), os.getenv("EMAIL_PASSWORD"))
        server.sendmail(os.getenv("MOREBOARD_EMAIL"), email, message.as_string())
        print("Email sent")


class EmailCall(email_pb2_grpc.EmailCallServicer):
    @database_connect
    def EmailUser(self, db, request, context):
        username, email_body = request.username, request.email_body
        try:
            sql = "SELECT email FROM user WHERE username = '%s'" % username
            db.execute(sql)
            email = db.fetchall()
            if email:
                email = email[0]["email"]
                message = MIMEText(email_body)
                message['Subject'] = "Moreboard Notification"
                message['From'] = os.getenv("MOREBOARD_EMAIL")
                message['To'] = email
                try:
                    send_email(email, message)
                    return email_pb2.EmailUserReply(message="Email Sent", status_code=200)
                except Exception as e:
                    raise e
            else:
                raise ValueError("That username is invalid")
        except ValueError as v:
            return email_pb2.EmailUserReply(error=str(v), status_code=404)
        except Exception as e:
            return email_pb2.EmailUserReply(error=str(e), status_code=500)


def serve():
    # Generic Service Stuff
    port = '4'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    email_pb2_grpc.add_EmailCallServicer_to_server(EmailCall(), server)
    server.add_insecure_port(os.getenv("IP") + ':' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
