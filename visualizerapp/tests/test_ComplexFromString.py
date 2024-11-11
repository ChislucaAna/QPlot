import unittest
from domain import Complex

#teste pentru fomate valide si invalide de numere complexe
#pentru functia Complex.From_string() 
class TestComplexFromString(unittest.TestCase):

    def test_valid_complex_numbers(self):
        #dictionar unde cheia e inputul de tip string si valoarea e o pereche de 2 inturi
        #!in python perechiile sun constante, nu le poti modifica dupa
        test_cases = {
            "3+4i": (3, 4),
            "1-2i": (1, -2),
            "-1+5i": (-1, 5),
            "0+0i": (0, 0),
            "5": (5, 0),  # 5 + 0i
            "-3": (-3, 0),  # -3 + 0i
            "2 - 3i": (2, -3), 
            " - 4 + 6i ": (-4, 6),
        }

        #pentru fiecare input si output el ruleaza functia si vede daca corespunde outputului asteptat.
        # sintagma with creeaza un subtest. daca el esueaza o sa le execute si pe urmatoarele, afisand outputul tuturor
        for input_str, expected in test_cases.items():
            with self.subTest(input=input_str):
                real, imag = Complex.from_string(input_str)
                self.assertEqual(real, expected[0])
                self.assertEqual(imag, expected[1])

    def test_invalid_complex_numbers(self):
        invalid_cases = [
            "3 + + 4i",
            "5 - - 2i",
            "++3 + 4i",
            "4 + i", 
            "i4",
            "3 + 4x",
        ]

        for input_str in invalid_cases:
            with self.subTest(input=input_str):
                with self.assertRaises(ValueError):
                    Complex.from_string(input_str)

if __name__ == '__main__':
    unittest.main()
