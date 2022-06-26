from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import sys
import pygame
import grid

a=510
b=480
ffps=1

class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.ui = uic.loadUi("mydesign.ui")
        self.uiy = uic.loadUi("settings.ui")
        self.uii = uic.loadUi("rules.ui")
        self.start()
        self.btn_start()
        self.btn_settings()
        self.btn_back()
        self.btn_size1()
        self.btn_size2()
        self.btn_size3()
        self.btn_size4()
        self.btn_exit()
        self.spin()
        self.rules()
        self.btn_back1()

    def start(self):
        self.ui.show()

    def settings(self):
        self.uiy.show()

    def info(self):
        self.uii.show()

    def btn_settings(self):
        self.ui.btn_settings.clicked.connect(lambda: self.settings())
        self.ui.btn_settings.clicked.connect(lambda: self.ui.close())

    def btn_start(self):
        self.ui.btn_start.clicked.connect(lambda: self.ui.close())
        self.ui.btn_start.clicked.connect(lambda: self.game())

    def btn_back(self):
        self.uiy.btn_back.clicked.connect(lambda: self.start())
        self.uiy.btn_back.clicked.connect(lambda: self.uiy.close())

    def btn_exit(self):
        self.ui.btn_exit.clicked.connect(lambda: self.ui.close())

    def size1(self):
        global a
        global b
        a=1920
        b=1080

    def size2(self):
        global a
        global b
        a=1560
        b=900

    def size3(self):
        global a
        global b
        a=1200
        b=780

    def size4(self):
        global a
        global b
        a=720
        b=720

    def btn_size1(self):
        self.uiy.pushButton.clicked.connect(lambda: self.size1())

    def btn_size2(self):
        self.uiy.pushButton_2.clicked.connect(lambda: self.size2())

    def btn_size3(self):
        self.uiy.pushButton_3.clicked.connect(lambda: self.size3())

    def btn_size4(self):
        self.uiy.pushButton_4.clicked.connect(lambda: self.size4())

    def spin(self):
        self.uiy.spinBox.valueChanged.connect(self.fps)

    def fps(self):
        global ffps
        ffps = self.uiy.spinBox.value()

    def rules(self):
        self.ui.btn_info.clicked.connect(lambda: self.info())
        self.ui.btn_info.clicked.connect(lambda: self.ui.close())

    def btn_back1(self):
        self.uii.btn_back1.clicked.connect(lambda: self.start())
        self.uii.btn_back1.clicked.connect(lambda: self.uii.close())

    def game(self):

        # Размеры окна
        width = a
        height = b
        size = (width, height)

        # Создаем окно
        pygame.init()
        pygame.display.set_caption("Game of Life")
        screen = pygame.display.set_mode(size)
        clock = pygame.time.Clock()
        fps = ffps

        # Толщина и размер сетки
        rate = 30
        thickness = 1

        Grid = grid.layout(width, height, rate, thickness)
        Grid.random()

        # Константы цветов RGB
        black = (0, 0, 0)
        white = (255, 255, 255)
        green = (76, 175, 80)

        # Основной цикл
        pause = False
        start = True
        while start:
            clock.tick(fps)
            screen.fill(black)

            Grid.conway(off=white, on=green, surface=screen, pause=pause)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   start = False
                if event.type == pygame.KEYUP:

                    #Выход
                    if event.key == pygame.K_ESCAPE:
                        start = False

                    #Пауза
                    if event.key == pygame.K_SPACE:
                        pause = not pause

                    if pause == False:
                        fps = ffps
                    if pause == True:
                        fps = 30

            # ПКМ
            if pygame.mouse.get_pressed()[2]:
                mouseX, mouseY = pygame.mouse.get_pos()
                Grid.rightmouse(mouseX, mouseY)

            # ЛКМ
            if pygame.mouse.get_pressed()[0]:
                mouseX, mouseY = pygame.mouse.get_pos()
                Grid.leftmouse(mouseX, mouseY)

            # Обновление экрана
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())