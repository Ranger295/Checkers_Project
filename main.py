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


def set_selection(cell):
    global brd
    global history

    if cell != history[-2] and brd[cell[1]][cell[0]][0] == 'b':
        # p_m = previous_move
        if history[-2] != 0:
            p_m = history[-2]
            if brd[cell[1]][cell[0]][1] == '_' and (abs(p_m[1] - cell[1]) != 1 or abs(p_m[0] - cell[0]) != 1):
                y = 0
                x = 0
                for row in brd:
                    for cell2 in row:
                        brd[x][y] = brd[x][y][:2] + '__'
                        x += 1
                    y += 1
                    x = 0
                return
        y = 0
        x = 0
        for row in brd:
            for cell2 in row:
                brd[x][y] = brd[x][y][:2] + '__'
                x += 1
            y += 1
            x = 0
        brd[cell[1]][cell[0]] = (brd[cell[1]][cell[0]])[:2] + 't' + '_'
        # p_m = previous_move
        if history[-2] != 0:
            p_m = history[-2]
            if brd[p_m[1]][p_m[0]][1] != '' and brd[cell[1]][cell[0]][1] == '_':
                brd[p_m[1]][p_m[0]] = (brd[p_m[1]][p_m[0]])[:2] + 't' + '_'
    else:
        if brd[cell[1]][cell[0]][0] == 'b':
            if brd[cell[1]][cell[0]][2] == '_':
                brd[cell[1]][cell[0]] = (brd[cell[1]][cell[0]])[:2] + 't' + '_'
            else:
                brd[cell[1]][cell[0]] = (brd[cell[1]][cell[0]])[:2] + '_' + '_'
        else:
            y = 0
            x = 0
            for row in brd:
                for cell2 in row:
                    brd[x][y] = brd[x][y][:2] + '__'
                    x += 1
                y += 1
                x = 0


def if_checker_can_beat(cell, p_m, enemy_color):
    can_beat = False
    if cell[0] > p_m[0] and cell[1] > p_m[1]:
        if brd[p_m[1] + 1][p_m[0] + 1][1] in enemy_color and brd[cell[1]][cell[0]][1] == '_':
            beaten_figure_pos = p_m[1] + 1, p_m[0] + 1
            can_beat = True
    if cell[0] > p_m[0] and cell[1] < p_m[1]:
        if brd[p_m[1] - 1][p_m[0] + 1][1] in enemy_color and brd[cell[1]][cell[0]][1] == '_':
            beaten_figure_pos = p_m[1] - 1, p_m[0] + 1
            can_beat = True
    if cell[0] < p_m[0] and cell[1] > p_m[1]:
        if brd[p_m[1] + 1][p_m[0] - 1][1] in enemy_color and brd[cell[1]][cell[0]][1] == '_':
            beaten_figure_pos = p_m[1] + 1, p_m[0] - 1
            can_beat = True
    if cell[0] < p_m[0] and cell[1] < p_m[1]:
        if brd[p_m[1] - 1][p_m[0] - 1][1] in enemy_color and brd[cell[1]][cell[0]][1] == '_':
            beaten_figure_pos = p_m[1] - 1, p_m[0] - 1
            can_beat = True
    if can_beat:
        return beaten_figure_pos
    else:
        return False


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