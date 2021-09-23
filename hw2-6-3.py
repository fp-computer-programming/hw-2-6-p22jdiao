# Author: JD 09/23/2021

ft = int(input("number of free throw:"))

twopts = int(input("number of 2 points:"))

threepts = int(input("number of 3 points:"))


score = ft + 2 * (twopts) + 3 * (threepts)

print("The player scored", score, "points in the game.")
