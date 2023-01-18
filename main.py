import random

import pygame
import os
import sys

# brd = board
clear_brd = [['w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___'],
             ['b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___'],
             ['w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___'],
             ['b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___'],
             ['w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___'],
             ['b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___'],
             ['w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___'],
             ['b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___']]

queen_move_variants = ['Wb_', 'W_b_', 'Wb__', 'Wb_b_', 'W_b__', 'W__b_', 'Wb_b__',
                       'Wb__b_', 'Wb____', 'W___b_', 'W_b_b_', 'W__b__', 'W___b_Wb_b_b_',
                       'Wb_b___', 'Wb___', 'Wb__b__', 'Wb___b_', 'Wb_____', 'W_b_b__',
                       'W_b__b_', 'W_b____', 'W__b_b_', 'W___b__', 'W____b_Wb_b_b__',
                       'Wb_b__b_', 'Wb__b_b_', 'Wb_b____', 'Wb__b___', 'Wb___b__',
                       'Wb____b_', 'Wb______', 'W_b_b_b_', 'W_b_b___', 'W_b__b__W_b___b_',
                       'W__b_b__', 'W__b__b_', 'W___b_b_', 'W_b_____', 'W__b____',
                       'W___b___', 'W____b__', 'W_____b_',
                       'Bw_', 'B_w_', 'Bw__', 'Bw_w_', 'B_w__', 'B__w_',
                       'Bw_w__', "  'Bw__w_", 'Bw____', 'B___w_', 'Bw___',
                       'B_w_w_', 'B__w__', 'B___w_', 'Bw_w_w_'  'Bw_w___',
                       'Bw__w__', 'Bw___w_', 'Bw_____', 'B_w_w__',
                       'B_w__w_', 'B_w____', 'B__w_w_', 'B___w__',
                       'B____w_Bw_w_w__', 'Bw_w__w_', 'Bw__w_w_',
                       'Bw_w____', 'Bw__w___', 'Bw___w__', 'Bw____w_',
                       'Bw______', 'B_w_w_w_', 'B_w_w___',
                       'B_w__w__B_w___w_', "  'B__w_w__", 'B__w__w_',
                       'B___w_w_', 'B_w_____', 'B__w____', 'B___w___',
                       'B____w__', 'B_____w_']

screen_rect = (0, 0, 648, 748)
history = [0, 0, 0]
who_winner = ''
who_moves = 'WHITE'
is_game_continue = False
pygame.init()
size = 648, 748
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
prtc_sprites = pygame.sprite.Group()
pygame.display.set_caption('Шашки для двоих')
programIcon = pygame.image.load('data\icon.png')
pygame.display.set_icon(programIcon)

checker_move_sound = pygame.mixer.Sound("data/checker_movement_sound.ogg")
end_of_the_game_sound = pygame.mixer.Sound("data/winner_sound.ogg")


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


class sprite_adder(pygame.sprite.Sprite):
    def __init__(self, all_sprites, sprite_name, pos):
        super().__init__(all_sprites)
        self.image = load_image(sprite_name)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        pass


sprite_adder(all_sprites, 'start_background.png', (0, 0))
sprite_adder(all_sprites, 'start_game_button.png', (82, 256))
while not is_game_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range(84, 564) and event.pos[1] in range(264, 444):
                is_game_continue = True
    all_sprites.draw(screen)
    pygame.display.flip()


def start_new_game():
    global brd
    global who_winner
    global who_moves
    brd = [['w___', 'bb__', 'w___', 'bb__', 'w___', 'bb__', 'w___', 'bb__'],
           ['bb__', 'w___', 'bb__', 'w___', 'bb__', 'w___', 'bb__', 'w___'],
           ['w___', 'bb__', 'w___', 'bb__', 'w___', 'bb__', 'w___', 'bb__'],
           ['b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___'],
           ['w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___'],
           ['bw__', 'w___', 'bw__', 'w___', 'bw__', 'w___', 'bw__', 'w___'],
           ['w___', 'bw__', 'w___', 'bw__', 'w___', 'bw__', 'w___', 'bw__'],
           ['bw__', 'w___', 'bw__', 'w___', 'bw__', 'w___', 'bw__', 'w___']]

    who_winner = ''
    who_moves = 'WHITE'
    file = open('data/count.txt', 'r')
    count = ((file.read()).split(','))
    new_count = []
    for text in count:
        new_count.append(f'{text.split(":")[0]}:0')
    file = open('data/count.txt', 'w')
    file.write(",".join(new_count))
    file.close()


def load_menu():
    global who_moves
    global who_winner
    if who_moves == 'WHITE':
        sprite_adder(all_sprites, 'next_move_white.png', (166, 4))
    else:
        sprite_adder(all_sprites, 'next_move_black.png', (166, 4))
    if who_winner == 'White':
        sprite_adder(all_sprites, 'white_won.png', (166, 4))
    if who_winner == 'Black':
        sprite_adder(all_sprites, 'black_won.png', (166, 4))
    sprite_adder(all_sprites, 'close_game.png', (4, 4))
    sprite_adder(all_sprites, 'new_game.png', (486, 4))


start_new_game()
load_menu()


def update_movement_count():
    file = open('data/count.txt', 'r')
    count = ((file.read()).split(','))
    file = open('data/count.txt', 'w')
    file.write(",".join([(f'{count[0].split(":")[0]}:{(int((count[0].split(":"))[1]) + 1)}'), count[1], count[2]]))
    file.close()


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


def if_queen_can_beat(cell, p_m, enemy_color):
    global queen_move_variants
    can_beat = False
    move_line_coords = []
    move_line = ''
    if cell[0] > p_m[0] and cell[1] > p_m[1]:
        if brd[cell[1]][cell[0]][1] == '_':
            x = p_m[0]
            y = p_m[1]
            move_line_coords.append(p_m)
            for _ in range(abs(cell[1] - p_m[1]) - 1):
                x += 1
                y += 1
                move_line += brd[y][x][1]
                move_line_coords.append((x, y))
            if brd[p_m[1]][p_m[0]][1] + move_line.lower() + brd[cell[1]][cell[0]][1] in queen_move_variants:
                can_beat = True
            else:
                move_line_coords = []
            move_line_coords.append(cell)
    if cell[0] > p_m[0] and cell[1] < p_m[1]:
        if brd[cell[1]][cell[0]][1] == '_':
            x = p_m[0]
            y = p_m[1]
            move_line_coords.append(p_m)
            for _ in range(abs(cell[1] - p_m[1]) - 1):
                x += 1
                y -= 1
                move_line += brd[y][x][1]
                move_line_coords.append((x, y))
            if brd[p_m[1]][p_m[0]][1] + move_line.lower() + brd[cell[1]][cell[0]][1] in queen_move_variants:
                can_beat = True
            else:
                move_line_coords = []
            move_line_coords.append(cell)
    if cell[0] < p_m[0] and cell[1] > p_m[1]:
        if brd[cell[1]][cell[0]][1] == '_':
            x = p_m[0]
            y = p_m[1]
            move_line_coords.append(p_m)
            for _ in range(abs(cell[1] - p_m[1]) - 1):
                x -= 1
                y += 1
                move_line += brd[y][x][1]
                move_line_coords.append((x, y))
            if brd[p_m[1]][p_m[0]][1] + move_line.lower() + brd[cell[1]][cell[0]][1] in queen_move_variants:
                can_beat = True
            else:
                move_line_coords = []
            move_line_coords.append(cell)
    if cell[0] < p_m[0] and cell[1] < p_m[1]:
        if brd[cell[1]][cell[0]][1] == '_':
            x = p_m[0]
            y = p_m[1]
            move_line_coords.append(p_m)
            for _ in range(abs(cell[1] - p_m[1]) - 1):
                x -= 1
                y -= 1
                move_line += brd[y][x][1]
                move_line_coords.append((x, y))
            if brd[p_m[1]][p_m[0]][1] + move_line.lower() + brd[cell[1]][cell[0]][1] in queen_move_variants:
                can_beat = True
            else:
                move_line_coords = []
            move_line_coords.append(cell)
    if can_beat:
        return move_line_coords
    else:
        return False


def if_queen_can_move(cell, p_m, enemy_color):
    can_move = False
    move_line = ''
    if cell[0] > p_m[0] and cell[1] > p_m[1]:
        if brd[cell[1]][cell[0]][1] == '_':
            x = p_m[0]
            y = p_m[1]
            for _ in range(abs(cell[1] - p_m[1]) - 1):
                x += 1
                y += 1
                move_line += brd[y][x][1]
            if 'b' not in move_line.lower() and 'w' not in move_line.lower():
                can_move = True

    if cell[0] > p_m[0] and cell[1] < p_m[1]:
        if brd[cell[1]][cell[0]][1] == '_':
            x = p_m[0]
            y = p_m[1]
            for _ in range(abs(cell[1] - p_m[1]) - 1):
                x += 1
                y -= 1
                move_line += brd[y][x][1]
            if 'b' not in move_line.lower() and 'w' not in move_line.lower():
                can_move = True
    if cell[0] < p_m[0] and cell[1] > p_m[1]:
        if brd[cell[1]][cell[0]][1] == '_':
            x = p_m[0]
            y = p_m[1]
            for _ in range(abs(cell[1] - p_m[1]) - 1):
                x -= 1
                y += 1
                move_line += brd[y][x][1]
            if 'b' not in move_line.lower() and 'w' not in move_line.lower():
                can_move = True
    if cell[0] < p_m[0] and cell[1] < p_m[1]:
        if brd[cell[1]][cell[0]][1] == '_':
            x = p_m[0]
            y = p_m[1]
            for _ in range(abs(cell[1] - p_m[1]) - 1):
                x -= 1
                y -= 1
                move_line += brd[y][x][1]
            if 'b' not in move_line.lower() and 'w' not in move_line.lower():
                can_move = True
    if can_move:
        return True
    else:
        return False


def make_move(cell):
    global brd
    global is_game_continue
    global history
    global who_winner
    global who_moves
    global checker_move_sound
    global end_of_the_game_sound
    can_beat = False
    # p_m = previous_move
    if history[-2] != 0:
        p_m = history[-2]
        if cell != p_m:
            if who_moves == 'WHITE':
                if brd[p_m[1]][p_m[0]] == 'bW__':
                    if abs(p_m[1] - cell[1]) == abs(p_m[0] - cell[0]):
                        if if_queen_can_beat(cell, p_m, 'bB'):
                            for coords in if_queen_can_beat(cell, p_m, 'bB'):
                                brd[coords[1]][coords[0]] = 'b___'
                            brd[p_m[1]][p_m[0]] = 'b___'
                            brd[cell[1]][cell[0]] = 'bW__'
                            checker_move_sound.play()
                            for i in range(7):
                                for next_cords in [(cell[0] + i, cell[1] + i), (cell[0] + i, cell[1] - i), \
                                                   (cell[0] - i, cell[1] + i), (cell[0] - i, cell[1] - i)]:
                                    if (next_cords[0] < 8 and next_cords[1] < 8) \
                                            and (next_cords[0] >= 0 and next_cords[1] >= 0):
                                        if if_queen_can_beat(next_cords, cell, 'bB') \
                                                and brd[next_cords[1]][next_cords[0]][2] not in 'bB':
                                            return
                            who_moves = 'BLACK'
                            update_movement_count()
                        if if_queen_can_move(cell, p_m, 'bB'):
                            brd[cell[1]][cell[0]] = 'bW__'
                            brd[p_m[1]][p_m[0]] = 'b___'
                            checker_move_sound.play()
                            who_moves = 'BLACK'
                            update_movement_count()
                elif brd[p_m[1]][p_m[0]] == 'bWt_':
                    if abs(p_m[1] - cell[1]) == abs(p_m[0] - cell[0]):
                        if if_queen_can_move(cell, p_m, 'bB'):
                            brd[cell[1]][cell[0]] = 'bW__'
                            brd[p_m[1]][p_m[0]] = 'b___'
                            checker_move_sound.play()
                            who_moves = 'BLACK'
                            update_movement_count()
                elif brd[p_m[1]][p_m[0]] == 'bwt_':
                    if cell[1] < p_m[1]:
                        if abs(p_m[1] - cell[1]) == 1 and abs(p_m[0] - cell[0]) == 1:
                            if cell[1] == 0:
                                brd[cell[1]][cell[0]] = 'bW__'
                            else:
                                brd[cell[1]][cell[0]] = 'bw__'
                            brd[p_m[1]][p_m[0]] = 'b___'
                            checker_move_sound.play()
                            who_moves = 'BLACK'
                            update_movement_count()
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
                            checker_move_sound.play()
                        for next_cords in [(cell[0] + 2, cell[1] + 2), (cell[0] + 2, cell[1] - 2), \
                                           (cell[0] - 2, cell[1] + 2), (cell[0] - 2, cell[1] - 2)]:
                            if (next_cords[0] < 8 and next_cords[1] < 8) \
                                    and (next_cords[0] >= 0 and next_cords[1] >= 0):
                                if if_checker_can_beat(next_cords, cell, 'bB'):
                                    return
                        who_moves = 'BLACK'
                        update_movement_count()
            elif who_moves == 'BLACK':
                if brd[p_m[1]][p_m[0]] == 'bB__':
                    if abs(p_m[1] - cell[1]) == abs(p_m[0] - cell[0]):
                        if if_queen_can_beat(cell, p_m, 'wW'):
                            for coords in if_queen_can_beat(cell, p_m, 'wW'):
                                brd[coords[1]][coords[0]] = 'b___'
                            brd[p_m[1]][p_m[0]] = 'b___'
                            brd[cell[1]][cell[0]] = 'bB__'
                            checker_move_sound.play()
                            for i in range(7):
                                for next_cords in [(cell[0] + i, cell[1] + i), (cell[0] + i, cell[1] - i), \
                                                   (cell[0] - i, cell[1] + i), (cell[0] - i, cell[1] - i)]:
                                    if (next_cords[0] < 8 and next_cords[1] < 8) \
                                            and (next_cords[0] >= 0 and next_cords[1] >= 0):
                                        if if_queen_can_beat(next_cords, cell, 'wW') \
                                                and brd[next_cords[1]][next_cords[0]][2] not in 'wW':
                                            return
                            who_moves = 'WHITE'
                            update_movement_count()
                        if if_queen_can_move(cell, p_m, 'wW'):
                            brd[cell[1]][cell[0]] = 'bB__'
                            brd[p_m[1]][p_m[0]] = 'b___'
                            checker_move_sound.play()
                            who_moves = 'WHITE'
                            update_movement_count()
                elif brd[p_m[1]][p_m[0]] == 'bBt_':
                    if abs(p_m[1] - cell[1]) == abs(p_m[0] - cell[0]):
                        if if_queen_can_move(cell, p_m, 'wW'):
                            brd[cell[1]][cell[0]] = 'bB__'
                            brd[p_m[1]][p_m[0]] = 'b___'
                            checker_move_sound.play()
                            who_moves = 'WHITE'
                            update_movement_count()
                elif brd[p_m[1]][p_m[0]] == 'bbt_':
                    if cell[1] > p_m[1]:
                        if abs(p_m[1] - cell[1]) == 1 and abs(p_m[0] - cell[0]) == 1:
                            if cell[1] == 7:
                                brd[cell[1]][cell[0]] = 'bB__'
                            else:
                                brd[cell[1]][cell[0]] = 'bb__'
                            brd[p_m[1]][p_m[0]] = 'b___'
                            checker_move_sound.play()
                            who_moves = 'WHITE'
                            update_movement_count()
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
                            checker_move_sound.play()
                        for next_cords in [(cell[0] + 2, cell[1] + 2), (cell[0] + 2, cell[1] - 2), \
                                           (cell[0] - 2, cell[1] + 2), (cell[0] - 2, cell[1] - 2)]:
                            if (next_cords[0] < 8 and next_cords[1] < 8) \
                                    and (next_cords[0] >= 0 and next_cords[1] >= 0):
                                if if_checker_can_beat(next_cords, cell, 'wW'):
                                    return
                        who_moves = 'WHITE'
                        update_movement_count()
        else:
            pass
    white_checkers = 0
    black_checkers = 0
    for row in brd:
        for cell in row:
            if cell[1] in 'bB':
                black_checkers += 1
            if cell[1] in 'wW':
                white_checkers += 1
    if black_checkers == 0:
        who_winner = 'White'
        is_game_continue = False
        end_of_the_game()
    if white_checkers == 0:
        who_winner = 'Black'
        is_game_continue = False
        end_of_the_game()


def update_game_field():
    global brd
    for item in all_sprites:
        item.kill()
    pos = [4, 104]
    for row in brd:
        for cell in row:
            if list(cell)[1] == 'b':
                icon_png = 'b_c.png'
            if list(cell)[1] == 'w':
                icon_png = 'w_c.png'
            if list(cell)[1] == 'B':
                icon_png = 'b_q.png'
            if list(cell)[1] == 'W':
                icon_png = 'w_q.png'
            if cell == 'bbt_':
                icon_png = 'b_c_c.png'
            if cell == 'bwt_':
                icon_png = 'w_c_c.png'
            if cell == 'bBt_':
                icon_png = 'b_q_c.png'
            if cell == 'bWt_':
                icon_png = 'w_q_c.png'
            if list(cell)[1] != '_':
                sprite_adder(all_sprites, icon_png, pos)
            pos[0] += 80
        pos = [4, pos[1]]
        pos[1] += 80


class Checkers_Board:
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = 0
        self.set_view(left, top, cell_size)

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
        global who_moves
        cell = self.get_cell(mouse_pos)
        x = mouse_pos[0]
        y = mouse_pos[1]
        if x in range(4, 158) and y in range(4, 96):
            sys.exit()
        if x in range(482, 644) and y in range(4, 96):
            start_new_game()
            who_moves = 'WHITE'
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


class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, dx, dy, winner):
        super().__init__(prtc_sprites)
        if winner == 'WHITE':
            name = 'w_q.png'
            sprite_adder(all_sprites, 'white_won.png', (164, 344))
        else:
            name = 'b_q.png'
        self.fire = [load_image(name)]
        for scale in (12, 15, 18, 21, 24, 27, 30, 33, 36, 39):
            self.fire.append(pygame.transform.scale(self.fire[0], (scale, scale)))
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = 0.05

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position, winner):
    particle_count = 8
    numbers = range(-6, 7)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers), winner)


def end_of_the_game():
    global is_game_continue
    global who_winner
    global brd
    end_of_the_game_sound.play()
    for i in range(3):
        for pos in [(114, 104), (244, 114), (354, 104), (484, 114),
                    (124, 234), (234, 224), (364, 234), (474, 224),
                    (104, 214), (254, 204), (344, 214), (494, 204)]:
            create_particles(pos, who_winner.upper())
    white_figures = 0
    black_figures = 0
    for row in brd:
        for cell in row:
            if list(cell)[1] == 'b':
                black_figures += 1
            elif list(cell)[1] == 'w':
                white_figures += 1

    file = open('data/count.txt', 'r')
    count = ((file.read()).split(','))
    file = open('data/count.txt', 'w')
    file.write(",".join([count[0], (f'{count[1].split(":")[0]}:{12 - white_figures}'),
                         (f'{count[2].split(":")[0]}:{12 - black_figures}')]))
    file.close()

    movement_count = (count[0].split(":"))[1]
    white_beaten = (count[1].split(":"))[1]
    black_beaten = (count[2].split(":"))[1]
    f0 = pygame.font.SysFont('Georgia', 54)
    text0 = f0.render(f'Итоги партии', True, (255, 155, 0))
    f1 = pygame.font.SysFont('Georgia', 44)
    text1 = f1.render(f'Количество ходов - {movement_count}', True, (255, 255, 255))
    f2 = pygame.font.SysFont('Georgia', 44)
    text2 = f2.render(f'Белых фигур взято - {12 - white_figures}', True, (255, 255, 255))
    f3 = pygame.font.SysFont('Georgia', 44)
    text3 = f3.render(f'Чёрных фигур взято - {12 - black_figures}', True, (255, 255, 255))

    file = open('data/count.txt', 'r')
    count = ((file.read()).split(','))
    new_count = []
    for text in count:
        new_count.append(f'{text.split(":")[0]}:0')
    file = open('data/count.txt', 'w')
    file.write(",".join(new_count))
    file.close()

    while not is_game_continue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(482, 644) and event.pos[1] in range(4, 96):
                    is_game_continue = True
                    start_new_game()
                    return
                elif event.pos[0] in range(4, 158) and event.pos[1] in range(4, 96):
                    sys.exit()
        all_sprites.update()
        prtc_sprites.update()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        update_game_field()
        load_menu()
        all_sprites.draw(screen)
        screen.fill((0, 0, 0), (0, 104, 648, 748))
        screen.blit(text0, (148, 104))
        screen.blit(text1, (104, 184))
        screen.blit(text2, (94, 264))
        screen.blit(text3, (84, 344))
        prtc_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(100)


checkers_board = Checkers_Board(8, 8, 4, 104, 80)
clock = pygame.time.Clock()
running = True
while running:
    file = open('data/count.txt', 'r')
    count = ((file.read()).split(','))
    f5 = pygame.font.SysFont('Georgia', 22)
    text5 = f5.render(f'Ход №{count[0].split(":")[1]}', True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            checkers_board.get_click(event.pos)

    # checkers_board.render(screen)
    all_sprites.update()
    prtc_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    update_game_field()
    load_menu()
    screen.blit(load_image("Checkers_Board.png"), (0, 100))
    all_sprites.draw(screen)
    prtc_sprites.draw(screen)
    screen.blit(text5, (274, 66))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()