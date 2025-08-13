# Matrix_Game_Solver
A Python application for solving matrix games using game theory principles, complete with a graphical user interface (GUI). 
This project provides a simple way to input and analyze two-player zero-sum games.

## Getting Started
Follow these steps:

### Prerequisites
Ensure you have Python 3.x installed. The project's dependencies are listed in requirements.txt. You can install them using pip:

```pip install -r requirements.txt```

This project relies on the **Pyomo** optimization package. While you can edit the code in any IDE, Pyomo often requires a specific environment setup to properly find its solvers. 
For this reason, it is best to run the program from an **Anaconda-managed** terminal to avoid errors related to missing dependencies or incorrect system paths.

### Running the Application
In the Anaconda Navigator, check if the **Pyomo** package is installed. In the "Environments" section, search for the **Pyomo** package and install it. Then launch a Python IDE and run the following code in your terminal: 

```python main.py```

### Usage
The application provides a GUI to easily solve a matrix game. Simply follow these steps:

1. Follow the steps outlined in the above section, "Running the Application". 

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

### Example Matrix:
Suppose we have the following matrix. 

$$ 
\begin{pmatrix}
2 & 3 \\
4 & 3
\end{pmatrix} $$

Assuming the row player is the maximiser, the row player will choose strategy 2 (the second row) since $$ 4 > 2 $$ and $$ 3 \geq 3 $$. If the row player chooses the second row, the column player will choose the second column, so the value of the game is $3$. Each player chooses the second strategy with probability 1. Once you've run the program, you'll see this: 

![](screenshots/input_panel_1_none)

We can enter the matrix dimensions ($2 x 2$) and "max" in the last entry field. 

![](screenshots/input_panel_1_filled)

Pressing "Enter" leads to:

![](screenshots/input_panel_2_filled)

Now we can enter the values of the matrix and hit "Enter":

![](screenshots/results_panel)

The value of the game is $3$, as we thought. Opening up the csv file gives:

![](screenshots/csv)
