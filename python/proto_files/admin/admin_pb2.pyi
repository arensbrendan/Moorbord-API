from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddClassReply(_message.Message):
    __slots__ = ["error", "message", "status_code"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    error: str
    message: str
    status_code: int
    def __init__(self, message: _Optional[str] = ..., error: _Optional[str] = ..., status_code: _Optional[int] = ...) -> None: ...

class AddClassRequest(_message.Message):
    __slots__ = ["class_name", "hour", "teacher_username"]
    CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
    HOUR_FIELD_NUMBER: _ClassVar[int]
    TEACHER_USERNAME_FIELD_NUMBER: _ClassVar[int]
    class_name: str
    hour: int
    teacher_username: str
    def __init__(self, teacher_username: _Optional[str] = ..., class_name: _Optional[str] = ..., hour: _Optional[int] = ...) -> None: ...

class AddUserReply(_message.Message):
    __slots__ = ["error", "message", "status_code"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    error: str
    message: str
    status_code: int
    def __init__(self, message: _Optional[str] = ..., error: _Optional[str] = ..., status_code: _Optional[int] = ...) -> None: ...

class AddUserRequest(_message.Message):
    __slots__ = ["email", "first_name", "last_name", "role_id", "user_password", "username"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    USER_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    first_name: str
    last_name: str
    role_id: int
    user_password: str
    username: str
    def __init__(self, username: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., user_password: _Optional[str] = ..., email: _Optional[str] = ..., role_id: _Optional[int] = ...) -> None: ...

class RemoveClassReply(_message.Message):
    __slots__ = ["error", "message", "status_code"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    error: str
    message: str
    status_code: int
    def __init__(self, message: _Optional[str] = ..., error: _Optional[str] = ..., status_code: _Optional[int] = ...) -> None: ...

class RemoveClassRequest(_message.Message):
    __slots__ = ["class_id"]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    class_id: int
    def __init__(self, class_id: _Optional[int] = ...) -> None: ...

class RemoveUserReply(_message.Message):
    __slots__ = ["error", "message", "status_code"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    error: str
    message: str
    status_code: int
    def __init__(self, message: _Optional[str] = ..., error: _Optional[str] = ..., status_code: _Optional[int] = ...) -> None: ...

class RemoveUserRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...
