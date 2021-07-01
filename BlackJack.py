import random


def play_again():
    NT_answer = input("Do you want to play again? (y/n)> ")
    player_answer = str(NT_answer).lower()
    if player_answer == "y":
        play_blackjack()
    else:
        exit()

def play_blackjack():
    player_hand = []
    dealer_hand = []


    player_first_card = random.randint(1, 11)
    player_hand.append(player_first_card)
    dealer_first_card = random.randint(1, 11)
    dealer_hand.append(dealer_first_card)

    print("Your starting hand is " + str(player_hand[0]) + ".")

    while True:
        player_action = input("What do you want to do?\n1. Hit\n2. Stay\n3. Doubledown\n4. Fold\n> ")
        if int(player_action) == 1:
            player_final_card = random.randint(1, 11)
            player_hand.append(player_final_card)
            print("The cards in your hand are " + str(player_hand) + "." + "The current total is: " + str(sum(player_hand)) + ".")
            if sum(player_hand) > 21:
                break
        if int(player_action) == 2:
            break
        if int(player_action) == 3:
            player_final_card = random.randint(1, 11)
            player_hand.append(player_final_card)
            print("The cards in your hand are " + str(player_hand) + "." + "The current total is: " + str(sum(player_hand)) + ".")
            break
        if int(player_action) == 4:
            print("You folded. You lose.")
            break

    dealer_final_card = random.randint(1, 11)
    dealer_hand.append(dealer_final_card)

    print("DEALER: Now let's play!!")
    if sum(player_hand) == 21 and sum(dealer_hand) < 21 or sum(dealer_hand) > 21:
        print("You win!")
        play_again()
    elif sum(player_hand) > 21 or sum(dealer_hand) == 21:
        print("You bust!")
        play_again()
    elif sum(player_hand) < sum(dealer_hand) or sum(player_hand) == sum(dealer_hand):
        print("You lose!")
        play_again()
