import pygame
import variables as var

pygame.init()

dis = pygame.display.set_mode((var.dis_width, var.dis_height))
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
snake_block = 10
snake_speed = 15

def dispay_score(score):
    value = score_font.render("Your Score: " + str(score), True, var.yellow)
    dis.blit(value, [0, 0])
 
 
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, var.black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [var.dis_width / 6, var.dis_height / 3])
 