# -*- coding: utf-8 -*-

from .gematik import GematikObjekt


class Afo(GematikObjekt):
    def __init__(self,
                 id,
                 titel,
                 beschreibung='',
                 afo_level='',
                 beschreibung_html='',
                 afo_version='',
                 quelle_referenz='',
                 pruefverfahren='',
                 prev=None,
                 next=None):

        super().__init__(id, titel, prev, next)

        self.beschreibung = beschreibung
        self.afo_level = afo_level
        self.beschreibung_html = beschreibung_html
        self.afo_version = afo_version
        self.quelle_referenz = quelle_referenz
        self.pruefverfahren = pruefverfahren

    def __str__(self):
        return (super().__str__() + ", " +
                "beschreibung: " + self.beschreibung + ", " +
                "afo_level: " + self.afo_level + ", " +
                "beschreibung_html: " + self.beschreibung_html + ", " +
                "afo_version: " + self.afo_version + ", " +
                "quelle_referenz: " + self.quelle_referenz + ", " +
                "pruefverfahren: " + self.pruefverfahren)
