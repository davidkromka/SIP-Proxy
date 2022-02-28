import socketserver
import sipfullproxy
import socket

if __name__ == '__main__':
    # get SIP Proxy IP
    ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip.connect(("8.8.8.8", 80))
    HOST = ip.getsockname()[0]
    PORT = 5060

    sip = sipfullproxy.UDPHandler
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (HOST, PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (HOST, PORT)
    sipfullproxy.config(HOST)
    server = socketserver.UDPServer((HOST, PORT), sip)
    print(HOST, PORT)
    # start SIP Proxy server
    server.serve_forever()
