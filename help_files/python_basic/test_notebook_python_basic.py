import sys
import unittest

from cours_python_utils import test_with_expected, check_fonction_in_code, \
    warning_on_print

__unittest = True
this = sys.modules[__name__]

WARNING_TOO_MUCH_CODE_MSG = "WARNING: You don't need that many lines"

def tester_exo(n, globals_dict):
    for k, v in globals_dict.items():
        setattr(this, k, v)
    launch_test_case(eval("TestExercice{0}".format(n)))


def launch_test_case(test_case):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    unittest.TextTestRunner(verbosity=2).run(suite)


class TestExerciceV0(unittest.TestCase):
    def test(self):
        self.assertEqual(i, "Hello world !")


class TestExerciceV2_1(unittest.TestCase):
    def test_code(self):
        nb_lignes = In[-1].count("\n") + 1
        if nb_lignes > 10:
            print(WARNING_TOO_MUCH_CODE_MSG.format(nb_lignes))

    def test_fonction(self):
        self.assertEqual(a1, 5)
        self.assertEqual(type(a1), int)


class TestExerciceV2_2(unittest.TestCase):
    def test_code(self):
        nb_lignes = In[-1].count("\n") + 1
        if nb_lignes > 10:
            print("WARNING: Mais pourquoi donc tant de lignes de code ? {0}".format(nb_lignes))

    def test_fonction(self):
        self.assertEqual(a2, 5)
        self.assertEqual(type(a2), float)


class TestExerciceV2_3(unittest.TestCase):
    def test_code(self):
        nb_lignes = In[-1].count("\n") + 1
        if nb_lignes > 10:
            print("WARNING: Mais pourquoi donc tant de lignes de code ? {0}".format(nb_lignes))

    def test_fonction(self):
        self.assertEqual(a3, "5")
        self.assertEqual(type(a3), str)


# class TestExerciceV2_4(unittest.TestCase):
#     def test_fonction(self):
#         test_with_expected(self, "e", int, 1403)
#         test_with_expected(self, "f", int, 151200)


class TestExerciceV2_5(unittest.TestCase):
    def test_fonction(self):
        import math
        self.assertEqual(resultat2_5, math.factorial(999))


class TestExerciceV2_6(unittest.TestCase):
    def test_fonction(self):
        self.assertEqual(resultat2_6, sum(it ** 2 for it in range(1488)))


class TestExerciceV2_7(unittest.TestCase):
    def test_fonction(self):
        self.assertEqual(resultat2_7, sum(3 * it for it in range(334)))


# class TestExerciceV2_8(unittest.TestCase):
#     def test_fonction(self):
#         test_with_expected(self, "resultatV2_8", int, sum(it for it in range(6000) if it % 3 == 0 or it % 5 == 0))


class TestExerciceV2_9(unittest.TestCase):
    def test_code(self):
        if "math" in In[-1]:
            self.fail("Il est interdit d'utiliser le module math (et du coup, d'avoir le mot math dans votre code")

    def test_fonction(self):
        import math
        self.assertAlmostEqual(resultat2_9, math.exp(10))

# Test for part 2
class TestExerciceF0(unittest.TestCase):
    def test(self):
        check_fonction_in_code(self, "hello_world", In)
        self.assertEqual(hello_world(), "Hello world !")


class TestExerciceF2_1(unittest.TestCase):
    def test_code(self):
        warning_on_print(In)

    def test_fonction(self):
        check_fonction_in_code(self, "one", In)
        test_with_expected(self, one, tuple(), 1)


class TestExerciceF2_2(unittest.TestCase):
    def test_code(self):
        warning_on_print(In)

    def test_fonction(self):
        check_fonction_in_code(self, "increment", In)
        for it in range(10):
            test_with_expected(self, increment, it, it + 1)


# class TestExerciceF2_3(unittest.TestCase):
#     def test_code(self):
#         warning_on_print(In)
#
#     def test_fonction(self):
#         check_fonction_in_code(self, "somme")
#         for x in range(10):
#             for y in range(10):
#                 test_with_expected(self, somme, (x, y), x + y)


class TestExerciceF2_4(unittest.TestCase):
    def test_code(self):
        warning_on_print(In)

    def test_fonction(self):
        check_fonction_in_code(self, "evaluate_polynom", In)
        for a, b, c, x in ((a, b, c, x)
            for a in range(5)
            for b in range(5)
            for c in range(5)
            for x in range(5)):
            test_with_expected(self, evaluate_polynom, (a, b, c, x), a * x ** 2 + b * x + c)


class TestExerciceF2_5(unittest.TestCase):
    def test_code(self):
        self.assertFalse("print" in In[-1], "ERROR : print is forbidden !")
        self.assertFalse("else" in In[-1], "ERROR : else is forbidden !")
        self.assertFalse("elif" in In[-1], "ERROR : elif is forbidden !")
        self.assertFalse(In[-1].count("if ") > 1, "ERROR : more than one if found")

    def test_fonction(self):
        check_fonction_in_code(self, "is_even", In)
        for x in range(10):
            test_with_expected(self, is_even, x, x % 2 == 0)


class TestExerciceF2_6(unittest.TestCase):
    def test_code(self):
        self.assertFalse("math" in In[-1], "math module is forbidden")

    def test_fonction(self):
        check_fonction_in_code(self, "factorial", In)
        import math
        for n in range(10):
            test_with_expected(self, factorial, n, math.factorial(n))


class TestExerciceF2_7(unittest.TestCase):
    def test_code(self):
        self.assertFalse("math" in In[-1], "math module is forbidden")
        self.assertTrue("factorial" in In[-1], "You must use your factorial function")
        if "def factorielle" in In[-1]:
            print("WARNING: no need to copy the code of the factorial function")

    def test_fonction(self):
        check_fonction_in_code(self, "combinatorial", In)
        import math
        for n in range(10):
            for k in range(n + 1):
                expected = (math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))
                test_with_expected(self, combinatorial, (n, k), expected)


# class TestExerciceF2_8(unittest.TestCase):
#     def test_code(self):
#         self.assertFalse("math" in In[-1], "Le module math est interdit !")
#         self.assertTrue("combinatoire" in In[-1], "Vous devez utiliser votre fonction combinatoire")
#         if "def combinatoire" in In[-1]:
#             print("WARNING: vous n'êtes pas censé recopier le code de la fonction combinatoire")
#
#     def test_fonction(self):
#         check_fonction_in_code(self, "gain_loto_gros_lot")
#         import math
#         for n in range(40, 50):
#             for k in range(1, 5):
#                 for montant in (50, 1000000):
#                     test_with_expected(
#                         self,
#                         gain_loto_gros_lot,
#                         (n, k, montant),
#                         montant / ((math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))),
#                         almost=True)
# def gain_loto_prof(n, k, montant):
#     gain_moyen = 0
#     for j in range(k):
#         gain_moyen += (montant / (100 ** j)) * combinatoire(k, k - j) * combinatoire(n - k, j) / combinatoire(n, k)
#     return gain_moyen


# class TestExerciceF2_9(unittest.TestCase):
#     def test_code(self):
#         self.assertFalse("math" in In[-1], "Le module math est interdit !")
#         self.assertTrue("combinatoire" in In[-1], "Vous devez utiliser votre fonction combinatoire")
#         if "def combinatoire" in In[-1]:
#             print("WARNING: vous n'êtes pas censé recopier le code de la fonction combinatoire")
#
#     def test_fonction(self):
#         check_fonction_in_code(self, "gain_loto")
#         for n in range(48, 50):
#             for k in range(5, 7):
#                 for montant in (50, 1000000):
#                     test_with_expected(self, gain_loto, (n, k, montant), gain_loto_prof(n, k, montant),
#                                                  almost=True)
# class TestExerciceF2_10(unittest.TestCase):
#     def test_fonction(self):
#         check_fonction_in_code(self, "maximum_fonction")
#
#         def f1(x):
#             return 4 - (x - 1) ** 2
#
#         test_with_expected(self, maximum_fonction, (f1, 0, 2), 1, places=2, almost=True)


class TestExerciceL0(unittest.TestCase):
    def test_1(self):
        self.assertEqual(create_empty_list(), [])


class TestExerciceL0_1(unittest.TestCase):
    def test_a(self):
        self.assertEqual(a, [1, 2])

    def test_b(self):
        self.assertEqual(b, [3, 4, 5])

    def test_c(self):
        self.assertEqual(c, [[1, 2], [3, 4, 5]])

    def test_d(self):
        self.assertEqual(d, list(it for it in range(1, 1001)))


class TestExerciceL0_2(unittest.TestCase):
    def test_add(self):
        liste = [1, 2]
        self.assertEqual(add(liste, 3), None, "add should not return anything")
        self.assertEqual(liste, [1, 2, 3], "add must actually add an element to the list")

    def test_second_element(self):
        test_with_expected(self, second_element, [1, 6, 9], expected=6)
        test_with_expected(self, second_element, [1, 42, 9, 15], expected=42)

    def test_last_element(self):
        test_with_expected(self, last_element, [1, 6, 9], expected=9)
        test_with_expected(self, last_element, [1, 42, 6, 9, 15], expected=15)
        self.assertTrue("-1" in In[-1], "Think about using negative indexing !")

    def test_remove_third_element(self):
        orig = [1, 2, 4, 8, 16, 32, 64, 128]
        copy = orig[:]

        for it in range(10):
            try:
                prev = copy[:]
                self.assertEqual(
                    remove_third_element(copy),
                    None,
                    "remove_third_element must not return anything")
                self.assertEqual(copy, orig[:2] + orig[3 + it:])
            except Exception as e:
                self.Fail("ERROR : your function called with {0} raised exception : {1}".format(prev, e))


class TestExerciceL1a(unittest.TestCase):
    def test_code(self):
        self.assertFalse("range" in In[-1], "Vous ne devez pas utiliser de range")
        self.assertEqual(In[-1].count("for "), 1,
                         "Vous devez utiliser exactement une boucle for, vous en avez utilisées {0}".format(
                             In[-1].count("for ")))

    def test_fonction(self):
        test_with_expected(self, somme_1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], expected=55)
        test_with_expected(self, somme_1, [1, 2, 4, 8, 16, 32, 64, 128, 256, 512], expected=1023)


# class TestExerciceL1b(unittest.TestCase):
#     def test_code(self):
#         self.assertEqual(In[-1].count("range"), 1, "Vous devez utiliser la fonction range")
#         self.assertEqual(In[-1].count("for "), 1,
#                          "Vous devez utiliser exactement une boucle for, vous en avez utilisées {0}".format(
#                              In[-1].count("for ")))
#
#     def test_fonction(self):
#         test_with_expected(self, somme_2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], expected=55)
#         test_with_expected(self, somme_2, [1, 2, 4, 8, 16, 32, 64, 128, 256, 512], expected=1023)
#
#
# class TestExerciceL3(unittest.TestCase):
#     def test_1(self):
#         test_with_expected(self, somme_1_sur_2, [1, 2, 7, 9], expected=8)
#         test_with_expected(self, somme_1_sur_2, [10, 2, 20, 30, 50], expected=80)
#
#
# class TestExerciceL5a(unittest.TestCase):
#     def test_1(self):
#         liste_1 = [1, -2, 7, -9]
#         test_with_expected(self, rendre_positif_1, liste_1, expected=[1, 2, 7, 9])
#         self.assertEqual(liste_1, [1, 2, 7, 9], "La liste donnée en entrée doit être modifiée")
#
#
# class TestExerciceL5b(unittest.TestCase):
#     def test_1(self):
#         liste_1 = [1, -2, 7, -9]
#         test_with_expected(self, rendre_positif_2, liste_1, expected=[1, 2, 7, 9])
#         self.assertEqual(liste_1, [1, -2, 7, -9], "La liste donnée en entrée ne doit pas être modifiée")
#
#
# class TestExerciceL7(unittest.TestCase):
#     def test_code(self):
#         self.assertEqual(In[-1].count("remove"), 0, "Vous n'avez pas le droit d'utiliser remove !")
#
#     def test_fonction(self):
#         liste_1 = [1, 2, 3, 4, 2]
#         supprimer(liste_1, 2)
#         self.assertEqual(liste_1, [1, 3, 4, 2])
#         supprimer(liste_1, 4)
#         self.assertEqual(liste_1, [1, 3, 2])


class TestExerciceL8(unittest.TestCase):
    def test_fonction(self):
        test_with_expected(self, even_first, [1, 2, 3, 4, 2, 7, 8, 10, 97], expected=[2, 4, 2, 8, 10, 1, 3, 7, 97])


# class TestExerciceL9(unittest.TestCase):
#     def test_code(self):
#         self.assertTrue("sort" not in In[-1], "Vous n'avez pas le droit d'utiliser sort, ni sorted !")
#
#     def test(self):
#         self.assertEqual(tri([6, 7, 8, 9, 1, 2, 3, 4, 5]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
#         self.assertEqual(tri([16, 75, 3, 9, 4, 6, 15]), [3, 4, 6, 9, 15, 16, 75])
#         self.assertEqual(tri([16, 75, 3, 9, 0, 6, 15]), [0, 3, 6, 9, 15, 16, 75])
