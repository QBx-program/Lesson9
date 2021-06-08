class Road:
    __Road_count = 0

    def __init__(self):
        self._length = 0
        self._width = 0
        Road.__Road_count += 1

    def new_Road(self, length, width):
        self._length = length
        self._width = width

    def calc_Road(self, weight, height):
        weight_Road = int(self._length*self._width*weight*height/1000)
        print(f'{self._length}м длины * {self._width}м ширины * {weight}кг массы * {height}см толщины = {weight_Road}тонн')




a = Road()
a.new_Road(5000, 20)
a.calc_Road(25, 5)
