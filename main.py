from replit import audio as a
import random
import pygame
import time


pygame.init()
pygame.mixer.init()
#==========================================================================================
def create_ship(used_locations):  # Ship creation function with used locations as a parameter
  while True:
    new_ship = (random.randint(0, 4), random.randint(0, 4))
    if new_ship not in used_locations:  # Check if the new ship location has been used
      used_locations.append(new_ship)  # Add the new ship to the used locations
      return new_ship

def replay():
  On=input("Do you want to play again? (y/n)").lower()    #Replay function
  if On=="y":
    game()
  else:
    print("Thanks for playing!")                 
    exit()

#==========================================================================================

def game():
 backroundmusic=a.play_file("Cool-Adventure-Intro.mp3",0.5)
 backroundmusic.set_loop(1)
 soundfile="explosion.wav"
 pygame.mixer.music.load(soundfile)
 Title="""
                                                
 _____     _   _   _        _____ _   _         
| __  |___| |_| |_| |___   |   __| |_|_|___ ___ 
| __ -| .'|  _|  _| | -_|  |__   |   | | . |_ -|
|_____|__,|_| |_| |_|___|  |_____|_|_|_|  _|___|
                                       |_|      
 """
 Title = "\033[1;35m" + Title + "\033[m"
 print(Title)                                          
 shots=10
 Validshot=False
 game_board = [["O", "O", "O", "O", "O"],
              ["O", "O", "O", "O", "O"],
              ["O", "O", "O", "O", "O"],        #Creation of game bored
              ["O", "O", "O", "O", "O"],         #Columns(A-E) Rows(1-5)
              ["O", "O", "O", "O", "O"]]
 used_locations = []  # List to store used ship locations
 for i in game_board:
  print(*i)
  ship1 = create_ship(used_locations)  # Pass used locations to create_ship function
  ship2 = create_ship(used_locations)  
  ship3 = create_ship(used_locations)  
  shipsleft=3

 print(ship1,ship2,ship3)
#========================================================================================================
 while shots!=0:
   if shipsleft != 0:
     print("You have", shots, "shots left and", shipsleft, "ships left")
     shots-=1
     while Validshot==False:
      shot=input("Enter the colum(A-E) and row(1-5) you want to shoot at: ")
      shot=shot.upper()
      if shot[1].isdigit() and shot[1] in "12345" and shot[0] in "ABCDE" and len(shot)==2:
        Validshot=True
      else:
        print("Invalid input")
#==========================================================================================
     Column=(shot[0])
     if Column=="A":
       Column=0
     elif Column=="B":
       Column=1
     elif Column=="C":                                         #Main Shooting
       Column=2
     elif Column=="D":
       Column=3
     elif Column=="E":
       Column=4
     Row=int(shot[1])-1

  
     
     if (Column,Row) == ship1 or (Column,Row) == ship2 or (Column,Row) == ship3:
       explosion=a.play_file("explosion.wav",0.5)
       print("HIT")
       game_board[Row][Column] = "X"
       shipsleft-=1
       Validshot=False
       if (Column,Row)==ship1:
         ship1=None
       elif (Column,Row)==ship2:
         ship2=None
       elif (Column,Row)==ship3:
         ship3=None
       for i in game_board:
         print(*i)
     else:
       hitHurt=a.play_file("hitHurt.wav",0.5)
       print("MISS")
       if game_board[Row][Column] != "X":
         game_board[Row][Column] = "."
       Validshot=False
       for i in game_board:
         print(*i)
   else:
     print("You sunk all the ships!")
     replay()
 print("You ran out of shots!")
 print(ship1, ship2, ship3)
 replay()
#=======================================================================================
#Start of gamemode 2
#=======================================================================================
player_board = [["O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O"],        #Creation of game bored
  ["O", "O", "O", "O", "O"],         #Columns(A-E) Rows(1-5)
  ["O", "O", "O", "O", "O"]]
enemy_board = [["O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O"],        #Creation of game bored
  ["O", "O", "O", "O", "O"],         #Columns(A-E) Rows(1-5)
  ["O", "O", "O", "O", "O"]]






















print("Welcome to Battleships! Type 1 for single player and 2 for against the computer")
mode=int(input())
if mode == 1:
  game()
else:
  print("Not made yet")
