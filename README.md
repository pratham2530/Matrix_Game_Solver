# Matrix_Game_Solver
A Python application for solving matrix games using game theory principles, complete with a graphical user interface (GUI). 
This project provides a simple way to input and analyze two-player zero-sum games.

## Getting Started
Follow these steps:

### Prerequisites
Ensure you have Python 3.x installed. The project's dependencies are listed in requirements.txt. You can install them using pip:

```pip install -r requirements.txt```

### Running the Application
After installing the dependencies, you can start the application by running the main Python file from your terminal:

python main.py

### Usage
The application provides a GUI to easily solve a matrix game. Simply follow these steps:

Run the application using the command above. A window with a grid for the matrix will appear.

Enter the values for your payoff matrix into the grid. For a two-player, zero-sum game, the matrix represents the payoffs for the row player.

Click the "Solve" or a similar button in the interface.

The application will then display the solution, including the optimal strategies for both players and the value of the game.

Example Matrix:
For the following payoff matrix:

[ 4,  2 ]
[ 1,  5 ]

The application would calculate the saddle point, optimal strategies, and the value of the game, presenting them clearly in the GUI.
