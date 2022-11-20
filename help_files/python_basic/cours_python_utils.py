import re
import traceback
import numpy as np

__unittest = True

print_re = re.compile("\n[ \t]*print *\(")

EXCEPTION_MSG = "Your function call failed with the arguments {0}" \
                " and raised the exception {1}\n{2}"
WRONG_VALUE_MSG = "With {0} as input, the function should return {1}," \
                  " but it returned {2}"
NO_PRINT_WARNING_MSG = " WARNING : you don't need to use the print function"
FUNCTION_NOT_FOUND = "ERROR : you are supposed to use the function {0}", \
                     " which was not found in your code"
VARIABLE_NOT_FOUND = "ERROR :you were supposed to define variable {0}, but it was not found"
VARIABLE_SHOULD_BE_NP_ARRAY = "ERROR : The variable {0} should be of type np.array." \
                              "Its actual type {1}"
VARIABLE_HAS_WRONG_RANK = "ERROR : variable {0} is not of the good rank ! It should have" \
                          " {1} dimension, it has {2}"
WRONG_SHAPE_MSG = "ERROR : variable {0} has not the good number of line and columns." \
                  "Its shape should be {1}, it is {2}"
ELEMENTS_DIFFERENCE_MSG = "ERROR : matrix shape is the one expected, but not the elements values."
MANDATORY_FUNCTION_MISSING_MSG = "ERROR : You must the function / methode {0}. Please reread " \
                                 "instructions if necessary."

def test_with_expected(test_f, f, args, expected, places=7, almost=False):
    if not isinstance(args, tuple):
        args = (args,)
    try:
        res = f(*args)
    except Exception as e:
        test_f.fail(EXCEPTION_MSG.format(args, e, traceback.format_exc()))
    if almost:
        test_f.assertAlmostEqual(res, expected, places=places, msg=WRONG_VALUE_MSG.format(args, expected, res))
    else:
        test_f.assertEqual(res, expected, WRONG_VALUE_MSG.format(args, expected, res))


def warning_on_print(In):
    if print_re.search(In[-1]):
        print("=" * len(NO_PRINT_WARNING_MSG))
        print(NO_PRINT_WARNING_MSG)
        print("=" * len(NO_PRINT_WARNING_MSG))


def check_fonction_in_code(test_f, function_name, In):
    if function_name not in In[-1]:
        test_f.fail(FUNCTION_NOT_FOUND.format(function_name))



def verify_matrix(test_f, global_dict, var_name, matrix_ref):
    if var_name not in global_dict:
        test_f.fail(VARIABLE_NOT_FOUND.format(var_name))
    matrix = global_dict[var_name]

    if not isinstance(matrix, np.ndarray):
        test_f.fail(VARIABLE_SHOULD_BE_NP_ARRAY.format(var_name, type(matrix)))

    if len(matrix.shape) != len(matrix_ref.shape):
        test_f.fail(VARIABLE_HAS_WRONG_RANK.format(
            var_name, len(matrix_ref.shape), len(matrix.shape)))

    if matrix.shape != matrix_ref.shape:
        test_f.fail(
            WRONG_SHAPE_MSG.format(
                var_name, matrix_ref.shape, matrix.shape))

    test_f.assertTrue((matrix == matrix_ref).all(),
                      ELEMENTS_DIFFERENCE_MSG)


def check_mandatory_function(test_f, In, func_name):
    if not func_name + "(" in In[-1]:
        test_f.fail(MANDATORY_FUNCTION_MISSING_MSG.format(func_name))
