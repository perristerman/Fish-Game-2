#skeleton of pygame
#step 1 (importing and initalizing python:
import pygame, random 

pygame.init()
#step 2 (Setting up our screen):
screen_info = pygame.display.Info()
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
#step 3 (Set up a clock):
clock = pygame.time.Clock()
#Color of bg
color = (0, 127, 255)
#putting in image of fish
fish_image = pygame.image.load('fish.png')
fish_image = pygame.transform.smoothscale(fish_image, (80, 80))
fish_rect = fish_image.get_rect()
fish_rect.center = (400, 300)

#trying to get the fish to move
speed = pygame.math.Vector2(0,10)
#0,0 is at the top left corner. We use a positive y value to go down and a negative y value to go up
rotation = random.randint(0, 360)
speed.rotate_ip(rotation)
fish_image = pygame.transform.rotate(fish_image, 180 - rotation)

def move_fish():
  global fish_image
  fish_rect.move_ip(speed)
  #move.ip is asking the image to move in position. It stops the computer from creating another image of the fish.
  screen_info = pygame.display.Info()
  if fish_rect.bottom > screen_info.current_h or fish_rect.top < 0 :
    speed[1] *= -1
    #this is a faster way of saying speed[1] = speed[1] * -1
    fish_image = pygame.transform.flip(fish_image, False, True)
    fish_rect.move_ip(1, speed[1])
#indexing - assigning something a number based off of a number. It always starts with 0. Ex: [Apples, bananas, strawberries]. Bananas is in [1]
  if fish_rect.right > screen_info.current_w or fish_rect.left < 0:
    speed[0] *= -1
    #this is a faster way of saying speed[1] = speed[1] * -1
    fish_image = pygame.transform.flip(fish_image, True, False)
    fish_rect.move_ip(0, speed[0])




def main():
  while True:
    clock.tick(60)
    move_fish()
    screen.fill(color)
    #screen.blit --> displays an image
    screen.blit(fish_image, fish_rect)
    pygame.display.flip()
    
    
#checking if the file you're running is the main file
if __name__ == '__main__':
  main()