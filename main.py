import pygame
import time
import random
from settings import *
from sprite import *

pygame.mixer.init()
pygame.init()

SCREEN = pygame.display.set_mode((width, hight))
channel1 = pygame.mixer.Channel(0)


def Paly(gameType, gameLevel):
    class Game:
        def __init__(self):
            pygame.init()
            self.amazing = pygame.mixer.Sound("sound/wow.mp3")
            self.wow = pygame.mixer.Sound("sound/wow.mp3")
            self.screen = pygame.display.set_mode((width, hight))
            pygame.display.set_caption(title)
            self.clock = pygame.time.Clock()
            self.BFS = False
            self.DFS = False
            self.ucs = False
            self.A_Star = False
            self.greedy = False
            self.reset = False
            self.counter = 0
            self.gameType = "".join(gameType)

        def draw_tile(self):
            self.tiles = []
            for row, x in enumerate(self.tile_grid):
                self.tiles.append([])
                for col, tile in enumerate(x):
                    self.tiles[row].append(
                        Tile(
                            self,
                            col,
                            row,
                            self.gameType,
                            tile,
                            self.tilesize,
                            self.gameSize,
                        )
                    )

        def Draw_Button(self):
            # self.screen.fill(backgroud_col)
            self.paly_bfs = Button(
                width - 280,
                70,
                150,
                60,
                buttons_col[gameType[0]],
                hover,
                "BFS",
                txt_col,
                25,
            )
            self.paly_bfs.draw_rect(self.screen)
            self.paly_dfs = Button(
                width - 280,
                150,
                150,
                60,
                buttons_col[gameType[0]],
                hover,
                "DFS",
                txt_col,
                25,
            )
            self.paly_dfs.draw_rect(self.screen)
            self.paly_ucs = Button(
                width - 280,
                230,
                150,
                60,
                buttons_col[gameType[0]],
                hover,
                "UCS",
                txt_col,
                25,
            )
            self.paly_ucs.draw_rect(self.screen)
            self.paly_A = Button(
                width - 280,
                310,
                150,
                60,
                buttons_col[gameType[0]],
                hover,
                "A*",
                txt_col,
                25,
            )
            self.paly_A.draw_rect(self.screen)
            self.paly_gready = Button(
                width - 280,
                390,
                150,
                60,
                buttons_col[gameType[0]],
                hover,
                "GREEDY",
                txt_col,
                25,
            )
            self.paly_gready.draw_rect(self.screen)
            self.reset = Button(
                width - 295, 490, 180, 60, reset_col, hover, "RESET", reset_txt_col, 25
            )
            self.reset.draw_ellipse(self.screen)
            self.Back = Button(
                width - 70, 570, 70, 30, back_col, hover, "Back", back_txt_col, 15
            )
            self.Back.draw_rect(self.screen)

        def steps(self):
            temp = str(self.counter)
            self.count = Button(
                620,
                10,
                100,
                40,
                backgroud_col[gameType[0]],
                hover,
                "STEPS = " + temp,
                buttons_col[gameType[0]],
                20,
            )
            self.count.draw_rect(self.screen)

        def new(self):
            self.all_sprite = pygame.sprite.Group() 
            self.tilesize, self.gameSize, start, goal = set_game(gameLevel)
            self.tile_grid = start
            self.tile_grid_complete = goal
            self.ind = 0
            self.draw()
            self.path = []
            self.draw_tile()

        def run(self):
            self.palying = True
            while self.palying:
                self.clock.tick(fps)
                self.events()
                self.update()
                self.draw()

        def update(self):

            if self.BFS == True:
                self.move(self.path[self.ind])
                self.draw_tile()
                self.ind += 1
                self.counter = len(self.path) - self.ind
                self.steps()
                if self.ind >= len(self.path):
                    channel1.play(self.wow)
                    Tile(
                        self,
                        self.gameSize - 1,
                        self.gameSize - 1,
                        self.gameType,
                        self.gameSize**2,
                        self.tilesize,
                        self.gameSize,
                    )
                    self.BFS = False

            if self.DFS:
                self.move(self.path[self.ind])
                self.draw_tile()
                self.ind += 1
                self.counter = len(self.path) - self.ind
                self.steps()
                if self.ind >= len(self.path):
                    channel1.play(self.wow)
                    Tile(
                        self,
                        self.gameSize - 1,
                        self.gameSize - 1,
                        self.gameType,
                        self.gameSize**2,
                        self.tilesize,
                        self.gameSize,
                    )
                    self.DFS = False
            if self.ucs:
                self.move(self.path[self.ind])
                self.draw_tile()
                self.ind += 1
                self.counter = len(self.path) - self.ind
                self.steps()
                if self.ind >= len(self.path):
                    channel1.play(self.wow)
                    Tile(
                        self,
                        self.gameSize - 1,
                        self.gameSize - 1,
                        self.gameType,
                        self.gameSize**2,
                        self.tilesize,
                        self.gameSize,
                    )
                    self.ucs = False
            if self.A_Star:
                self.move(self.path[self.ind])
                self.draw_tile()
                self.ind += 1
                self.counter = len(self.path) - self.ind
                self.steps()
                if self.ind >= len(self.path):
                    channel1.play(self.wow)
                    Tile(
                        self,
                        self.gameSize - 1,
                        self.gameSize - 1,
                        self.gameType,
                        self.gameSize**2,
                        self.tilesize,
                        self.gameSize,
                    )
                    self.A_Star = False
            if self.greedy:
                self.move(self.path[self.ind])
                self.draw_tile()
                self.ind += 1
                self.counter = len(self.path) - self.ind
                self.steps()
                if self.ind >= len(self.path):
                    channel1.play(self.wow)
                    Tile(
                        self,
                        self.gameSize - 1,
                        self.gameSize - 1,
                        self.gameType,
                        self.gameSize**2,
                        self.tilesize,
                        self.gameSize,
                    )
                    self.greedy = False
            self.all_sprite.update()

        def move(self, mov):
            row, col = find_zero(self.tile_grid)
            if mov == "up":
                self.tile_grid[row][col], self.tile_grid[row + 1][col] = (
                    self.tile_grid[row + 1][col],
                    self.tile_grid[row][col],
                )
            elif mov == "down":
                self.tile_grid[row][col], self.tile_grid[row - 1][col] = (
                    self.tile_grid[row - 1][col],
                    self.tile_grid[row][col],
                )

            elif mov == "right":
                self.tile_grid[row][col], self.tile_grid[row][col - 1] = (
                    self.tile_grid[row][col - 1],
                    self.tile_grid[row][col],
                )

            elif mov == "left":
                self.tile_grid[row][col], self.tile_grid[row][col + 1] = (
                    self.tile_grid[row][col + 1],
                    self.tile_grid[row][col],
                )

            pygame.time.delay(300)

        def draw(self):
            self.screen.fill(backgroud_col[gameType[0]])
            self.all_sprite.draw(self.screen)
            self.Draw_Button()
            self.steps()
            pygame.display.flip()

        def events(self):
            for event in pygame.event.get():

                # close window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    if self.paly_bfs.click(mouse_x, mouse_y):
                        self.ind = 0
                        path = Solve("BFS", gameLevel)
                        if path:
                            self.path = path
                            self.BFS = True

                    if self.paly_dfs.click(mouse_x, mouse_y):
                        self.ind = 0
                        path = Solve("DFS", gameLevel)
                        if path:
                            self.path = path
                            self.DFS = True

                    if self.paly_ucs.click(mouse_x, mouse_y):
                        self.ind = 0
                        path = Solve("UCS", gameLevel)
                        if path:
                            self.path = path
                            self.ucs = True

                    if self.paly_A.click(mouse_x, mouse_y):
                        self.ind = 0
                        path = Solve("A_star", gameLevel)
                        if path:
                            self.path = path
                            self.A_Star = True

                    if self.paly_gready.click(mouse_x, mouse_y):
                        self.ind = 0
                        path = Solve("Gready", gameLevel)
                        if path:
                            self.path = path
                            self.greedy = True

                    if self.reset.click(mouse_x, mouse_y):
                        Sounds[gameType[0]].set_volume(1)
                        self.new()

                    if self.Back.click(mouse_x, mouse_y):
                        Sounds[gameType[0]].set_volume(1)
                        gameType.pop(-1)
                        level_menu(gameType)

    game = Game()
    while True:
        game.new()
        game.run()


def level_menu(gameType):
    while True:
        Sounds[gameType[0]].play(-1)
        Sounds[gameType[0]].set_volume(0.2)
        SCREEN.fill(backgroud_col[gameType[0]])
        ChoozeLevel = Button(
            400,
            130,
            200,
            60,
            backgroud_col[gameType[0]],
            hover,
            "Choose The Difficulty Level",
            buttons_col[gameType[0]],
            40,
        )
        ChoozeLevel.draw_rect(SCREEN)
        easy = Button(
            200, 270, 200, 60, buttons_col[gameType[0]], hover, "EASY", yellwo, 25
        )
        easy.draw_rect(SCREEN)
        med = Button(
            600, 270, 200, 60, buttons_col[gameType[0]], hover, "MEDIUM", yellwo, 25
        )
        med.draw_rect(SCREEN)
        hard = Button(
            200, 410, 200, 60, buttons_col[gameType[0]], hover, "HARD", yellwo, 25
        )
        hard.draw_rect(SCREEN)
        ex = Button(
            600, 410, 200, 60, buttons_col[gameType[0]], hover, "EXTREME", yellwo, 25
        )
        ex.draw_rect(SCREEN)
        Back = Button(width - 70, 570, 70, 30, back_col, hover, "Back", white, 15)
        Back.draw_rect(SCREEN)
        for event in pygame.event.get():

            # close window
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if Back.click(mouse_x, mouse_y):
                    Sounds[gameType[0]].stop()
                    main_menu()

                if easy.click(mouse_x, mouse_y):
                    Paly(gameType + ["1"], 1)

                if med.click(mouse_x, mouse_y):
                    Paly(gameType + ["2"], 2)

                if hard.click(mouse_x, mouse_y):
                    Paly(gameType + ["3"], 3)

                if ex.click(mouse_x, mouse_y):
                    Paly(gameType + ["4"], 4)
        pygame.display.update()


def main_menu():
    while True:
        SCREEN.fill(BGColor)
        ChoosePuzzle = Button(
            400, 130, 200, 60, BGColor, hover, "Choose The Puzzle", reset_col, 40
        )
        ChoosePuzzle.draw_rect(SCREEN)
        IcyTower = Button(
            100, 280, 200, 60, (132, 118, 101), hover, "ICY TOWER", BGColor, 25
        )
        IcyTower.draw_rect(SCREEN)
        FeednigFrenzy = Button(
            360, 280, 280, 60, (132, 118, 101), hover, "FEEDING FRENZY", BGColor, 25
        )
        FeednigFrenzy.draw_rect(SCREEN)
        FrogFrenzy = Button(
            700, 280, 230, 60, (132, 118, 101), hover, "FROG FRENZY", BGColor, 25
        )
        FrogFrenzy.draw_rect(SCREEN)
        for event in pygame.event.get():

            # close window
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if IcyTower.click(mouse_x, mouse_y):
                    level_menu(
                        ["1"]
                    )  # gameType should be list 3l4n lma arg3 back a4el a5er 5twa
                if FrogFrenzy.click(mouse_x, mouse_y):
                    level_menu(["2"])
                if FeednigFrenzy.click(mouse_x, mouse_y):
                    level_menu(["3"])
        pygame.display.update()


main_menu()
