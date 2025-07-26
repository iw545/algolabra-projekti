import random

class RPS:
    def __init__(self, markovs):
        self.options = ["1", "2", "3", "4"]
        self.letters = ["", "R", "P", "S"]
        self.points = {"Pelaaja": 0, "Tietokone": 0}
        self.history = ""
        self.markovs = markovs
        self.current_markov = random.choice(self.markovs)
        self.best = sum(self.current_markov.results)
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

        #päivitä tieto mitä vaihtoehtoa pelaaja käytti
        if len(self.history) > 1:
            self.current_markov.matrix[self.history[-2:]][self.letters[option]] += 1

        #vaihda markov mallia 5 edellisen kierroksen pisteiden perusteella jos tarve
        for i in self.markovs:
            if sum(i.results) > self.best:
                self.best = sum(i.results)
                self.current_markov = i

        self.play()

    def compare(self, option):

        #oletusarvo result 0 = tasapeli
        result = 0

        #tietokone valitsee kivi / sakset / paperi
        computer = self.computer_choose()

        comparison = sorted([option, computer])

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
        frequencies = self.current_markov.matrix.get(self.history[-2:])
        predict_move = max(frequencies.values())

        #muuta vaihtoehto sen mukaan minkä pelaaja todennäköisimmin valitsee
        if predict_move == "R":
            choice = 3
        elif predict_move == "P":
            choice = 2
        else:
            choice = 3

        return choice

class MarkovChain:
    def __init__(self, results, matrix):
        self.results = results
        self.matrix = matrix

#testaus
#results 1 = voitto, 0 = tasapeli, -1 = häviö
'''dictionary rakenteessa ai vertaa minkä 2 kierroksen yhdistelmän jälkeen
pelaaja on pelannut seuraavaksi (esim kivi, kivi jälkeen joko kivi / paperi / sakset, jokaisella
oma arvo merkkaa monta kertaa pelaaja on valinnut sen vaihtoehdon)
'''
markov1 = MarkovChain([1,0,1,1,-1], {"RR": {"R": 2, "P": 1, "S": 0},
                                     "RS": {"R": 0, "P": 0, "S": 1},
                                     "RP": {"R": 0, "P": 1, "S": 0},
                                     "PR": {"R": 1, "P": 3, "S": 0},
                                     "PP": {"R": 2, "P": 2, "S": 0},
                                     "PS": {"R": 1, "P": 0, "S": 0},
                                     "SR": {"R": 0, "P": 0, "S": 0},
                                     "SP": {"R": 1, "P": 0, "S": 0},
                                     "SS": {"R": 0, "P": 2, "S": 3}})

markov2 = MarkovChain([0,-1,1,0,0], {"RR": {"R": 0, "P": 1, "S": 1},
                                     "RS": {"R": 1, "P": 0, "S": 1},
                                     "RP": {"R": 1, "P": 1, "S": 0},
                                     "PR": {"R": 1, "P": 0, "S": 0},
                                     "PP": {"R": 2, "P": 0, "S": 1},
                                     "PS": {"R": 0, "P": 0, "S": 3},
                                     "SR": {"R": 0, "P": 1, "S": 0},
                                     "SP": {"R": 0, "P": 0, "S": 0},
                                     "SS": {"R": 1, "P": 2, "S": 0}})

markov_models = [markov1, markov2]

game = RPS(markov_models)
game.play()
