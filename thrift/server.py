import thriftpy
pingpong_thrift = thriftpy.load('pingpong.thrift', module_name='pingpong_thrift')

from thriftpy.rpc import make_server

class Hello:
    def __init__(self):
        self.n= 1
    def ping(self):
        return 'pong'

    def add(self):
        self.n += 1
        return self.n

server = make_server(pingpong_thrift.PingPong, Hello(), '127.0.0.1', 6000)
server.serve()
