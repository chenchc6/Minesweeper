# Minesweeper Game Module

This Minesweeper game module provides the core functionalities for generating a Minesweeper board, placing mines, updating the board after the first click, and retrieving mine positions. 

## Features

- Board generation with a specified grid size and number of mines.
- Placement of mines ensuring the first clicked cell is not a mine.
- Updating numbers around mines to indicate how many mines are adjacent to a cell.
- Retrieving the positions of all mines.
- Printing the board to the console.

## Installation

Follow the instructions below to set up and run the module:

### 1. Clone the Repository

```bash
git clone https://github.com/monniechuang/Minesweeper.git
```

### 2. Ensure Python is Installed

Make sure you have Python 3.6 or higher installed.


### 3. Run the Program

Navigate to the directory and run the program:

```bash
cd Minesweeper
python3 Minesweeper.py
```

## Usage

When you run the program, you will be prompted to enter the grid size, the number of mines, and the position of the first clicked cell. 

1. **Enter the grid size**: This is the size of the Minesweeper board (e.g., enter `5` for a 5x5 grid).
2. **Enter the number of mines**: This is the total number of mines to be placed on the board. The number of mines must be less than the total number of cells.
3. **Enter the position of the first clicked cell**: This is the cell that the user clicks first. The row and column numbers must be within the valid range of the grid.

After entering the required inputs, the program will display the initial board, update the board after the first click, and print the positions of all the mines.

## Example

```plaintext
Please enter the grid size: 5
Please enter the number of mines: 5

Initial board:
 0  0  0  0  0
 0  0  0  0  0
 0  0  0  0  0
 0  0  0  0  0
 0  0  0  0  0

Please enter the row of the first click (0 to 4): 2
Please enter the column of the first click (0 to 4): 2

Board after first click:
 1  1  1  0  0
 1 -1  1  0  0
 1  2  2  1  1
 0  1 -1  2 -1
 0  1  2 -1  1

Mine positions: [(1, 1), (3, 2), (3, 4), (4, 3), (2, 4)]

```

