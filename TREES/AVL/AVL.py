import sys
import random


class Node(object):
    def __init__(self, klucz):
        self.klucz = klucz
        self.lewy = None
        self.prawy = None
        self.wysokosc = 1


class DrzewoAVL(object):

    def dodaj_node(self, korzen, klucz):
        if not korzen:
            return Node(klucz)
        elif klucz < korzen.klucz:
            korzen.lewy = self.dodaj_node(korzen.lewy, klucz)
        else:
            korzen.prawy = self.dodaj_node(korzen.prawy, klucz)

        korzen.wysokosc = 1 + max(self.podajWysokosc(korzen.lewy), self.podajWysokosc(korzen.prawy))
        zbalansowanie = self.podajBalans(korzen)
        if zbalansowanie > 1:
            if self.podajBalans(korzen.lewy) >= 0:
                return self.obrotPrawo(korzen)
            else:
                korzen.lewy = self.obrotLewo(korzen.lewy)
                return self.obrotPrawo(korzen)
        if zbalansowanie < -1:
            if self.podajBalans(korzen.prawy) <= 0:
                return self.obrotLewo(korzen)
            else:
                korzen.prawy = self.obrotPrawo(korzen.prawy)
                return self.obrotLewo(korzen)
        return korzen

    def usun_node(self, korzen, klucz):
        if not korzen:
            return korzen
        elif klucz < korzen.klucz:
            korzen.lewy = self.usun_node(korzen.lewy, klucz)
        elif klucz > korzen.klucz:
            korzen.prawy = self.usun_node(korzen.prawy, klucz)
        else:
            if korzen.lewy is None:
                temp = korzen.prawy
                korzen = None
                return temp
            temp = self.najmniejszaWartosc(korzen.prawy)
            korzen.klucz = temp.klucz
            korzen.prawy = self.usun_node(korzen.prawy, temp.klucz)

        if korzen is None:
            return korzen

        korzen.wysokosc = 1 + max(self.podajWysokosc(korzen.lewy), self.podajWysokosc(korzen.prawy))

        zbalansowanie = self.podajBalans(korzen)

        if zbalansowanie > 1:
            if self.podajBalans(korzen.lewy) >= 0:
                return self.obrotPrawo(korzen)
            else:
                korzen.lewy = self.obrotLewo(korzen.lewy)
                return self.obrotPrawo(korzen)
        if zbalansowanie < -1:
            if self.podajBalans(korzen.prawy) <= 0:
                return self.obrotLewo(korzen)
            else:
                korzen.prawy = self.obrotPrawo(korzen.prawy)
                return self.obrotLewo(korzen)
        return korzen

    def obrotLewo(self, z):
        y = z.prawy
        temp2 = y.lewy
        y.lewy = z
        z.prawy = temp2
        z.wysokosc = 1 + max(self.podajWysokosc(z.lewy), self.podajWysokosc(z.prawy))
        y.wysokosc = 1 + max(self.podajWysokosc(y.lewy), self.podajWysokosc(y.prawy))
        return y

    def obrotPrawo(self, z):
        y = z.lewy
        temp2 = y.prawy
        y.prawy = z
        z.lewy = temp2
        z.wysokosc = 1 + max(self.podajWysokosc(z.lewy), self.podajWysokosc(z.prawy))
        y.wysokosc = 1 + max(self.podajWysokosc(y.lewy), self.podajWysokosc(y.prawy))
        return y

    def podajWysokosc(self, korzen):
        if not korzen:
            return 0
        return korzen.wysokosc

    def podajBalans(self, korzen):
        if not korzen:
            return 0
        return self.podajWysokosc(korzen.lewy) - self.podajWysokosc(korzen.prawy)

    def najmniejszaWartosc(self, korzen):
        if korzen is None or korzen.lewy is None:
            return korzen
        return self.najmniejszaWartosc(korzen.lewy)

    def preOrder(self, korzen):
        if not korzen:
            return
        print("{0} ".format(korzen.klucz), end="")
        self.preOrder(korzen.lewy)
        self.preOrder(korzen.prawy)

    def inOrder(self, korzen):
        if not korzen:
            return
        self.inOrder(korzen.lewy)
        print("{0} ".format(korzen.klucz), end="")
        self.inOrder(korzen.prawy)

    def printing(self, aktualnie, ind, ostatni):
        if aktualnie is not None:
            sys.stdout.write(ind)
            if ostatni:
                sys.stdout.write("R----")
                ind += "     "
            else:
                sys.stdout.write("L----")
                ind += "|    "
            print(aktualnie.klucz)
            self.printing(aktualnie.lewy, ind, False)
            self.printing(aktualnie.prawy, ind, True)

def AVL_TREE_FUNC():
    koniec = False
    wybor1 = 0
    wybor2 = 0
    wybor3 = 0
    wybor4 = -1
    nums = []
    drzewo = DrzewoAVL()
    korzen = None


    print("----AVL Tree----\nWybierz tryb wprowadzania danych wejściowych:")
    print("1. Manualny")
    print("2. Automatyczny")
    while True:
        try:
            wybor1 = int(input())
            if wybor1 == 1 or wybor1 == 2:
                break
            else:
                print("Prosze wprowadzić wartość 1 lub 2")
        except ValueError:
            print("Prosze wprowadzić wartość 1 lub 2")

    if wybor1 == 1:
        print("Wprowadz maksymalnie 10 liczb oddzielonych spacja")
        while True:
            try:
                nums = [int(x) for x in input().split()]
                if 0 < len(nums) <= 10:
                    break
                else:
                    print("Prosze wprowadzić conajmniej jedna liczbe oraz co najwyzej 10 liczb")
            except ValueError:
                print("Prosze wprowadzic wartości liczbowe")

    else:
        for i in range(10):
            n = random.randint(1, 1000)
            nums.append(n)

    for num in nums:
        korzen = drzewo.dodaj_node(korzen, num)

    while not koniec:
        print("Wybierz procedure:")
        print("1. Wyszukanie najmniejszej oraz największej wartości z wypisanie ściezki")
        print("2. Usuń dany element drzewa")
        print("3. Wypisz wszystkie elementy drzewa metodą in-order")
        print("4. Wypisz wszystkie elementy drzewa metodą pre-order")
        print("5. Usniecie calego drzewa")
        print("6. Wyjscie")

        while True:
            try:
                wybor2 = int(input())
                if 0 < wybor2 < 7:
                    break
                else:
                    print("Prosze wprowadzić odpowiednią wartość")
            except ValueError:
                print("Prosze wprowadzić odpowiednią wartość")

        if wybor2 == 1:
            print(min(nums))
            print(max(nums))
            drzewo.printing(korzen, "", True)

        elif wybor2 == 2:
            print("Ile węzłów chcesz usunąć?")
            while True:
                try:
                    wybor3 = int(input())
                    if 0 < wybor3 < 11:
                        break
                    else:
                        print("Prosze wprowadzić odpowiednią wartość")
                except ValueError:
                    print("Prosze wprowadzić odpowiednią wartość")
            for i in range(wybor3):
                print("Podaj wartosc klucza do usuniecia")
                while True:
                    try:
                        wybor4 = int(input())
                        if -1 < wybor3 < 10:
                            break
                        else:
                            print("Prosze wprowadzić odpowiednią wartość")
                    except ValueError:
                        print("Prosze wprowadzić odpowiednią wartość")
                drzewo.usun_node(korzen, wybor4)

        elif wybor2 == 3:
            drzewo.inOrder(korzen)
            print("\n")

        elif wybor2 == 4:
            drzewo.preOrder(korzen)
            print("\n")

        elif wybor2 == 5:
            print("Usunieto drzewo")

        elif wybor2 == 6:
            koniec = True
