class Stationery:

    title = 'Отрисовка'

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def draw(self):
        print('Рисование ручкой')

class Pencil(Stationery):

    def draw(self):
        print('Рисование карандашом')

class Handle(Stationery):

    def draw(self):
        print('Рисование маркером')

run = Stationery()
run.draw()

run = Pen()
run.draw()

run = Pencil()
run.draw()

run = Handle()
run.draw()