import random

money = 100
#Write your game of chance functions here
def get_game() :
    print("Please select what game you'd like to play : CoinFlip, Cho-Han, Cards, Roulette")
    return input()

def get_coin_flip(bet, call) : 
    flip = random.randint(0,1)
    if (flip == call):
        bet += bet
        print("You called it correctly! You won " + str(bet) + " dollars")
        return bet
    else :
        bet = -bet
        print("You lost : " + str(bet) + " dollars! Sorry!")
        return bet

def get_dice_roll(bet, call) : 
    roll_1 = random.randint(1,6)
    roll_2 = random.randint(1,6)
    total_roll = roll_1 + roll_2
    if (total_roll%2 == 0) and (call == True) :
        bet += bet
        print("You called it correctly! You won " + str(bet) + " dollars")
        return bet
    if not(total_roll%2 == 0) and (call == False) : 
        bet += bet
        print("You called it correctly! You won " + str(bet) + " dollars")
        return bet
    else : 
        bet = -bet
        print("You lost : " + str(bet) + " dollars! Sorry!")
        return bet

def get_card_pick(bet) : 
    cardlist = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
    cardpickc = random.randint(1,4)
    print(cardpickc)
    cardpickr = random.randint(1,13)
    print(cardpickr)
    card1 = cardlist[cardpickc][cardpickr]
    del cardlist[cardpickc][cardpickr]
    cardpickc = random.randint(0,3)
    cardpickr = random.randint(0,12)
    card2 = cardlist[cardpickc][cardpickr]
    del cardlist[cardpickc][cardpickr]
    if (card1 > card2) : 
        bet += bet
        print("You got the higher card! You won " + str(bet) + " dollars")
        return bet
    if (card2 > card1) : 
        bet = -bet
        print("You lost : " + str(bet) + " dollars! Sorry!")
        return bet
    elif (card1 == card2) : 
        print ("It was a tie!")
        return 0;

def get_roulette_spin(bet, call, call_type) : 
    roulette_number = random.randint(0,37)
    if (roulette_number == 37):
        roulette_number = 0
    if (call_type == "Number") : 
        if (call == roulette_number): 
            bet += bet
            print("You guessed the correct number! You won " + str(bet) + " dollars")
            return bet
        else: 
            bet = -bet
            print("You lost : " + str(bet) + " dollars! Sorry!")
            return bet
    if (call_type == "Odd or Even") : 
        if (roulette_number == 0):
            bet = -bet
            print("You lost : " + str(bet) + " dollars! Sorry!")
            return bet
        if (call == "Odd") and (roulette_number%2 != 0):
            bet += bet
            print("You guessed correct! You won " + str(bet) + " dollars")
            return bet
        if (calll == "Even") and (roulette_number%2 == 0):
            bet += bet
            print("You guessed correct! You won " + str(bet) + " dollars")
            return bet
        else : 
            bet = -bet
            print("You lost : " + str(bet) + " dollars! Sorry!")
            return bet
    return
   
def run_game_coinflip():
    global money
    print("How much would you like to bet?")
    bet = int(input())
    if (bet >= 0 ) and (bet <= money) : 
        print("Would you like to call head or tails?")
        call = input()
        if (call == "heads"):
            call = 1
        else:
            call = 0
        money += get_coin_flip(bet, call)
        print("You now have " + str(money) + " dollars to bet")
    else : 
        print("The bet amount is invalid, please try again")
        return

def run_game_cho_han():
    global money
    print("How much would you like to bet?")
    bet = int(input())
    if (bet >= 0 ) and (bet <= money) : 
        print("Would you like to call even or odds?")
        call = input()
        if (call == "even"):
            call = True
        else:
            call = False
        money += get_dice_roll(bet, call)
        print("You now have " + str(money) + " dollars to bet")
    else : 
        print("The bet amount is invalid, please try again")
        return

def run_game_cards() : 
    global money
    print("How much would you like to bet?")
    bet = int(input())
    if (bet >= 0 ) and (bet <= money) : 
        money += get_card_pick(bet)
        print("You now have " + str(money) + " dollars to bet")
    else : 
        print("The bet amount is invalid, please try again")

def run_game_roulette() :
    global money
    print("How much would you like to bet?")
    bet = int(input())
    if (bet >= 0 ) and (bet <= money) : 
        print("What type of Call would you like to make? (Odd or Even) or (Number)")
        call_type = input()
        if (call_type == "Number"):
            print("What number would you like to call? (1 to 36)")
            call = int(input())
        elif (call_type == "Odd or Even"): 
            print("What do you think it'll be, Odd or Even?")
            call = input()
        money += get_roulette_spin(bet, call, call_type)
        print("You now have " + str(money) + " dollars to bet")
        return;
    else : 
        print("The bet amount is invalid, please try again")
        return;

def determine_game(game_choice) : 
    if (game_choice == "CoinFlip") or (game_choice == "coin flip") or (game_choice == "Coin flip") or (game_choice == "Coin Flip") or (game_choice == "coinflip"):
        run_game_coinflip()
    
    elif (game_choice == "Cho-Han") or (game_choice == "Cho han") or (game_choice == "Cho-han") or (game_choice == "Cho Han") or (game_choice == "cho han"): 
        run_game_cho_han()

    elif (game_choice == "Cards")  or (game_choice == "cards") or (game_choice == "card") : 
        run_game_cards()

    elif (game_choice == "Roulette")  or (game_choice == "roulette"): 
        run_game_roulette()
    else : 
        print ("We could not figure out what you wanted to play, please try again")
        return;


#Call your game of chance functions here
game_choice = get_game()
determine_game(game_choice)


