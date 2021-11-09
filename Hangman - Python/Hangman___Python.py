import random
import os

#gen_word takes the difficulty and returns a random word from file word_list
#word returned is selected based on length of the word
#if difficulty is "easy" randomly generate a word <= 4 characters
#if difficulty is "medium" randomly generate a word 5 or 6 characters
#if difficulty is "hard" randomly generate a word > 6 characters
def gen_word(difficulty):
    word = (random.choice(open("word_list.txt").read().split()))
    if difficulty == "easy":
        while(len(word) > 4):
            word = (random.choice(open("word_list.txt").read().split()))
    elif difficulty == "medium":
        while ((len(word) <= 4) or (len(word) > 6)):
            word = (random.choice(open("word_list.txt").read().split()))
    else: 
        while (len(word) <= 6):
            word = (random.choice(open("word_list.txt").read().split()))
    return (word)

#Run program until user enters a quit character value
while(True):
    try:
        diff = input("choose difficulty\n1 - easy\n2- medium\n3 - hard\nOther to quit\n")
        if diff == '1':
            word = (gen_word("easy"))
        elif diff == '2':
            word = (gen_word("medium"))
        elif diff == '3':
            word = (gen_word("hard"))
        else:
            break

        old_correct = 100
        letterList = []
        remaining = 6
        #iterate through ever character in word and print _ in it's place
        #this lets users know the str len
        for c in word:
            print("_", end='')
        print()
        while (remaining != 0):
            correct = 100
            print("You have ", remaining, "attempts remaining")
            letter = input("choose a letter:")
            letterList.append(letter)
            print(letterList)
            for c in word:
                if c in letterList:
                    print(c, end='')
                    correct = correct + 1
                else:
                    print("_", end='')
            print()
            if correct == len(word):
                print("Congratulations! You Won!\n")
                break
            if correct == old_correct:
                remaining = remaining - 1
            old_correct = correct
            print()
        print(word)
            
    except:
        print ("try again")