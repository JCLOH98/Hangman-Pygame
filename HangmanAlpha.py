import pygame
import sys
import random
import time
import re

from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

GREY = (200,200,200)

pygame.init()

pygame.display.set_caption("Hangman")

Display = pygame.display.set_mode((500,500))

Color = ["BLACK","WHITE","RED","GREEN","BLUE"]

Font = pygame.font.Font("freesansbold.ttf",45)
Font2 = pygame.font.Font("freesansbold.ttf",20)

Display.fill(WHITE)

def randomNum():
    RandomNum = random.randint(0,4) # as elements of color is 0,1,2,3,4
    return RandomNum

def List(number):
    Word = Color[number]
    return Word

#This is to make sure the word and random number is constant
TheNum = randomNum()
TheWord = List(TheNum)

#print('RandomNum = ',TheNum)
#print(TheWord)
#print(len(TheWord),'\n\n')
#print('RandomNum = ',TheNum)
print(TheWord)
#print(len(TheWord),'\n\n')

#This is to check that the number and word is constant
#This is to check if it got the word from the list

EmptyList = []

for i in range(len(TheWord)):
    EmptyList.append('-')

print(EmptyList)
print("".join(EmptyList))

Hidden = Font.render("".join(EmptyList),True,BLACK)
HiddenRect = Hidden.get_rect()
HiddenRect.center = (400,250)
Display.blit(Hidden,HiddenRect)

Condition = 0;#if condition is 10, then end game

def Hangman(condition):
    if (condition == 0):
        pygame.draw.line(Display, GREY, (10,400),(300,400),8)#baseline
        pygame.draw.line(Display, GREY, (50,50),(50,400),8)#stick1
        pygame.draw.line(Display, GREY, (50,60),(250,60),8)#stick2
        pygame.draw.line(Display, GREY, (150,60),(150,100),8)#rope
        pygame.draw.circle(Display, GREY, (150,150),50,8)#head
        pygame.draw.line(Display, GREY, (150,200),(150,300),8)#body
        pygame.draw.line(Display, GREY, (150,210),(100,250),8)#lefthand
        pygame.draw.line(Display, GREY, (150,210),(200,250),8)#righthand
        pygame.draw.line(Display, GREY, (150,300),(100,350),8)#leftleg
        pygame.draw.line(Display, GREY, (150,300),(200,350),8)#rightleg

    elif (condition == 1):
        pygame.draw.line(Display, BLACK, (10,400),(300,400),8)#baseline

    elif (condition == 2):
        pygame.draw.line(Display, BLACK, (50,50),(50,400),8)#stick1

    elif (condition == 3):
        pygame.draw.line(Display, BLACK, (50,60),(250,60),8)#stick2

    elif (condition == 4):
        pygame.draw.line(Display, BLACK, (150,60),(150,100),8)#rope

    elif (condition == 5):
        pygame.draw.circle(Display, BLACK, (150,150),50,8)#head

    elif (condition == 6):
        pygame.draw.line(Display, BLACK, (150,200),(150,300),8)#body

    elif (condition == 7):
        pygame.draw.line(Display, BLACK, (150,210),(100,250),8)#lefthand

    elif (condition == 8):
        pygame.draw.line(Display, BLACK, (150,210),(200,250),8)#righthand

    elif (condition == 9):
        pygame.draw.line(Display, BLACK, (150,300),(100,350),8)#leftleg

    elif (condition == 10):
        pygame.draw.line(Display, BLACK, (150,300),(200,350),8)#rightleg

TheTime = 0
Start = time.time() #current time


Display.blit(Font2.render("Time(s):",True,BLACK),(300,10))

while True:
    Hangman(Condition)
    End = time.time() #end time
    #print("Start:", Start)s
    #print("End:", End)
    if (int(End) - int(Start) == 1):
        pygame.draw.rect(Display,WHITE,(385,0,100,50))
        TheTime = TheTime + 1 
        print(TheTime, 'seconds has passed')
        Timer = Font2.render(str(TheTime),True,BLACK)
        Display.blit(Timer, (400,10))
        Start = time.time()
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            pygame.draw.rect(Display,WHITE,(300,200,200,100)) #hide word
            pygame.draw.rect(Display,WHITE,(300,50,200,100)) # hide invalid input
            UserInput = event.key
            #print(chr(event.key))
            #This is use to check if it changes the ASCII int value to the char
            if re.search("[a-z]",chr(event.key)):
                if chr(event.key).upper() in TheWord:
                    for i in range(len(TheWord)):
                        if (TheWord[i] == (chr(event.key)).upper()):
                            EmptyList[i] = TheWord[i]
                        #print("the word[",i,"]: ",TheWord[i])
                        #print("key pressed: ",(chr(event.key)).upper())

                else:
                    Condition = Condition + 1

                Hidden = Font.render("".join(EmptyList),True,BLACK)
                HiddenRect = Hidden.get_rect()
                HiddenRect.center = (400,250)
                Display.blit(Hidden,HiddenRect)
                
            else:
                Input = Font2.render("INVALID INPUT!!!",True,BLACK)
                InputRect = Input.get_rect()
                InputRect.center = (400,100)
                Display.blit(Input, InputRect)
                Display.blit(Hidden,HiddenRect)

    

    pygame.display.update()
    pygame.time.Clock().tick(30) #30fps

        
