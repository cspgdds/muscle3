# @generated by generate_proto_mypy_stubs.py.  Do not edit!
from abc import (
    ABCMeta as abc___ABCMeta,
    abstractmethod as abc___abstractmethod,
)

from concurrent.futures import (
    Future as concurrent___futures___Future,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.timestamp_pb2 import (
    Timestamp as google___protobuf___timestamp_pb2___Timestamp,
)

from typing import (
    Any as typing___Any,
    Callable as typing___Callable,
    Iterable as typing___Iterable,
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    cast as typing___cast,
)


class ResultStatus(int):
    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> int: ...
    @classmethod
    def keys(cls) -> typing___List[str]: ...
    @classmethod
    def values(cls) -> typing___List[int]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[str, int]]: ...
RESULT_STATUS_SUCCESS = typing___cast(ResultStatus, 0)
RESULT_STATUS_ERROR = typing___cast(ResultStatus, 1)
RESULT_STATUS_PENDING = typing___cast(ResultStatus, 2)

class Operator(int):
    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> int: ...
    @classmethod
    def keys(cls) -> typing___List[str]: ...
    @classmethod
    def values(cls) -> typing___List[int]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[str, int]]: ...
OPERATOR_NONE = typing___cast(Operator, 0)
OPERATOR_F_INIT = typing___cast(Operator, 1)
OPERATOR_O_I = typing___cast(Operator, 2)
OPERATOR_S = typing___cast(Operator, 3)
OPERATOR_B = typing___cast(Operator, 4)
OPERATOR_O_F = typing___cast(Operator, 5)
OPERATOR_MAP = typing___cast(Operator, 6)

class LogLevel(int):
    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> int: ...
    @classmethod
    def keys(cls) -> typing___List[str]: ...
    @classmethod
    def values(cls) -> typing___List[int]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[str, int]]: ...
LOG_LEVEL_DEBUG = typing___cast(LogLevel, 0)
LOG_LEVEL_INFO = typing___cast(LogLevel, 1)
LOG_LEVEL_PROFILE = typing___cast(LogLevel, 2)
LOG_LEVEL_WARNING = typing___cast(LogLevel, 3)
LOG_LEVEL_ERROR = typing___cast(LogLevel, 4)
LOG_LEVEL_CRITICAL = typing___cast(LogLevel, 5)

class LogMessage(google___protobuf___message___Message):
    instance_id = ... # type: typing___Text
    operator = ... # type: Operator
    level = ... # type: LogLevel
    text = ... # type: typing___Text

    @property
    def timestamp(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

    def __init__(self,
        instance_id : typing___Optional[typing___Text] = None,
        operator : typing___Optional[Operator] = None,
        timestamp : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        level : typing___Optional[LogLevel] = None,
        text : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LogMessage: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class LogResult(google___protobuf___message___Message):

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LogResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class Port(google___protobuf___message___Message):
    name = ... # type: typing___Text
    operator = ... # type: Operator

    def __init__(self,
        name : typing___Optional[typing___Text] = None,
        operator : typing___Optional[Operator] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Port: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class RegistrationRequest(google___protobuf___message___Message):
    instance_name = ... # type: typing___Text
    network_locations = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    @property
    def ports(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Port]: ...

    def __init__(self,
        instance_name : typing___Optional[typing___Text] = None,
        network_locations : typing___Optional[typing___Iterable[typing___Text]] = None,
        ports : typing___Optional[typing___Iterable[Port]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RegistrationRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class RegistrationResult(google___protobuf___message___Message):
    status = ... # type: ResultStatus
    error_message = ... # type: typing___Text

    def __init__(self,
        status : typing___Optional[ResultStatus] = None,
        error_message : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RegistrationResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class Conduit(google___protobuf___message___Message):
    sender = ... # type: typing___Text
    receiver = ... # type: typing___Text

    def __init__(self,
        sender : typing___Optional[typing___Text] = None,
        receiver : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Conduit: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class PeerRequest(google___protobuf___message___Message):
    instance_name = ... # type: typing___Text

    def __init__(self,
        instance_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PeerRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class PeerResult(google___protobuf___message___Message):
    class PeerDimensions(google___protobuf___message___Message):
        peer_name = ... # type: typing___Text
        dimensions = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]

        def __init__(self,
            peer_name : typing___Optional[typing___Text] = None,
            dimensions : typing___Optional[typing___Iterable[int]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> PeerResult.PeerDimensions: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

    class PeerLocations(google___protobuf___message___Message):
        instance_name = ... # type: typing___Text
        locations = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        def __init__(self,
            instance_name : typing___Optional[typing___Text] = None,
            locations : typing___Optional[typing___Iterable[typing___Text]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> PeerResult.PeerLocations: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

    status = ... # type: ResultStatus
    error_message = ... # type: typing___Text

    @property
    def conduits(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Conduit]: ...

    @property
    def peer_dimensions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[PeerResult.PeerDimensions]: ...

    @property
    def peer_locations(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[PeerResult.PeerLocations]: ...

    def __init__(self,
        status : typing___Optional[ResultStatus] = None,
        error_message : typing___Optional[typing___Text] = None,
        conduits : typing___Optional[typing___Iterable[Conduit]] = None,
        peer_dimensions : typing___Optional[typing___Iterable[PeerResult.PeerDimensions]] = None,
        peer_locations : typing___Optional[typing___Iterable[PeerResult.PeerLocations]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PeerResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class MuscleManager(typing___Any, metaclass=abc___ABCMeta):
    @abc___abstractmethod
    def SubmitLogMessage(self,
        rpc_controller: typing___Any,
        request: LogMessage,
        done: typing___Optional[typing___Callable[[LogResult], None]],
    ) -> concurrent___futures___Future[LogResult]: ...
    @abc___abstractmethod
    def RegisterInstance(self,
        rpc_controller: typing___Any,
        request: RegistrationRequest,
        done: typing___Optional[typing___Callable[[RegistrationResult], None]],
    ) -> concurrent___futures___Future[RegistrationResult]: ...
    @abc___abstractmethod
    def RequestPeers(self,
        rpc_controller: typing___Any,
        request: PeerRequest,
        done: typing___Optional[typing___Callable[[PeerResult], None]],
    ) -> concurrent___futures___Future[PeerResult]: ...
class MuscleManager_Stub(MuscleManager):
    def __init__(self, rpc_channel: typing___Any) -> None: ...
    def SubmitLogMessage(self,
        rpc_controller: typing___Any,
        request: LogMessage,
        done: typing___Optional[typing___Callable[[LogResult], None]],
    ) -> concurrent___futures___Future[LogResult]: ...
    def RegisterInstance(self,
        rpc_controller: typing___Any,
        request: RegistrationRequest,
        done: typing___Optional[typing___Callable[[RegistrationResult], None]],
    ) -> concurrent___futures___Future[RegistrationResult]: ...
    def RequestPeers(self,
        rpc_controller: typing___Any,
        request: PeerRequest,
        done: typing___Optional[typing___Callable[[PeerResult], None]],
    ) -> concurrent___futures___Future[PeerResult]: ...