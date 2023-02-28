# Routes
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

### /api/generic/get_all_users_from_class
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
    "message": "array of user information for that class"
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
