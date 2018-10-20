"""
import pygame,math

pygame.init()

surface_size = 1024
main_surface = pygame.display.set_mode((surface_size,surface_size))
my_clock = pygame.time.Clock()

def draw_tree(order, theta, size, position, heading, color=(200,100,250),depth=0):

    trunk_ratio = 0.29 # How big is the trunk relative to whole tree?
    trunk = size * trunk_ratio # length of trunk
    delta_x = trunk * math.cos(heading)
    delta_y = trunk * math.sin(heading)
    (u, v) = position
    newposition = (u + delta_x, v + delta_y)
    pygame.draw.line(main_surface, color, position, newposition)
    pygame.draw.circle(main_surface, color, (int(position[0]),int(position[1])), 3)

    if order > 0: # Draw another layer of subtrees

        # These next six lines are a simple hack to make the tw→major halves
        # of the recursion different colors. Fiddle here to change˓→colors
        # at other depths, or when depth is even, or odd, etc.
        if depth == 0:
            color1 = (255,0,0)
            color2 = (0,0,255)
        else:
            color1 = color
            color2 = color

# make the recursive calls to draw the two subtrees
        newsize = size*(1 - trunk_ratio)
        draw_tree(order-1, theta, newsize, newposition, heading-theta, color1, depth+1)
        draw_tree(order-1, theta, newsize, newposition, heading+theta,color2, depth+1)

def gameloop():
    theta = 0
    while True:
        # Handle evente from keyboard, mouse, etc.
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        theta += 0.01

        # Draw everything
        main_surface.fill((255, 255, 0))
        draw_tree(9, theta, surface_size*0.8, (surface_size//2,surface_size-50), -math.pi/2)

        pygame.display.flip()
        my_clock.tick(120)

gameloop()
pygame.quit()



import pygame, math

pygame.init()

surface_size = 700
main_surface = pygame.display.set_mode((surface_size,surface_size))
my_clock = pygame.time.Clock()

def draw_tree_artesanal (order,theta,size,position,heading,color = (0,0,0),depth=0):

    trunk_ratio = 0.30
    trunk = size*trunk_ratio
    delta_x = trunk*math.cos(heading)
    delta_y = trunk*math.sin(heading)
    (u,v) = position
    new_position = (u+delta_x,v+delta_y)

    pygame.draw.line(main_surface,color,position,new_position)
    pygame.draw.circle(main_surface,color,(int(position[0]),int(position[1])),3)

    if order>0:

        #No entiendo bien el tema de los colores

        if depth == 0:
            color1 = (205,240,0)
            color2 = (240,200,15)
        else:
            color1 = color
            color2 = color

        newsize = size*(1-trunk_ratio)
        draw_tree_artesanal(order-1,theta,newsize,new_position,heading-theta,color1,depth+1)
        draw_tree_artesanal(order-1,theta,newsize,new_position,heading+theta,color2,depth+1)

def gameloop():
    theta = 0
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        theta += 0.01

        main_surface.fill((0,200,220))  # NO ENTIENDO BIEN PARA QUE ES
        draw_tree_artesanal(9,theta,0.75*surface_size,(surface_size//2,surface_size-50), -math.pi/2)

        pygame.display.flip() # NO ENTIENDO PARA QUE ES
        my_clock.tick(120)   # NO ENTIENDO PARA QUE ES

gameloop()
pygame.quit()
"""
import pygame, math

pygame.init()

surface = 1073
main_surface = pygame.display.set_mode((surface,surface))
my_clock = pygame.time.Clock()


def draw_tree_artesanal_2(order,theta,size,position,heading,color = (0,0,0),depth=0):

    trunk_ratio = 0.30
    trunk = size*trunk_ratio
    delta_x = trunk*math.cos(heading)
    delta_y = trunk*math.sin(heading)
    (u,v) = position
    new_position = (u + delta_x, v + delta_y)

    pygame.draw.line(main_surface,color,position,new_position)
    pygame.draw.circle(main_surface,color,(int(position[0]),int(position[1])),3)
    if order>0:
        if depth == 0:
            color1 = (205, 240, 0)
            color2 = (240, 200, 15)
        else:
            color1 = color
            color2 = color

        new_size = size*(1-trunk_ratio)
        draw_tree_artesanal_2(order-1,theta,new_size,new_position,heading-theta,color1,depth+1)
        draw_tree_artesanal_2(order - 1, theta, new_size, new_position, heading + theta, color2, depth + 1)

def gameloop():
    theta = 0
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        theta += 0.01

        main_surface.fill((0,0,255))

        draw_tree_artesanal_2(9,theta,0.8*surface,(surface//2,surface-50),-math.pi/2)

        pygame.display.flip()
        my_clock.tick(180)

gameloop()
pygame.quit()


