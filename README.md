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

```python main.py```

### Usage
The application provides a GUI to easily solve a matrix game. Simply follow these steps:

1. Run the application using the command above.

2. Enter the matrix dimensions (row first, and then the column) and enter if the row player is the maximiser or the minimiser.
   Usually, for a two-player, zero-sum game, the matrix represents the payoffs for the row player - so in this case, the row player is the maximiser.
   After entering the inputs, click "Enter".

3. Now, the application will display a scrollable area (canvas) containing entry fields to enter the payoffs.
   You may have to scroll horizontally and vertically to enter all the values.

4. If you need to change the matrix dimensions or if the row player is the maximiser or miniser, you can click "Go Back!".
   Otherwise, once the matrix values are inputted press "Enter".

5. Finally, the application will show the value of the matrix game in a smaller boxed region starting with "Output - ... ".
   The blue link with "Open csv file" allows you to take a look at the optimal probabilities of each strategy. 
   
The application will then display the solution, including the optimal strategies for both players and the value of the game.

#### Example Matrix:
For the following payoff matrix:

$$ x + y = 3 $$

The application would calculate the saddle point, optimal strategies, and the value of the game, presenting them clearly in the GUI.
