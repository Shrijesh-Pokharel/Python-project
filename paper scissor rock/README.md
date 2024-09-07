 # Rock, Paper, Scissor Game

This is a simple implementation of the classic game Rock, Paper, Scissor using Python. The game is played between a user and a computer opponent. The computer randomly selects an option from the three possible actions: Rock, Paper, or Scissor. The user inputs their chosen action. The winner of the game is determined by the following rules:

Rock crushes Scissor, so the user wins.
Scissor cuts Paper, so the user wins.
Paper covers Rock, so the user wins.
If both players choose the same action, the game is a tie.

## How to Play
Run the code.
The program will prompt you to enter your choice: `rock`, `paper`, or `scissor`.
Enter your choice and press enter.
The program will display the result of the game.
## Code Explanation
The code starts by importing the `random` module to enable random selection of the computer's move.

Next, the program prompts the user to enter their choice using the `input()` function. The `user's input` is stored in the user_action variable.

The `possible_action` list contains the three possible actions that the user and computer can take. The computer's choice is made by selecting an element randomly from this list using the `random.choice()` function. The computer's choice is assigned to the `opponent_action` variable.

The code then prints out the user's and computer's choices, and checks if the user's choice is the same as the computer's choice. If they are the same, the game is a tie.

If the user's choice is not the same as the computer's choice, the code checks if the user's choice is a winning move based on the rules outlined above. If the user's choice is a winning move, a message is displayed indicating that the user has won. Otherwise, a message is displayed indicating that the user has lost.

## Conclusion
This is a simple and fun implementation of the classic game Rock, Paper, Scissor. With the code provided, you can play the game anytime you want.
