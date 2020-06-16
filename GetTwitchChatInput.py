import socket, logging
from emoji import demojize

#Declare Server Variables

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'terrararfana'
token = 'oauth:o3bir3etkffrugs1eajt5yzfg4fiym'
channel = '#tommyinnit'

#Create A Socket Called Sock

sock = socket.socket()

#Connect to server

sock.connect((server, port))

#Send to server

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

#Recive

resp = sock.recv(2048).decode('utf-8')

resp

#Logging setup

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

#Logging

logging.info(resp)

#Ping Pong Server Staying and Continuious Logging

while True:
    resp = sock.recv(2048).decode('utf-8')

    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))
        
    elif len(resp) > 0:
        logging.info(demojize(resp))
    print('WORKING')
