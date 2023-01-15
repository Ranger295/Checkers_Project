from random import random

import pygame
import os
import sys

# brd = board
brd = [['w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___'],
       ['b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___'],
       ['w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___'],
       ['b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___'],
       ['w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___'],
       ['b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___'],
       ['w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___'],
       ['b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___']]
history = [0, 0, 0]
who_moves = 'WHITE'

pygame.init()
pygame.font.init()
size = 648, 748
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()


def start_new_game():
    global brd
    brd = [['w___', 'bb__', 'w___', 'bb__', 'w___', 'bb__', 'w___', 'bb__'],
           ['bb__', 'w___', 'bb__', 'w___', 'bb__', 'w___', 'bb__', 'w___'],
           ['w___', 'bb__', 'w___', 'bb__', 'w___', 'bb__', 'w___', 'bb__'],
           ['b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___'],
           ['w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___'],
           ['bw__', 'w___', 'bw__', 'w___', 'bw__', 'w___', 'bw__', 'w___'],
           ['w___', 'bw__', 'w___', 'bw__', 'w___', 'bw__', 'w___', 'bw__'],
           ['bw__', 'w___', 'bw__', 'w___', 'bw__', 'w___', 'bw__', 'w___']]


start_new_game()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def make_move(cell):
    global brd
    global history
    global who_moves
    can_beat = False
    # p_m = previous_move
    if history[-2] != 0:
        p_m = history[-2]
        if cell != p_m:
            if who_moves == 'WHITE':
                if brd[p_m[1]][p_m[0]] == 'bW__':
                    if abs(p_m[1] - cell[1]) == abs(p_m[0] - cell[0]):
                        if if_queen_can_beat(cell, p_m, 'bB'):
                            brd[p_m[1]][p_m[0]] = 'b___'
                            brd[cell[1]][cell[0]] = 'bW__'
                elif brd[p_m[1]][p_m[0]] == 'bwt_':
                    if cell[1] < p_m[1]:
                        if abs(p_m[1] - cell[1]) == 1 or abs(p_m[0] - cell[0]) == 1:
                            if cell[1] == 0:
                                brd[cell[1]][cell[0]] = 'bW__'
                            else:
                                brd[cell[1]][cell[0]] = 'bw__'
                            brd[p_m[1]][p_m[0]] = 'b___'
                            who_moves = 'BLACK'
                elif brd[p_m[1]][p_m[0]] == 'bw__':
                    if abs(p_m[1] - cell[1]) == 2 and abs(p_m[0] - cell[0]) == 2:
                        if if_checker_can_beat(cell, p_m, 'bB'):
                            beaten_figure_pos = if_checker_can_beat(cell, p_m, 'bB')
                            brd[beaten_figure_pos[0]][beaten_figure_pos[1]] = 'b___'
                            brd[p_m[1]][p_m[0]] = 'b___'
                            if cell[1] == 0:
                                brd[cell[1]][cell[0]] = 'bW__'
                            else:
                                brd[cell[1]][cell[0]] = 'bw__'
                        for next_cords in [(cell[0] + 2, cell[1] + 2), (cell[0] + 2, cell[1] - 2), \
                                           (cell[0] - 2, cell[1] + 2), (cell[0] - 2, cell[1] - 2)]:
                            if (next_cords[0] < 8 and next_cords[1] < 8) \
                                    and (next_cords[0] >= 0 and next_cords[1] >= 0):
                                if if_checker_can_beat(next_cords, cell, 'bB'):
                                    return
                        who_moves = 'BLACK'


            elif who_moves == 'BLACK':
                if brd[p_m[1]][p_m[0]] == 'bbt_':
                    if cell[1] > p_m[1]:
                        if abs(p_m[1] - cell[1]) == 1 or abs(p_m[0] - cell[0]) == 1:
                            if cell[1] == 7:
                                brd[cell[1]][cell[0]] = 'bB__'
                            else:
                                brd[cell[1]][cell[0]] = 'bb__'
                            brd[p_m[1]][p_m[0]] = 'b___'
                            who_moves = 'WHITE'
                elif brd[p_m[1]][p_m[0]] == 'bb__':
                    if abs(p_m[1] - cell[1]) == 2 and abs(p_m[0] - cell[0]) == 2:
                        if if_checker_can_beat(cell, p_m, 'wW'):
                            beaten_figure_pos = if_checker_can_beat(cell, p_m, 'wW')
                            brd[beaten_figure_pos[0]][beaten_figure_pos[1]] = 'b___'
                            brd[p_m[1]][p_m[0]] = 'b___'
                            if cell[1] == 7:
                                brd[cell[1]][cell[0]] = 'bB__'
                            else:
                                brd[cell[1]][cell[0]] = 'bb__'
                        for next_cords in [(cell[0] + 2, cell[1] + 2), (cell[0] + 2, cell[1] - 2), \
                                           (cell[0] - 2, cell[1] + 2), (cell[0] - 2, cell[1] - 2)]:
                            if (next_cords[0] < 8 and next_cords[1] < 8) \
                                    and (next_cords[0] >= 0 and next_cords[1] >= 0):
                                if if_checker_can_beat(next_cords, cell, 'wW'):
                                    return
                        who_moves = 'WHITE'
        else:
            pass


class Checkers_Board:
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size = 0
        self.set_view(left, top, cell_size)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size,
                                  self.cell_size), 1)

    def get_click(self, mouse_pos):
        global history
        cell = self.get_cell(mouse_pos)
        if cell != None:
            history.append(cell)
            set_selection(cell)
            make_move(cell)
            if history[-2] != 0:
                print("prev_cell:", history[-2], brd[history[-2][1]][history[-2][0]], "now_cell:", cell,
                      brd[cell[1]][cell[0]])

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        else:
            return cell_x, cell_y


class sprite_adder(pygame.sprite.Sprite):
    def __init__(self, all_sprites, figure_name, pos):
        super().__init__(all_sprites)
        self.image = load_image(figure_name)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        pass


checkers_board = Checkers_Board(8, 8, 4, 104, 80)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            checkers_board.get_click(event.pos)
    # checkers_board.render(screen)
    screen.fill((0, 0, 0))
    update_game_field()
    screen.blit(load_image("Checkers_Board.png"), (0, 100))
    all_sprites.draw(screen)
    # text = "\n".join(["   ".join(x) for x in brd])
    # print(text)
    # my_font = pygame.font.SysFont('Calibri', 30)
    # text_surface = my_font.render(text, False, (255, 255, 255))
    # screen.blit(text_surface, (0, 0))
    pygame.display.flip()
    all_sprites.update()
pygame.quit()
