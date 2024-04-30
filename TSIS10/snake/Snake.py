import pygame
import time
import psycopg2
# from psycopg2 import sql
# import sys
import random

# Initialize Pygame
pygame.init()

# Sound for eating
eatingFood = pygame.mixer.Sound("eatingFood.mp3")
eatingFood.set_volume(0.09)


# Window sizer
window_x = 720
window_y = 480

# Set up the game window
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Snake Game')



# For TSIS10
conn = psycopg2.connect("dbname=snake user=postgres password=2525")
cur = conn.cursor()
conn.autocommit = True



def get_user_name():
    input_box = pygame.Rect(270, 200, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font = pygame.font.Font(None, 32)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text.strip() == '':
                            continue
                        else:
                            done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        
        game_window.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        game_window.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(game_window, color, input_box, 2)
        pygame.display.flip()

    return text

# Checking for user
# Globar variable for knowing if user is new or lost last time, by exists
exists = True
def check_or_create_user(user_name):
    global db_snake_position
    global died_last_time
    died_last_time = False
    global db_direction
    global exists
    global db_user_score
    global db_user_level
    global db_score_count
    global db_snake_body
    cur.execute(f"SELECT user_name FROM snakescore WHERE user_name = '{user_name}'")
    # If doesn't exist
    if cur.fetchone() is None:
        exists = False
        cur.execute("INSERT INTO snakescore (user_name, user_score, position, direction, level, score_count, snake_body) VALUES (%s, 0, ARRAY[0, 0], 0, 0, 0, ARRAY[0, 0, 0, 0, 0])", (user_name,))

    else:
        sql = f'''
        SELECT * FROM snakescore WHERE user_name LIKE '%{user_name}%'
        '''
        cur.execute(sql)
        result = cur.fetchall()
        if result:
            print
            print(result[0])
            db_user_score = result[0][1]
            db_snake_position = result[0][2]
            db_direction = result[0][3]
            db_user_level = result[0][4]
            db_score_count = result[0][5]
            db_snake_body = result[0][6]

        if result[0][4] == 0:
            died_last_time = True
        else:
            died_last_time = False

# Updating db
def update_score_position_direction_level(user_name, score, snake_position, direction, user_level, score_count, snake_body):
    cur.execute("""UPDATE snakescore 
                SET user_score = %s, position = %s, direction = %s, level = %s, score_count = %s, snake_body = %s
                WHERE user_name = %s""", (score, snake_position, direction, user_level, score_count, snake_body, user_name))


# def update_position(user_name, position):
#     cur.execute("UPDATE snakescore SET position = %s WHERE user_name = $s", (position, user_name))



def main():
    global game_window

    # Defining colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)



    # FPS (frames per second) controller
    fps = pygame.time.Clock()

    # Define the snake initial position, speed, and direction
    user_name = get_user_name()
    check_or_create_user(user_name)

    # Extracting data from db snakescore

    if exists and db_user_score != 0:
        snake_position = db_snake_position
        direction = db_direction
        score = db_user_score
        score_count = db_score_count
        level = db_user_level
        snake_body = db_snake_body
    else:
        # Snake's setup
        snake_position = [100, 50]
        direction = 'RIGHT'
        # Score and level
        score_count = 0
        score = 0
        level = 1
        snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]


    snake_speed = 15
    change_to = direction


    

    # Food generation function with timer and size
    def generate_food():
        return {
            'position': [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10],
            'size': 10 if random.random() > 0.3 else 20,  # 30% chance to get a bigger fruit
            'timer': time.time() + 5  # 5 seconds before the food disappears
        }

    # Initialize the fruit
    fruit = generate_food()

    # Displaying score and level function
    def show_score_and_level(color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render(f'Score: {score}   Level: {level}', True, color)
        score_rect = score_surface.get_rect()
        score_rect.topleft = (10, 10)
        game_window.blit(score_surface, score_rect)

    # Game over function
    def game_over():
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render(f'Your Score is: {score}', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x / 2, window_y / 4)
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(2)


    # Some pre-settlements
    game_active = True
    run = True


    # Main game loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                update_score_position_direction_level(user_name, score, snake_position, direction, level, score_count, snake_body)
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return main()
                elif event.key == pygame.K_SPACE:
                    game_active = not game_active
                    update_score_position_direction_level(user_name, score, snake_position, direction, level, score_count, snake_body)
                elif event.key == pygame.K_ESCAPE:
                    update_score_position_direction_level(user_name, score, snake_position, direction, level, score_count, snake_body)
                    run = False
                    pygame.quit()
                    quit()
                
        
        if game_active:
            print(snake_position)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and direction != 'DOWN':
                change_to = 'UP'
            elif keys[pygame.K_DOWN] and direction != 'UP':
                change_to = 'DOWN'
            elif keys[pygame.K_LEFT] and direction != 'RIGHT':
                change_to = 'LEFT'
            elif keys[pygame.K_RIGHT] and direction != 'LEFT':
                change_to = 'RIGHT'


            # Update the direction of the snake
            direction = change_to

            # Move the snake
            if direction == 'UP':
                snake_position[1] -= 10
            elif direction == 'DOWN':
                snake_position[1] += 10
            elif direction == 'LEFT':
                snake_position[0] -= 10
            elif direction == 'RIGHT':
                snake_position[0] += 10

            # Check for collision with walls
            if snake_position[0] < 0 or snake_position[0] >= window_x or snake_position[1] < 0 or snake_position[1] >= window_y:
                game_active = False
                score = 0
                update_score_position_direction_level(user_name, score, snake_position, direction, level, score_count, snake_body)
                game_over()

            # Check for collision with the snake body
            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    game_active = False
                    score = 0
                    update_score_position_direction_level(user_name, score, snake_position, direction, level, score_count, snake_body)
                    game_over()

            # Handle the fruit timer
            if time.time() > fruit['timer']:
                fruit = generate_food()

            # Check for collision with the fruit
            print(list(snake_position))
            snake_body.insert(0, list(snake_position))
            if abs(snake_position[0] - fruit['position'][0]) < fruit['size'] and abs(snake_position[1] - fruit['position'][1]) < fruit['size']:
                eatingFood.play()
                score += fruit['size']
                score_count += fruit['size']
                if score_count >= 50:
                    level += 1
                    score_count = 0
                    snake_speed += 1
                    if snake_speed == 15 and level > 1:
                        snake_speed += level
                
                if fruit['size'] > 10:
                    snake_body.insert(0, list(snake_position))
                    
                fruit = generate_food()
            else:
                snake_body.pop()

            # Display everything
            game_window.fill(black)
            for pos in snake_body:
                # print(len(snake_body))
                # print(snake_body, "Pos:", snake_position)
                pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
            
            pygame.draw.rect(game_window, red, pygame.Rect(fruit['position'][0], fruit['position'][1], fruit['size'], fruit['size']))

            show_score_and_level(white, 'times new roman', 20)
            pygame.display.update()
            fps.tick(snake_speed)
    


if __name__ == '__main__':
    main()

    # Closing connection
    cur.close()
    conn.close()