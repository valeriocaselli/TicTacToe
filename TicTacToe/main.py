import pygame
class Circle(pygame.sprite.Sprite):
    def __init__(self, center_x, center_y):
        pygame.sprite.Sprite.__init__(self)
        self.center_x = center_x
        self.center_y = center_y

    def draw(self):
        pygame.draw.circle(screen, "BLUE", (self.center_x, self.center_y), 25, 2)

class X(pygame.sprite.Sprite):
    def __init__(self, center_x, center_y):
        pygame.sprite.Sprite.__init__(self)
        self.center_x = center_x
        self.center_y = center_y
        self.image = pygame.image.load("images/mark-x.png")
        self.image = pygame.transform.scale(self.image, (50, 50)).convert_alpha()
        self.rect_image = self.image.get_rect()
        self.rect_image.center = (self.center_x, self.center_y)

    def draw(self):
        screen.blit(self.image, self.rect_image)

def init_game():
    '''
    The function displays the initial game screen
    '''
    screen.fill("#fcfcd5")
    pygame.draw.line(screen, "BLACK",
                     (GAME_WINDOW_WIDTH * 2 / 3, GAME_WINDOW_HEIGHT * 1 / 3),
                     (GAME_WINDOW_WIDTH * 2 / 3, GAME_WINDOW_HEIGHT * 4 / 3), 1)
    pygame.draw.line(screen, "BLACK",
                     (GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT * 1 / 3),
                     (GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT * 4 / 3), 1)
    pygame.draw.line(screen, "BLACK",
                     (GAME_WINDOW_WIDTH * 1 / 3, GAME_WINDOW_HEIGHT * 2 / 3),
                     (GAME_WINDOW_WIDTH * 4 / 3, GAME_WINDOW_HEIGHT * 2 / 3), 1)
    pygame.draw.line(screen, "BLACK",
                     (GAME_WINDOW_WIDTH * 1 / 3, GAME_WINDOW_HEIGHT),
                     (GAME_WINDOW_WIDTH * 4 / 3, GAME_WINDOW_HEIGHT), 1)

def insert_symbol(i: int, j: int, center_x: int, center_y: int):
    '''
    The function inserts the 'x' or 'o' symbol into the grid in row i and column j, depending on the game turn.
    The function takes two integers as parameters too
    Then, the functions creates a x entity or a circle entity, depending on the game turn.
    :param i: row index
    :param j: column index
    :param center_x: x coordinate for the x entity or the circle entity
    :param center_y: y coordinate for the y entity or the circle entity
    '''
    if game_turn % 2 == 0:
        grid[i][j] = grid[i][j].replace(' ', 'x')
        x = X(center_x, center_y)
        x_group.add(x)
    else:
        grid[i][j] = grid[i][j].replace(' ', 'o')
        circle = Circle(center_x, center_y)
        circle_group.add(circle)

def check_win(grid):
    '''
    The function checks whether there is a win or a draw
    '''
    global game_turn
    global win
    global draw

    if game_turn >= 4:
        if grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2] and grid[0][0] != ' ':
            win = True
        elif grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2] and grid[1][0] != ' ':
            win = True
        elif grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2] and grid[2][0] != ' ':
            win = True
        elif grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0] and grid[0][0] != ' ':
            win = True
        elif grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1] and grid[0][1] != ' ':
            win = True
        elif grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2] and grid[0][2] != ' ':
            win = True
        elif grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0] != ' ':
            win = True
        elif grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[0][2] != ' ':
            win = True

    if game_turn == 9 and not win:
        draw = True


pygame.init()

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 400

GAME_WINDOW_WIDTH = 240
GAME_WINDOW_HEIGHT = 240

CELL_WIDTH = GAME_WINDOW_WIDTH // 3
CELL_HEIGHT = GAME_WINDOW_HEIGHT // 3

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption("TicTacToe")
font = pygame.font.SysFont(None, 24)

circle_group = pygame.sprite.Group()
x_group = pygame.sprite.Group()

grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

game_turn = 0
running = True

win = False
draw = False

while running:
    if not win and not draw:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos[0], event.pos[1]

                if CELL_HEIGHT <= mouse_y <= CELL_HEIGHT * 2:
                    # First row
                    if CELL_WIDTH <= mouse_x <= CELL_WIDTH * 2:
                        if grid[0][0] == ' ':
                            insert_symbol(0, 0, CELL_WIDTH * 3 / 2, CELL_HEIGHT * 3 / 2)
                            game_turn += 1
                        else:
                            pass
                    if CELL_WIDTH * 2 <= mouse_x <= CELL_WIDTH * 3:
                        if grid[0][1] == ' ':
                            insert_symbol(0, 1, CELL_WIDTH * 5 / 2, CELL_HEIGHT * 3 / 2)
                            game_turn += 1
                        else:
                            pass
                    if CELL_WIDTH * 3 <= mouse_x <= CELL_WIDTH * 4:
                        if grid[0][2] == ' ':
                            insert_symbol(0, 2, CELL_WIDTH * 7 / 2, CELL_HEIGHT * 3 / 2)
                            game_turn += 1
                        else:
                            pass
                if CELL_HEIGHT * 2 <= mouse_y <= CELL_HEIGHT * 3:
                    # Second row
                    if CELL_WIDTH <= mouse_x <= CELL_WIDTH * 2:
                        if grid[1][0] == ' ':
                            insert_symbol(1, 0, CELL_WIDTH * 3 / 2, CELL_HEIGHT * 5 / 2)
                            game_turn += 1
                        else:
                            pass
                    if CELL_WIDTH * 2 <= mouse_x <= CELL_WIDTH * 3:
                        if grid[1][1] == ' ':
                            insert_symbol(1, 1, CELL_WIDTH * 5 / 2, CELL_HEIGHT * 5 / 2)
                            game_turn += 1
                        else:
                            pass
                    if CELL_WIDTH * 3 <= mouse_x <= CELL_WIDTH * 4:
                        if grid[1][2] == ' ':
                            insert_symbol(1, 2, CELL_WIDTH * 7 / 2, CELL_HEIGHT * 5 / 2)
                            game_turn += 1
                        else:
                            pass
                if CELL_HEIGHT * 3 <= mouse_y <= CELL_HEIGHT * 4:
                    # Third row
                    if CELL_WIDTH <= mouse_x <= CELL_WIDTH * 2:
                        if grid[2][0] == ' ':
                            insert_symbol(2, 0, CELL_WIDTH * 3 / 2, CELL_HEIGHT * 7 / 2)
                            game_turn += 1
                        else:
                            pass
                    if CELL_WIDTH * 2 <= mouse_x <= CELL_WIDTH * 3:
                        if grid[2][1] == ' ':
                            insert_symbol(2, 1, CELL_WIDTH * 5 / 2, CELL_HEIGHT * 7 / 2)
                            game_turn += 1
                        else:
                            pass
                    if CELL_WIDTH * 3 <= mouse_x <= CELL_WIDTH * 4:
                        if grid[2][2] == ' ':
                            insert_symbol(2, 2, CELL_WIDTH * 7 / 2, CELL_HEIGHT * 7 / 2)
                            game_turn += 1
                        else:
                            pass

                check_win(grid)
        init_game()

        for entity in x_group:
            entity.draw()
        for entity in circle_group:
            entity.draw()


    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    win = False
                    draw = False
                    game_turn = 0
                    for entity in x_group:
                        entity.kill()
                    for entity in circle_group:
                        entity.kill()
                    for i in range(3):
                        for j in range(3):
                            grid[i][j] = ' '
        if win and not draw:
            if game_turn % 2 != 0:
                    win_text = font.render("X wins! Press TAB to restart game", True, "BLACK")
            else:
                    win_text = font.render("O wins! Press TAB to restart game", True, "BLACK")

            win_text_rect = win_text.get_rect()
            win_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 10)
            screen.blit(win_text, win_text_rect)
        if not win and draw:
            draw_text = font.render("Draw! Press TAB to restart game", True, "BLACK")
            draw_text_rect = draw_text.get_rect()
            draw_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 10)
            screen.blit(draw_text, draw_text_rect)



    pygame.display.update()

pygame.quit()