#!/usr/bin/python
# -*- coding: utf-8 -*-



u"""Skrypt zawiera definicję klasy Przedmiot, która służy do przechowywania
danych o wynikach studentów na danym przedmiocie i obliczania procentowej
obecności na zajęciach, ilości punktów, etc."""

# Należy poprawić ten notatki według standardów Pythona.



######################################################################
# Importowanie modułów

import string  # Potrzebuję tego modułu, by sproawdzić string do samych
# małych liter.

######################################################################



class Przedmiot(object):
    u"""Klasa reprezentująca przedmiot zajęciowy."""

    def __init__(self, nazwa_przedmiotu, semestr, rok_akad):
        u"""Trzeba podać NAZWĘ przedmiotu, SEMESTR zimowy lub letni,
        i ROK_AKADEMICKI.

        Tworzy dwulinijkowy string __opis_przedmiotu
        z nazwą przedmiotu w pierwszej, w drugiej jest podany semestr
        i rok akademicki. Następnie tworzy atrybuty: __lista_studentów = [],
        __ilosc zajęć = 0, __ilosc_zestawow_zadan = 0,
        __zestawy_zadan_puktacja = []."""

        self.przed_atrybuty(nazwa_przedmiotu, semestr, rok_akad)


    def przed_atrybuty(self, nazwa_przedmiotu, semestr, rok_akad):
        self.__opis_przed = str(nazwa_przedmiotu) + ', semestr ' \
                            + str(semestr) + ' ' + str(rok_akad) + '\n'
        
        self.__lista_stud = []
        self.__opis_wyn = "Imie      Nazwisko  "
        self.__nazwa_pliku_z_wyn = nazwa_przedmiotu + '-' + semestr \
                                   + '-' + rok_akad + '-Wyniki.txt'



    def dodaj_studenta(self, student_inst):
        u"""Dodaje instację studenda STUDENT_INST do atrybutu
            __LISTA_STUDENTOW"""
        self.__lista_stud.append(student_inst)


    def sortuj_studentow(self):
        u"""Sortuje listę studentów alfabetycznie."""
        pass

    def zapisz_do_pliku(self):
        with open(self.__nazwa_pliku_z_wyn, 'w') as wyniki:
            wyniki.write(self.__opis_przed)
            for student in self.__lista_stud:
                wyniki.write(student.wyniki_studenta())


######################################################################
# Klasa Grupa


class Grupa(Przedmiot):
    u"""Klasa reprezentująca grupę zajęciową danego PRZEDMIOTu
    (Przedmiot)"""

    def __init__(self, nazwa_przedmiotu, semestr, rok_akad, numer_grupy):
        self.przed_atrybuty(nazwa_przedmiotu, semestr, rok_akad)
        self.grupa_atrybuty(nazwa_przedmiotu, semestr, rok_akad, numer_grupy)


    def grupa_atrybuty(self, nazwa_przedmiotu, semestr, rok_akad,
                       numer_grupy):

        self.__num_grupy = numer_grupy
        self.nazwa_pliku_z_wyn = nazwa_przedmiotu + '-' + semestr \
                                      + '-' + rok_akad + '-' \
                                      + 'Grupa-' + str(numer_grupy) \
                                      + '-Wyniki.txt'
        # Nie rozumiem, czemu tego nie nadpisuje?!
        self.__ilosc_zajec = 0  # Liczba zajęć jaka się odbyła. Liczone są
        # również te na które nikt nie przyszedł.
        self.__ilosc_sprawdzianow = 0 # Kolokwium = łac. odpowiedź ustana.
        # Mi to nie pasuje.

        
    def odbyly_sie_zajecia(self):
        u"""Zwiększa atrybut SELF.__ILOSC_ZAJEC o 1."""
        self.__ilosc_zajec += 1


    def byl_sprawdzian(self):
        self.__ilosc_sprawdzianow += 1


    def bylo_zajec(self):
        return self.__ilosc_zajec
        


######################################################################
# Klasa Grupa Zestawy Zadań


class GrupaZesZad(Grupa):
    u"""Grupa Zestaw Zadań"""

    def __init__(self, nazwa_przedmiotu, semestr, rok_akad, numer_grupy):
        self.przed_atrybuty(nazwa_przedmiotu, semestr, rok_akad)
        self.grupa_atrybuty(numer_grupy)
        self.grupa_zes_zad_atry()


    def grupa_zes_zad_atry(self):
        self.__ilosc_zestawow_zadan = 0
        self.__zestawy_zadan_punktacja = []


    def byl_zestaw_zadan(self, punktacja_zestawu):
        u"""Jeśli był nowy zestaw zadań, to punktację zadań dodajemy do listy
        punktacji.

        Metoda sprawdza, czy lista jest krotką. Krotką, bo raz ustawiona,
        punktacja ma być niezmienna."""
        assert isinstance(punktacja_zestawu, tuple), \
            u"Punktacja zestawu nie jest krotką!"

        self.__zestawy_zadan_puktacja.append(punktacja_zestawu)

    

######################################################################
# Klasa Grupa Projekt Ocena


class GrupaProOce(Grupa):
    u"""Grupa, projekt za ocenę."""

    def __init__(self, nazwa_przedmiotu, semestr, rok_akademicki,
                 numer_grupy):
        self.__ilosc_projektow = 0

        Grupa.__init__(self, nazwa_przedmiotu, semestr, rok_akademicki,
                       numer_grupy)


    def byl_projekt(self):
        self.__ilosc_projektow += 1

    

######################################################################
# Klasa Grupa Projekt Punkty


class GrupaProPun(Grupa):
    u"""Grupa, projekt za punkty."""

    def __init__(self, nazwa_przedmiotu, semestr, rok_akademicki,
                 numer_grupy):
        Grupa.__init__(self, nazwa_przedmiotu, semestr, rok_akademicki,
                       numer_grupy)

        self.__ilosc_projektow = 0
        self.__projekty_punktacja = []


    def byl_projekt(self, punkty_za_projekt):
        assert isinstance(punktacja_zestawu, int), \
            u"Punktacja zestawu musi być intem!"

        self.__ilosc_projektow += 1
        self.__zestawy_zadan_puktacja.append(punktacja_zestawu)

    

######################################################################
# Klasa Grupa Projekt Ocena


class GrupaProOce(Grupa):
    u"""Grupa, projekt za ocenę."""

    def __init__(self, nazwa_przedmiotu, semestr, rok_akademicki,
                 numer_grupy):
        Grupa.__init__(self, nazwa_przedmiotu, semestr, rok_akademicki,
                       numer_grupy)
        self.__ilosc_projektow = 0


    def byl_projekt(self):
        self.__ilosc_projektow += 1

    

######################################################################
# Klasa Grupa Sprawdzian Punkty


class GrupaSprPun(Grupa):
    u"""Grupa projekt sprawdzian za oceną."""

    def __init__(self, nazwa_przedmiotu, semestr, rok_akademicki,
                 numer_grupy):
        Grupa.__init__(self, nazwa_przedmiotu, semestr, rok_akademicki,
                       numer_grupy)
        self.__ilosc_sprawdzianow = 0
        


    def byl_sprawdzian(self, punktacja_sprawdzianu):
        u"""Jeśli był nowy zestaw zadań, to punktację zadań dodajemy do listy
        punktacji.

        Metoda sprawdza, czy lista jest intem POPRAW. Krotką, bo raz
        ustawiona,
        punktacja ma być niezmienna."""
        assert isinstance(punktacja_sprawdzianu, int), \
            u"Punktacja sprawdzianu nie jest intem!"

        self.__ilosc_sprawdzianow += 1
        self.__sprawdziany_puktacja.append(punktacja_sprawdzianu)



######################################################################
# Klasa Grupa Zestaw Zadań Projekt Ocena


class GrupaZesZadProOce(object):
    u"""Grupa, zestaw zadań, projekt za ocenę."""

    # Straszna chała, ale działa.
    
    def __init__(self, nazwa_przedmiotu, semestr, rok_akad,
                 numer_grupy):
        # self.przed_atrybuty(nazwa_przedmiotu, semestr, rok_akad)
        # self.grupa_atrybuty(nazwa_przedmiotu, semestr, rok_akad, numer_grupy)
        # self.grupa_zes_zad_atry()
        # self.grupa_zes_zad_pro_oce()

        self.__opis_przed = str(nazwa_przedmiotu) + ', semestr ' \
                            + str(semestr) + ' ' + str(rok_akad) + '\n'

        self.__lista_stud = []
        
        self.__num_grupy = numer_grupy
        self.__nazwa_pliku_z_wyn = nazwa_przedmiotu + '-' + semestr \
                                 + '-' + rok_akad + '-' \
                                 + 'Grupa-' + str(numer_grupy) \
                                 + '-Wyniki.txt'

        self.__ilosc_zajec = 0  # Liczba zajęć jaka się odbyła. Liczone są
        # również te na które nikt nie przyszedł.

        self.__ilosc_zestawow_zadan = 0
        self.__zestawy_zadan_punktacja = []
        
        self.__liczba_proj = 0
        self.__opis_wyn = "Imie       Nazwisko      " \
                          "Fre. %   Punkty   Oce. sre. z projektow\n"

        # Zrób tak, by += w powyższym wzorze działało.


    def dodaj_studenta(self, student_inst):
        u"""Dodaje instację studenda STUDENT_INST do atrybutu
            __LISTA_STUDENTOW"""
        self.__lista_stud.append(student_inst)


    def odbyly_sie_zajecia(self):
        u"""Zwiększa atrybut SELF.__ILOSC_ZAJEC o 1."""
        self.__ilosc_zajec += 1


    def bylo_zajec(self):
        return self.__ilosc_zajec


    def byl_zestaw_zadan(self, punktacja_zestawu):
        u"""Jeśli był nowy zestaw zadań, to punktację zadań dodajemy do listy
        punktacji.

        Metoda sprawdza, czy lista jest krotką. Krotką, bo raz ustawiona,
        punktacja ma być niezmienna."""
        assert isinstance(punktacja_zestawu, tuple), \
            u"Punktacja zestawu nie jest krotką!"

        self.__ilosc_zestawow_zadan += 1
        self.__zestawy_zadan_punktacja.append(punktacja_zestawu)


    def byl_proj(self):
        self.__liczba_proj += 1

        
    def liczba_proj(self):
        return self.__liczba_proj

    def max_punkty(self):
        max_punktow = 0

        for krot_punkt in self.__zestawy_zadan_punkt:
            max_punktow += sum(krot_punkt, 0.0)

        return max_punktow


    def zapisz_do_pliku(self):
        with open(self.__nazwa_pliku_z_wyn, 'w') as wyniki:
            wyniki.write(self.__opis_przed)
            wyniki.write(self.__opis_wyn)
            for student in self.__lista_stud:
                wyniki.write(student.wyniki_studenta())

