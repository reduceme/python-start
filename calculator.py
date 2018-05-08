"""
Written by  : regddai - github.com/reduceme
Description : Uses Pythons eval() function
              as a way to implement calculator.

Functions available are:
--------------------------------------------
                         + : addition
                         - : subtraction
                         * : multiplication
                         / : division
                         % : percentage
                         e : 2.718281...
                        pi : 3.141592...
                      sine : sin(rad)
                    cosine : cos(rad)
                   tangent : tan(rad)
                 remainder : XmodY
               square root : sqrt(n)
  round to nearest integer : round(n)
convert degrees to radians : rad(deg)
"""

import math
import sys

def calc(term):
    term = term.replace(' ', '')
    term = term.replace('^', '**')
    term = term.replace('=', '')
    term = term.replace('?', '')
    term = term.replace('%', '/100')
    term = term.replace('rad', 'radians')
    term = term.replace('mod', '%')

    functions = ['sin', 'cos', 'tan', 'cosh', 'sinh', 'tanh', 'sqrt', 'pi', 'radians', 'e']

    for function in functions:
        if function in term.lower():
            withmath = 'math.' + function
            term = term.replace(function, withmath)

    try:
        term = eval(term)

    except ZeroDivisionError:
        print('Can\'n divide by 0')
        exit(1)

    except NameError:
        print('check usage method')
        exit(1)

    return term

def result(term):
    print('\n' + str(calc(term)))

def main():
    print("\nScientific Calculator\nEg: sin(rad(90)) + 50% * (sqrt(16)) + round(1.42^2) - 12mod3\nEnter quit to exit")

    if sys.version_info.major >= 3:
        while True:
            k = input('\nwhat is ')
            if k == 'quit':
                break
            result(k)

    else:
        while True:
            k = raw_input('\nwhat is ')
            if k == 'quit':
                break;
            result(k)

if __name__ == '__main__':
    main()
