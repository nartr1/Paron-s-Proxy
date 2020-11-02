import importlib
import socket
import sys
import parselib
from threading import Thread


class ProxyRunner(Thread):

    client = False
    sender = ""

    def __init__(self, client):
        super(ProxyRunner, self).__init__()
        try:
            self.server = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
        except socket.error as ex:
            print(f"Socket creation failed with: {ex}")
            sys.exit(0)  

    def run(self):
        
        while True:
            data = ""
            try:
                if self.client and len(parser.CLIENT_QUEUE):
                    while len(parselib.CLIENT_QUEUE):
                        packet = parselib.CLIENT_QUEUE.pop()
                        self.server.sendall(packet)
                data = self.server.recvfrom(4096)
            except Exception as ex:
                print(f"Packet send failed with {ex}")
            try:
                if data:
                    parselib.Parse(data, self.client)
            except Exception as ex:
                print(f"Parser failed with {ex}")
            importlib.reload(parselib)
                
