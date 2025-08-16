import random

class AI:
    def __init__(self):
        self.options = ["1", "2", "3", "4"]
        self.letters = ["", "R", "S", "P"]
        self.words = ["", "Kivi", "Sakset", "Paperi"]

    def compare(self, history, markov, option):
        #oletusarvo result 0 = tasapeli
        result = 0

        #tietokone valitsee kivi / sakset / paperi
        computer = self.computer_choose(history, markov, option)

        comparison = sorted([option, computer])

        #tieto mitkä valinnat pelaaja ja tietokone teki
        print(f"Pelaaja valitsi: {self.words[option]}")
        print(f"Tekoäly valitsi: {self.words[computer]}")
        print("-----------------------------")

        #molemmat valitsi saman, tasapeli
        if comparison[0] == comparison[1]:
            return result, computer

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

        return result, computer

    def computer_choose(self, history, markov, option):
        if len(history) < 2:
            choice = random.choice([1,2,3])
            return choice

        #etsitään max 6 merkin jonoja historiasta, esim. "kspspk"
        sequence_length = min(len(history), 6)
        sequence = history[-sequence_length:]

        #tarkista onko pelattu nykyistä merkkijonoa aikaisemmin
        #jos on, valitse todennäköisin vaihtoehto minkä seuraavana pelaaja pelaa
        #tallenna uudet tiedot samalla tämän kierroksen pelaajan pelatusta valinnasta
        predict_move = self.search_and_update(sequence, option, markov)

        #muuta vaihtoehto sen mukaan minkä pelaaja todennäköisimmin valitsee
        if predict_move == "R":
            choice = 3
        elif predict_move == "P":
            choice = 2
        else:
            choice = 1

        return choice

    def search_and_update(self, sequence, option, markov):
        result = 0

        #alkuun tarkista onko koko merkkijono jo dictionaryssä ja valitse saman tien jos on
        if sequence in markov.matrix:
            result = max(markov.matrix[sequence])

        #jos ei löydy koko merkkijonoa, tarkista niin kauan miten pitkälle pystyy
        #esim jos "kspksp" ei löydy, tarkista alkaen "sp" -> "ksp" -> "pksp"
        #ja niin edelleen miten pitkälle asti löytyy ja sen jälkeen tee valinta
        #for i in self.current_markov.matrix:
        else:
            part_length = 2
            while True:
                part = sequence[-part_length:]
                if len(part) == len(sequence):
                    break
                if part in markov.matrix:
                    result = max(markov.matrix[part])
                    part_length += 1
                else:
                    break

        #päivitä tieto mitä vaihtoehtoa pelaaja käytti
        markov.matrix[sequence][self.letters[option]] += 1

        #jos ei löydy mitään merkkijonoa nykyisistä pelaajan valinnoista, tee satunnainen valinta
        if result == 0:
            return random.choice(["R", "P", "S"])

        return result