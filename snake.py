import pygame as pg
from random import randrange
import math




def main():
    pg.init()
    window = 1000
    title_size = 50
    get_random_position = lambda: [randrange(title_size // 2, window - title_size // 2, title_size),
                                   randrange(title_size // 2, window - title_size // 2, title_size)]
    snake = pg.Rect(*get_random_position(), title_size - 2, title_size - 2)
    length = 1
    food = pg.Rect(*get_random_position(), title_size - 2, title_size - 2)  
    segments = [snake.copy()]
    snake_dir = (0, 0)
    screen = pg.display.set_mode([window] * 2)
    clock = pg.time.Clock()
    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
    move_interval = 100
    last_move_time = 0
    buffered_dir = None
    font = pg.font.SysFont("Arial", 30)
    score = 0
    enemy = pg.Rect(*get_random_position(), title_size - 2, title_size - 2)
    last_enemy_move = 0
    
    def pause_game():
        is_paused = True
        while is_paused:
            pause_text = font.render("GAME IS PAUSED TO UNPAUSE PRESS ENTER", True, (255, 255, 255))  
            text_rect = pause_text.get_rect(center=(window // 2, window // 2))  
            screen.blit(pause_text, text_rect)
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        is_paused = False
                if event.type == pg.QUIT:
                    is_paused = False
                    pg.quit()
                    exit()
    
    def distance (pos1, pos2):
        return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

    def draw_scoreboard():
        scoreboard_bg = pg.Surface((150, 40), pg.SRCALPHA)
        scoreboard_bg.fill((0, 0, 0, 128))
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(scoreboard_bg, (10, 10))
        screen.blit(score_text, (20, 15)) 
    
    snake.center, food.center, enemy.center = get_random_position(), get_random_position(), get_random_position()
        
    while True:
        current_time = pg.time.get_ticks()
        delta_time = current_time - last_move_time

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w and dirs[pg.K_w]:
                    buffered_dir = (0, -title_size)
                    dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
                if event.key == pg.K_s and dirs[pg.K_s]:
                    buffered_dir = (0, title_size)
                    dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
                if event.key == pg.K_a and dirs[pg.K_a]:
                    buffered_dir = (-title_size, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
                if event.key == pg.K_d and dirs[pg.K_d]:
                    buffered_dir = (title_size, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}
                if event.key == pg.K_ESCAPE:
                    pause_game()

        screen.fill('#808080')

        
        self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
        if snake.left < 0 or snake.right > window or snake.top < 0 or snake.bottom > window or self_eating:
            snake.center, food.center, enemy.center = get_random_position(), get_random_position(), get_random_position()   
            length = 1
            score = 0
            snake_dir = (0, 0)
            segments = [snake.copy()]
            

        
        if enemy and snake.colliderect(enemy):
            snake.center, food.center, enemy.center = get_random_position(), get_random_position(), get_random_position()
            length = 1
            score = 0
            snake_dir = (0, 0)
            segments = [snake.copy()]
            last_enemy_move = 0


        if enemy and score >= 5 and score != last_enemy_move and (score - 5) % 5 == 0:
            while True:
                new_enemy_pos = get_random_position()
                enemy.center = new_enemy_pos
        
        # Check if the new enemy position collides with the snake or food
                snake_collision = any(segment.colliderect(enemy) for segment in segments)
                food_collision = food.colliderect(enemy)
        
        # Check if the enemy is too close to the snake's head
                too_close = distance(snake.center, enemy.center) < 30  # Adjust 100 as needed
        
        # If no collision and not too close, break the loop
                if not snake_collision and not food_collision and not too_close:
                    break
    
            last_enemy_move = score
        
        if snake.center == food.center:
            while True:
                new_food_pos = get_random_position()
                food.center = new_food_pos
        
        # Check if the new enemy position collides with the snake or food
                snake_collision = any(segment.colliderect(food) for segment in segments)
                enemy_collision = enemy.colliderect(food) if enemy else False
        
        # Check if the enemy is too close to the snake's head
                too_close = distance(snake.center, enemy.center) < 30  # Adjust 100 as needed
        
        # If no collision and not too close, break the loop
                if not snake_collision and not enemy_collision and not too_close:
                    break
            
            length += 1
            score += 1 

        
        pg.draw.rect(screen, 'red', enemy)
        
        pg.draw.rect(screen, '#ffbf00', food)
        
        for segment in segments:
            pg.draw.rect(screen, '#a1c9ee', segment)

        draw_scoreboard()

        if delta_time >= move_interval:
            last_move_time = current_time
            if buffered_dir:
                if (snake_dir[0] * buffered_dir[0] >= 0) and (snake_dir[1] * buffered_dir[1] >= 0):
                    snake_dir = buffered_dir
                buffered_dir = None
            snake.move_ip(snake_dir)
            segments.append(snake.copy())
            segments = segments[-length:]

        pg.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()