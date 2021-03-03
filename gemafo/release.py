# -*- coding: utf-8 -*-

from .gematik import GematikObjekt


class Release(GematikObjekt):
    def __init__(self,
                 id,
                 titel,
                 beschreibung='',
                 prev=None,
                 next=None):

        super().__init__(id, titel, prev, next)
        self.beschreibung = beschreibung

    def __str__(self):
        return (super().__str__() + ", "
                + "beschreibung: " + self.beschreibung)
