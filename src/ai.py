import random

class AI:
    def compare(self, rps, option):
        #oletusarvo result 0 = tasapeli
        result = 0

        #tietokone valitsee kivi / sakset / paperi
        computer = self.computer_choose(rps, option)

        comparison = sorted([option, computer])

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

    def computer_choose(self, rps, option):
        if len(rps.history) < 2:
            choice = random.choice([1,2,3])
            return choice

        #etsitään max 6 merkin jonoja historiasta, esim. "kspspk"
        sequence_length = min(len(rps.history), 6)
        sequence = rps.history[-sequence_length:]

        #tarkista onko pelattu nykyistä merkkijonoa aikaisemmin
        #jos on, valitse todennäköisin vaihtoehto minkä seuraavana pelaaja pelaa
        #tallenna uudet tiedot samalla tämän kierroksen pelaajan pelatusta valinnasta
        predict_move = self.search_and_update(rps, sequence, option)

        #muuta vaihtoehto sen mukaan minkä pelaaja todennäköisimmin valitsee
        # 1 = kivi, 2 = sakset, 3 = paperi
        if predict_move == "R":
            choice = 3
        elif predict_move == "P":
            choice = 2
        else:
            choice = 1

        return choice

    def search_and_update(self, rps, sequence, option):
        result = 0

        #alkuun tarkista onko koko merkkijono jo dictionaryssä ja valitse saman tien jos on
        if sequence in rps.current_markov.matrix:
            result = max(rps.current_markov.matrix[sequence])

        #jos ei löydy koko merkkijonoa, tarkista niin kauan miten pitkälle pystyy
        #esim jos "kspksp" ei löydy, tarkista alkaen "sp" -> "ksp" -> "pksp"
        #ja niin edelleen miten pitkälle asti löytyy ja sen jälkeen tee valinta
        else:
            part_length = 2
            while True:
                part = sequence[-part_length:]
                if len(part) == len(sequence):
                    break
                if part in rps.current_markov.matrix:
                    result = max(rps.current_markov.matrix[part])
                    part_length += 1
                else:
                    break

        #päivitä tieto mitä vaihtoehtoa pelaaja käytti
        rps.current_markov.matrix[sequence][rps.letters[option]] += 1

        #jos ei löydy mitään merkkijonoa nykyisistä pelaajan valinnoista, tee satunnainen valinta
        if result == 0:
            return random.choice(["R", "P", "S"])

        return result
