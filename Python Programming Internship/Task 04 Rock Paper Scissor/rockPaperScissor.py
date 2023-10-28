import random as rd

listChoices = ["Rock","Paper","Scissor"]
life = 3
point = 0
botPoints = 0
print("\n\n")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("|||||||||||||||||||||||| ROCK, PAPER & SCISSOR ||||||||||||||||||||||||||||\n")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("\n\n")

print("BOT: Hey, Let's play rock,paper and scissor game.\n")
while(1):
    print(f"                                                          LIFE : {life}")
    print(f"                                                          YOUR POINTS : {point}")
    print(f"                                                          BOT POINTS : {botPoints}")
    if life==0:
        print("You have no more lifes to play...")
        print("\nBOT: Do You want to play again ? ")
        ask = input("You: ")
        if ask.lower()=="yes":
            life = 3
            point=0
            botPoints=0
            continue
        else:
            break
    else:
        print("BOT: Pick one, Rock, Paper or Scissor ?\n")
        botChoice = rd.choice(listChoices)
        select = input("Select: ")
        if select == "Rock" and botChoice == "Scissor":
            print(f"BOT: {botChoice}")
            print("BOT: You Win :( ")
            point+=1
        if select == "Rock" and botChoice == "Paper":
            print(f"BOT: {botChoice}")
            print("BOT: I Win! :) ")
            botPoints+=1
            life-=1
        if select == "Rock" and botChoice == "Rock":
            print(f"BOT: {botChoice}")
            print("BOT: Tie!")
        if select == "Paper" and botChoice == "Paper":
            print(f"BOT: {botChoice}")
            print("BOT: Tie! ")
        if select == "Paper" and botChoice == "Rock":
            print(f"BOT: {botChoice}")     
            print("BOT: You Won!! :(")
            point+=1
        if select == "Paper" and botChoice == "Scissor":
            print(f"BOT: {botChoice}")
            print("BOT: I Won!! :) *|*  ")
            life-=1
            botPoints+=1
        if select == "Scissor" and botChoice == "Paper":
            print(f"BOT: {botChoice}")
            print("BOT: You won :( I lose...... ")
            point+=1
        if select == "Scissor" and botChoice == "Rock":
            print(f"BOT: {botChoice}")
            print("BOT: I won!! :) haha!")
            botPoints+=1
            life-=1
        if select == "Scissor" and botChoice == "Scissor":
            print(f"BOT: {botChoice}")
            print("BOT: Tie! ")

    