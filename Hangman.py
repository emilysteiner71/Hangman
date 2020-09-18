#Welcome to my Hangman Python game!

#The computer gets a random word from the word list. The user will have to guess this word
import random
lines = open("wordlist.txt", "r").read().splitlines()
myline = random.choice(lines)
blanks = list("_" * len(myline))

print ("HHH     HHH                 NNNN       NN  GGGGGGGGGGG  MMMMM             MMMMM                 NNNN       NN")
print ("HHH     HHH        A        NNNNNN     NN  GGGGGGGGGGG  MMMMMM           MMMMMM        A        NNNNNN     NN")
print ("HHH     HHH       A A       NNN NNN    NN  GG           MMM MMM         MMM MMM       A A       NNN NNN    NN")
print ("HHHHHHHHHHH      A   A      NNN  NNN   NN  GG           MMM  MMM       MMM  MMM      A   A      NNN  NNN   NN")
print ("HHHHHHHHHHH     AAAAAAA     NNN   NNN  NN  GG           MMM   MMM     MMM   MMM     AAAAAAA     NNN   NNN  NN")
print ("HHHHHHHHHHH     AAAAAAA     NNN    NNN NN  GG    GGGGG  MMM    MM     MM    MMM     AAAAAAA     NNN    NNN NN")
print ("HHH     HHH    AA     AA    NNN     NNNNN  GG       GG  MMM     MM   MM     MMM    AA     AA    NNN     NNNNN")
print ("HHH     HHH   AA       AA   NNN      NNNN  GGGGGGGGGGG  MMM      MMMMM      MMM   AA       AA   NNN      NNNN")
print ("HHH     HHH  AA         AA  NNN       NNN  GGGGGGGGGGG  MMM       MMM       MMM  AA         AA  NNN       NNN")

print ()
input("Press enter to start")
print ("The computer has selected a word. It's your job to figure out what it is by guessing letters. But be careful! Each wrong answer will add to the hangman :o Get 6 wrong and you lose!")
print (" ".join(blanks))
print()
print ("Your man:")
print ("_________")
print ("||     |")
print ("||")
print ("||")
print ("||")
print ("||")
print ("||")
print ("==========                    wrong attempts: ")

incorrect_answers = 0
wrong_answers = list("")
while incorrect_answers < 6:
    letter = input("Please enter a lowercase letter: ")
    found = False
    for x in range(len(myline)):
       if myline[x] == letter:
           found = True
           blanks[x] = letter
    if found:
        print (" ".join(blanks))
        empty = 0
        for x in blanks:
            if x == "_":
                empty += 1
        if empty == 0:
            print ("Congratulations! The word was %s. You won!" % myline)
            incorrect_answers = 9

    else:
        print ("Sorry, that's not a correct letter")
        wrong_answers.append(letter)
        incorrect_answers += 1
        if incorrect_answers == 1:
            print (" ".join(blanks))
            print()
            print ("Your man:")
            print ("_________")
            print ("||     |")
            print ("||    /`\\")
            print ("||    |_|")
            print ("||")
            print ("||")
            print ("||")
            print ("==========                    wrong attempts: %s" % (" ".join(wrong_answers)))
        elif incorrect_answers == 2:
            print (" ".join(blanks))
            print()
            print ("Your man:")
            print ("_________")
            print ("||     |")
            print ("||    /`\\")
            print ("||    |_|")
            print ("||     |")
            print ("||     |")
            print ("||")
            print ("==========                    wrong attempts: %s" % (" ".join(wrong_answers)))
        elif incorrect_answers == 3:
            print (" ".join(blanks))
            print()
            print ("Your man:")
            print ("_________")
            print ("||     |")
            print ("||    /`\\")
            print ("||    |_|")
            print ("||   --|")
            print ("||     |")
            print ("||")
            print ("==========                    wrong attempts: %s" % (" ".join(wrong_answers)))
        elif incorrect_answers == 4:
            print (" ".join(blanks))
            print()
            print ("Your man:")
            print ("_________")
            print ("||     |")
            print ("||    /`\\")
            print ("||    |_|")
            print ("||   --|--")
            print ("||     |")
            print ("||")
            print ("==========                    wrong attempts: %s" % (" ".join(wrong_answers)))
        elif incorrect_answers == 5:
            print (" ".join(blanks))
            print()
            print ("Your man:")
            print ("_________")
            print ("||     |")
            print ("||    /`\\")
            print ("||    |_|")
            print ("||   --|--")
            print ("||     |")
            print ("||    /")
            print ("==========                    wrong attempts: %s" % (" ".join(wrong_answers)))
        elif incorrect_answers == 6:
            print (" ".join(blanks))
            print()
            print ("Your man:")
            print ("_________")
            print ("||     |")
            print ("||    /`\\")
            print ("||    |_|")
            print ("||   --|--")
            print ("||     |")
            print ("||    / \\")
            print ("==========                    wrong attempts: %s" % (" ".join(wrong_answers)))
            print ("You let your man die! You lose!")
            print ("The word was %s" %myline)












