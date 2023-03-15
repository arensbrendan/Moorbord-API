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
