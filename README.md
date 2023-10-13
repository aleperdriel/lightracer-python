# Multiplayer lightracer game in python

Welcome to my first multiplayer game ! This is a school project reproducing a simple version of the light cycles game from the movie*Tron*. 

This game is pretty simple : several players drive a vehicle always moving forward, its direction being the only parameter that they can manage.\
Each vehicle leaves a wall on their trail, the last player to crash into one of the walls win!

## Quickstart
You will need python to run this game, I created it using the **3.8.10** version

- First, you will have to install pygame. You can do it with pip :
```bash
  pip install pygame
```
If you have trouble installing it you can check the [pygame wiki](https://www.pygame.org/wiki/GettingStarted) for more information

**If you are the player hosting the server for the game:**
- Check the settings on the *server.py* file :
```python
# line 6
# You can change '8888' by any other port if this one is already in use
server_socket.bind(('127.0.0.1', 8888))
```


**If you are a player trying to access the server to play with your friend :**
- You will need to edit the ip address and possibly the port on the *network.py* file :
```python
# line 6
# Change it to the ip address of the server you try to access

self.server = '127.0.0.1'

# Change it to the port used on the server part
self.port = 8888
```


## How it works

This project is made in python, using the [pygame](https://www.pygame.org/) library. The networking is handled with sockets.

Multithreading is used on this project to handle the different processes interacting with each other. 
Each client is handled on a different thread and sends its real-time updated data, that the server sends back to every other client.

The visuals are managed on each client directly, based on the information sent by the server about the other players.

You will find 3 main files :
- **network.py** : it defines the class Network, used for the connection to the server and the data exchanges between the clients and the server
  
- **client.py** : handling the client individual part and the data flow
  
- **server.py** : this file is used to create the server on your local computer and is a bridge between the different clients to handle the game's data and part of the logic
## Authors

I worked alone on this project, if you want to follow other projects of mine, you can look at my github profile : [@aleperdriel](https://www.github.com/aleperdriel)

## Notes about the project
This project is actually not done. I had a few time-related issues about it. The first commit is a first version of a locally two-player lightracer but I struggled to adapt it to the socket version. 