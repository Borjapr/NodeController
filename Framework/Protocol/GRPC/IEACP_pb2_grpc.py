# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import IEACP_pb2 as IEACP__pb2


class AgentStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetVersion = channel.unary_unary(
        '/Agent/GetVersion',
        request_serializer=IEACP__pb2.MsgNull.SerializeToString,
        response_deserializer=IEACP__pb2.MsgVersion.FromString,
        )
    self.Terminate = channel.unary_unary(
        '/Agent/Terminate',
        request_serializer=IEACP__pb2.MsgNull.SerializeToString,
        response_deserializer=IEACP__pb2.MsgNull.FromString,
        )
    self.Start = channel.unary_unary(
        '/Agent/Start',
        request_serializer=IEACP__pb2.MsgNull.SerializeToString,
        response_deserializer=IEACP__pb2.MsgNull.FromString,
        )
    self.CreateAgent = channel.unary_unary(
        '/Agent/CreateAgent',
        request_serializer=IEACP__pb2.MsgCreateAgent.SerializeToString,
        response_deserializer=IEACP__pb2.MsgOK.FromString,
        )
    self.ModifyAgent = channel.unary_unary(
        '/Agent/ModifyAgent',
        request_serializer=IEACP__pb2.MsgCreateAgent.SerializeToString,
        response_deserializer=IEACP__pb2.MsgOK.FromString,
        )
    self.DeleteAgent = channel.unary_unary(
        '/Agent/DeleteAgent',
        request_serializer=IEACP__pb2.MsgNameAgent.SerializeToString,
        response_deserializer=IEACP__pb2.MsgOK.FromString,
        )
    self.ListAgent = channel.unary_unary(
        '/Agent/ListAgent',
        request_serializer=IEACP__pb2.MsgNull.SerializeToString,
        response_deserializer=IEACP__pb2.MsgAgents.FromString,
        )
    self.CreateOP = channel.unary_unary(
        '/Agent/CreateOP',
        request_serializer=IEACP__pb2.MsgCreateOP.SerializeToString,
        response_deserializer=IEACP__pb2.MsgOK.FromString,
        )
    self.ModifyOP = channel.unary_unary(
        '/Agent/ModifyOP',
        request_serializer=IEACP__pb2.MsgCreateOP.SerializeToString,
        response_deserializer=IEACP__pb2.MsgOK.FromString,
        )
    self.StartAgents = channel.unary_unary(
        '/Agent/StartAgents',
        request_serializer=IEACP__pb2.MsgNull.SerializeToString,
        response_deserializer=IEACP__pb2.MsgNull.FromString,
        )
    self.StopAgents = channel.unary_unary(
        '/Agent/StopAgents',
        request_serializer=IEACP__pb2.MsgNull.SerializeToString,
        response_deserializer=IEACP__pb2.MsgNull.FromString,
        )
    self.OP_List = channel.unary_unary(
        '/Agent/OP_List',
        request_serializer=IEACP__pb2.MsgNull.SerializeToString,
        response_deserializer=IEACP__pb2.MsgOPs.FromString,
        )
    self.DeleteOP = channel.unary_unary(
        '/Agent/DeleteOP',
        request_serializer=IEACP__pb2.MsgNameAgentOP.SerializeToString,
        response_deserializer=IEACP__pb2.MsgOK.FromString,
        )
    self.EnableOP = channel.unary_unary(
        '/Agent/EnableOP',
        request_serializer=IEACP__pb2.MsgNameAgentOP.SerializeToString,
        response_deserializer=IEACP__pb2.MsgOK.FromString,
        )
    self.DisableOP = channel.unary_unary(
        '/Agent/DisableOP',
        request_serializer=IEACP__pb2.MsgNameAgentOP.SerializeToString,
        response_deserializer=IEACP__pb2.MsgOK.FromString,
        )


class AgentServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetVersion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Terminate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Start(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateAgent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModifyAgent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAgent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListAgent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateOP(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModifyOP(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartAgents(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopAgents(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def OP_List(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteOP(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EnableOP(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DisableOP(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AgentServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetVersion': grpc.unary_unary_rpc_method_handler(
          servicer.GetVersion,
          request_deserializer=IEACP__pb2.MsgNull.FromString,
          response_serializer=IEACP__pb2.MsgVersion.SerializeToString,
      ),
      'Terminate': grpc.unary_unary_rpc_method_handler(
          servicer.Terminate,
          request_deserializer=IEACP__pb2.MsgNull.FromString,
          response_serializer=IEACP__pb2.MsgNull.SerializeToString,
      ),
      'Start': grpc.unary_unary_rpc_method_handler(
          servicer.Start,
          request_deserializer=IEACP__pb2.MsgNull.FromString,
          response_serializer=IEACP__pb2.MsgNull.SerializeToString,
      ),
      'CreateAgent': grpc.unary_unary_rpc_method_handler(
          servicer.CreateAgent,
          request_deserializer=IEACP__pb2.MsgCreateAgent.FromString,
          response_serializer=IEACP__pb2.MsgOK.SerializeToString,
      ),
      'ModifyAgent': grpc.unary_unary_rpc_method_handler(
          servicer.ModifyAgent,
          request_deserializer=IEACP__pb2.MsgCreateAgent.FromString,
          response_serializer=IEACP__pb2.MsgOK.SerializeToString,
      ),
      'DeleteAgent': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAgent,
          request_deserializer=IEACP__pb2.MsgNameAgent.FromString,
          response_serializer=IEACP__pb2.MsgOK.SerializeToString,
      ),
      'ListAgent': grpc.unary_unary_rpc_method_handler(
          servicer.ListAgent,
          request_deserializer=IEACP__pb2.MsgNull.FromString,
          response_serializer=IEACP__pb2.MsgAgents.SerializeToString,
      ),
      'CreateOP': grpc.unary_unary_rpc_method_handler(
          servicer.CreateOP,
          request_deserializer=IEACP__pb2.MsgCreateOP.FromString,
          response_serializer=IEACP__pb2.MsgOK.SerializeToString,
      ),
      'ModifyOP': grpc.unary_unary_rpc_method_handler(
          servicer.ModifyOP,
          request_deserializer=IEACP__pb2.MsgCreateOP.FromString,
          response_serializer=IEACP__pb2.MsgOK.SerializeToString,
      ),
      'StartAgents': grpc.unary_unary_rpc_method_handler(
          servicer.StartAgents,
          request_deserializer=IEACP__pb2.MsgNull.FromString,
          response_serializer=IEACP__pb2.MsgNull.SerializeToString,
      ),
      'StopAgents': grpc.unary_unary_rpc_method_handler(
          servicer.StopAgents,
          request_deserializer=IEACP__pb2.MsgNull.FromString,
          response_serializer=IEACP__pb2.MsgNull.SerializeToString,
      ),
      'OP_List': grpc.unary_unary_rpc_method_handler(
          servicer.OP_List,
          request_deserializer=IEACP__pb2.MsgNull.FromString,
          response_serializer=IEACP__pb2.MsgOPs.SerializeToString,
      ),
      'DeleteOP': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteOP,
          request_deserializer=IEACP__pb2.MsgNameAgentOP.FromString,
          response_serializer=IEACP__pb2.MsgOK.SerializeToString,
      ),
      'EnableOP': grpc.unary_unary_rpc_method_handler(
          servicer.EnableOP,
          request_deserializer=IEACP__pb2.MsgNameAgentOP.FromString,
          response_serializer=IEACP__pb2.MsgOK.SerializeToString,
      ),
      'DisableOP': grpc.unary_unary_rpc_method_handler(
          servicer.DisableOP,
          request_deserializer=IEACP__pb2.MsgNameAgentOP.FromString,
          response_serializer=IEACP__pb2.MsgOK.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Agent', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
