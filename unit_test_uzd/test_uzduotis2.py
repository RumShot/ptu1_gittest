import unittest
from uzduotis2 import *


class TestSakinys(unittest.TestCase):
    def setUp(self):
        self.tekstas = Sakinys("Viskas bus Labai gerai :)")

    def test_atbulai(self):
        self.assertEqual(self.tekstas.atbulai(), "): iareg iabaL sub saksiV")

    def test_didziosiomis(self):
        self.assertEqual(self.tekstas.didziosiomis(),"VISKAS BUS LABAI GERAI :)")

    def test_mazosiomis(self):
        self.assertEqual(self.tekstas.mazosiomis(),"viskas bus labai gerai :)")

    def test_ieskoti(self):
        self.assertEqual(self.tekstas.ieskoti("a"), 4)
        self.assertEqual(self.tekstas.ieskoti("i"), 3)
        self.assertEqual(self.tekstas.ieskoti("Labai"), 1)

    def test_pakeisti(self):
        self.assertEqual(self.tekstas.pakeisti("i", "a"), "Vaskas bus Labaa geraa :)")
        self.assertEqual(self.tekstas.pakeisti("a", "x"), "Viskxs bus Lxbxi gerxi :)")
        self.assertEqual(self.tekstas.pakeisti("s", "hh"), "Vihhkahh buhh Labai gerai :)")

    def test_atspausdintiZodi(self):
        self.assertEqual(self.tekstas.atspausdintiZodi(0), "Viskas")
        self.assertEqual(self.tekstas.atspausdintiZodi(4), ":)")
        self.assertEqual(self.tekstas.atspausdintiZodi(2), "Labai")

    def test_info(self):
        self.assertEqual(self.tekstas.info(), [5, 0, 2, 17])

if __name__ == "__main__":
    unittest.main()