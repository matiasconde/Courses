#"C:\Users\Uso familiar\AppData\Local\Programs\Python\Python36\

import pygame
import time

g = 0.0001

class QueenSprite:

    def __init__(self,img,target_position):
        self.imagen = img
        self.target_position = target_position
        (x,y) = target_position
        self.position = (x,0)
        self.y_velocity = 0

    def draw(self,background):
        background.blit(self.imagen,self.position)

    def update(self):
        self.y_velocity += g
        (x,y) = self.position
        self.position = (x,y+self.y_velocity)
        dist_to_go = self.target_position[1] - self.position[1]

        if dist_to_go < 0:
            self.y_velocity = -0.65*self.y_velocity
            (x,y) = self.target_position
            self.position = (x,y+dist_to_go)

    def contains_point(self,point):
        (x0,y0) = self.position
        (x,y) = point
        delta_x = self.imagen.get_width()
        delta_y = self.imagen.get_height()
        return (x0 <= x <= x0 + delta_x and y0 <= y <= y0 + delta_y)

    def handle_click(self,point):
        if self.contains_point(point):
            self.y_velocity += -0.3

class DukeSprite:

    def __init__(self,img,target_position):
        self.imagen = img
        self.position = target_position
        self.frame_count = 0
        self.patch_num = 0

    def draw(self,background):
        rect = (self.patch_num*100,0,100,self.imagen.get_height())
        background.blit(self.imagen,self.position,rect)

    def update(self):
        if self.frame_count > 0:
            self.frame_count = (self.frame_count + 1) % 60
            self.patch_num = self.frame_count // 6

    def contains_point(self,point):
        (x0,y0) = self.position
        (x,y) = point
        ancho = 100
        alto = self.imagen.get_height()
        #return (x0 <= x <= x0 + ancho) and (y0 <= y <= y0 + alto)
        return(x >= x0 and x < x0 + ancho and y >= y0 and y < y0 + alto)

    def handle_click(self,point):
        if self.frame_count == 0:
           self.frame_count = 5

class CardsSprites:

    def __init__(self,img,target_position,path_num):
        self.imagen = img
        self.position = target_position
        self.path_num = path_num

    def draw(self,background):
        vert = self.path_num // 13
        anch = self.path_num % 13
        # print (vert)
        ancho = 49.153846153846153846153846153846
        vertical = 64
        card = (anch*ancho,vert*vertical,ancho,64)
        background.blit(self.imagen,self.position,card)


class Tablero:

    def __init__(self,board_set,pixel_size,n):

        a = pixel_size // n
        self.size = a*n
        self.casillero_size = a
        self.board = board_set
        self.n = n

    def playgame_queens(self,color1 = (25, 177, 234),color2 = (255, 255, 255),path = "Ficha de dama blanca.png"):

        pygame.init()
        surface_size = self.size
        background = pygame.display.set_mode((surface_size, surface_size))

        color = [color1, color2]
        img = pygame.image.load(path)
        list_of_sprites = []
        offset = (self.casillero_size - img.get_width()) // 2
        for i, v in enumerate(self.board):
            list_of_sprites.append(QueenSprite(img, (i * self.casillero_size + offset, v * self.casillero_size + offset)))


        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break
            if event.type != pygame.NOEVENT:
                print(event)
            if event.type == pygame.KEYDOWN:
                value = event.dict["key"]
                if value == 27:
                    break
                if value == 114:
                    color[0] = (255,0,0)
                elif value == ord("g"): #en lugar de ord("g") se podría haber puesto 103 que es el codigo, lo dejo como ejemplo
                    color[0] = (0,255,0)
                elif value == 98:
                    color[0] = (0,0,98)
            if event.type == pygame.MOUSEBUTTONDOWN:
                coordinate_mouse = event.dict["pos"]
                for queens in list_of_sprites:
                    if queens.contains_point(coordinate_mouse):
                        queens.handle_click(coordinate_mouse)

            for row in range(self.n):
                color_index = row % 2
                for col in range(self.n):
                    casillero = (self.casillero_size * col, self.casillero_size * row, self.casillero_size, self.casillero_size)
                    background.fill(color[color_index], casillero)
                    color_index = (color_index + 1) % 2

            for sprite in list_of_sprites:
                sprite.update()
                sprite.draw(background)

            pygame.display.flip()

        pygame.quit()

    def playgame_duke(self,color1 = (25, 177, 234),color2 = (255, 255, 255),path = "Duke_spritesheets.png"):

        pygame.init()
        surface_size = self.size
        background = pygame.display.set_mode((surface_size, surface_size))

        color = [color1, color2]
        img = pygame.image.load(path)
        list_of_sprites = []
        offset = (self.casillero_size - img.get_width()) // 2
        duke1 = DukeSprite(img,(self.casillero_size*2,0))
        duke2 = DukeSprite(img,(self.casillero_size*4,50))

        my_time = pygame.time.Clock()

        list_of_sprites.append(duke1)
        list_of_sprites.append(duke2)

        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break
            if event.type != pygame.NOEVENT:
                print(event)
            if event.type == pygame.KEYDOWN:
                value = event.dict["key"]
                if value == 27:
                    break
                if value == 114:
                    color[0] = (255,0,0)
                elif value == ord("g"): #en lugar de ord("g") se podría haber puesto 103 que es el codigo, lo dejo como ejemplo
                    color[0] = (0,255,0)
                elif value == 98:
                    color[0] = (0,0,98)
            if event.type == pygame.MOUSEBUTTONDOWN:
                coordinate_mouse = event.dict["pos"]
                for sprite in list_of_sprites:
                    if sprite.contains_point(coordinate_mouse):
                        sprite.handle_click(coordinate_mouse)


            for row in range(self.n):
                color_index = row % 2
                for col in range(self.n):
                    casillero = (self.casillero_size * col, self.casillero_size * row, self.casillero_size, self.casillero_size)
                    background.fill(color[color_index], casillero)
                    color_index = (color_index + 1) % 2

            for sprite in list_of_sprites:
                sprite.update()
                sprite.draw(background)

            pygame.display.flip()

            my_time.tick(60)

        pygame.quit()


    def deal_cards(self,color1 = (58,216,26),color2 = (58,216,26),path = "C:\\Users\\Uso familiar\\Pictures\\Deck.png"):

        import random
        pygame.init()
        surface_size = self.size
        background = pygame.display.set_mode((surface_size, surface_size))

        color = [color1, color2]

        img = pygame.image.load(path)
        total_numbers_cards = list(range(52))
        random.shuffle(total_numbers_cards)
        list_of_sprites = []
        offset = (self.casillero_size - img.get_width()) // 2

        for i in range(5):
            v = total_numbers_cards[i]
            list_of_sprites.append(CardsSprites(img,(100*i+200,self.size//2),v))
            print(v)

        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break

            for row in range(self.n):
                color_index = row % 2
                for col in range(self.n):
                    casillero = (self.casillero_size * col, self.casillero_size * row, self.casillero_size, self.casillero_size)
                    background.fill(color[color_index], casillero)
                    color_index = (color_index + 1) % 2

            for sprite in list_of_sprites:
                sprite.draw(background)

            pygame.display.flip()

        pygame.quit()


Juego = Tablero([3,7,0,4,6,1,5,6],840,12)

Juego.deal_cards(path = "C:\\Users\\Uso familiar\\Pictures\\Deck.png")


# HAY UN BUGGGGG SALUDAN LOS DOS A LA VEZ CUANDO CLICKEO EL DE LA DERECHA Y COINCIDEN LOS ESPACIOS EN Y