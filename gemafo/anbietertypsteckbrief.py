# -*- coding: utf-8 -*-

from .quelle import Quelle


class Anbietertypsteckbrief(Quelle):
    def __init__(self,
                 id,
                 titel,
                 version='',
                 anbietertyp_version='',
                 dokumentenkuerzel='',
                 dateiname_pdf='',
                 dateiname_xlsx='',
                 prev=None,
                 next=None):

        super().__init__(id, titel, prev, next)
        self.version = version
        self.anbietertyp_version = anbietertyp_version
        self.dokumentenkuerzel = dokumentenkuerzel
        self.dateiname_pdf = dateiname_pdf
        self.dateiname_xlsx = dateiname_xlsx

    def __str__(self):
        return (super().__str__() + ", "
                + "version: " + self.version + ", "
                + "anbietertyp_version: " + self.anbietertyp_version + ", "
                + "dokumentenkuerzel: " + self.dokumentenkuerzel + ", "
                + "dateiname_pdf: " + self.dateiname_pdf + ", "
                + "dateiname_xlsx: " + self.dateiname_xlsx)
