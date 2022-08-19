import random

suits = ( 'HEARTS' , 'DIAMONDS' , 'CLUBS' , 'SPADES' )
ranks = ( 'TWO' , 'THREE' , 'FOUR' , 'FIVE' , 'SIX' , 'SEVEN' , 'EIGHT' , 'NINE' , 'TEN' , 'JACK' , 'QUEEN' , 
          'KING' , 'ACE' )
values = { 'TWO' : 2 , 'THREE' : 3 , 'FOUR' : 4 , 'FIVE' : 5 , 'SIX' : 6 , 'SEVEN' : 7 , 'EIGHT' : 8 , 'NINE' : 9 , 'TEN' : 10 , 'JACK' : 10 , 'QUEEN' : 10 , 'KING' : 10 ,'ACE' : 11 }

playing = True

total_chips = 100 #to deal with total chips of the player

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
       
    
    def __str__(self):
        return ( (self.rank) + ' of ' + (self.suit) )



class Deck():
    def __init__(self):
        self.deck = []
        
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
   
    def  shuffle_deck(self):
         random.shuffle(self.deck)
    
    def deal_one(self):
        return self.deck.pop(0)
    

class Hand():
    
    def __init__(self):
        self.hand_cards = []
        self.tot_value  = 0
        self.aces       = 0  #an attribute to track aces 
    
    def add_cards(self,card):
        # card --> a single card pulled from a deck of cards
        self.hand_cards.append(card)
        self.tot_value += values[card.rank]
        
        if card.rank == 'ACE':
            self.aces += 1
    
    def adjust_for_ace(self):
        #the total value of all hand cards is greater than 21 and we do have an ace as well
        if  self.tot_value > 21 and self.aces > 0 :
            self.tot_value -= 10
            self.aces      -= 1

class Chips():
    
    def __init__(self,total):
        self.tot_chips = total   
        self.bet   = 0
    
    def win_bet(self):
        self.tot_chips += self.bet
    
    def lose_bet(self):
        self.tot_chips -= self.bet


def take_bet(chips):
    '''a function to take input (bet) by the player'''
    while True:
        try:
            print(f"\nYou have currently chips total to bet:\n{chips.tot_chips}")
            chips.bet = int( input('How many chips would you like to bet?\n') )
        except ValueError:
             print('Sorry,enter an integer:\n') 
        else:
            if chips.tot_chips < chips.bet:
                print("sorry! you don't have enough chips.so,try again!")
            else:
                print(f'you got {chips.bet} as bet.')
                break

                
def hit_or_stand():
   
    '''Ask player --> would you like to pull one more card from the deck or want to stop pulling cards?'''
    
    global playing
    
    while True:
        x = input("\nhit or stand? enter 'h' or 's'\n")
        
        if x[0].lower() == 'h':
            return 'h'
        
        elif x[0].lower() == 's':
            playing = False
            return 's'
        
        else:
            print("\nSorry! I did not understand that.Please enter 'h' or 's'\n")
            continue
        
        break


def hit(deck,hand):
    single_card = deck.deal_one()
    hand.add_cards(single_card)   #add a card from the deck ,checks for aces and calculates total value of all
    hand.adjust_for_ace()         #cards and finally ,adjust for ace.
    
    
def show_some_cards(player,dealer):
    
    #show only one card of dealer's hand
    print("\ndealer's hand:")
    print('First card hidden!')
    
    print('Second card:\n')
    card = dealer.hand_cards[1]
    print((f" {18*'-'}   ")) 
    for i in range(3):
        if i == 1:
            print((f"|{card.__str__().center(18)}|"))
        else:
            print((f"|{18*' '}|  "))
    print((f" {18*'-'}   ")) 
    
    #show value of second card of dealer's hand
    print(f'\nThe Current value of shown card of the dealer is {values[card.rank]}')
    
    #show all cards of player's hand cards 
    print("\nplayer's hand:\n")
    
    n=len(player.hand_cards)
    
    print(n*(f" {18*'-'}   "))
    for i in range(3):
            
            if i == 1:
                  
                for j in range(n):
                    card = player.hand_cards[j]
                    print((f"|{card.__str__().center(18)}|"),end = '  ')
                else:
                    print()
            
            else:
                print(n*(f"|{18*' '}|  "))
    
    print(n*(f" {18*'-'}   "))

    #show total value of  all hand cards of player
    print(f"\nThe total value of all cards of the player is {player.tot_value}")
    

    

def show_all_cards(player,dealer):
   
    player1 = len(player.hand_cards),"Player hand cards:",player
    dealer1 = len(dealer.hand_cards), "Dealer hand cards:",dealer
    
    #show all cards of player as well as of the dealer 
    for n,p,x in player1,dealer1:
        print(f"\n{p}\n")                        #print statements
        print(n*(f" {18*'-'}   "))
    
        for i in range(3):
            if i == 1:
                for j in range(n):
        
                    card = x.hand_cards[j]
                    print((f"|{card.__str__().center(18)}|"),end = '  ')
                else:
                    print()
            else:
                print(n*(f"|{18*' '}|  "))
    
        print(n*(f" {18*'-'}   "))
     
   
    
    
    #calculate and display total value of all dealer hand cards
    print(f"\nTotal value of all hand cards of the player is {player.tot_value}")
    
   
   
       #calculate and display total value of all dealer hand cards
    print(f"\nTotal value of all hand cards of the dealer is {dealer.tot_value}")

    
#functions to deal end game scenarios
def player_busted(chips):
    global total_chips
    print('player busted! dealer won!')
    chips.lose_bet()
    total_chips = chips.tot_chips

def player_won(chips):
    global total_chips
    print('player won!dealer lose!')
    chips.win_bet()
    total_chips = chips.tot_value
    
def dealer_busted(chips):
    global total_chips
    print('dealer busted!player won!')
    chips.win_bet()
    total_chips = chips.tot_chips

def dealer_won(chips):
    global total_chips
    print('dealer won!player lose!')
    chips.lose_bet()
    total_chips = chips.tot_chips

def push():
    #both player and dealer got 21
    print('dealer and player tie !Push')    

def play_again():
	global playing
	while True:
		game_on = input("\nEnter 'y' for YES and 'n' for NO.\n") 
		
		if game_on[0].lower() == 'y':
			playing = True
			return 'y'
			
		elif game_on[0].lower() == 'n':
			print('Thank you for playing!')
			return 'n'
		
		else:
			print('Cannot understand,please enter a valid letter\n')
#main

#print an opening statement
print('\nWelcome to Black Jack!\nThe player needs to reach as close to 21 as possible without busting.\nThe dealer needs to     cross   that mark without busting.\n')



while True:
    
    #create and shuffle deck , and deal two cards to each player
    new_deck = Deck()
    new_deck.shuffle_deck()
    
    player_hand = Hand()
    dealer_hand = Hand()
  
    for i in range(2):
 
        player_hand.add_cards(new_deck.deal_one())
        dealer_hand.add_cards(new_deck.deal_one())
    
    #create chips for player
    player_chips = Chips(total_chips)
    
    #prompt the player for the bet
    take_bet(player_chips)
    
    #show cards but keep one card of the dealer hidden
    show_some_cards(player_hand,dealer_hand)
    
    while playing:
        
        #prompt the player to hit or stand
        h_or_s = hit_or_stand()
        
        if  h_or_s == 'h':                                                     #hit 
            print('\na card is drawn by the player:\n')
            hit(new_deck,player_hand)
        
        elif h_or_s == 's':                  #stand
            print("\nPlayer stands, so, its  dealer's turn")
            playing = False
        
        #show cards of the player and one card of the dealer hidden 
        show_some_cards(player_hand,dealer_hand)
        
        #if player's card total value exceeds 21, player busts
        if  player_hand.tot_value > 21:
            player_busted(player_chips)
            
            break
    
    #if player hasn't busted, play dealer's hand until dealer busted or beat the player 
    if player_hand.tot_value <= 21:
        
        while dealer_hand.tot_value < player_hand.tot_value:
            hit(new_deck,dealer_hand)
            
        #show all cards
        print('\nfinally showing all hand cards:\n')
        show_all_cards(player_hand,dealer_hand)
        
        #run different scenarios
        if  dealer_hand.tot_value > 21:
            dealer_busted(player_chips)
        
        elif dealer_hand.tot_value > player_hand.tot_value:
            dealer_won(player_chips)
            
        elif dealer_hand.tot_value == player_hand.tot_value:
            push()
        
        elif dealer_hand.tot_value < player_hand.tot_value:
            player_won(player_chips)
        
    #inform player of their chips total
    print(f'\nfinally , player chips: {player_chips.tot_chips}')
    
    #ask to play again
    if player_chips.tot_chips > 0:
    	
        game_on = play_again()
        if    game_on == 'y' :
            continue  
        elif  game_on ==  'n' :
            break                            
    
    else:
        print('\nno more chips left to play.')
        break                         #to break the first while loop 
       
    

