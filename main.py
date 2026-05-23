from data.idgen import idlist
from data.comparerfunc import cardcompare
import random

def main():
    print("Welcome to Guess the Spire! This is a guess game based on Slay the Spire 2")
    close_game = False
    while close_game == False:
        print("1. Start game")
        print("2. Information")
        print("3. Quit")

        choice = input(">")
        if choice == "1":
            picked = random.choice(list(idlist.keys()))
            pickid = idlist[picked]
            matched = {
                "Colour": "Unknown",
                "Energy Cost": "Unknown",
                "Card Type": "Unknown",
                "Card Rarity": "Unknown",
                "Tags": ["Unknown"],
            }
            forfeit = False
            print("A card has be chosed, try to guess it!")
            while forfeit == False:
                guess = input(">").lower()
                if guess == "quit" or guess == "ff":
                    print(f"The picked card was {picked}")
                    forfeit = True
                elif guess not in list(idlist.keys()):
                    print("Sorry, I don't recognize that card, check your spelling and try again.")
                else:
                    guessid = idlist[guess]
                    if guessid == pickid:
                        print(f"Congrats! You successfully guessed that {guess} was the picked card!")
                        break
                    cardcompare(pickid, guessid, matched)
                    print(f"Looks like {guess} wasn't the picked card. Let's see the info you got so far!")
                    for key, value in list(matched.items()):
                        print(f"{key}: {value}")

                    print("Take another guess!")


        elif choice == "2":
            print("The game picks a card from the ingame cards,")
            print("then you input a card name and the game tells you if there are any values in common.")
            print("The game ends once you guess the right card.")
            print("The guesses must be properly written (spaces, etc).")
            print("If the game doesn't recognize your imput try checking your spelling!")
            print("Remember! If you want to stop playing mid run you can alway type 'Quit' or 'ff'.")
            print ("-" * 20)
        
        elif choice == "3":
            print("Thanks for playing Guess the Spire!")
            close_game = True

        else:
            print("Invalid choice, choose again.")

    
if __name__ == "__main__":
    main()