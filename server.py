#importing socket and threading

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

client = {}
addresses = {}


HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s hs conectid 2 dis servr." % client_address)
        client.send(bytes("Greentins hooman!1"+"Plz tip ur nam and press enter", "utf8"))
        addresses[client] = client_address
        Thread(target = handle_client, args = (client)).start()


def handle_client(client):
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'wenlcome %s! iF u evr want tu quit, type {quit} to exit.' %name
    client.send(bytes(welcome, "utf8"))
    msg = "%s hs joned dis chet1" %name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s hs lft dis chet." %name, "utf8"))
            break


def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)


if _name_ == "_main_":
    SERVER.listen(5)
    print("watin fr conection")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()



