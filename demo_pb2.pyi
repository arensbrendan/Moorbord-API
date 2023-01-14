from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseReply(_message.Message):
    __slots__ = ["lastname"]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    lastname: str
    def __init__(self, lastname: _Optional[str] = ...) -> None: ...

class DatabaseRequest(_message.Message):
    __slots__ = ["firstname"]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    firstname: str
    def __init__(self, firstname: _Optional[str] = ...) -> None: ...

class GoodbyeReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class GoodbyeRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HelloReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class HelloRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class InfoReply(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class InfoRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class InsultReply(_message.Message):
    __slots__ = ["insult"]
    INSULT_FIELD_NUMBER: _ClassVar[int]
    insult: str
    def __init__(self, insult: _Optional[str] = ...) -> None: ...

class InsultRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
