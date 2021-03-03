""" tests/conftest.py """

import pytest

from gemafo.gematik import GematikObjekt


@pytest.fixture(scope="class")
def gematik_object():
    return GematikObjekt("GemObj001", "Titel")
