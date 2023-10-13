from network import Network
import pygame
import threading

grid_unit = 10

dir_right = pygame.Vector2(1,0)
dir_left = pygame.Vector2(-1,0)
dir_up = pygame.Vector2(0,-1)
dir_down = pygame.Vector2(0,1)


class Player:
    
    def __init__(self, x: float, y: float, name: str, color: pygame.Color) -> None:
        self.pos = pygame.Vector2(x, y)
        self.name = name
        self.color = color
        self.walls = []
        self.direction = pygame.Vector2(0, 1)
    
    def display(self):
        for wall in self.walls:
            rect = (wall.x * grid_unit,wall.y * grid_unit, grid_unit, grid_unit)
            pygame.draw.rect(screen, self.color, rect)
        body = (self.walls[0].x * grid_unit,self.walls[0].y * grid_unit, grid_unit, grid_unit)
        pygame.draw.rect(screen, "red", body)
    
    def move(self): 
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_RIGHT] and player1.direction != dir_left:
            player1.direction = dir_right
        elif keys[pygame.K_LEFT] and player1.direction != dir_right:
            player1.direction = dir_left

        elif keys[pygame.K_UP] and player1.direction != dir_down:
            player1.direction = dir_up

        elif keys[pygame.K_DOWN] and player1.direction != dir_up:
            player1.direction = dir_down
        
        new_pos = self.walls[0] + self.direction
        self.walls.insert(0, (new_pos))
        self.update_pos(new_pos)
    
    def update_pos(self, pos: pygame.Vector2):
        self.pos = pos
        
    def is_colliding(self, walls) -> bool: 
        if self.pos in walls[1:]:
            return True
    
    def game_over(self) -> None:
        print('Game over!')
    
class Game:
    def __init__(self, screen_width: float, screen_height: float, bg_color: pygame.color, players: [Player] = [Player(0,0,"player", "blue")]):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bg_color = bg_color
        self.players = players
        self.running = True
    
    def update(self) -> None:
        for player in self.players:
            player.move()   
            self.check_collision(player)
            player.display()
        
        self.send_to_server()
    
    def send_to_server(self):
        data = {
            'index': network.player_index,
            'walls': (self.players[0].walls[0].x, self.players[0].walls[0].y)
        }
        network.send_data_all(network.client_socket, data)     
        
                
    def check_collision(self, player):
        if player.is_colliding(player.walls):
            player.game_over()
            
            self.running = False
        
        if player.pos.x > game.screen_width/grid_unit or player.pos.x < 0 or player.pos.y > game.screen_height/grid_unit or player.pos.y < 0 :
            player.game_over()
            self.running = False
            
           
# pygame setup
pygame.init()

network = Network()

# Player and game settings
clock = pygame.time.Clock()
fps = 50

game = Game(1280,720, pygame.Color(0,0,0))
orange = pygame.Color(255, 100, 0)

screen = pygame.display.set_mode((game.screen_width, game.screen_height))

player_pos = pygame.Vector2(game.screen_width / 2 / grid_unit, game.screen_height /2 / grid_unit)
player1 =  Player(player_pos.x, player_pos.y, "Player1", orange)
game.players = [player1]

player1.walls = [
    player1.pos
]

while game.running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game.running == False:
            running = False

    screen.fill("black")
    game.update()

    try:
        print(f'New data : {network.receive(network.client_socket)}')
    except Exception as e:
        print(e)
        pass
    

    pygame.display.flip()

    dt = clock.tick(fps) / 1000

