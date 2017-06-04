#!/usr/bin/python
# -*- coding: utf-8 -*-



# Należy poprawić ten notatki według standardów Pythona.

######################################################################



class Student(object):
    u"""Klasa reprezentująca studenta uczęszczającego do danej grupy."""

    def __init__(self, imie_studenta, nazwisko_studenta, przedmiot_inst):

        self.__imie_studenta = imie_studenta
        self.__nazwisko_studenta = nazwisko_studenta
        self.__przed_inst = przedmiot_inst

        self.__ocena = ''
        self.__komentarz = ''



######################################################################



class StudentCwi(Student):
    u"""Klasa reprezentująca studenta który oddaje punktowane
    zestawy zadań"""


    def __init__(self, imie_studenta, nazwisko_studenta, przedmiot_inst):

        # super(StudentCwi, self).__init__(imie_studenta, nazwisko_studenta,
        #                                  przedmiot_inst)
        self.__obecnosc = 0


    def byl_na_zajeciach(self):
        u"""Zwiększa atrybut __obecność o 1."""

        self.__obecnosc += 1


    def frekwencja(self):
        u"""Zwraca float wyrażającego procentową obecność na zajęciach."""
        ilosc_zajec = self.__przedmiot_inst.bylo_zajec()

        return 100 * float(self.__obecnosc) / ilosc_zajec



######################################################################



class StudentCwiZesZad(StudentCwi):
    u"""Student Ćwiczenia Zestwy Zadań"""

    def __init__(self, imie_studenta, nazwisko_studenta, przedmiot_inst):

        # StudentCwiczenia.__init__(self, imie_studenta, nazwisko_studenta,
        #                           przedmiot_inst)
        self.__rozwiazane_zestawy_zadan = []


    def oddany_zestaw_zadan(self, punkty_za_zadania):
        # punkty_za_zadania mają być krotką
        self.__rozwiazane_zestawy_zadan.append(punkty_za_zadania)



######################################################################



class StudentCwiProOce(StudentCwi):
    u"""Student Ćwiczenia Projekty"""

    def __init__(self, imie_studenta, nazwisko_studenta, przedmiot_inst):

        # StudentCwiczenia.__init__(self, imie_studenta, nazwisko_studenta,
        #                           przedmiot_inst)
        self.__oceny_za_projekty = []


    def oddany_projekt(self, ocena_za_projekt):
        # punkty_za_zadania mają być krotką
        self.__oceny_za_projekt.append(ocena_za_projekt)



##############################

class StudentCwiZesZadProOce(object):
    u"""Student, ćwiczenia, zestwy zadań i projekty za oceny."""

    # Chała która działa. Popraw.

    def __init__(self, imie_studenta, nazwisko_studenta, przedmiot_inst):
        self.__imie_stud = imie_studenta
        self.__nazw_stud = nazwisko_studenta
        self.__przed_inst = przedmiot_inst
        self.__przed_inst.dodaj_studenta(self)

        self.__ocena = 'Nic' # Ocena sumaryczna za przedmiot.
        self.__komentarz = '' # Dodatkowy komentarz odnośnie osiągnięć
        # studenta.

        self.__obecnosc = 0 # Liczba zajęć na których student był.

        self.__rozw_zes_zad = [] # List zawierający rozwiązane
        # przez studenta zestawy zadań. Zestaw zadań reprezentuje krotka
        # z punktami które dostał za zadania (bądź podpunkt zadania,
        # jeśli to on są puntkowane), albo "False" jeśli nie oddał żadnego.
        # Na razie jest to nie zaimplementowane, bo jeśli nie oddał zestawu, bo "False" nie jest
        # zaimplementowany.

        self.__oceny_za_proj = []
        # super(StudentCwiZesZadProOce, self).__init__(imie_studenta,
        #                                              nazwisko_studenta,
        #                                              przedmiot_inst)


    def oddany_projekt(self, ocena_za_projekt):
        # punkty_za_zadania mają być krotką
        self.__oceny_za_proj.append(ocena_za_projekt)


    def byl_na_zajeciach(self):
        u"""Zwiększa atrybut __obecność o 1."""

        self.__obecnosc += 1


    def oddany_zestaw_zadan(self, punkty_za_zadania):
        # punkty_za_zadania mają być krotką
        self.__rozw_zes_zad.append(punkty_za_zadania)


    def oddany_projekt(self, ocena_za_projekt):
        # punkty_za_zadania mają być krotką
        self.__oceny_za_proj.append(ocena_za_projekt)

    def dodaj_komentarz(self, komentarz):
        self.__komentarz += komentarz + '\n\n'


    def wyniki_studenta(self):
        opis_wynik_stud = self.__imie_stud.ljust(11) \
                          + self.__nazw_stud.ljust(11)
        # Zmień opis_wynik_stu na opis_wynik_stud
        ilosc_zajec = self.__przed_inst.bylo_zajec()

        # print opis_wynik_stud

        if (ilosc_zajec != 0):
            frek_str = str(round(100 * float(self.__obecnosc)
                                 / ilosc_zajec, 2))# .rjust(7)
            opis_wynik_stud += "  " + frek_str.rjust(7) + "  "
            del frek_str
            opis_wynik_stud = opis_wynik_stud.rjust(5)
        else:
            opis_wynik_stud += "  Nic  "


        if (len(self.__rozw_zes_zad) > 0):
            punkty_zad = 0.0
            max_punkty = self.__przed_inst.max_punkty()

            for krotka_punk in self.__rozw_zes_zad:
                punkty_zad += sum(krotka_punk, 0.0)

            # To powinno być na zewnątrz pętli
            punkt_str = str(punkty_zad) + "/" + str(int(max_punkty))

            opis_wynik_stud += "  " + punkt_str.rjust(5) + "  "
            del punkt_str

        else:
            opis_wynik_stud += "  Nic  "


        ilosc_proj = self.__przed_inst.liczba_proj()

        if (ilosc_proj != 0):
            oce_srd_proj = sum(self.__oceny_za_proj, 0.0) / ilosc_proj
        else:
            oce_srd_proj = "  Nic  "

        opis_wynik_stud += "  " + str(oce_srd_proj).rjust(4) + "\n"

        if (self.__komentarz != ''):
            opis_wynik_stud += self.__komentarz


        return opis_wynik_stud
