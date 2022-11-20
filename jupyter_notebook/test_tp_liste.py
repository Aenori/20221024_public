import unittest
import sys
import traceback

this = sys.modules[__name__]

__unittest = True


class TestExercice0(unittest.TestCase):
    def test_1(self):
        self.assertEqual(creer_liste_vide(), [])


def test_with_expected(self, f, *args, expected):
    try:
        res = f(*args)
    except Exception as e:
        self.fail("L'appel de votre fonction a échoué avec les arguments {0} et l'exception {1}\n{2}".format(args, e,
                                                                                                             traceback.format_exc()))
    self.assertEqual(res, expected,
                     "Avec {0} en entrée, votre fonction devrait renvoyer {1}, elle a renvoyé {2}".format(args,
                                                                                                          expected,
                                                                                                          res))


class TestExercice0_1(unittest.TestCase):
    def test_a(self):
        self.assertEqual(a, [1, 2])

    def test_b(self):
        self.assertEqual(b, [3, 4, 5])

    def test_c(self):
        self.assertEqual(c, [[1, 2], [3, 4, 5]])

    def test_d(self):
        self.assertEqual(d, list(it for it in range(1, 1001)))


class TestExercice0_2(unittest.TestCase):
    def test_ajoute(self):
        liste = [1, 2]
        self.assertEqual(ajoute(liste, 3), None, "Ajoute ne doit rien renvoyer")
        self.assertEqual(liste, [1, 2, 3], "Ajoute doit ajouter un élément à la liste en entrée")

    def test_deuxieme_element(self):
        test_with_expected(self, deuxieme_element, [1, 6, 9], expected=6)
        test_with_expected(self, deuxieme_element, [1, 42, 9, 15], expected=42)

    def test_dernier_element(self):
        test_with_expected(self, dernier_element, [1, 6, 9], expected=9)
        test_with_expected(self, dernier_element, [1, 42, 6, 9, 15], expected=15)
        self.assertTrue("-1" in In[-1], "Utilisez les index négatifs !")

    def test_supprimer_troisieme_element(self):
        orig = [1, 2, 4, 8, 16, 32, 64, 128]
        copy = orig[:]

        for it in range(10):
            try:
                prev = copy[:]
                self.assertEqual(supprimer_troisieme_element(copy), None, "Votre fonction ne doit rien renvoyer")
                self.assertEqual(copy, orig[:2] + orig[3 + it:])
            except Exception as e:
                self.Fail(
                    "Votre fonction a provoqué une erreur lorsqu'elle a été appelée avec {0} : erreur {1}".format(prev,
                                                                                                                  e))


class TestExercice1a(unittest.TestCase):
    def test_code(self):
        self.assertFalse("range" in In[-1], "Vous ne devez pas utiliser de range")
        self.assertEqual(In[-1].count("for "), 1,
                         "Vous devez utiliser exactement une boucle for, vous en avez utilisées {0}".format(
                             In[-1].count("for ")))

    def test_fonction(self):
        test_with_expected(self, somme_1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], expected=55)
        test_with_expected(self, somme_1, [1, 2, 4, 8, 16, 32, 64, 128, 256, 512], expected=1023)


class TestExercice1b(unittest.TestCase):
    def test_code(self):
        self.assertEqual(In[-1].count("range"), 1, "Vous devez utiliser la fonction range")
        self.assertEqual(In[-1].count("for "), 1,
                         "Vous devez utiliser exactement une boucle for, vous en avez utilisées {0}".format(
                             In[-1].count("for ")))

    def test_fonction(self):
        test_with_expected(self, somme_2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], expected=55)
        test_with_expected(self, somme_2, [1, 2, 4, 8, 16, 32, 64, 128, 256, 512], expected=1023)


class TestExercice3(unittest.TestCase):
    def test_1(self):
        test_with_expected(self, somme_1_sur_2, [1, 2, 7, 9], expected=8)
        test_with_expected(self, somme_1_sur_2, [10, 2, 20, 30, 50], expected=80)


class TestExercice5a(unittest.TestCase):
    def test_1(self):
        liste_1 = [1, -2, 7, -9]
        test_with_expected(self, rendre_positif_1, liste_1, expected=[1, 2, 7, 9])
        self.assertEqual(liste_1, [1, 2, 7, 9], "La liste donnée en entrée doit être modifiée")


class TestExercice5b(unittest.TestCase):
    def test_1(self):
        liste_1 = [1, -2, 7, -9]
        test_with_expected(self, rendre_positif_2, liste_1, expected=[1, 2, 7, 9])
        self.assertEqual(liste_1, [1, -2, 7, -9], "La liste donnée en entrée ne doit pas être modifiée")


class TestExercice7(unittest.TestCase):
    def test_code(self):
        self.assertEqual(In[-1].count("remove"), 0, "Vous n'avez pas le droit d'utiliser remove !")

    def test_fonction(self):
        liste_1 = [1, 2, 3, 4, 2]
        supprimer(liste_1, 2)
        self.assertEqual(liste_1, [1, 3, 4, 2])
        supprimer(liste_1, 4)
        self.assertEqual(liste_1, [1, 3, 2])


class TestExercice8(unittest.TestCase):
    def test_fonction(self):
        test_with_expected(self, pair_d_abord, [1, 2, 3, 4, 2, 7, 8, 10, 97], expected=[2, 4, 2, 8, 10, 1, 3, 7, 97])


class TestExercice9(unittest.TestCase):
    def test_code(self):
        self.assertTrue("sort" not in In[-1], "Vous n'avez pas le droit d'utiliser sort, ni sorted !")

    def test(self):
        self.assertEqual(tri([6, 7, 8, 9, 1, 2, 3, 4, 5]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(tri([16, 75, 3, 9, 4, 6, 15]), [3, 4, 6, 9, 15, 16, 75])
        self.assertEqual(tri([16, 75, 3, 9, 0, 6, 15]), [0, 3, 6, 9, 15, 16, 75])


def tester_exo(n, globals_dict):
    for k, v in globals_dict.items():
        setattr(this, k, v)
    launch_test_case(eval("TestExercice{0}".format(n)))


def launch_test_case(test_case):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    unittest.TextTestRunner(verbosity=2).run(suite)
