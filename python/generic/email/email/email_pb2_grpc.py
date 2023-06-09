# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import python.generic.email.email.email_pb2 as email__pb2


class EmailCallStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.EmailUser = channel.unary_unary(
                '/EmailCall/EmailUser',
                request_serializer=email__pb2.EmailUserRequest.SerializeToString,
                response_deserializer=email__pb2.EmailUserReply.FromString,
                )


class EmailCallServicer(object):
    """Missing associated documentation comment in .proto file."""

    def EmailUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EmailCallServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'EmailUser': grpc.unary_unary_rpc_method_handler(
                    servicer.EmailUser,
                    request_deserializer=email__pb2.EmailUserRequest.FromString,
                    response_serializer=email__pb2.EmailUserReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'EmailCall', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EmailCall(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def EmailUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EmailCall/EmailUser',
            email__pb2.EmailUserRequest.SerializeToString,
            email__pb2.EmailUserReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
