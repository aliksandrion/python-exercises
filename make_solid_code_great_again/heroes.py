from antagonistfinder import AntagonistFinder


class SuperHero:
    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def roundhouse_kick(self):
        print('Bump')

    def attack(self):
        self.roundhouse_kick()


class Incinerate_with_lasers:
    def ultimate(self):
        print('Wzzzuuuup!')


class Fire_a_gun:
    def ultimate(self):
        print('PIU PIU')


class Superman(Incinerate_with_lasers, SuperHero):
    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)


class ChackNorris(Fire_a_gun, SuperHero):
    def __init__(self):
        super(ChackNorris, self).__init__('Chack Norris', True)


class Mass_Media:
    @staticmethod
    def create_news(place, hero):
        if not getattr(place, 'coordinates', True):
            place_name = getattr(place, 'coordinates', True)
        else:
            place_name = getattr(place, 'name', 'place')
        hero_name = getattr(hero, 'name', 'hero')
        print(f'{hero_name} saved the {place_name}!')
