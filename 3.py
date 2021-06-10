class Work:
    __Work_count = 0

    def __init__(self, *args, **kwargs):
        if args:
            self.name = args[0]
            self.surname = args[1]
            self.position = args[2]
        if kwargs:
            self._incom = kwargs['wage'] + kwargs['bonus']
        Work.__Work_count += 1

    def show_work(self):
        print(self.name, self.surname, self.position, self._incom)

class Position(Work):
    __Position_count = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.posit = args[2]
        self.wage = kwargs['wage']
        self.bonus = kwargs['bonus']
        Position.__Position_count += 1

    def get_full_name(self):
        print(self.surname, self.name)

    def get_total_income(self):
        print(self._incom)

    def wage_bonus(self):
        print(f'wage: {self.wage}, bonus: {self.bonus}')

p = Work('Ivan', 'Ivanov', 'CEO', **{'wage': 150000, 'bonus': 50000})
p.show_work()

p1 = Position('Petr', 'Petrov', 'CCO', **{'wage': 100000, 'bonus': 20000})
p1.get_full_name()
p1.get_total_income()
p1.wage_bonus()

p3 = Position('Ignat', 'Ignatov', 'Manager', **{'wage': 50000, 'bonus': 10000})
p3.get_full_name()
p3.get_total_income()
p3.wage_bonus()

# class Work:
#     __Work_count = 0
#
#     def __init__(self, *args, **kwargs):
#         if args:
#             self.name = args[0]
#             self.surname = args[1]
#             self.position = args[2]
#         if kwargs:
#             self._incom = {}
#             self._incom['wage'] = kwargs['wage']
#             self._incom['bonus'] = kwargs['bonus']
#         Work.__Work_count += 1
#
#     def show_work(self):
#         print(self.name, self.surname, self.position, self._incom)
#
# class Position(Work):
#     __Position_count = 0
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.posit = args[2]
#         self.wage = kwargs['wage']
#         self.bonus = kwargs['bonus']
#         Position.__Position_count += 1
#
#     def get_full_name(self):
#         print(self.surname, self.name)
#
#     def get_total_income(self):
#         print(self._incom['wage']+self._incom['bonus'])
#
#     def wage_bonus(self):
#         print(f'wage: {self.wage}, bonus: {self.bonus}')
#
# p = Work('Ivan', 'Ivanov', 'CEO', **{'wage': 150000, 'bonus': 50000})
# p.show_work()
#
# p1 = Position('Petr', 'Petrov', 'CCO', **{'wage': 100000, 'bonus': 20000})
# p1.get_full_name()
# p1.get_total_income()
# p1.wage_bonus()
#
# p3 = Position('Ignat', 'Ignatov', 'Manager', **{'wage': 50000, 'bonus': 10000})
# p3.get_full_name()
# p3.get_total_income()
# p3.wage_bonus()
#
