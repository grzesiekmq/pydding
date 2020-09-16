from math import *
import itertools


def divides_evenly(a, b):
    return a % b == 0


def missing_angle(angle1, angle2):
    result = 180 - (angle1 + angle2)
    if result < 90:
        return 'acute'

    elif result > 90:
        return 'obtuse'

    return 'right'


def combinations(k, n):
    return int((factorial(n) / (factorial(k) * factorial(n - k))))

# works only for sorted vertices!


def polygon(lst):

    arr = []
    for i, j in zip(range(len(lst)), range(1, len(lst))):
        arr.append(lst[i][0] * lst[j][1] - lst[i][1] * lst[j][0])
    last = len(lst)-1
    arr.append(lst[last][0] * lst[0][1] - lst[last][1] * lst[0][0])
    area = abs(sum(arr)/2)
    return area


def triangular_number_seq(n):
    if n == 1:
        return 1

    return n + triangular_number_seq(n - 1)


def get_distance(a, b):
    x_diff_squared = (b['x'] - a['x']) ** 2
    y_diff_squared = (b['y'] - a['y']) ** 2
    return round(sqrt(x_diff_squared + y_diff_squared), 3)


def is_circle_collision(c1, c2):
    y = c2[2]
    x = c1[1]
    r1 = c1[0]
    r2 = c2[0]
    xDiffSquared = (y - x) ** 2
    yDiffSquared = (y - x) ** 2
    distance = int(sqrt(xDiffSquared + yDiffSquared))
    return distance < r1 + r2


def calculate_centroid(x1, y1, x2, y2, x3, y3):
    x = (x1 + x2 + x3) / 3
    y = (y1 + y2 + y3) / 3
    centroid = (round(x, 2), round(y, 2))
    return centroid


def newton(c):
    step = 0.0001
    def derive(function, value):
	    result = (function(value + step) - function(value)) / step
	    return float("%.3f" % result)
    def f(x):
	    fn = c[0]*x**3 + c[1]*x**2 + c[2]*x + c[3]		
	    return fn
    x = 0.0
    while abs(f(x) / derive(f, x)) >= step: 
	    x -= f(x) / derive(f, x)
    return round(x, 3)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 2) + fib(n - 1)


def calc_det2x2(matrix):

    arr = list(itertools.chain.from_iterable(matrix))
    a, b, c, d = arr

    return a * d - b * c


def sum_of_cubes(nums):
    if len(nums) == 0:
        return 0

    return sum(map(lambda el:  el ** 3, nums))


def is_divisible(num, divisor):
    return num % divisor == 0


def diagonal_difference(lst):

    primary = []
    secondary = []

    arrRange = range(len(lst))
    for i in arrRange:
        primary.append(lst[i][i])

    for i, j in zip(arrRange, reversed(arrRange)):
        secondary.append(lst[i][j])

    primarySum = sum(primary)

    secondarySum = sum(secondary)

    return abs(primarySum - secondarySum)


def double_factorial(num):

    if num == -1 or num == 0:
        return 1

    if num % 2 == 0:
        return num * double_factorial(num - 2)

    return num * double_factorial(num - 2)


def reversed_binary_integer(num):
	return int(bin(num)[-1:1:-1], 2)

def matrix_mul(m1, m2):
	i = 0
	j = 1

	def get(matrix):
	    return (matrix[i][j] for i, j in itertools.product((i, j), repeat=2))

	a1, a2, a3, a4 = get(m1)
	b1, b2, b3, b4 = get(m2)

	
	
	one = a1*b1 + a2*b3
	two = a1*b2 + a2*b4
	three = a3*b1 + a4*b3
	four = a3*b2 + a4*b4

	return [[one, two], [three, four]]