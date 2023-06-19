## Importing Libraries ##

import pygame
import time
import random
import json
import os

# Details

snekVersion = 4
snekName = os.path.basename(__file__).split('.')[0] or str("DEEZ").upper()
authors = [
    ["Jasper Bartram", "Game Creator"],
    ["Alfie Standing", "QA Tester & Source Gifter"],
    ["Asher Loveridge", "QA Tester"],
    ["Joseph Ho", "QA Tester"],
    ["Arthur Sheringham", "QA Tester"],
    ["Notepad++", "Script Editor"],
    ["Visual Studio", "Script Editor"],
    ["Visual Studio Code", "Script Editor"],
    ["GitHub", "Repository Holder & Codespaces"]
]

print("Game Starting!")

# Window size
window_x = int(600)
window_y = int(600)
 
# defining colors
pitch_black = pygame.Color(0,0,0)
black = pygame.Color(15, 50, 15)
close_black = pygame.Color(150, 250, 150)
white = pygame.Color(205, 205, 205)
red = pygame.Color(252, 3, 36)
green = pygame.Color(140, 252, 3)
green2 = pygame.Color(54, 148, 0)
blue = pygame.Color(3, 98, 252)

splash_messages = [
    "Real",
    "Official",
    "Cooler than the last",
    "Version 4000",
    "Cool gaem",
    "Even cooler than me",
    "Credits don't exist",
    "Check output plz",
    "emojis 😎😎",
    "UTF-8",
    "0-Width Space Character",
    "Also try google snake!",
    "Eat moss!",
    "One of a kind!",
    "Yaaayy!",
    "Exclusive!",
    "Classy!",
    "Pixels!",
    "Enhanced!",
    "99% Bug Free!",
    "8 Colours!",
    "Waterproof!",
    "Tell your friends!",
    "Music not make by anyone!"
    "Snake but saveable!",
    "Save the game using Q!"
]

print("\n=======CREDITS=======\n")
for auth in authors:
    print(str(auth[0]) + ": " + str(auth[1]))
time.sleep(3)

# Initialising pygame
pygame.init()

difficulies = {
    "EASY": 1,
    "NORMAL": 5,
    "HARD": 10,
    "INSANE": 15,
    "UNFAIR": 25,
    "IMPOSSIBLE": 50,
    "NIGHTMARE": 150,
    "LUCID NIGHTMARE": 300,
    "HELL": 10000
}

difficulty = "UNFAIR" # EASY, NORMAL, HARD, INSANE, UNFAIR, IMPOSSIBLE, NIGHTMARE, HELL
score_increase = difficulies[difficulty]
 
# Initialise game window
pygame.display.set_caption(f'{snekName.lower()} ({difficulty} MODE)')
game_window = pygame.display.set_mode((int(window_x), int(window_y)))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()
 
# defining snake default position
snake_position = [100, 50]
 
# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
sFruit_pos = None

# initial score
score = 0
snake_speed = 10

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# update save data
def update_save():
    dat = {
        "fruit": {
            "x": fruit_position[0],
            "y": fruit_position[1]
        },
        
        "difficulty": difficulty,
        "score": score,
        "snake": {
            "speed": snake_speed,
            "position": snake_position,
            "body": snake_body,
            "direction": direction
        }
    }
    
    with open('save.json', 'w') as f:
        f.write(json.dumps(dat))
        
# overwrites the save data with default ones
def clear_save():
    dat = {
        "fruit": {
            "x": random.randrange(1, (int(window_x//10))) * 10,
            "y": random.randrange(1, (int(window_y//10))) * 10
        },
        
        "difficulty": difficulty,
        "score": 0,
        "snake": {
            "speed": 10,
            "position": [100, 50],
            "body": [[100, 50],
                      [90, 50],
                      [80, 50],
                      [70, 50]
                      ],
            "direction": 'RIGHT'
        }
    }
    
    with open('save.json', 'w') as f:
        f.write(json.dumps(dat))

with open('save.json', 'r') as save:
    try:
        content = json.loads(save.read())
        
        fruitDat = content["fruit"]
        scoreDat = content["score"]
        snakeDat = content["snake"]
        
        sFruit_pos = [fruitDat['x'], fruitDat['y']]
        
        snake_speed = snakeDat["speed"]
        snake_position = snakeDat["position"]
        snake_body = snakeDat["body"]
        
        direction = snakeDat["direction"]
        change_to = direction
        
        score = scoreDat
    except e as Exception:
        print(e)

global fruit_position
if sFruit_pos == None:
    fruit_position = [random.randrange(1, (window_x//10)) * 10,
                    random.randrange(1, (window_y//10)) * 10]
else:
    fruit_position = sFruit_pos
 
fruit_spawn = True

# displaying Score function
def show_score(choice, color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    diff_font = pygame.font.SysFont(font, size)
    
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score: ' + str(score), True, close_black)
    
    diff_surface = score_font.render('Difficulty: ' + str(difficulty[0:1]) + str(difficulty[1:len(difficulty)]).lower() + f" ({score_increase})", True, close_black)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    diff_rect = diff_surface.get_rect()
    
    # position difficulty text
    diff_rect.midtop = (window_x/2, 0)
    
    # update save data
    update_save()
    
    # displaying text
    game_window.blit(score_surface, score_rect)
    game_window.blit(diff_surface, diff_rect)
 
# game over function
def game_over():
   
    # creating font object my_font
    my_font = pygame.font.SysFont('source code pro', 50)
     
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        '' + str(score), True, red)
     
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # end game save data
    clear_save()
    
    # after 2 seconds we will quit the program
    time.sleep(2)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()
    
# game over function
def display_different_diff():
   
    # creating font object my_font
    my_font = pygame.font.SysFont('source code pro', 15)
     
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'Your difficulty (' + difficulty +') is different from your save difficulty!', True, red)
    game_over_surface2 = my_font.render(
        'Press R during the match to change to saved difficulty!!', True, red)
     
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
    game_over_rect2 = game_over_surface2.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_over_rect2.midtop = (window_x/2, window_y/4 + 15)
     
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    game_window.blit(game_over_surface2, game_over_rect2)
    pygame.display.flip()
    
# start menu display
def display_start_menu():
    # display black background
    game_window.fill(pitch_black)
    
    # creating font object my_font
    my_font = pygame.font.SysFont('source code pro', 35)
    my_font2 = pygame.font.SysFont('source code pro', 15)
    
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        f'{snekName.upper()}!!11!1!', True, red)
    game_over_surface2 = my_font2.render(
        '(' + splash_messages[random.randrange(0, len(splash_messages) - 1)] + '!)', True, red)
     
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
    game_over_rect2 = game_over_surface2.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_over_rect2.midtop = (window_x/2, window_y/4 + 35)
     
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    game_window.blit(game_over_surface2, game_over_rect2)
    pygame.display.flip()
    

canChange = True
global diff
global err

diff = ""
err = ""

with open('save.json', 'r') as save:
    try:
        content = json.loads(save.read())
        diff = content["difficulty"]
        
        if difficulty != diff:
            display_different_diff()
            time.sleep(6)
        display_start_menu()
        time.sleep(5)
        canChange = False
    except err as Exception:
        print(err)
 
# Main Function
while True:
    pygame.display.set_caption(f'owo snek ({difficulty} MODE)')
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_w:
                change_to = 'UP'
            if event.key == pygame.K_i:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_s:
                change_to = 'DOWN'
            if event.key == pygame.K_k:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_a:
                change_to = 'LEFT'
            if event.key == pygame.K_j:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_d:
                change_to = 'RIGHT'
            if event.key == pygame.K_l:
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFTBRACKET:
                score_increase -= 1
                difficulty = "CUSTOM"
            if event.key == pygame.K_r:
                difficulty = diff
                score_increase = difficulies[difficulty]
            if event.key == pygame.K_RIGHTBRACKET:
                score_increase += 1
                difficulty = "CUSTOM"
            if event.key == pygame.K_q:
                update_save()
            
                pygame.quit()
                quit()
 
    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 1
        snake_speed += score_increase
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
     
    i = 0
    for pos in snake_body:
        i += 1
        if (i % 2 == 0): 
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
        else:
            pygame.draw.rect(game_window, green2,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
 
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
            
    
 
    # displaying score countinuously
    show_score(1, white, 'source code pro', 20)
 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second / Refresh Rate
    fps.tick(snake_speed)