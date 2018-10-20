"""import pygame

def main():

    pygame.init()

    surface_size = 800

    main_surface = pygame.display.set_mode((surface_size,surface_size))

    color = (220, 210, 20)
    color2 = (0, 200, 19)
    small_rect = (300, 200, 150, 90)
    ball = pygame.image.load("C:\\Users\\Uso familiar\\Desktop\\pelota de rugby.jpg")
    my_font = pygame.font.SysFont("Arial",12)

    while True:
        event = pygame.event.poll()

        if event.type == pygame.QUIT:
            break

        the_text = my_font.render("Hello World",True,(10,10,120))
        main_surface.fill(color)
        main_surface.fill(color2,small_rect)
        main_surface.blit(ball,(10,20))
        main_surface.blit(the_text,(40,50))
        pygame.display.flip()

pygame.quit()

main()
"""
import pygame,time

def main_game():

    pygame.init()
    surface = 1024
    main_surface = pygame.display.set_mode((surface,surface))
    ball = pygame.image.load("pelota de rugby.jpg")
    t0 = time.clock()
    my_font = pygame.font.SysFont("Courier",20)

    frame_count = 0
    frame_rate = 0

    while True:
        event = pygame.event.poll()
        frame_count += 1
        if event.type == pygame.QUIT:
            break

        if frame_count%500 == 0:
            t1 = time.clock()
            frame_rate = 500/(t1-t0)
            t0 = t1
        main_surface.fill((0,140,100))
        main_surface.fill((0,0,222),(100,100,45,54))
        main_surface.blit(ball,(400,300))
        my_text = my_font.render("Frame Rate = {0} - Frame Count = {1}".format(frame_rate,frame_count),True,(0,0,0))
        main_surface.blit(my_text,(10,10))
        pygame.display.flip()

    main_game.quit()

main_game()


