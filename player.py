import json

class Player:
    def __init__(self):
        self.name = ''
        self.title = ''
        self.level = 0
        self.combat_skill = 0
        self.combat_skill_bonus = 0
        self.combat_skill_malus = 0
        self.endurance = 0
        self.endurance_max = 0

        self.kai_discipline = []
        self.weapon_skill = ''
        self.belt_pouch = {}
        self.backpack = []
        self.meals = 0
        self.special_items = []

        self.current_chapter = 1
        self.chapter_path = []

    def print(self):
        print('DESCRIPTION DU PROFIL JOUEUR')
        print(f'Nom : {self.name}')
        print(f'Rang: {self.title} de niveau {self.level}')
        print(f'Habilité: {self.combat_skill}')
        print(f'Bonus habilité: {self.combat_skill_bonus}')
        print(f'Malus habilité: {self.combat_skill_malus}')
        print(f'Endurance maxi: {self.endurance_max}')
        print(f'Endurance courante: {self.endurance}')
        print('')
        print(f'Dsisciplines:')
        for kd in self.kai_discipline:
            if kd == 'Maîtrise des armes':
                print(f"{kd}: {self.weapon_skill}")
            else:
                print(kd)
        print('')
        print(f'Bourse: {self.belt_pouch}')
        print(f'Sac à dos - objets: {self.backpack}')
        print(f'Sac à dos - repas: {self.meals}')
        print(f'Objets spéciaux: {self.special_items}')

    def loadfile(self, filename):
        # load the json file
        with open(filename, encoding='utf-8') as json_file:
            data = json.load(json_file)
        self.name = data['name']
        self.title = data['title']
        self.level = data['level']
        self.combat_skill = data['combat_skill']
        self.combat_skill_bonus = data['combat_skill_bonus']
        self.combat_skill_malus = data['combat_skill_malus']
        self.endurance_max = data['endurance_max']
        self.endurance = data['endurance']
        self.meals = data['meals']
        self.kai_discipline = data['kai_discipline']
        self.weapon_skill = data['weapon_skill']