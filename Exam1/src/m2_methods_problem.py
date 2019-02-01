###############################################################################
#   You are going to do a great job on this exam!
#   Read each question carefully.
#   Be sure to commit and push after each question
#   Be sure to right-click on src, and Mark Directory as Sources root
#   You will be asked to write 3 functions that demonstrate your
#   understanding of the concepts covered in class
#
###############################################################################
import rosegraphics as rg


def main():
    #   Tests are called from here.  Do not make any changes to main
    test_count_primes()
    test_multiply_primes()


###############################################################################
# done 1  READ the doc-string for the is_prime function defined below.
# You do NOT need to understand its implementations,
# just its specification (per the doc-string).
# You should  ** CALL **  functions as needed in implementing the
# other functions.  After you have READ this, change its _TODO_ to DONE.
###############################################################################


def is_prime(n):
    """
    What comes in:  An integer n >= 1.
    What goes out:
      -- Returns True if the given integer is prime,
         else returns False.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
    Note: The algorithm used here is simple and clear but slow.
    """
    if n == 1:
        return False

    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True

# -------------------------------------------------------------------------
# Students:
#   Do NOT touch the above  is_prime  function - it has no _TODO_.
#   Do NOT copy code from this function.
#
# Instead, ** CALL ** this function as needed in the problems below.
# -------------------------------------------------------------------------


def test_count_primes():
    ###############################################################################
    # done: 2  READ the doc-string for the count_primes function below,
    #   but DO NOT begin coding.
    # After you have READ this, change its _TODO_ to DONE.
    ###############################################################################
    print('#######################################')
    print('Test 1 of count primes')
    print('m = 1 and n = 3')
    print('Expected count = 2')
    print('Actual count = ', count_primes(1, 3))

    ###############################################################################
    #   TODO: 3. Add the additional test cases for this function below
    # After you have coded this, change its _TODO_ to DONE.
    ###############################################################################
    print()
    print('Your tests will go here!')
    return


def count_primes(m,n):
    """
    #    What comes in:
    #      -- A positive integer m.
    #      -- A positive integer n > m.
    #    What goes out:  The count of prime numbers between m and n,
    #                     including both m and n
    #    Side effects:
    #     Prints each prime number between m and n,
    #     inclusive of both m and n
    #     First example, if m = 1 and n = 3
    #     The following numbers should be printed to the console:
    #       2
    #       3
    #     The count returned by the program will be 2
    #
    #     Second example, if m = 20 and n = 22
    #     Nothing will be printed to the console,
    #     since none of the numbers are prime.
    #
    #     The count returned by the program will be 0
    #
    #     Third example, if m = 2 and n = 8
    #     The following numbers should be printed to the console:
    #       2
    #       3
    #       5
    #       7
    #     The count returned by the program will be 4
    #     Write the code to test that the correct count
    #     has been returned for the three examples above.
    #     You can examine the printout
    #     to see if the correct values were printed
    #     We have provided one test example, in test_count_primes
    #     you must provide the
    #     second and third examples above
    """
    total = 0
    for k in range(2, m, n // 2 + 1):

        if n % k == 0:
            return False

    return True





    ################################################################################
    #   TODO: 4. Write the function count_primes(m,n) below here
    # After you have coded and tested, change its _TODO_ to DONE.
    ################################################################################



def test_multiply_primes():
    ################################################################################
    #   TODO: 6. Read the doc string for multiply_primes, below, then
    #       then read the test cases here.
    #   After you have read both, change this _TODO_ to DONE.
    ###############################################################################
    print('\n')
    print('#######################################')
    print('Test 1 of multiply primes')
    print('m = 1 and n = 3')
    print('Expected output = 6')
    print('Actual output = ', multiply_primes(1, 3))

    print('\nTest 2 of multiply primes')
    print('This is a special case!')
    print('m = 20 and n = 22')
    print('Expected output = 0')
    print('Actual output = ', multiply_primes(20, 22))

    print('\nTest 3 of multiply primes')
    print('m = 2 and n = 8')
    print('Expected output = 210')
    print('Actual output = ', multiply_primes(2, 8))


def multiply_primes(m,n):
    """
       #    What comes in:
       #      -- A positive integer m.
       #      -- A positive integer n > m.
       #    What goes out:  The product of prime numbers between m and n,
       #                     including both m and n
       #    Side effects:
       #     None
       #
       #     First example, if m = 1 and n = 3
       #     The product returned by the program will be 6,
       #     since 2*3 is 6
       #
       #     Second example, if m = 20 and n = 22
       #     0 will be returned, since there were no prime numbers
       #
       #     Third example, if m = 2 and n = 8
       #     The product returned by the program will be 210,
       #     since 2*3*5*7 is 210
       """
    ################################################################################
    #   TODO: 6. Write the function multiply_primes(m,n) below here
    # After you have coded and tested, change this _TODO_ to DONE.
    ###############################################################################


main()
