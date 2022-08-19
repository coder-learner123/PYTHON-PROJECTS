## Tic Tac Toe game using Python


def initialize_board():
    board = [ [0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            board[i][j] = 3*i+j+1
    return board
 
def display_board():
    print('current state of board is: ')
    for i in range(3):
        print('-' * 13)
        for j in range(3):
            print('|', board[i][j], end =' ')
        print('|')
    print(('-' * 13))
    

def user_in_num():                           # input number to place your character
    while True:
        num = input()
        if num.isdigit():                    #check if given string contains integers or not
            if int(num) in range(1,10):      #check if given num lies in range (1-9)
                return int(num)
            else:
                print('enter a valid range (1-9): ')
        else:
            print('enter a valid digit: ')
     
def user_in_string(player_button):           #input your character to place at corresponding place in the grid
    while True:
        string = input()
        if string == char[player_button%2] :
            return string
        else:
            print('enter a valid letter : ')

def calc(num):                               #calculate corresponding row and col for input number 
    r = (num-1)//3     
    c = num -3*r-1
    return  r,c    


def check_place(r,c):                        #check if the place is already occupied or not 
          
          if type(board[r][c]) == int:
              return True
          else:
              return False

def board_update(r,c,string):
     board[r][c] = string
    
def check_win(r,c,string):                                 #check winning state or game continuation state
    
    first , second, Third, fourth  = True, True, True, True
    for i in range(3):
    	if board[i][c] != string:                          # check for same string in corresponding column
    		first = False
    		
    	if board[r][i] != string:                          # check for same string in corresponding row
    		second = False
    
    	if board[i][i] != string:                          #check for same string in NWtoSE diagonal
    		third = False
    	
    	if board[i][2-i] != string:                        # check for same string in SWtoNE diagonal
    		fourth = False
   
    return (first or second or third or fourth)
    
# main function to control other functions in the program       	

def GAME():                                                  # main function to control other functions in the program       	
    for player_button in range(9):
        
        right_place = False  
        
        while right_place == False:     
            print(f'user{players[player_button%2]}: enter number (1-9) to place your {char[player_button%2]}')
            num = user_in_num()
            print(f'user {players[player_button%2]} entered {num}')
            r,c = calc(num)
            right_place = check_place(r,c)
            if right_place == False:
                print(f'This place is already filled. Try with another number(1-9) to place your {char[player_button%2]}')    
          
        print(f'user {players[player_button%2]} enter {char[player_button%2]}: ')
        string = user_in_string(player_button)
        print(f'user {players[player_button%2]} entered {string}')
        
        board_update(r,c,string)
        display_board()
      
        game_state = check_win(r,c,string)
        if  game_state :
              display_board()
              print(f'winner of the game is {players[player_button%2]}')
              break
    else:
             print('all places filled. None is winner')
    
#main
        
board = initialize_board()  
print('Welcome to tic_tac_toe !\nchoose from "#" or "@" as characters')
print('Enter number from  the number palatte:\n ')
display_board()
players = ['First player', 'second player']


print('user1 is assigned -"#" \nuser2 is assigned - "@"')
char =[ '#' ,'@']    
GAME()
