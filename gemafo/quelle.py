# -*- coding: utf-8 -*-

from .gematik import GematikObjekt


class Quelle(GematikObjekt):
    def __init__(self,
                 id,
                 titel,
                 dokumentenkuerzel='',
                 version='',
                 vorgaenger=None,
                 nachfolger=None):

        super().__init__(id, titel, vorgaenger, nachfolger)
        self.dokumentenkuerzel = dokumentenkuerzel
        self.version = version

    def __str__(self):
        return (super().__str__() + ", "
                + "dokumentenkuerzel: " + self.dokumentenkuerzel + ", "
                + "version: " + self.version)
