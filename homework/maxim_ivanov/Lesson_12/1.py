from operator import itemgetter, attrgetter


class Flowers:
    type = 'flowers'
    name = 'flower'

    def __init__(self, lifetime, color, length, cost):
        self.lifetime = lifetime
        self.color = color
        self.length = length
        self.cost = cost

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Rose(Flowers):
    name = 'rose'

    def __init__(self, lifetime, color, length, cost):
        super().__init__(lifetime, color, length, cost)


class Tulip(Flowers):
    name = 'tulip'

    def __init__(self, lifetime, color, length, cost):
        super().__init__(lifetime, color, length, cost)


class Snowdrop(Flowers):
    name = 'snowdrop'

    def __init__(self, lifetime, color, length, cost):
        super().__init__(lifetime, color, length, cost)


class Bouquet:
    def __init__(self, *args):
        self.flowers = [*args]
        self.__cost_bouquet = self.__calc_cost_bouquet()
        self.__wilting_time = self.__calc_wilting_time()

    def add_flower(self, flower):
        self.flowers.append(flower)

    def __calc_cost_bouquet(self):
        return sum(x.cost for x in self.flowers)

    def __calc_wilting_time(self):
        return sum(x.lifetime for x in self.flowers) / len(self.flowers)

    @property
    def get_cost_bouquet(self):
        return self.__cost_bouquet

    @property
    def get_wilting_time(self):
        return self.__wilting_time

    def sort_flowers(self, value='cost', ascending=False):
        sorted_flowers = sorted(self.flowers, key=attrgetter(value), reverse=ascending)
        return sorted_flowers

    def search_flowers(self, name):
        return list(filter(lambda flower: flower.name == name, self.flowers))


rose_red = Rose(48, 'красный', 40, 100)
tulip_yellow = Tulip(24, 'желтый', 50, 50)
snowdrop_white = Snowdrop(12, 'белый', 30, 150)

my_bouquet = Bouquet(rose_red, tulip_yellow, snowdrop_white)
