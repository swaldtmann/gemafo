# -*- coding: utf-8 -*-

import pytest

# from .context import gemafo
from gemafo.gematik import GematikObjekt


class TestGematikObjektClass:

    def test_init_sets_(self):
        """ Test that init sets the name """
        gemobj = GematikObjekt("GemObj001", "Titel")
        assert gemobj.id == "GemObj001"
        assert gemobj.titel == "Titel"

    def test_init_error_when_no_titel(self):
        """ Test that init fails without the name """
        expected_error = r"__init__\(\) missing 1 required positional argument: \'titel\'"  # noqa: E501
        with pytest.raises(TypeError, match=expected_error):
            gemobj = GematikObjekt("GemObj001")  # noqa: F841

    def test_gematikobjekt_class_creation(self, gematik_object):
        assert len(dir(gematik_object)) == 41
        assert gematik_object.id == "GemObj001"
        assert gematik_object.titel == "Titel"
        assert gematik_object.prev is None
        assert gematik_object.next is None
        msg = ('id: GemObj001, titel: Titel, prev: None, '
               'next: None')
        assert str(gematik_object) == msg
        assert repr(gematik_object) == 'GematikObjekt(id="GemObj001", titel="Titel")'  # noqa: E501


#     def test_afo_class_creation(self):
#         a = gemafo.Afo("A_4646", "Titel", "Beschreibung",
#                         "MUSS",
#                         beschreibung_html='<p>Beschreibung</p>',
#                         afo_version='_0',
#                         quelle_referenz='gemKPT_Betr',
#                         pruefverfahren='Anforderungen zur betrieblichen '
#                                        'Eignung "Prozessprüfung"',
#                         next="A_4646_1")

#         self.assertEqual(len(dir(a)), 41)
#         self.assertEqual(a.beschreibung, 'Beschreibung')
#         self.assertEqual(a.afo_level, 'MUSS')
#         self.assertEqual(a.beschreibung_html, '<p>Beschreibung</p>')
#         self.assertEqual(a.afo_version, '_0')
#         msg = ('id: A_4646, titel: Titel, prev: None, next: '
#                'A_4646_1, beschreibung: Beschreibung, afo_level: '
#                'MUSS, beschreibung_html: <p>Beschreibung</p>, '
#                'afo_version: _0, '
#                'quelle_referenz: gemKPT_Betr, '
#                'pruefverfahren: Anforderungen zur betrieblichen '
#                'Eignung "Prozessprüfung"')
#         self.assertEqual(str(a), msg)
#         self.assertEqual(repr(a), 'Afo(id="A_4646", titel="Titel")')
#         # a.print_attributes()

#     def test_release_class_creation(self):
#         a = gemafo.Release("R4.0.1-2", "Titel", "Beschreibung",
#                             next="A_4646_1")

#         self.assertEqual(len(dir(a)), gematikobjekt_class_len + 1)
#         self.assertEqual(a.beschreibung, 'Beschreibung')
#         msg = ('id: R4.0.1-2, titel: Titel, prev: None, next: '
#                'A_4646_1, beschreibung: Beschreibung')
#         self.assertEqual(str(a), msg)
#         self.assertEqual(repr(a), 'Release(id="R4.0.1-2", titel="Titel")')

#     def test_quelle_class_creation(self):
#         a = gemafo.Quelle("gemKPT_Betr_V3.7.0", "Titel",
#                            dokumentenkuerzel="gemKPT_Betr",
#                            version="V3.7.0",
#                            next="gemKPT_Betr_V3.6.0")

#         self.assertEqual(len(dir(a)), gematikobjekt_class_len + 2)
#         msg = ('id: gemKPT_Betr_V3.7.0, titel: Titel, prev: None, '
#                'next: gemKPT_Betr_V3.6.0, '
#                'dokumentenkuerzel: gemKPT_Betr, '
#                'version: V3.7.0')
#         self.assertEqual(str(a), msg)
#         self.assertEqual(repr(a),
#                          'Quelle(id="gemKPT_Betr_V3.7.0", titel="Titel")')


# if __name__ == '__main__':
#     unittest.main()
