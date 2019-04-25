print("...rock...")
print("...paper...")
print("...scissors...")
player1 = input("Enter Player 1's choice: ")
player2 = input("Enter Player 2's choice: ")
print("SHOOT!")


if player1 == 'rock' and player2 == 'rock':
    print("Tie Game")
elif player1 == 'rock' and player2 == 'paper':
    print("player2 wins")
elif player1 == 'rock' and player2 == 'scissors':
    print("player1 wins")
elif player1 == 'scissors' and player2 =='scissors':
    print("Tie Game")
elif player1 == 'scissors' and player2 == 'rock':
    print("player2 wins")
elif player1 == 'scissors' and player2 == 'paper':
    print("player1 wins")
elif player1 == 'paper' and player2 == 'paper':
    print("Tie Game")
elif player1 == 'paper' and player2 == 'scissors':
    print("player2 wins")
elif player1 == 'paper' and player2 == 'rock':
    print("player1 wins")
else: 
    print("something went wrong")