class Tomato:
    states = ['absent', 'blooming', 'green', 'red']  # Стадии созревания

    def __init__(self, index):
        self._index = index  # Индекс (публичное свойство)
        self._state = self.states[0]  # Стадия созревания (первое значение из states)

    def grow(self):
        """Переход на следующую стадию созревания"""
        current_state_index = self.states.index(self._state)
        if current_state_index < len(self.states) - 1:
            self._state = self.states[current_state_index + 1]

    def is_ripe(self):
        """Проверка, что томат созрел"""
        return self._state == 'red'


class TomatoBush:
    def __init__(self, number_of_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(number_of_tomatoes)]  # Список объектов Tomato

    def grow_all(self):
        """Вырастить все томаты"""
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        """Проверить, что все томаты спелые"""
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        """Собрать урожай, очистив список томатов"""
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        self.name = name  # Имя садаводника (публичное свойство)
        self._plant = plant  # Растение (объект класса TomatoBush)

    def work(self):
        """Уход за растением, чтобы оно становилось более зрелым"""
        self._plant.grow_all()

    def harvest(self):
        """Сбор урожая"""
        if self._plant.all_are_ripe():
            print(f"{self.name} собрал урожай.")
            self._plant.give_away_all()
        else:
            print(f"{self.name} не может собрать урожай, так как некоторые томаты еще не созрели.")

    @staticmethod
    def knowledge_base():
        """Вывод справки по садоводству"""
        print("Справка по садоводству:")
        print("1. Поливайте помидоры регулярно.")
        print("2. Обеспечьте достаточное количество света.")
        print("3. Следите за вредителями.")
        print("4. Собирать урожай следует, когда помидоры полностью красные.")


# Тест 1
Gardener.knowledge_base()  # Вызов справки по садоводству

# Тест 2
bush = TomatoBush(3)  # Создание объекта класса TomatoBush
gardener = Gardener("Алексей", bush)  # Создание объекта класса Gardener

# Тест 3
gardener.work()  # Уход за кустом

# Тест 4
gardener.harvest()  # Попробуем собрать урожай, когда томаты еще не дозрели

# Увеличиваем созревание
gardener.work()
gardener.harvest()  # Попробуем собрать урожай снова

# Увеличиваем созревание до полного спелости
gardener.work()
gardener.work()

# Тест 5
gardener.harvest()  # Теперь должно получится собрать урожай