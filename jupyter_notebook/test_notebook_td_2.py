import unittest
import sys
import traceback
import collections
import re
import random
import pprint
this = sys.modules[__name__]

import cours_python_utils as cpy_utils
## test_with_expected
## check_fonction_in_code

def check_variable_and_value( self, var_name, exp_type, exp_value, almost = False ):
    if not var_name in globals():
        self.fail("Vous n'avez pas défini de variable " + var_name)
    var = globals()[var_name]
    self.assertIsInstance( var, exp_type, "{0} doit être de type {1}".format( var_name, exp_type ) )
    if not almost:
        self.assertEqual( var, exp_value, '{0} doit être égal à {1}, {0} est égal à {2}'.format( var_name, exp_value, var ) )
    else:
        self.assertAlmostEqual( var, exp_value, msg = '{0} doit être égal à {1}, {0} est égal à {2}'.format( var_name, exp_value, var ) )

class TestExercice0( unittest.TestCase ):
    def test(self):
        self.assertEqual( i, "Hello world !" )
    
class TestExercice2_1( unittest.TestCase ):
    def test_code(self):
        nb_lignes = In[-1].count( "\n" ) + 1
        if nb_lignes > 10:
            print( "WARNING: Mais pourquoi donc tant de lignes de code ? {0}".format( nb_lignes ) )

    def test_fonction(self):
        check_variable_and_value( self, "a1", int, 5 )

class TestExercice2_2( unittest.TestCase ):
    def test_code(self):
        nb_lignes = In[-1].count( "\n" ) + 1
        if nb_lignes > 10:
            print( "WARNING: Mais pourquoi donc tant de lignes de code ? {0}".format( nb_lignes ) )

    def test_fonction(self):
        check_variable_and_value( self, "a2", float, 5.0 )

class TestExercice2_3( unittest.TestCase ):
    def test_code(self):
        nb_lignes = In[-1].count( "\n" ) + 1
        if nb_lignes > 10:
            print( "WARNING: Mais pourquoi donc tant de lignes de code ? {0}".format( nb_lignes ) )

    def test_fonction(self):
        check_variable_and_value( self, "a3", str, "5" )

class TestExercice2_4( unittest.TestCase ):
    def test_fonction(self):
        check_variable_and_value( self, "e", int, 1403 )
        check_variable_and_value( self, "f", int, 151200 )

class TestExercice2_5( unittest.TestCase ):
    def test_fonction(self):
        import math
        check_variable_and_value( self, "resultat2_5", int, math.factorial(999) )

class TestExercice2_6( unittest.TestCase ):
    def test_fonction(self):
        check_variable_and_value( self, "resultat2_6", int, sum(it**2 for it in range(1488) ) )

class TestExercice2_7( unittest.TestCase ):
    def test_fonction(self):
        check_variable_and_value( self, "resultat2_7", int, sum(3*it for it in range(334) ) )

class TestExercice2_8( unittest.TestCase ):
    def test_fonction(self):
        check_variable_and_value( self, "resultat2_8", int, sum(it for it in range(6000) if it % 3 == 0 or it % 5 == 0 ) )

class TestExercice2_9( unittest.TestCase ):
    def test_code(self):
        if "math" in In[-1]:
            self.fail("Il est interdit d'utiliser le module math (et du coup, d'avoir le mot math dans votre code")

    def test_fonction(self):
        import math
        check_variable_and_value( self, "resultat2_9", float, math.exp(10), almost = True )


def tester_exo( n, globals_dict ):
    for k, v in globals_dict.items():
        setattr( this, k, v )
    launch_test_case( eval( "TestExercice{0}".format(n) ) )

def launch_test_case( test_case ):
  suite = unittest.TestLoader().loadTestsFromTestCase( test_case )
  unittest.TextTestRunner(verbosity=2).run(suite)

