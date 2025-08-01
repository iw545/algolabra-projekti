import random
from collections import defaultdict

class RPS:
    def __init__(self, markovs):
        self.options = ["1", "2", "3", "4"]
        self.letters = ["", "R", "S", "P"]
        self.words = ["", "Kivi", "Sakset", "Paperi"]
        self.points = {"Pelaaja": 0, "Tietokone": 0}
        self.history = ""
        self.markovs = markovs
        self.current_markov = random.choice(self.markovs)
        self.best_markov = sum(self.current_markov.results)
        self.focus = 5

    def play(self):
        while True:
            option = input("Valitse: 1 (kivi), 2 (sakset), 3 (paperi), 4 (lopeta peli)")
            if option in self.options:
                option = int(option)
                if option == 4:
                    exit()
                break
            print("Valitse uudestaan (1/2/3/4)")
            continue

        #tallennetaan pelaajan valinnat
        self.history += self.letters[option]

        #vertaa pelaajan valintaa tietokoneen valintaan
        result = self.compare(option)

        if result == 0:
            print("Tasapeli")
            self.current_markov.results.append(0)
        elif option == result:
            print("Kierroksen voitti Pelaaja")
            self.points["Pelaaja"] += 1
            self.current_markov.results.append(-1)
        else:
            print("Kierroksen voitti Tietokone")
            self.points["Tietokone"] += 1
            self.current_markov.results.append(1)

        print("Pistetilanne:")
        for x, y in self.points.items():
            print(x, y)

        #vaihda markov mallia 5 edellisen kierroksen pisteiden perusteella jos tarve
        for i in self.markovs:
            if sum(i.results) > self.best_markov:
                self.best_markov = sum(i.results)
                self.current_markov = i

        self.play()

    def compare(self, option):
        #oletusarvo result 0 = tasapeli
        result = 0

        #tietokone valitsee kivi / sakset / paperi
        computer = self.computer_choose()

        comparison = sorted([option, computer])

        #tieto mitkä valinnat pelaaja ja tietokone teki
        print(f"Pelaaja valitsi: {self.words[option]}")
        print(f"Tietokone valitsi: {self.words[computer]}")
        print("-----------------------------")

        #molemmat valitsi saman, tasapeli
        if comparison[0] == comparison[1]:
            return result

        match comparison:
            #kivi vs sakset, kivi voittaa
            case (1,2):
                result = 1
            #kivi vs paperi, paperi voittaa
            case (1,3):
                result = 3
            #sakset vs paperi, sakset voittaa
            case (2,3):
                result = 2

        return result

    def computer_choose(self):
        if len(self.history) < 2:
            choice = random.choice([1,2,3])
            return choice

        choice = 1
        #frequencies = self.current_markov.matrix.get(self.history[-2:])
        #predict_move = max(frequencies.values())

        #etsitään max 6 merkin jonoja historiasta, esim. "kspspk"
        sequence = min(len(self.history), 6)

        #tarkista onko pelaaja pelannut nykyistä merkkijonoa aikaisemmin
        #jos on, valitse todennäköisin vaihtoehto minkä seuraavana pelaa
        #tallenna uudet tiedot samalla tämän kierroksen pelaajan pelatusta valinnasta
        predict_move = self.search_and_update(sequence)

        #muuta vaihtoehto sen mukaan minkä pelaaja todennäköisimmin valitsee
        if predict_move == "R":
            choice = 3
        elif predict_move == "P":
            choice = 2
        else:
            choice = 1

        return choice
    
    def search_and_update(self, sequence):
        #alkuun tarkista onko koko merkkijono jo dictionaryssä ja valitse saman tien jos on
        if sequence in self.current_markov.matrix:
            return max(self.current_markov.matrix[sequence].values())

        #jos ei löydy koko merkkijonoa, tarkista niin kauan miten pitkälle pystyy
        #esim jos "kspksp" ei löydy, tarkista alkaen "sp" -> "ksp" -> "pksp"
        #ja niin edelleen miten pitkälle asti löytyy ja sen jälkeen tee valinta
        #jos ei löydy mitään, tee satunnainen valinta
        #for i in self.current_markov.matrix:
        
        #while True:


        #päivitä tieto mitä vaihtoehtoa pelaaja käytti
        #if len(self.history) > 1:
            #self.current_markov.matrix[self.history[-2:]][self.letters[option]] += 1

        return "R"

class MarkovChain:
    def __init__(self, results):
        self.results = results
        self.matrix = defaultdict(lambda: defaultdict(int))

#testaus
#results 1 = voitto, 0 = tasapeli, -1 = häviö
'''default dictionary rakenteessa ai vertaa minkä 2-6 valinnan yhdistelmän jälkeen
pelaaja on pelannut seuraavaksi (esim kivi, kivi jälkeen joko kivi / paperi / sakset, jokaisella
oma arvo merkkaa monta kertaa pelaaja on valinnut sen vaihtoehdon)
'''
markov1 = MarkovChain([0,1,1,0,-1])
markov2 = MarkovChain([-1,-1,0,1,0])
markov3 = MarkovChain([1,-1,1,1,0])
markov_models = [markov1, markov2, markov3]

game = RPS(markov_models)
game.play()
