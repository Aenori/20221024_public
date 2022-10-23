import unittest
import sys
import traceback
import collections
import re
import random
import pprint
this = sys.modules[__name__]

__unittest = True

import cours_python_utils as cpy_utils

def check_variable_and_value( self, var_name, exp_type, exp_value, almost = False ):
    if not var_name in globals():
        self.fail("Vous n'avez pas défini de variable " + var_name)
    var = globals()[var_name]
    self.assertIsInstance( var, exp_type, "{0} doit être de type {1}".format( var_name, exp_type ) )
    if not almost:
        self.assertEqual( var, exp_value, '{0} doit être égal à {1}, {0} est égal à {2}'.format( var_name, exp_value, var ) )
    else:
        self.assertAlmostEqual( var, exp_value, msg = '{0} doit être égal à {1}, {0} est égal à {2}'.format( var_name, exp_value, var ) )

def check_function_exists( self, function_name ):
    self.assertTrue( function_name in globals(), "Vous devez définir une fonction {0}".format( function_name ) )
    self.assertTrue( re.compile(function_name + " *\(").search(In[-1]) is not None, "ATTENTION, votre fonction existe, mais pas dans votre code, vous utlisez une vieille version !" )
    self.assertTrue( callable( globals()[function_name] ), "{0} n'est pas une fonction !".format( function_name ) )

def exec_and_get_stdout( f ):
    sys.stdout = FakeStdout()
    f()
    res = sys.stdout.line_list
    sys.stdout = sys.__stdout__
    return res

class FakeStdout:
    def __init__(self):
        self.line_list = []

    def write(self, x):
        self.line_list.append( x )

    def flush(self):
        pass

class TestExercice0( unittest.TestCase ):
    def test(self):
        self.assertTrue( "hello_world" in globals(), "Vous devez définir une fonction hello_world" )
        self.assertEqual( hello_world(), "Hello world !" )
    
class TestExercice2_1( unittest.TestCase ):
    def test_code(self):
        self.assertFalse( "print" in In[-1], "La fonction print est interdite !" )

    def test_fonction(self):
        check_function_exists(self, "un" )
        self.assertEqual( un(), 1, "Votre fonction doit renvoyer 1" )

class TestExercice2_2( unittest.TestCase ):
    def test_code(self):
        self.assertFalse( "print" in In[-1], "La fonction print est interdite !" )

    def test_fonction(self):
        check_function_exists(self, "incremente" )
        for it in range(10):
            cpy_utils.test_with_expected( self, incremente, it, it + 1 )

class TestExercice2_3( unittest.TestCase ):
    def test_code(self):
        self.assertFalse( "print" in In[-1], "La fonction print est interdite !" )

    def test_fonction(self):
        check_function_exists(self, "somme" )
        for x in range(10):
            for y in range(10):
                cpy_utils.test_with_expected( self, somme, (x,y), x+y )

class TestExercice2_4( unittest.TestCase ):
    def test_code(self):
        self.assertFalse( "print" in In[-1], "La fonction print est interdite !" )

    def test_fonction(self):
        check_function_exists(self, "evaluation_polynome" )
        for a in range(5):
            for b in range(5):
                for c in range(5):
                    for x in range(5):
                        cpy_utils.test_with_expected( self, evaluation_polynome, (a,b,c,x), a*x**2 + b*x + c )

class TestExercice2_5( unittest.TestCase ):
    def test_code(self):
        self.assertFalse( "print" in In[-1], "La fonction print est interdite !" )
        self.assertFalse( "else"  in In[-1], "L'instruction else est interdite !" )
        self.assertFalse( "elif"  in In[-1], "L'instruction elif est interdite !" )
        self.assertFalse( In[-1].count("if ") > 1, "Vous n'avez pas le droit à plus d'un if" )

    def test_fonction(self):
        check_function_exists(self, "est_pair" )
        for x in range(10):
            cpy_utils.test_with_expected( self, est_pair, x, x%2==0 )

class TestExercice2_6( unittest.TestCase ):
    def test_code(self):
        self.assertFalse( "math"  in In[-1], "Le module math est interdit !" )

    def test_fonction(self):
        check_function_exists(self, "factorielle" )
        import math
        for n in range(10):
            cpy_utils.test_with_expected( self, factorielle, n, math.factorial(n) )

class TestExercice2_7( unittest.TestCase ):
    def test_code(self):
        self.assertFalse( "math"  in In[-1], "Le module math est interdit !" )
        self.assertTrue( "factorielle" in In[-1], "Vous devez utiliser votre fonction factorielle" )
        if "def factorielle" in In[-1]:
            print( "WARNING: vous n'êtes pas censé recopier le code de la fonction factorielle" )

    def test_fonction(self):
        check_function_exists(self, "combinatoire" )
        import math
        for n in range(10):
            for k in range(n+1):
                cpy_utils.test_with_expected( self, combinatoire, (n,k), (math.factorial(n)//(math.factorial(k)*math.factorial(n-k)) ))

class TestExercice2_8( unittest.TestCase ):
    def test_code(self):
        self.assertFalse( "math"  in In[-1], "Le module math est interdit !" )
        self.assertTrue( "combinatoire" in In[-1], "Vous devez utiliser votre fonction combinatoire" )
        if "def combinatoire" in In[-1]:
            print( "WARNING: vous n'êtes pas censé recopier le code de la fonction combinatoire" )

    def test_fonction(self):
        check_function_exists(self, "gain_loto_gros_lot" )
        import math
        for n in range(40,50):
            for k in range(1,5):
                for montant in (50,1000000):
                    cpy_utils.test_with_expected( 
                            self, 
                            gain_loto_gros_lot, 
                            (n,k,montant), 
                            montant/((math.factorial(n)//(math.factorial(k)*math.factorial(n-k)) )),
                            almost = True)

def gain_loto_prof(n,k,montant):
    gain_moyen = 0
    for j in range(k):
        gain_moyen += (montant/(100**j))*combinatoire(k,k-j)*combinatoire(n-k,j)/combinatoire(n,k)
    return gain_moyen


class TestExercice2_9( unittest.TestCase ):
    def test_code(self):
        self.assertFalse( "math"  in In[-1], "Le module math est interdit !" )
        self.assertTrue( "combinatoire" in In[-1], "Vous devez utiliser votre fonction combinatoire" )
        if "def combinatoire" in In[-1]:
            print( "WARNING: vous n'êtes pas censé recopier le code de la fonction combinatoire" )

    def test_fonction(self):
        check_function_exists(self, "gain_loto" )
        import math
        for n in range(48,50):
            for k in range(5,7):
                for montant in (50,1000000):
                    cpy_utils.test_with_expected( self, gain_loto, (n,k,montant), gain_loto_prof(n,k,montant), almost = True )

class TestExercice2_10( unittest.TestCase ):
    def test_fonction(self):
        check_function_exists(self, "maximum_fonction" )
        def f1(x):
            return 4 - (x-1)**2
        cpy_utils.test_with_expected( self, maximum_fonction, (f1,0,2), 1, places = 2, almost = True )


def tester_exo( n, globals_dict ):
    for k, v in globals_dict.items():
        setattr( this, k, v )
    launch_test_case( eval( "TestExercice{0}".format(n) ) )

def launch_test_case( test_case ):
  suite = unittest.TestLoader().loadTestsFromTestCase( test_case )
  unittest.TextTestRunner(verbosity=2).run(suite)

