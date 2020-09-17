def is_valid_credit_card(number):
    s = list(str(number))
    s = list(map(int, s))

    is_even = False
    digits = []

    for digit in s[::-1]:
        if is_even:
            digit *= 2
            if digit > 9:
                digit -= 9
        digits.append(digit)

        is_even = not is_even
    return sum(digits) % 10 == 0


def isbn10(s):
    arr = []
    s = list(map(int, s))
    for digit in s[:1:-1]:
        arr.append(digit)

    sum10 = sum(list(map(lambda el: el * digit, s)))

    return sum10 % 11 == 0


def isbn13(s):
    is_even = False
    s = list(map(int, s))
    digits = []

    for digit in s:

        if is_even:
            digit *= 3

        digits.append(digit)

        is_even = not is_even

    return sum(digits) % 10 == 0 and len(s) == 13
