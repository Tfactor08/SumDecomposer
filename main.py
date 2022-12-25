from math import factorial as fact


def _get_coeff(n, k) -> int:
    '''Returns coefficient in front of the term in accordance with given `n` and `k` states'''
    result = fact(n) / (fact(k) * fact(n-k))

    return int(result)


def _get_powers(n, k) -> tuple:
    '''Returns powers of the variables in accordance with given `n` and `k` states'''
    return (n-k, k)


def _format_power(power) -> str:
    '''Formats given power from n to ⁿ and returns it'''
    if power == 1:
        return ''

    result = ''

    powers_tuple = ('⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹')
    powers_dict = dict(zip(range(10), powers_tuple))
    
    for char in str(power):
        result += powers_dict[int(char)]

    return result


def _get_term(coeff, powers) -> str:
    '''Creates the term using coefficient and powers of the variables and returns it'''
    result = ''
    variables = ('a', 'b')

    result += str(coeff) if coeff > 1 else ''

    for var, power in zip(variables, powers):
        if power != 0:
            result += f'{var}{_format_power(power)}'

    return result
 

def _get_terms(n) -> str:
    '''Contains main loop. Returns terms of the sum'''
    for k in range(n+1):
        powers = _get_powers(n, k)
        coeff = _get_coeff(n, k)

        yield _get_term(coeff, powers)
   

def get_sum(n) -> str:
    '''Joins the terms into sum'''
    terms = _get_terms(n)

    return ' + '.join(terms)


def main():
    while True:
        n = int(input())

        print(get_sum(n))
        

if __name__ == '__main__':
    main()

