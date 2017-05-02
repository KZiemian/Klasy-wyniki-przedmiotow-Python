#!/usr/bin/python
# -*- coding: utf-8 -*-



# Należy poprawić ten notatki według standardów Pythona.

######################################################################



class Student(object):
    u"""Klasa reprezentująca studenta uczęszczającego do danej grupy."""

    def __init__(self, imie_studenta, nazwisko_studenta, przedmiot_inst):

        self.__imie_studenta = imie_student
        self.__nazwisko_studenta = nazwisko_studenta
        self.__przedmiot_inst = przedmiot_inst
        
        self.__ocena = ''
        self.__komentarz = ''



######################################################################
    


class StudentCwiczenia(Student):
    u"""Klasa reprezentująca studenta który oddaje punktowane
    zestawy zadań"""


    def __init__(self, imie_studenta, nazwisko_studenta):

        Student.__init__(self, imie_studenta, nazwisko_studenta)
        self.__obecnosc = 0
        
    
    def byl_na_zajeciach(self):
        u"""Zwiększa atrybut __obecność o 1."""
        
        self.__obecnosc += 1


    def frekwencja(self):
        u"""Zwraca float wyrażającego procentową obecność na zajęciach."""

        return 100 * float(self.__obecnosc) / self.__przedmiot_inst.



######################################################################



class StudentCwiZesZad(StudentCwiczenia):
    u"""Student Ćwiczenia Zestwy Zadań"""
    
    def __init__(self, imie_studenta, nazwisko_studenta, przedmiot_inst):

        StudentCwiczenia.__init__(self, imie_studenta, nazwisko_studenta,
                                  przedmiot_inst)
        self.__rozwiazane_zestawy_zadan = []
        
        
    def oddany_zestaw_zadan(self, punkty_za_zadania):
        # punkty_za_zadania mają być krotką
        self.__rozwiazane_zestawy_zadan.append(punkty_za_zadania)



######################################################################



class StudentCwiczeniaProOce(StudentCwiczenia):
    u"""Student Ćwiczenia Projekty"""
    
    def __init__(self, imie_studenta, nazwisko_studenta, przedmiot_inst):

        StudentCwiczenia.__init__(self, imie_studenta, nazwisko_studenta,
                                  przedmiot_inst)
        self.__oceny_za_projekty = []
        
        
    def oddany_projekt(self, ocena_za_projekt):
        # punkty_za_zadania mają być krotką
        self.__oceny_za_projekt.append(ocena_za_projekt)



######################################################################



class StudentCwiZesZadProOcen(StudentCwiczenia):
    u"""Student, ćwiczenia, zestwy zadań i projekty za oceny."""
    
    def __init__(self, imie_studenta, nazwisko_studenta, przedmiot_inst):

        StudentCwiZesZad.__init__(self, imie_studenta, nazwisko_studenta,
                                  przedmiot_inst)
        self.__oceny_za_projekty = []
        
        
    def oddany_projekt(self, ocena_za_projekt):
        # punkty_za_zadania mają być krotką
        self.__oceny_za_projekt.append(ocena_za_projekt)

        
        
    def oddany_zestaw_zadan(self, punkty_za_zadania):
        # punkty_za_zadania mają być krotką
        self.__rozwiazane_zestawy_zadan.append(punkty_za_zadania)

