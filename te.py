import itertools
from lib import math_extended, validation


def RSA_encrypt(txt, n, k):
    nr_lst = map(lambda x: ord(x.upper()), list(txt))
    s = [str(i) for i in nr_lst]
    res = int("".join(s))

    return pow(res, k, n)


def RSA_decrypt(ctxt, p, q):
    n = p * q
    phi = (p-1)*(q-1)

    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, y, x = egcd(b % a, a)
        return (g, x - (b//a) * y, y)

    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception('No modular inverse')
        return x % m

    j = modinv(7, phi)

    return pow(ctxt, j, n)



	


# examples

print('is valid isbn10:', validation.isbn10('0316066524'))
print('is valid isbn13:', validation.isbn13('9780316066525'))



print('is valid credit card num:', validation.is_valid_credit_card(6011000000000012))


print('centroid:', math_extended.calculate_centroid(1, 2, 3, 4, 5, 6))
print('combinations:', math_extended.combinations(5, 52))
print('diagonal difference:', math_extended.diagonal_difference(
    [[1, 2, 3], [4, 5, 6], [9, 8, 9]]))
print('divides evenly:', math_extended.divides_evenly(10, 2))
print('dbl factorial:', math_extended.double_factorial(5))
print('fib:', math_extended.fib(5))
print('distance:', math_extended.get_distance(
    {'x': -2, 'y': -2}, {'x': 4, 'y': 3}))
print('is circle collide:', math_extended.is_circle_collision(
    [2, 2, 1], [5, 5, 10]))
print('is divisible:', math_extended.is_divisible(10, 5))
print('matrix:', math_extended.matrix_mul([[4, 2], [3, 1]], [[5, 6], [3, 8]]))
print('missing angle type:', math_extended.missing_angle(50, 50))
print('root:', math_extended.newton([1, 2, 3, 4]))
print('polygon area:', math_extended.polygon([[2, 5], [5, 1], [-4, 3]]))
print('reversed binary int:', math_extended.reversed_binary_integer(5))
print('sum of cubes:', math_extended.sum_of_cubes([1, 2, 3]))
print('triangular num sequence:', math_extended.triangular_number_seq(5))
