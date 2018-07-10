import socket


# function section


def send_dns():
    print("send packet")
    print("DNS target IP:", TCP_IP)
    print("DNS target port:", TCP_PORT)
    print("DNS target name:", TCP_Target)
    # print("message:", message)
    newmsg = bytes(DNS_type + "*" + TCP_IP + "*" + TCP_Target, 'utf-8')
    s.connect((TCP_IP, TCP_PORT))
    s.send(newmsg)


def receive_dns():
    print("client waiting for answer ...")

    data = str(s.recv(BUFFER_SIZE))
    s.close()
    rcv_data = data[2:-1].split('*')
    print("recieved packet")
    print("DNS query type IP:", rcv_data[0])
    print("DNS query target names:", rcv_data[2])
    print("DNS query tareget Ips:", rcv_data[3])
    # show_result_dns(rcv_data)


def show_result_dns(message):
    print("received message:", message)


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
TCP_Target = 'aut.ac.ir'
DNS_type = 'A'  # CNAME
BUFFER_SIZE = 1024
# MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
send_dns()

receive_dns()
