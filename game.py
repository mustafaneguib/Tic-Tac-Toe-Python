#name=input("What is your name?")
from random import randint
import time
import os



def isGameBoardIndexNumeric(i):
    if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8":
        return True
    else:
        return False

def printGameBoard(game_board):
    print("%s %s %s" % (game_board[0], game_board[1], game_board[2]))
    print("%s %s %s" % (game_board[3], game_board[4], game_board[5]))
    print("%s %s %s" % (game_board[6], game_board[7], game_board[8]))


print("Welcome to Mustafa's Tic Tac Toe Python Game")
time.sleep(2)
print("Designed & developed by Mustafa Neguib")
time.sleep(2)
print("Twitter:@mustafaneguib")
time.sleep(2)

print("Player 1 your playing piece is O")
print("Player 2 your playing piece is X")
time.sleep(2)

player_pieces=["O","X"]
#play Please Wait animation. this is just a show off feature, and is only meant as a show off feature
please_wait="Please Wait"
#clear the screen
os.system('cls')  # For Windows
x=0
while(x<5):
    please_wait=please_wait+"."
    print(please_wait)
    time.sleep(1)
    # clear the screen
    os.system('cls')  # For Windows
    x=x+1
#randomize the turns. this will decide whether player 1 or player 2 will go first.
player_turn=randint(0,1)
print("Player %d you will go first" %(player_turn))

game_finished=False
game_board=["0","1","2",
            "3","4","5",
            "6","7","8",]

print("Each box on the playing board represents a single digit from 0 to 8.")
winning_player=0
while(game_finished == False):

    printGameBoard(game_board)

    print("Player %d please enter any number between 0 and 8 (inclusive) in order to place your piece" %(player_turn+1))
    piece_position=input()
    try:
        if int(piece_position) >= 0 and int(piece_position) <= 8:
            game_board[int(piece_position)] = player_pieces[player_turn]
            #check the state of the game
            #ignore the X character that is already in the board
            if (game_board[0]!="0" or game_board[1]!="1" or game_board[2]!="2") and (game_board[0]==game_board[1] and game_board[1]==game_board[2]):
                game_finished = True
                if game_board[0]=="O":
                    winning_player=1
                else:
                    winning_player=2
            elif (game_board[3]!="3" or game_board[4]!="4" or game_board[5]!="5") and (game_board[3]==game_board[4] and game_board[4]==game_board[5]):
                game_finished = True
                if game_board[3]=="O":
                    winning_player=1
                else:
                    winning_player=2
            elif (game_board[6]!="6" or game_board[7]!="7" or game_board[8]!="8") and (game_board[6] == game_board[7] and game_board[7] == game_board[8]):
                game_finished = True
                if game_board[6]=="O":
                    winning_player=1
                else:
                    winning_player=2
            elif (game_board[0]!="0" or game_board[3]!="3" or game_board[6]!="6") and (game_board[0] == game_board[3] and game_board[3] == game_board[6]):
                game_finished = True
                if game_board[0]=="O":
                    winning_player=1
                else:
                    winning_player=2
            elif (game_board[1]!="1" or game_board[4]!="4" or game_board[7]!="7") and (game_board[1] == game_board[4] and game_board[4] == game_board[7]):
                game_finished = True
                if game_board[1]=="O":
                    winning_player=1
                else:
                    winning_player=2
            elif (game_board[2]!="2" or game_board[5]!="5" or game_board[8]!="8") and (game_board[2] == game_board[5] and game_board[5] == game_board[8]):
                game_finished = True
                if game_board[2]=="O":
                    winning_player=1
                else:
                    winning_player=2
            elif (game_board[0]!="0" or game_board[4]!="4" or game_board[8]!="8") and (game_board[0] == game_board[4] and game_board[4] == game_board[8]):
                game_finished = True
                if game_board[0]=="O":
                    winning_player=1
                else:
                    winning_player=2
            elif (game_board[2]!="2" or game_board[4]!="4" or game_board[6]!="6") and (game_board[2] == game_board[4] and game_board[4] == game_board[6]):
                game_finished=True
                if game_board[2]=="O":
                    winning_player=1
                else:
                    winning_player=2
            else:
                count=0
                for i in game_board:
                    if isGameBoardIndexNumeric(i):
                        count=count+1

                if count==0:
                    game_finished=True

        else:
            print("Player %d you have entered an invalid value" % (player_turn + 1))
            time.sleep(1)
            continue

    except ValueError:
        print("Player %d you have entered an invalid value" % (player_turn + 1))
        time.sleep(1)
        continue

    if (player_turn == 0):
        player_turn = 1
    else:
        player_turn = 0

    os.system('cls')  # For Windows

if game_finished==True:
    if winning_player!=0:
        print("Congratulations Player %d you have won the game" %(winning_player))
    else:
        print("The game has ended in a stalemate")


