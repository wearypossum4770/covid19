import pytest
from covid.linguistics import LanguageDict

class TestLanguageDict(TestCase):
    def test_spanish_maria(self):
        maria = LanguageDict("maría")
        assert maria == 'maria'
    def test_spanish_genesis(self):
        genesis = LanguageDict('Génesis')
        assert genesis == 'Genesis'
    def test_irish_shavon(self):
        shavon = LanguageDict('Siobán')
        assert shavon == 'Sioban'
    def test_german_uberraschgnarz(self):
        uberraschgnarz = LanguageDict('Überraschgnarz')
        assert uberraschgnarz = "Uberraschgnarz"