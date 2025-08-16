import random
from collections import defaultdict
from ai import AI

class RPS:
    def __init__(self, markovs):
        self.options = ["1", "2", "3", "4"]
        self.letters = ["", "R", "S", "P"]
        self.words = ["", "Kivi", "Sakset", "Paperi"]
        self.points = {"Pelaaja": 0, "Tekoäly": 0}
        self.history = ""
        self.markovs = markovs
        self.current_markov = random.choice(self.markovs)
        self.focus = 5

    def play(self):
        #vaihda markov mallia edellisen "self.focus" muuttujassa
        #kerrotun lukumäärän kierrosten pisteiden perusteella ennen kierroksen alkua jos tarve
        #oletusarvo self.focus = 5, tulokset voi muuttua paremmiksi / huonommiksi tekoälyn
        #älyn kannalta sen mukaan onko alempi / korkeampi tuo luku
        markov_at_start = self.current_markov
        for i in self.markovs:
            if sum(i.results[-self.focus:]) > sum(self.current_markov.results[-self.focus:]):
                self.current_markov = i
        if markov_at_start != self.current_markov:
            print("Markov AI malli vaihtui tehokkaampaan.")

        while True:
            option = input("Valitse: 1 (kivi), 2 (sakset), 3 (paperi), 4 (lopeta peli)")
            if option in self.options:
                option = int(option)
                if option == 4:
                    exit()
                break
            print("Valitse uudestaan (1/2/3/4)")
            continue

        #vertaa pelaajan valintaa tietokoneen valintaan
        ai_logic = AI()
        result, computer = ai_logic.compare(self.history, self.current_markov, option)

        if result == 0:
            print("Tasapeli")
            self.current_markov.results.append(0)
        elif option == result:
            print("Kierroksen voitti Pelaaja")
            self.points["Pelaaja"] += 1
            self.current_markov.results.append(-1)
        else:
            print("Kierroksen voitti Tekoäly")
            self.points["Tekoäly"] += 1
            self.current_markov.results.append(1)

        #tallennetaan pelaajan ja tekoälyn valinnat
        self.history += self.letters[option]
        self.current_markov.history += self.letters[computer]

        #tulosta tilastot kierroksen lopuksi
        print("Pistetilanne:")
        #miten monen kierroksen valinnat näytetään tilastoissa
        history_length = 20
        for x, y in self.points.items():
            if x == "Pelaaja":
                print(x, y, "---", "Viimeisen", history_length, "kierroksen valinnat:",
                      self.history[-history_length:])
            else:
                print(x, y, "---", "Viimeisen", history_length, "kierroksen valinnat:",
                      self.current_markov.history[-history_length:])

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
    markov_models = [markov1, markov2, markov3]

    game = RPS(markov_models)
    game.play()
