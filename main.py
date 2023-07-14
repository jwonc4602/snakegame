import pygame
import time
import random
import variables as var
import helper

pygame.init()
 
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()

def playgame():
    game_over = False
    game_close = False
 
    x1 = var.dis_width / 2
    y1 = var.dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, var.dis_width - var.snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, var.dis_height - var.snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            var.dis.fill(var.blue)
            helper.message("You Lost! Press C-Play Again or Q-Quit", var.red)
            helper.display_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        playgame()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -var.pixel_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = var.pixel_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -var.pixel_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = var.pixel_size
                    x1_change = 0
 
        if x1 >= var.dis_width or x1 < 0 or y1 >= var.dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        var.dis.fill(var.blue)
        pygame.draw.rect(var.dis, var.green, [foodx, foody, var.pixel_size, var.pixel_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        helper.draw_snake(var.snake_block, snake_List)
        helper.display_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, var.dis_width - var.snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, var.dis_height - var.snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(helper.snake_speed)
 
    pygame.quit()
    quit()