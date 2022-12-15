import json
import io

class GameData:
    def __init__(self):
        self.levels = ['Postulant', 'Novice', 'Apprenti', 'Disciple', 'Initié', 'Aspirant', 'Gardien', 'Guerrier',
                       'Savant', 'Maître']
        self.kai_disciplines = {}
        self.load_disciplines()
        self.chapters = {}
        self.load_chapters()

    def get_textchoice(self, num, choice):
        return self.chapters[str(num)]["Acces" + str(choice) + "-Texte"]
    def get_textchapter(self, num):
        return self.chapters[str(num)]["Texte"]

    def load_disciplines(self):
        with io.open('data/kai_discipline.json', 'r', encoding='utf-8') as f:
            self.kai_disciplines = json.load(f)

    def load_chapters(self):
        with io.open('data/chapters.json', 'r', encoding='utf-8') as f:
            self.chapters = json.load(f)

    def print(self):
        print('DONNEES GENERIQUE DU JEU')
        print(f'Rangs : {self.levels}')

        print('')
        print(f'Discipline :')
        for key, value in self.kai_disciplines.items():
            print(f"{key}: {value}")

        print('')
        print('Chapitre 10:')
        print(self.get_textchapter(10))
        print(self.get_textchoice(10, 1))

        print('')
        print(f'Dernier fichier de sauvegarde : {self.last_game()}')

    def last_game(self):
        file = 'data/player202212141045.json'
        return file
