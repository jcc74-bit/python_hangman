# Program ID: Word Guesser
# Author: Jiaxin Chen
# Purpose: Make a word guesser game

#initalize variable 
cg= []
bg= 7
invalid=True
play_again="yes"
incorrect_guess= []

#play again loop
while(play_again=="yes"):
    cg.clear()
    #getting a word
    word=input("enter a word for someone to guess: ")
    charlist= list(word)
    letters= len(charlist)
    print ("there are " + str(letters) + " letters in this word")
    #blank spaces for the wprd
    for i in range (letters):
        cg.append("_")
    while bg>0 and "_" in cg:
        print(" ")
        print (" ".join(cg))
        print ("you have " + str(bg) + " more chances")
        guess = input("guess the word or choose a letter: ").lower()
        #if thw word is guessed
        if guess == word:
            print("congrats you win")
            break
        #if the letters are all guessed      
        elif guess in charlist:
            for letter in range(letters):
                if charlist[letter] == guess:
                  cg[letter]=guess
            print("congrats correct guess. If you knpw the word, type the full word.")
        #if the letter if wrong
        else:
            bg=bg-1
            print("not in the word, you suck. " + str(bg) + " more chances left")
            #prints bad guess list
            incorrect_guess.append(guess)
            print (incorrect_guess)
        #no more chances   
        if bg==0:
            print("you lose, youre so bad at this. The word was: " + str(word) + " . Wasnt it obvious? ")
            print (incorrect_guess)
    #checks if input for play again is right        
    while(invalid): 
        play_again = input("Do you want to play again? (yes/no): ")
        if (play_again=="yes" ):
          user_input=""
          invalid=False
        elif(play_again=="no"):
          invalid=False
        else:
          print("Invalid input. Please enter yes or no." )
#tells them game over
print("game over")
