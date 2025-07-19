#alkuun väliaikainen yksinkertainen tapa tietokoneella valita oma vaihtoehto sattumanvaraisesti (kivi / sakset / paperi)
import random

class RPS:
    def __init__(self):
        self.options = ["1", "2", "3"]
        self.results = []
        self.points = {"Pelaaja": 0, "Tietokone": 0}

    def play(self):

        while True:
            option = input("Valitse: 1 (kivi), 2 (sakset), 3 (paperi)")
            if option in self.options:
                option = int(option)
                break
            else:
                print("Valitse uudestaan (1/2/3)")
                continue

        result = self.compare(option)
        self.results.append(result)

        if option == result:
            print("Kierroksen voitti Pelaaja")
            self.points["Pelaaja"] += 1
        else:
            print("Kierroksen voitti Tietokone")
            self.points["Tietokone"] += 1

        print("Pistetilanne:")
        for x, y in self.points.items():
            print(x, y)

        self.play()

    def compare(self, option):

        #oletusarvo result 0 = tasapeli
        result = 0
        computer = random.choice([1,2,3])
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
    
#testaus
game = RPS()
game.play()