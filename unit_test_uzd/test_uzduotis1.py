import unittest
from uzduotis1 import *


class TestKeliamieji(unittest.TestCase):
    def test_skaiciu_suma(self):
        self.assertEqual(56, skaiciu_suma(45, 5, 6))
        self.assertEqual(18, skaiciu_suma(6, 6, 6))
        self.assertEqual(26, skaiciu_suma(-3, 16, 13))

    def test_saraso_suma(self):
        self.assertEqual(56, saraso_suma(sarasas = [45, 5, 6]))
        self.assertEqual(18, saraso_suma(sarasas = [6, 6, 6]))
        self.assertEqual(26, saraso_suma(sarasas = [-3, 16, 13]))

    def test_didziausias_skaicius(self):
        self.assertEqual(789, didziausias_skaicius(5, 8, 789, 94, 78))
        self.assertEqual(896, didziausias_skaicius(896, 8, 789, 94, 78))
        self.assertEqual(999, didziausias_skaicius(5, 999, 789, 94, 78))

    def test_stringas_atbulai(self):
        self.assertEqual("sula",stringas_atbulai("alus"))
        self.assertEqual("vilnius",stringas_atbulai("suinliv"))
        self.assertEqual("nuodeme",stringas_atbulai("emedoun"))

    def test_info_apie_sakini(self):
        self.assertEqual([6, 1, 20, 3], info_apie_sakini("Laba diena laba diena lab 522"))
        self.assertEqual([6, 3, 18, 4], info_apie_sakini("lala  1236 Diena Laba Diena lab"))
        self.assertEqual([6, 3, 9, 3], info_apie_sakini("vienas DU tryS 4 5 6"))

    def test_unikalus_sarasas(self):
        self.assertEqual([4, 5, 'Labas', 6, True, 10], unikalus_sarasas([4, 5, "Labas", 6, "Labas", True, 5, True, 10]))
        self.assertEqual([2, 1, 6, 8, 5,'Duobe'], unikalus_sarasas([2, 1, 6, 8, 5, True, 'Duobe']))
        self.assertEqual([4, 5, 'ate', 6, False, 10], unikalus_sarasas([4, 5, "ate", 6, "ate", False, 5, False, 10]))

    def test_test_prime(self):
        self.assertTrue(test_prime(5))
        self.assertFalse(test_prime(8))
        self.assertTrue(test_prime(13))

    def test_isrikiuoti_nuo_galo(self):
        self.assertEqual("keturi # trys # du # Vienas", isrikiuoti_nuo_galo("Vienas du trys keturi"))
        self.assertEqual("sultys # degtine # tekila # Alus", isrikiuoti_nuo_galo("Alus tekila degtine sultys"))
        self.assertEqual("maras # karas # Badas", isrikiuoti_nuo_galo("Badas karas maras"))

    def test_ar_keliamieji(self):
        self.assertTrue(ar_keliamieji(2020))
        self.assertFalse(ar_keliamieji(2100))
        self.assertTrue(ar_keliamieji(2000))

    def test_patikrinti_data(self):
        self.assertEqual([8140, 22, 1162], patikrinti_data("2000-01-01 12:12:12"))
        self.assertEqual([11358, 31, 1622], patikrinti_data("1991-03-11 12:12:12"))
        self.assertEqual([11218, 30, 1602], patikrinti_data("1991-07-29 12:12:12"))


if __name__ == "__main__":
    unittest.main()