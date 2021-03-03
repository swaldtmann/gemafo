# -*- coding: utf-8 -*-
# from . import helpers

from difflib import Differ
from inspect import getmembers
from types import FunctionType
from pprint import pprint

SKIP_SAME_LINES = False


class GematikObjekt(object):
    def __init__(self,
                 id,
                 titel,
                 vorgaenger=None,
                 nachfolger=None):
        self.id = id
        self.titel = titel
        self.vorgaenger = vorgaenger
        self.nachfolger = nachfolger

    def __str__(self):
        return ("id: " + self.id + ", "
                + "titel: " + self.titel + ", "
                + "vorgaenger: " + str(self.vorgaenger) + ", "
                + "nachfolger: " + str(self.nachfolger))

    def __repr__(self):
        return f'{type(self).__name__}(id=\"{self.id}\", '\
               f'titel=\"{self.titel}\")'

    def diff_obj_type(self, other_object):
        return type(self) == type(other_object)

    def diff_text_attributes(self, other, attrib):
        text1 = getattr(self, attrib)
        text2 = getattr(other, attrib)
        if not isinstance(text1, str):
            return None
        if not isinstance(text2, str):
            return None
        lDifference = list()
        d = Differ()
        for line in d.compare(
            text1.splitlines(keepends=True),
            text2.splitlines(keepends=True)
        ):
            if SKIP_SAME_LINES and line.startswith('  '):
                # Skip  "'  ' line common to both sequences"
                continue
            lDifference.append(line)
        return lDifference

    def show_version_diff(self, dict_of_afos, other_version_id=None):
        dDiff = dict()
        if not other_version_id:
            raise ValueError("Keine andere Version zum diff gefunden!")
        other_object = dict_of_afos[other_version_id]
        if not self.diff_obj_type(other_object):
            raise ValueError("Objekttypen sind unterschiedlich! "
                             "Diff abgebrochen!")
        vars_self = set(vars(self))
        vars_other_version = set(vars(dict_of_afos[other_version_id]))
        # print(vars_self)
        # print(vars_other_version)
        if vars_self != vars_other_version:
            raise ValueError("Objektattribute nicht identisch! "
                             "Diff abgebrochen!")
        for attrib in vars_other_version:
            # print(attrib)
            # FIXME:
            lDiff = self.diff_text_attributes(other_object, attrib)
            if lDiff:
                dDiff[attrib] = self.diff_text_attributes(other_object, attrib)
        return dDiff

    def attributes(self):
        # returns a dict of attributes of this class
        disallowed_names = {
            name for name, value in getmembers(type(self))
            if isinstance(value, FunctionType)}
        return {
            name: getattr(self, name) for name in dir(self)
            if (name[0] != '_'
                and name not in disallowed_names
                and hasattr(self, name))
        }

    def print_attributes(self):
        pprint(self.attributes())
