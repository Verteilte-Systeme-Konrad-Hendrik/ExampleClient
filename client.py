import grpc
import orchestration_pb2 as orch_pb
import orchestration_pb2_grpc as orch_pb_grpc
from concurrent import futures
import sys

class ServerFacingClient(orch_pb_grpc.ServerFacingClientServicer):

    def NotifyRoundFinished(self, round_nr, context):
        print("Got example message")
        if round_nr.round != 0:
            results = node_stub.pullMessageForRound(round_nr)
            print("Got some messages")
            print(results.messages)

        else:
            print("Get test message!")

        return orch_pb.Empty()


port=int(sys.argv[1])

node_channel = grpc.insecure_channel("localhost:"+str(port))
node_stub = orch_pb_grpc.ClientCommunicationStub(node_channel)

client_info = node_stub.registerListener(orch_pb.Empty())

my_port = client_info.port

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
orch_pb_grpc.add_ServerFacingClientServicer_to_server(ServerFacingClient(), server)
server.add_insecure_port("0.0.0.0:"+str(my_port))
server.start()
print("Started listening client!")
server.wait_for_termination()