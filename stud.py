#!/usr/bin/python
# -*- coding: utf-8 -*-



from przedgrup import *

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

        super(StudentCwi, self).__init__(imie_studenta, nazwisko_studenta,
                                         przedmiot_inst)
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

        StudentCwiczenia.__init__(self, imie_studenta, nazwisko_studenta,
                                  przedmiot_inst)
        self.__rozwiazane_zestawy_zadan = []
        
        
    def oddany_zestaw_zadan(self, punkty_za_zadania):
        # punkty_za_zadania mają być krotką
        self.__rozwiazane_zestawy_zadan.append(punkty_za_zadania)



######################################################################



class StudentCwiProOce(StudentCwi):
    u"""Student Ćwiczenia Projekty"""
    
    def __init__(self, imie_studenta, nazwisko_studenta, przedmiot_inst):

        StudentCwiczenia.__init__(self, imie_studenta, nazwisko_studenta,
                                  przedmiot_inst)
        self.__oceny_za_projekty = []
        
        
    def oddany_projekt(self, ocena_za_projekt):
        # punkty_za_zadania mają być krotką
        self.__oceny_za_projekt.append(ocena_za_projekt)



##############################

class StudentCwiZesZadProOce(StudentCwi):
    u"""Student, ćwiczenia, zestwy zadań i projekty za oceny."""
    
    def __init__(self, imie_studenta, nazwisko_studenta, przedmiot_inst):
        self.__oceny_za_proj = []
        super(StudentCwiZesZadProOce, self).__init__(imie_studenta,
                                                     nazwisko_studenta,
                                                     przedmiot_inst)
        
        
    def oddany_projekt(self, ocena_za_projekt):
        # punkty_za_zadania mają być krotką
        self.__oceny_za_proj.append(ocena_za_projekt)

        
    def oddany_zestaw_zadan(self, punkty_za_zadania):
        # punkty_za_zadania mają być krotką
        self.__rozwiazane_zestawy_zadan.append(punkty_za_zadania)

    def wyniki_studenta(self):
        opis_wynik_stu = self.__imie_studenta.ljust(10) \
                         + self.__nazwisko_studenta.ljust(10)
        # Zmień opis_wynik_stu na opis_wynik_stud

        if (self.bylo_zajec() != 0):
            opis_wynik_stu += "  " + str(100 * float(self.__obecnosc)
                                         / self.bylo_zajec()) + "  "
        else:
            opis_wynik_stu = "  Nic  "

        ilosc_proj = self.__przed_inst.ilosc_proj()

        if (ilosc_proj != 0):
            oce_srd_proj = sum(self.__oceny_za_proj, 0.0) / ilosc_proj
        else:
            oce_srd_proj = "  Nic\n"

        opis_wynik_stu += "  " + str(oce_srd_proj) + "\n"


        return opis_wynik_stu
