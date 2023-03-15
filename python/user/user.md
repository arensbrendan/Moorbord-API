# User

[Add User](#add-user)<br>
[Remove User](#remove-user)<br>
[Get All Classes From Teachers](#get-all-classes-from-teachers)<br>
[Get All Teachers](#get-all-teachers)<br>

<br><br>
## Add User
[Back to the top](#user)
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

## Remove User
[Back to the top](#user)
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

## Get All Classes From Teachers
[Back to the top](#user)
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

## Get All Teachers
[Back to the top](#user)
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