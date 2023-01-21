from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LoginReply(_message.Message):
    __slots__ = ["correct"]
    CORRECT_FIELD_NUMBER: _ClassVar[int]
    correct: bool
    def __init__(self, correct: bool = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ["body", "password", "username"]
    BODY_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    body: str
    password: str
    username: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., body: _Optional[str] = ...) -> None: ...
