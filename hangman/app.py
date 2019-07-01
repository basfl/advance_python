
from game_util import gen_word


def play_game(random_word):
    #random_word = gen_word()
    my_guess = []
    """
    creating list with same length as generated word
    and assign initial * to each index
    """
    [my_guess.append("*") for i in range(len(random_word))]
#print(f"my guess is {my_guess}")
    cnt = 0
    correct_guess = 0
    guessed_character_set = set()
    while cnt < 3:
        #print(f"correct_guess={correct_guess} and random_word ={len(random_word)}")
        if correct_guess == len(random_word):
            print("You won !!!!")
            break
        print(my_guess)
        guess =input("please guess a character:\n")
        if len(guess) == 1:
            if guess not in guessed_character_set:
                guessed_character_set.add(guess)
                if guess in random_word:
                    print("you guess correct \n")
                    rs = [i for i, ltr in enumerate(
                        random_word) if ltr == guess]
                    correct_guess = correct_guess+len(rs)
                    for i in range(len(rs)):
                        my_guess[rs[i]] = guess
                else:
                    print("sorry guess wrong \n")
                    cnt = cnt+1
            else:
                print("you already tried this character!!!")
        else:
            print("please enter only one character !!!")
            continue
    print("sorry you lost!!!")


##############################################
if __name__ == "__main__":
    play_game(gen_word())
