import random
import json
from collections import defaultdict
from ai import AI
from game import Game

class RPS:
    def __init__(self, markovs):
        self.options = ["1", "2", "3", "4", "5"]
        self.letters = ["", "R", "S", "P"]
        self.words = ["", "Kivi", "Sakset", "Paperi"]
        self.points = {"Pelaaja": 0, "Tekoäly": 0}
        self.history = ""
        self.default_markovs = markovs
        self.markovs = []
        self.focus = 5

        #lataa edellisten pelattujen pelien tallennetut tiedot .json tiedostoista
        with open("src/player_data.json", "r", encoding='utf-8') as file:
            player_data = json.load(file)
            if not player_data:
                pass
            else:
                self.history = player_data['history']
                self.points = player_data['points']

        with open("src/markovs_data.json", "r", encoding='utf-8') as file:
            markovs_data = json.load(file)
            if not markovs_data:
                self.markovs = markovs
            else:
                for markov_data in markovs_data:
                    markov = MarkovChain(markov_data['results'])
                    current_matrix = defaultdict(lambda: defaultdict(int))
                    for sequence, values in markov_data['matrix'].items():
                        current_matrix[sequence].update(values)
                    markov.matrix = current_matrix
                    markov.history = markov_data['history']
                    self.markovs.append(markov)

        self.current_markov = random.choice(self.markovs)

    def play(self):
        '''
        vaihda markov mallia edellisen "self.focus" muuttujassa
        kerrotun lukumäärän kierrosten pisteiden perusteella ennen kierroksen alkua jos tarve
        oletusarvo self.focus = 5, tulokset voi muuttua paremmiksi / huonommiksi tekoälyn
        älyn kannalta sen mukaan onko alempi / korkeampi tuo luku
        '''
        markov_at_start = self.current_markov
        for i in self.markovs:
            if sum(i.results[-self.focus:]) > sum(self.current_markov.results[-self.focus:]):
                self.current_markov = i
        if markov_at_start != self.current_markov:
            print("Markov AI malli vaihtui tehokkaampaan.")

        while True:
            option = input("Valitse: 1 (kivi), 2 (sakset), " \
            "3 (paperi), 4 (lopeta peli), 5 (asetukset): ")
            if option in self.options:
                option = int(option)
                if option == 4:
                    exit()
                if option == 5:
                    while True:
                        option = input("Nollataanko tilastot ja tekoälyt? 1 (kyllä), 2 (ei): ")
                        option = int(option)
                        if option == 1:
                            with open("src/player_data.json", "w", encoding='utf-8') as file:
                                file.write('[]')
                            with open("src/markovs_data.json", "w", encoding='utf-8') as file:
                                file.write('[]')
                            self.points = {"Pelaaja": 0, "Tekoäly": 0}
                            self.history = ""
                            self.markovs = self.default_markovs
                            print("Tilastot ja tekoälyt nollattu.")
                            self.play()
                        if option == 2:
                            self.play()
                        else:
                            print("Virheellinen valinta.")
                            continue
                break
            else:
                print("Virheellinen valinta.")
                continue

        #vertaa pelaajan valintaa tietokoneen valintaan
        ai_logic = AI()
        result, computer = ai_logic.compare(self, option)

        #kierroksen tilastojen käsittely (tulostukset mm. valinnat, pistetilanne)
        current_round = Game()
        current_round.show_results(self, result, computer, option)

        #tallenna tiedot .json tiedostoihin kierroksen jälkeen
        #pelaajan tiedot
        player_data = {
            "history": self.history,
            "points": self.points}
        with open("src/player_data.json", "w", encoding='utf-8') as file:
            json.dump(player_data, file)

        #tekoälyjen tiedot
        markovs_data = []
        for markov in self.markovs:
            markovs_data.append(
                {'results': markov.results,
                 'matrix': dict(markov.matrix),
                 'history': markov.history})
        with open("src/markovs_data.json", "w", encoding='utf-8') as file:
            json.dump(markovs_data, file)

        #pelaa uudestaan
        self.play()

class MarkovChain:
    def __init__(self, results):
        self.results = results
        self.matrix = defaultdict(lambda: defaultdict(int))
        self.history = ""

#testaus
#results 1 = voitto, 0 = tasapeli, -1 = häviö
'''default dictionary rakenteessa tekoäly vertaa minkä 2-6 valinnan yhdistelmän jälkeen
pelaaja on pelannut seuraavaksi (esim kivi, kivi jälkeen joko kivi / paperi / sakset, jokaisella
oma arvo merkkaa monta kertaa pelaaja on valinnut sen vaihtoehdon)
'''

if __name__ == "__main__":
    markov1 = MarkovChain([0,1,1,0,-1])
    markov2 = MarkovChain([-1,-1,0,1,0])
    markov3 = MarkovChain([1,-1,1,1,0])
    markov4 = MarkovChain([-1,-1,-1,1,0])
    markov5 = MarkovChain([1,1,1,1,0])
    markov_models = [markov1, markov2, markov3, markov4, markov5]

    game = RPS(markov_models)
    game.play()
