
# -*- coding: utf-8 -*-

from difflib import Differ
from inspect import getmembers
from types import FunctionType
from pprint import pprint

SKIP_SAME_LINES = False


class DoubleLinkeNode(object):
    def __init__(self,
                 prev=None,
                 next=None):
        self.prev = prev
        self.next = next

    def is_head(self):
        return self.prev is None

    def is_tail(self):
        return self.next is None

    # O(N), expensive!
    def tail(self):
        if self.is_tail:
            return self
        return self.next.end()

    # O(N), expensive!
    def head(self):
        if self.is_head():
            return self
        return self.prev.head()

    # insert behind this node
    def insert(self, node):
        node.next = self.next
        node.prev = self
        self.next = node
        if self.next is not None:
            self.next.prev = node

    # insert behind last node
    # O(N), expensive!
    def append(self, node):
        end = self.tail()
        self.insert(node)


class GematikObjekt(DoubleLinkeNode):
    def __init__(self,
                 id,
                 titel,
                 prev=None,
                 next=None):
        self.id = id
        self.titel = titel
        super().__init__(prev, next)

    def __str__(self):
        return ("id: " + self.id + ", "
                + "titel: " + self.titel + ", "
                + "prev: " + str(self.prev) + ", "
                + "next: " + str(self.next))

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
