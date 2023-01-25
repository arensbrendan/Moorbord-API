# Routes
### /api/generic/login
### Expected Request <br><br>/api/generic/login?username=USERNAME&password=PASSWORD<br>

| Variable | Data Type | Required | Additional Validation |
|----------|-----------|----------|-----------------------|
| username | string    | True     | No                    |
| password | string    | True     | No                    |   

### <br>Exepected Response:<br>
#### Healthy Call
```json 
{
    "message": "True|False"
}
```
#### Unhealthy Call
```json 
{
    "error": error message
}
```


### /api/admin/add_user
### Expected Request<br><br>
```json
{
    "firstname": firstname,
    "lastname": lastname,
    "user_password": password,
    "email": email,
    "role": role
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

### <br>Exepected Response:<br>
#### Healthy Call
```json 
{
    "message": "User added"
}
```
#### Unhealthy Call
```json 
{
    "error": error message
}
```

### /api/admin/remove_user
### Expected Request<br><br>
```json
{
    "user_id": user id
}
```
### <br>

| Variable      | Data Type | Required | Additional Validation                                              |
|---------------|-----------|----------|--------------------------------------------------------------------|
| firstname     | integer   | True     | No                                                                 |

### <br>Exepected Response:<br>
#### Healthy Call
```json 
{
    "message": "User Removed"
}
```
#### Unhealthy Call
```json 
{
    "error": error message
}
```