import random

class Minesweeper:
    def __init__(self, grid_size, mine_count):
        '''
        Initializes the Minesweeper game with a specified grid size and number of mines.
        
        :param grid_size: Size of the grid (e.g., 5 for a 5x5 grid)
        :param mine_count: Number of mines to be placed on the board
        '''
        self.grid_size = grid_size
        self.mine_count = mine_count
        self.board = self._generate_empty_board()
        self.mines = []

    def _generate_empty_board(self):
        '''
        Generates an empty grid of the specified size filled with zeros.
        
        :return: A 2D list representing the empty board
        '''
        return [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def _place_mines(self, exclude_row, exclude_col):
        '''
        Places mines randomly on the board, ensuring the first clicked cell is not a mine.
        
        :param exclude_row: Row index of the first clicked cell
        :param exclude_col: Column index of the first clicked cell
        '''
        mines_placed = 0
        while mines_placed < self.mine_count:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            
            # Ensure the mine is not placed on the first clicked cell and not on an already existing mine
            if (row != exclude_row or col != exclude_col) and self.board[row][col] != -1:
                self.board[row][col] = -1
                self.mines.append((row, col))
                mines_placed += 1

    def _update_numbers(self):
        '''
        Updates the numbers on the board to indicate the count of adjacent mines for each cell.
        '''
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.board[row][col] == -1:
                    self._increment_numbers_around(row, col)

    def _increment_numbers_around(self, row, col):
        '''
        Increments the mine count for cells surrounding a newly placed mine.
        
        :param row: Row index of the mine
        :param col: Column index of the mine
        '''
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < self.grid_size and 0 <= j < self.grid_size and self.board[i][j] != -1:
                    self.board[i][j] += 1

    def first_click(self, row, col):
        '''
        Handles the first click by placing mines and updating the board.
        
        :param row: Row index of the first clicked cell
        :param col: Column index of the first clicked cell
        :return: The updated board
        '''
        self._place_mines(row, col)
        self._update_numbers()
        return self.board

    def print_board(self):
        '''
        Prints the current state of the board.
        '''
        for row in self.board:
            print(' '.join(f'{cell:2}' for cell in row))

    def get_mine_positions(self):
        '''
        Returns the positions of all mines.
        
        :return: A list of tuples representing the positions of the mines
        '''
        return self.mines

def main():
    '''
    Main function to run the Minesweeper game. Handles user input and game flow.
    '''
    # Get user input for grid size and number of mines, with validation
    while True:
        try:
            grid_size = int(input("Please enter the grid size: "))
            mine_count = int(input("Please enter the number of mines: "))
            if mine_count >= grid_size * grid_size:
                print("The number of mines must be less than the total number of cells. Please enter again.")
            else:
                break
        except ValueError:
            print("Please enter valid numbers.")

    # Initialize the game with user input
    game = Minesweeper(grid_size, mine_count)
    print('Initial board:')
    game.print_board()

    # Get user input for the first click position, with validation
    while True:
        try:
            first_click_row = int(input(f"Please enter the row of the first click (0 to {grid_size - 1}): "))
            first_click_col = int(input(f"Please enter the column of the first click (0 to {grid_size - 1}): "))
            if 0 <= first_click_row < grid_size and 0 <= first_click_col < grid_size:
                break
            else:
                print("Please enter valid row and column numbers.")
        except ValueError:
            print("Please enter valid numbers.")

    # Update the board based on the first click
    updated_board = game.first_click(first_click_row, first_click_col)
    print('Board after first click:')
    game.print_board()

    # Display the positions of all mines
    mine_positions = game.get_mine_positions()
    print('Mine positions:', mine_positions)

if __name__ == "__main__":
    main()
