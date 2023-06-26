import turtle as t
from random import randint

# setup


class CellularAutomata:

    def __init__(self, cell_size, grid_width, grid_height):
        self.CELL_SIZE = cell_size

        # init turtle graphics
        self.turtle = t.Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.speed(0)
        t.tracer(0,0)
        
        self.screen = t.Screen()
        self.screenTk = self.screen.getcanvas().winfo_toplevel()
        self.screenTk.attributes("-fullscreen", True)

        # init grid
        self.grid_width = grid_width
        self.grid_height = grid_height
        gridline = [0 for _ in range(grid_width)]
        self.grid = [list(gridline) for _ in range(grid_height)]

    # Output a textual represention of the grid
    def debug_grid(self):
        for row in self.grid:
            for cell in row:
                print(cell, end=" ")
            print()
        print()

    # Set a specific cell's value
    def set_cell(self, x, y, val, draw):
        self.grid[y][x] = val
        if draw:
            self.draw_cell(x * self.CELL_SIZE, y * self.CELL_SIZE, val)

    # Fetch a specific cell's value
    def get_cell(self, x, y):
        return self.grid[y][x]

    # Used instead of turtle.setpos so that the coords are centered
    # at the top right and Y increases further down the screen
    def move_turtle(self, x, y):
        padding = 25
        screen_width = self.screen.window_width()
        screen_height = self.screen.window_height()
        start_x = -screen_width / 2
        start_y = screen_height / 2
        x_pos = start_x + (x + padding)
        y_pos = start_y - (y + padding)
        self.turtle.goto(x_pos, y_pos)

    def draw_cell(self, x, y, val):
        self.move_turtle(x, y)
        self.turtle.penup()

        if val == 0:
            self.turtle.fillcolor("white")
        elif val == 1:
            self.turtle.fillcolor("black")
        elif val == 2:
            self.turtle.fillcolor("red")
        
        self.turtle.begin_fill()
        for _ in range(4):
            self.turtle.forward(self.CELL_SIZE)
            self.turtle.right(90)
        self.turtle.end_fill()

        t.update()
    
    def update(self):
        x_pos = randint(0, self.grid_width-1)
        y_pos = randint(0, self.grid_height-1)
        value = randint(0, 2)
        self.set_cell(x_pos, y_pos, value, True)

    def full_render(self):
        self.turtle.clear()

        for x in range(self.grid_width):
            for y in range(self.grid_height):
                
                x_pos = x * self.CELL_SIZE
                y_pos = y * self.CELL_SIZE
                cell = self.get_cell(x, y)
                
                self.draw_cell(x_pos, y_pos, cell)
        
        t.update()


e = CellularAutomata(2, 100, 100)

while True:
    e.update()