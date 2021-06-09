class Worker:
    __Worker_count = 0

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.cash = {'wage': 0, 'bonus': 0}
        self.cash['wage'] = wage
        self.cash['bonus'] = bonus
        self._incom = self.cash['wage'] + self.cash['bonus']
        self.__Worker_count += 1

    def show_worker(self):
        print(f'{self.name} {self.surname} - {self.position}: {self._incom}')


class Position(Worker):
    __Position_count = 0

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        self.position = position
        self.wage = wage
        self.bonus = bonus
        Position.__Position_count += 1

    def get_fullname(self):
        return f'{self.surname} {self.name}'

    def income(self):
        return self._incom


p1 = Position('Ivan', 'Ivanov', 'CEO', 150000, 50000)
p2 = Position('Petr', 'Petrov', 'CCO', 100000, 20000)
p3 = Position('Ignat', 'Ignatov', 'Manager', 50000, 10000)

print(p1.get_fullname())
print(p1.income())
print(p1.position)
print(p2.get_fullname())
print(p2.income())
print(p2.position)
print(p3.get_fullname())
print(p3.income())
print(p3.position)

print(Worker.show_worker(p1))
print(Worker.show_worker(p2))
print(Worker.show_worker(p3))

