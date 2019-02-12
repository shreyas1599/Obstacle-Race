#Features to be implemented: Randomize shape of obstacles, choose your character, randomize colour of obstacles


import pygame
import random
import time

pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

#colors 
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green= (0,255,0)
blue = (0,0,200)
bright_blue = (0,0,255)
pause = False
car_width = 100

pikachu = pygame.image.load('pikachu.png')
def pika(x,y):
    gameDisplay.blit(pikachu,(x,y))

def obstacles(obstacle_x,obstacle_y,obstacle_height,obstacle_width,color):
    pygame.draw.rect(gameDisplay,color,[obstacle_x,obstacle_y,obstacle_width,obstacle_height])

def display_score(score):
    font = pygame.font.SysFont(None,25)
    text = font.render("Score: " + str(score),True,red)
    gameDisplay.blit(text,(0,0))

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",115)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height)/2)
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update
    
def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action!=None:
            action()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
    
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf,textRect = text_objects(msg,smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)

def display_exit_message(dodged):
    while True:
        font = pygame.font.SysFont(None,100)
        gameDisplay.fill(black)
        button("Play Again",(1/8)*display_width,(3/4)*display_height,150,50,green,bright_green,game_loop)
        button("Quit",(3/4-1/12)*display_width,(3/4)*display_height,150,50,red,bright_red,quitgame)
        text_score = font.render("Score: " + str(dodged), True, (102, 102, 255))
        gameDisplay.blit(text_score,((1/3)*display_width,(1/4)*display_height))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
def quitgame():
    pygame.quit()
    quit()

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            gameDisplay.fill(black)
        largeText = pygame.font.Font("freesansbold.ttf",200)
        textSurf,textRect = text_objects("PIKA RACE",largeText)
        textRect.center = ((1/4)*display_width,(1/4)*display_height)
        gameDisplay.blit(textSurf,textRect)
        button("Start!",(1/8)*display_width,(3/4)*display_height,150,50,bright_green,green,game_loop)
        #button("Rules",(1/2)*display_width-50,(3/4)*display_height,150,50,(230, 92, 0),(255, 133, 51),rules)
        button("Quit",(3/4)*display_width,(3/4)*display_height,150,50,(0, 102, 153),(26, 178, 255),quitgame)
        pygame.display.update()

def rules():
    gameDisplay.blit("text",(20,20))
    pygame.display.update()

def game_loop():
    x = display_width*0.1
    y = display_height*0.6
    y_change = 0
    gameExit = False
    dodged = 0
    obstacle_change = 5
    obstacle_x = display_width*(0.8)
    obstacle_y = 0
    obstacle_width = 70
    obstacle_height_1 = random.randrange(200,250)
    obstacle_height_2 = random.randrange(200,250)
    obstacle_height_1 = random.randrange(200,250)
    obstacle_height_2 = random.randrange(200,250)
    color_1 = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    color_2 = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    y_change = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    y_change *= -1

        y += y_change
        if y <= 0 or y >=display_height:
            display_exit_message(dodged)
        # to check if pikachu is in between the two obstacles
        if x > obstacle_x and x < obstacle_width + obstacle_x and not(y > obstacle_height_1 and y < display_height-obstacle_height_2):
            display_exit_message(dodged)
        # load new frame with obstacle
        if obstacle_x + obstacle_width < 0:
            obstacle_x = display_width
            obstacle_height_1 = random.randrange(200,250)
            obstacle_height_2 = random.randrange(200,250)
            obstacle_height_1 = random.randrange(200,250)
            obstacle_height_2 = random.randrange(200,250)
            dodged+=1
            obstacle_change += dodged*0.005
            color_1 = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
            color_2 = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

        gameDisplay.fill(black)
        display_score(dodged)
        obstacle_x -= obstacle_change
        obstacles(obstacle_x,obstacle_y,obstacle_height_1,obstacle_width,color_1)
        obstacles(obstacle_x,display_height-obstacle_y,-1*obstacle_height_2,obstacle_width,color_2) 
        pika(x,y)
        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()
