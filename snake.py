import tkinter as tk
import random

# Game Constants
GAME_WIDTH = 600
GAME_HEIGHT = 400
SPEED = 100  # Lower number = faster game (in milliseconds)
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake!")
        self.window.resizable(False, False)

        self.score = 0
        self.direction = 'down'

        # Score Label
        self.label = tk.Label(self.window, text="Score: {}".format(self.score), font=('consolas', 20))
        self.label.pack()

        # Game Canvas
        self.canvas = tk.Canvas(self.window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
        self.canvas.pack()

        self.window.update()

        # Center the window
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = int((screen_width/2) - (window_width/2))
        y = int((screen_height/2) - (window_height/2))
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Controls Binding
        self.window.bind('<Left>', lambda event: self.change_direction('left'))
        self.window.bind('<Right>', lambda event: self.change_direction('right'))
        self.window.bind('<Up>', lambda event: self.change_direction('up'))
        self.window.bind('<Down>', lambda event: self.change_direction('down'))

        # Initialize Game Objects
        self.snake_coordinates = []
        self.snake_squares = []
        
        for i in range(0, BODY_PARTS):
            self.snake_coordinates.append([0, 0])

        for x, y in self.snake_coordinates:
            square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.snake_squares.append(square)

        self.food_coordinates = None
        self.food_object = None
        self.create_food()

        # Start game loop
        self.next_turn()
        self.window.mainloop()

    def create_food(self):
        x = random.randint(0, int((GAME_WIDTH / SPACE_SIZE)) - 1) * SPACE_SIZE
        y = random.randint(0, int((GAME_HEIGHT / SPACE_SIZE)) - 1) * SPACE_SIZE
        self.food_coordinates = [x, y]
        self.food_object = self.canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

    def next_turn(self):
        x, y = self.snake_coordinates[0]

        if self.direction == "up":
            y -= SPACE_SIZE
        elif self.direction == "down":
            y += SPACE_SIZE
        elif self.direction == "left":
            x -= SPACE_SIZE
        elif self.direction == "right":
            x += SPACE_SIZE

        # Insert new head coordinates
        self.snake_coordinates.insert(0, [x, y])
        square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        self.snake_squares.insert(0, square)

        # Check if snake ate food
        if x == self.food_coordinates[0] and y == self.food_coordinates[1]:
            self.score += 1
            self.label.config(text="Score: {}".format(self.score))
            self.canvas.delete("food")
            self.create_food()
        else:
            # Remove last piece of snake if no food eaten
            del self.snake_coordinates[-1]
            self.canvas.delete(self.snake_squares[-1])
            del self.snake_squares[-1]

        # Collision Check
        if self.check_collisions():
            self.game_over()
        else:
            self.window.after(SPEED, self.next_turn)

    def change_direction(self, new_direction):
        if new_direction == 'left' and self.direction != 'right':
            self.direction = new_direction
        elif new_direction == 'right' and self.direction != 'left':
            self.direction = new_direction
        elif new_direction == 'up' and self.direction != 'down':
            self.direction = new_direction
        elif new_direction == 'down' and self.direction != 'up':
            self.direction = new_direction

    def check_collisions(self):
        x, y = self.snake_coordinates[0]

        # Wall collisions
        if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
            return True

        # Self collisions
        for body_part in self.snake_coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False

    def game_over(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2,
                                font=('consolas', 50), text="GAME OVER", fill="red", tag="gameover")


if __name__ == "__main__":
    SnakeGame()