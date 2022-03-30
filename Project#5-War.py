import random
# The ASCII art is property of: https://www.asciiart.eu (I didn't create the ASCII art)
card_1= """
 _____
|A    |
|     |
"""
card_2 ="""
 _____ 
|2    | 
|     |
"""
card_3 = """
 _____ 
|3    |
|     |
"""
card_4 = """
 ____ 
|4    |
|     |
"""
card_5 = """
 _____  
|5    |
|     |
"""
card_6 = """
 _____
|6    | 
|     |
"""
card_7 = """
 _____
|7    |
|     |
"""
card_8 = """
 _____
|8    |
|     |
"""
card_9 = """
 _____
|9    |
|     |
"""
card_10 = """
 _____ 
|10   |
|     | 
"""
card_11 = """
 _____  
|J    | 
|     |
"""
card_12 = """
 _____  
|Q    | 
|     |
"""
card_13 = """
 _____
|K    |    
|     |
"""
def distributeCards(x, y):
    for i in range(2):
        x.append(y[i])
    return x

def distributeCards_pc(ActualDeck):
    x = []
    y = []

    for i in range(26):
        x.append(ActualDeck[i])
        
    for i in range(26,52):
        y.append(ActualDeck[i])

    return y
def distributeCards_user(ActualDeck):
    x = []
    y = []

    for i in range(26):
        x.append(ActualDeck[i])
        
    for i in range(26,52):
        y.append(ActualDeck[i])

    return x

def printDeck(copy):
    x= copy
    x.sort()
    return x

def sortDeck(copy):
    deck = printDeck(copy)
    return deck
    

def Addingtwolists(y,x):

    for i in range(26): #were putting the list of cards of x in the bottom of y
        y.append(x[i])
    return y
    
def splitDeck(Deck):
    #two lists to separate 26 cards in each one
    x = []
    y = []

    for i in range(26): # the list x gets the first 26 cards
        x.append(Deck[i])
        
    for i in range(26,52): # the list y gets the remaining cards
        y.append(Deck[i])

    add = Addingtwolists(y,x) # here we put one in top of another

    return add
    
def shuffleDeck(Deck):
    shuffled = Deck
    random.shuffle(shuffled) # we use the built in function random to shuffle the deck (we imported random first)
    return shuffled
    
def initializeDeck():
    Deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    return Deck * 4 # we will multiply the 13 cards times 4 to get 54 cards in total
    
def WinPercentage(num_Games,num_GamesWon_user,num_GamesWon_pc):
    print("These are the Win Percentages:")
    print()
    Win_percentage_user = 0
    Win_percentage_pc = 0
    if num_GamesWon_user > 0:
        Win_percentage_user = (num_GamesWon_user / num_Games) * 100
    if num_GamesWon_pc > 0:
        Win_percentage_pc = (num_GamesWon_pc / num_Games) * 100
    print("""
 __| |_________________| |__
(__   _________________   __)
   | |                 | |
   | |                 | |
   | |user won = {}% | |
   | |pc won = {}%   | |  
   | |                 | |
   | |                 | |
 __| |_________________| |__
(__   _________________   __)
   | |                 | |
""".format(Win_percentage_user,Win_percentage_pc))
    print()

    
def DisplayCards():
    print("These are the Cards: ")
    print()
    Deck = initializeDeck()
    
    Deck = shuffleDeck(Deck)
    
    SplitDeck = splitDeck(Deck)
    
    ActualDeck = SplitDeck
    
    copy = SplitDeck.copy()
    
    copy_of_Deck = sortDeck(copy)

    print(copy_of_Deck)
    
    
def DisplayScore(num_GamesWon_user,num_GamesWon_pc):
    print("Scores:")
    print()
    print("""
 __| |_________________| |__
(__   _________________   __)
   | |                 | |
   | |                 | |
   | |user won = {}    | |
   | |pc won = {}      | |  
   | |                 | |
   | |                 | |
 __| |_________________| |__
(__   _________________   __)
   | |                 | |
""".format(num_GamesWon_user,num_GamesWon_pc))
    print("Each player has 26 cards sorted and splitted cards: (list form)")
    Deck = initializeDeck()
    Deck = shuffleDeck(Deck)
    SplitDeck = splitDeck(Deck)
    ActualDeck = SplitDeck
    copy = SplitDeck.copy()
    copy_of_Deck = sortDeck(copy)
    user_cards = distributeCards_user(ActualDeck)
    pc_cards = distributeCards_pc(ActualDeck)
    print(f"user cards are: {user_cards}")
    print(f"pc cards are: {pc_cards}")
    
    
    
def main():
    title = """
.------..------..------.     .------..------..------..------.     .------..------..------..------.
|W.--. ||A.--. ||R.--. |.-.  |C.--. ||A.--. ||R.--. ||D.--. |.-.  |G.--. ||A.--. ||M.--. ||E.--. |
| :/\: || (\/) || :(): ((5)) | :/\: || (\/) || :(): || :/\: ((5)) | :/\: || (\/) || (\/) || (\/) |
| :\/: || :\/: || ()() |'-.-.| :\/: || :\/: || ()() || (__) |'-.-.| :\/: || :\/: || :\/: || :\/: |
| '--'W|| '--'A|| '--'R| ((1)) '--'C|| '--'A|| '--'R|| '--'D| ((1)) '--'G|| '--'A|| '--'M|| '--'E|
`------'`------'`------'  '-'`------'`------'`------'`------'  '-'`------'`------'`------'`------'
"""
    print(title)

    Deck = initializeDeck() #here we initialize the deck

    print("..Shuffling..the..Decks...")
    print()
    Deck = shuffleDeck(Deck) #here we shuffle the deck
    
    SplitDeck = splitDeck(Deck) #here we cut the 52 cards into two and put the top to the bottom
    
    ActualDeck = SplitDeck #we assign the actual deck 

    copy = SplitDeck.copy() #we assign the copy of the deck
    
    copy_of_Deck = sortDeck(copy) #we sort the copy of the deck

    print("user cards: 26 total")
    print("This were your first 3 cards:")
    user_cards = distributeCards_user(ActualDeck)
    for i in range(0,3):
        if user_cards[i] == 1:
            print(card_1, end= "")
        elif user_cards[i] == 2:
            print(card_2, end= "")
        elif user_cards[i] == 3:
            print(card_3, end= "")
        elif user_cards[i] == 4:
            print(card_4, end= "")
        elif user_cards[i] == 5:
            print(card_5, end= "")
        elif user_cards[i] == 6:
            print(card_6, end= "")
        elif user_cards[i] == 7:
            print(card_7, end= "")
        elif user_cards[i] == 8:
            print(card_8, end= "")
        elif user_cards[i] == 9:
            print(card_9, end= "")
        elif user_cards[i] == 10:
            print(card_10, end= "")
        elif user_cards[i] == 11:
            print(card_11, end= "")
        elif user_cards[i] == 12:
            print(card_12, end= "")
        elif user_cards[i] == 13:
            print(card_13, end= "")
    print("pc cards: 26 total")
    print("This were the pc first 3 cards:")
    pc_cards = distributeCards_pc(ActualDeck)
    for i in range(0,3):
        if pc_cards[i] == 1:
            print(card_1, end= "")
        elif pc_cards[i] == 2:
            print(card_2, end= "")
        elif pc_cards[i] == 3:
            print(card_3, end= "")
        elif pc_cards[i] == 4:
            print(card_4, end= "")
        elif pc_cards[i] == 5:
            print(card_5, end= "")
        elif pc_cards[i] == 6:
            print(card_6, end= "")
        elif pc_cards[i] == 7:
            print(card_7, end= "")
        elif pc_cards[i] == 8:
            print(card_8, end= "")
        elif pc_cards[i] == 9:
            print(card_9, end= "")
        elif pc_cards[i] == 10:
            print(card_10, end= "")
        elif pc_cards[i] == 11:
            print(card_11, end= "")
        elif pc_cards[i] == 12:
            print(card_12, end= "")
        elif pc_cards[i] == 13:
            print(card_13, end= "")
    #Here starts the Battle!
    print("The Battle Began!!")

    for i in range(0,len(user_cards)):
        if user_cards[i] == pc_cards[i]:
            if user_cards[3] > pc_cards[3]:
                user_cards = distributeCards(user_cards, pc_cards)
            elif user_cards[3] < pc_cards[3]:
                pc_cards = distributeCards(pc_cards, user_cards)
        elif user_cards[i] > pc_cards[i]:
            user_cards = distributeCards(user_cards, pc_cards)
        elif user_cards[i] < pc_cards[i]:
            pc_cards = distributeCards(pc_cards, user_cards)

    check_pccards = len(pc_cards)
    check_usercards = len(user_cards)

    if check_pccards > check_usercards:
        print("PC Won the Game !!!!")
        print(";^)")
        botwon = 0
        return botwon
    if check_pccards < check_usercards:
        print("User Wins the Game!!!!")
        name = input("Write your Initials: ")
        print("""
            '._==_==_=_.'
            .-\:      /-.
           | (|:{} |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`
""".format(name))
        print(":^(")
        userwon = 1
        return userwon

 
if __name__ == "__main__": #were the program starts

    # values that are going to be saved and used to calculate the matchs won
    num_Games = 0
    num_GamesWon_user = 0
    num_GamesWon_pc = 0
    
    print("Menu:")
    print("""
1. Play = 1
2. Display Scores = 2
3. Display Cards = 3
4. Win Percentage = 4
5. Quit = 5
""")
    remote = True #loop controller

    while remote:
        options = int(input("Choose on of the following(use only numbers): "))

        if options == 1: #enter the game if input is 1
            x = main()
            num_Games +=1 #when finishing the game we count 1 game
            if x == 1: #if the user wins the game will return 1 and here we will add one win to the user
                num_GamesWon_user +=1
                print()
            if x == 0: #if the computer wins the game returns 0 and we add here one win to the pc
                num_GamesWon_pc +=1
                print()
            
        elif options == 2: #sends you to the score menu
            DisplayScore(num_GamesWon_user,num_GamesWon_pc) 
        elif options == 3: #Shows you the cards in decending order
            DisplayCards()
        elif options == 4: #sends you to the percentage win menu
            WinPercentage(num_Games,num_GamesWon_user,num_GamesWon_pc)
        elif options == 5: #exits the game with 5 as input
            print("Thanks for playing!, :^)")
            remote = False
            break
        else: # if user inputs a different number, the pc will not understand
            print("""
I don't understand you.  :^/
(use numbers from 1 to 5)
""")
