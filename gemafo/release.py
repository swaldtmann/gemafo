# -*- coding: utf-8 -*-

from .gematik import GematikObjekt


class Release(GematikObjekt):
    def __init__(self,
                 id,
                 titel,
                 beschreibung='',
                 vorgaenger=None,
                 nachfolger=None):

        super().__init__(id, titel, vorgaenger, nachfolger)
        self.beschreibung = beschreibung

    def __str__(self):
        return (super().__str__() + ", "
                + "beschreibung: " + self.beschreibung)
