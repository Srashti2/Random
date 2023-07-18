list= ["camel","horse","cow","donkey","pig"]

import random
chosen_word = random.choice(list)
#print(type(chosen_word))
#print(chosen_word)

display = []
no_of_letters= len(chosen_word)
print(no_of_letters)
for i in range(0,len(chosen_word)):
     display.append("_")
print(display)

turns=6
while turns>0:
     print("Hint: Animals")
     guess = input("Please guess the word: ").lower()


     try:
          target_index= chosen_word.index(guess)
          #print(target_index)
     except ValueError:
          print("Please enter another value")

     if chosen_word.__contains__(guess):
          display[target_index]=guess
          while display.__contains__("_") != True:
               turns=0
               print("You Won!")
               break

     else:
          print("You lost one life")
          turns-=1
          print(f"Your remaining turns are {turns}")
          while turns==0:
               print("Game Over")
               print(f"Right Answer was {chosen_word}")     
               break

     print(display)

