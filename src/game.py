class Game:
    def show_results(self, rps,
                     result, computer, option):
        #tieto mitkä valinnat pelaaja ja tietokone teki
        print(f"Pelaaja valitsi: {rps.words[option]}")
        print(f"Tekoäly valitsi: {rps.words[computer]}")
        print("-----------------------------")

        if result == 0:
            print("Tasapeli")
            rps.current_markov.results.append(0)
        elif option == result:
            print("Kierroksen voitti Pelaaja")
            rps.points["Pelaaja"] += 1
            rps.current_markov.results.append(-1)
        else:
            print("Kierroksen voitti Tekoäly")
            rps.points["Tekoäly"] += 1
            rps.current_markov.results.append(1)

        #tallennetaan pelaajan ja tekoälyn valinnat
        rps.history += rps.letters[option]
        rps.current_markov.history += rps.letters[computer]

        #tulosta tilastot kierroksen lopuksi
        print("Pistetilanne:")
        #miten monen kierroksen valinnat näytetään tilastoissa
        history_length = 10
        for x, y in rps.points.items():
            if x == "Pelaaja":
                print(x, y, "---", "Viimeisen", history_length, "kierroksen valinnat:",
                      rps.history[-history_length:])
            else:
                print(x, y, "---", "Viimeisen", history_length, "kierroksen valinnat:",
                      rps.current_markov.history[-history_length:])
