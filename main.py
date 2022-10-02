import random as rd
import math

#taking inputs

l = int(input("Enter the lower bound of the range :"))
u = int(input("Enter the upper bound of the range :"))

number = rd.randint(l,u)
limit = round(math.log(u - l + 1, 2)) 
print("\n\tYou've to Guess the number in ",limit," chances!\n")
count = 0
while count < limit :
    count += 1
    guess_number = int(input("Guess the number ! : "))
    if guess_number == number:
        print("Congratulations ! /n You Won!")
        print("You Guess the number correctly ! in ",count,"try")
        break
    elif number > guess_number:
        print("you guessed too small !")
    elif number < guess_number:
        print('you guessed to big number !')
if count >= limit:
    print("Sorry !You have Crossed the Limit")
    print("Better Luck Next Time!")        