import os
import random
import time

# Window dimensions
window_width = 20
window_height = 20

# Snake initial position
snake_x = window_width // 2
snake_y = window_height // 2

# Snake initial movement
snake_x_change = 0
snake_y_change = 0

# Snake segments
snake_segments = [[snake_x, snake_y]]
snake_length = 1

# Food initial position
food_x = random.randint(0, window_width - 1)
food_y = random.randint(0, window_height - 1)

# Game state
game_over = False
score = 0

# Function to display the game board
def display_board():
    os.system("cls" if os.name == "nt" else "clear")
    for y in range(window_height):
        for x in range(window_width):
            if x == snake_x and y == snake_y:
                print("O", end="")
            elif x == food_x and y == food_y:
                print("*", end="")
            elif [x, y] in snake_segments:
                print("o", end="")
            else:
                print(".", end="")
        print()
    print("Score:", score)

# Function to read user input
def get_user_input():
    direction = None
    while direction not in ["a", "d", "w", "s"]:
        direction = input("Enter direction (a/d/w/s): ").lower()
    return direction

# Main game loop
while not game_over:
    display_board()

    # Snake movement
    key = get_user_input()
    if key == "a" and snake_x_change != 1:
        snake_x_change = -1
        snake_y_change = 0
    elif key == "d" and snake_x_change != -1:
        snake_x_change = 1
        snake_y_change = 0
    elif key == "w" and snake_y_change != 1:
        snake_y_change = -1
        snake_x_change = 0
    elif key == "s" and snake_y_change != -1:
        snake_y_change = 1
        snake_x_change = 0

    # Update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for boundary collisions
    if snake_x < 0 or snake_x >= window_width or snake_y < 0 or snake_y >= window_height:
        game_over = True

    # Check for snake-food collision
    if snake_x == food_x and snake_y == food_y:
        score += 1
        snake_length += 1
        food_x = random.randint(0, window_width - 1)
        food_y = random.randint(0, window_height - 1)

    # Update snake segments
    snake_segments.append([snake_x, snake_y])
    if len(snake_segments) > snake_length:
        del snake_segments[0]

    # Check for snake collisions with itself
    if [snake_x, snake_y] in snake_segments[:-1]:
        game_over = True

    time.sleep(0.1)

# Game over screen
display_board()
print("Game Over!")
print("Final Score:", score)
