import socketio

token = ''

sio = socketio.Client()


@sio.event
def connect():
    print(f'Connected with ID {sio.sid}')


@sio.on('event')
def on_message(event):
    print(repr(event))
    if type(event) == dict:
        if event["type"] == 'donation':
            print('New donate!')


sio.connect(f'https://sockets.streamlabs.com?token={token}')
sio.wait()
