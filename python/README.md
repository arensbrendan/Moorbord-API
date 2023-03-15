[Class](#class)<br>
[Generic](#generic)<br>
[Room](#Room)<br>
[Seating](#seating)<br>
[User](#room)

# Routes

## Class

### /api/class/add_class
### Expected Request<br><br>
```json
{
    "teacher_username": "teacher username",
    "class_name": "class name",
    "hour": "hour"
}
```
### <br>

| Variable         | Data Type | Required | Additional Validation                          |
|------------------|-----------|----------|------------------------------------------------|
| teacher_username | string    | True     | Must be a username ascribed to a teacher       |
| class_name       | string    | True     | No                                             |
| hour             | integer   | True     | Teacher must not have other class at this hour |


### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Class added"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

### /api/class/remove_class
### Expected Request<br><br>
```json
{
    "class_id": "class id"
}
```
### <br>

| Variable | Data Type | Required | Additional Validation                                              |
|----------|-----------|----------|--------------------------------------------------------------------|
| class_id | integer   | True     | No                                                                 |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Class Removed"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

### /api/class/get_all_users_from_class
### Expected Request<br><br>/api/class/get_all_users_from_class?class_id=5<br>

### <br>

| Variable | Data Type | Required | Additional Validation                                              |
|----------|-----------|----------|--------------------------------------------------------------------|
| class_id | integer   | True     | No                                                                 |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "array of user information for that class"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```


### /api/class/add_user_to_class
### Expected Request<br><br>
```json
{
    "class_id": "class id", 
    "user_id": "user id"
}
```
### <br>

| Variable | Data Type | Required | Additional Validation |
|----------|-----------|----------|-----------------------|
| class_id | integer   | True     | No                    |
| user_id  | integer   | True     | No                    |


### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "User has been added to that class"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

### /api/class/remove_user_from_class
### Expected Request<br><br>
```json
{
    "class_id": "class id", 
    "user_id": "user id"
}
```
### <br>

| Variable | Data Type | Required | Additional Validation |
|----------|-----------|----------|-----------------------|
| class_id | integer   | True     | No                    |
| user_id  | integer   | True     | No                    |


### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "User has been added to that class"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

### /api/class/get_all_chairs_from_class
### Expected Request<br><br>/api/class/get_all_chairs_from_class?class_id=6<br>

| Variable | Data Type | Required | Additional Validation |
|----------|-----------|----------|-----------------------|
| class_id | integer   | True     | No                    |


### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "array with all chairs in the provided class"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

### /api/class/get_all_classes
### Expected Request<br><br>/api/class/get_all_classes?user_id=59

| Variable | Data Type | Required | Additional Validation |
|----------|-----------|----------|-----------------------|

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "array of all classes"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## Generic

### /api/generic/login
### Expected Request <br><br>/api/generic/login?username=USERNAME&password=PASSWORD<br>

| Variable | Data Type | Required | Additional Validation |
|----------|-----------|----------|-----------------------|
| username | string    | True     | No                    |
| password | string    | True     | No                    |   

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "True|False"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

### /api/generic/email_user
### Expected Request<br><br>
```json
{
    "email_to": "List of emails",
    "email_subject": "Subject of the email",
    "email_body": "Body of the email"
}
```
### <br>

| Variable      | Data Type         | Required | Additional Validation |
|---------------|-------------------|----------|-----------------------|
| email_to      | array of integers | True     | No                    |
| email_subject | string            | True     | No                    |
| email_body    | string            | True     | No                    |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Email Sent"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## Room
### /api/room/add_room
### Expected Request<br><br>
```json
{
    "room_name": "Test",
    "room_width": 12,
    "room_length": 1925
}
```
### <br>

| Variable    | Data Type | Required | Additional Validation |
|-------------|-----------|----------|-----------------------|
| room_name   | string    | Yes      | No                    |
| room_width  | integer   | Yes      | No                    |
| room_length | integer   | Yes      | No                    |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Room added"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

### /api/room/remove_room
### Expected Request<br><br>
```json
{
    "room_id": 1
}
```
### <br>

| Variable | Data Type | Required | Additional Validation |
|----------|-----------|----------|-----------------------|
| room_id  | integer   | Yes      | No                    |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Room removed"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## Seating
### /api/seating/add_chairs_to_class
### Example Request<br><br>
```json
{
    "class_id": 6,
    "arrangement": [{
        "x": 10,
        "y": 30,
        "student_id": 2
    },
    {
        "x": 23,
        "y": 21,
        "student_id": 3
    }]
}
```
### <br>

| Variable    | Data Type        | Required | Additional Validation |
|-------------|------------------|----------|-----------------------|
| class_id    | integer          | Yes      | No                    |
| arrangement | array of objects | Yes      | No                    |

### Object inside of arrangement

| Variable   | Data Type | Required | Additional Validation |
|------------|-----------|----------|-----------------------|
| x          | integer   | Yes      | No                    |
| y          | integer   | Yes      | No                    |
| student_id | integer   | Yes      | No                    |


### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Chairs added"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

### /api/seating/remove_chair_from_seating_arrangement
### Example Request<br><br>
```json
{
    "chair_ids": [3, 4]
}
```
### <br>

| Variable  | Data Type         | Required | Additional Validation                                              |
|-----------|-------------------|----------|--------------------------------------------------------------------|
| chair_ids | array of integers | True     | No                                                                 |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Chairs Removed"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```


### /api/seating/get_student_from_chair
### Example Request:<br>
#### /api/seating/get_student_from_chair?chair_id=3
<br>

| Variable | Data Type | Required | Additional Validation                                              |
|----------|-----------|----------|--------------------------------------------------------------------|
| chair_id | integer   | True     | No                                                                 |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Student information pertaining to that chair"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## User

### /api/admin/add_user
### Expected Request<br><br>
```json
{
    "firstname": "firstname",
    "lastname": "lastname",
    "user_password": "password",
    "email": "email",
    "role": "role"
}
```
### <br>

| Variable      | Data Type | Required | Additional Validation                                              |
|---------------|-----------|----------|--------------------------------------------------------------------|
| firstname     | string    | True     | No                                                                 |
| lastname      | string    | True     | No                                                                 | 
| user_password | string    | True     | Minimum 8 characters.  At least one letter and at least one number |
| email         | string    | True     | Looks for something like something@something.something             |
| role          | integer   | True     | Looking for a valid role_id.  Currently that's something from 0-3  |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "User added"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

### /api/admin/remove_user
### Expected Request<br><br>
```json
{
    "user_id": "user id"
}
```
### <br>

| Variable      | Data Type | Required | Additional Validation                                              |
|---------------|-----------|----------|--------------------------------------------------------------------|
| firstname     | integer   | True     | No                                                                 |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "User Removed"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

### /api/generic/get_all_classes_from_teachers
### Expected Request<br><br>
```json
{
    "user_id": "user id"
}
```
### <br>

| Variable | Data Type | Required | Additional Validation                                              |
|----------|-----------|----------|--------------------------------------------------------------------|
| user_id  | integer   | True     | No                                                                 |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "a list of all the class data for the teacher"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

### /api/generic/get_all_teachers
### Expected Request<br><br>
```json
{
  
}
```
### <br>

| Variable | Data Type | Required | Additional Validation                                              |
|----------|-----------|----------|--------------------------------------------------------------------|

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "a list of all of the teachers"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```
