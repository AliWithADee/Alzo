def is_prime(n):
    if n < 2 or n % 2 == 0: return False
    if n == 2 or n == 3: return True

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def is_square(n):
    if n < 1:
        return False
    else:
        for i in range(int(n / 2) + 1):
            if (i * i) == n:
                return True
        return False


def split_number(_n):
    n = str(_n)
    L = len(n)
    if L % 2 == 0:
        mid = L // 2
        half1, half2 = n[:mid], n[mid:]
        return int(half1), int(half2)
    else:
        mid1 = L // 2
        mid2 = mid1 + 1
        half11, half21, half12, half22 = n[:mid1], n[mid1:], n[:mid2], n[mid2:]
        return int(half11), int(half21), int(half12), int(half22)


def get_composite_sums(n):
    L = len(str(n))

    if L % 2 == 0:
        half1, half2 = split_number(n)
        return half1 + half2
    else:
        if L == 1: return None

        half11, half21, half12, half22 = split_number(n)
        return (half11 + half21), (half12 + half22)


def is_alzo(n):
    if len(str(n)) % 2 == 0:
        half1, half2 = split_number(n)  # Split number into two halves
        if not (is_prime(half1) and is_prime(half2)): return False  # If both are not prime then return false
        s1 = half1 + half2  # Find the sum

        L = len(str(s1))
        if L % 2 == 0:
            # If the sum has an even number of digits,
            # return whether its sum is a square number
            return is_square(get_composite_sums(s1))
        else:
            if L == 1: return False

            # If the sum has an odd number of digits,
            # return whether the sum of one of these sums is square.
            s21, s22 = get_composite_sums(s1)
            if not (is_square(s21) or is_square(s22)): return False
    else:
        if len(str(n)) == 1: return False

        half11, half21, half12, half22 = split_number(n)
        if not ((is_prime(half11) and is_prime(half21)) or (is_prime(half12) and is_prime(half22))): return False
        s11, s12 = half11 + half21, half12 + half22
        sqr1 = True
        sqr2 = True

        L1 = len(str(s11))
        if L1 % 2 == 0:
            sqr1 = is_square(get_composite_sums(s11))
        else:
            if L1 == 1:
                sqr1 = False
            else:
                s21, s22 = get_composite_sums(s11)
                sqr1 = is_square(s21) or is_square(s22)

        L2 = len(str(s12))
        if L2 % 2 == 0:
            sqr2 = is_square(get_composite_sums(s12))
        else:
            if L2 == 1:
                sqr2 = False
            else:
                s21, s22 = get_composite_sums(s12)
                sqr2 = is_square(s21) or is_square(s22)

        return sqr1 or sqr2

    return True


def find_alzo(lower, upper):
    if upper < lower:
        return print("There are no Alzo numbers between {} and {}!".format(lower, upper))

    count = 0
    for i in range(lower, upper+1):
        if is_alzo(i):
            count += 1
            print("[{}] {} is Alzo!".format(count, i))

    if count > 0:
        return print("\nThere are {} Alzo numbers between {} and {} (inclusive)".format(count, lower, upper))

    return print("There are no Alzo numbers between {} and {}!".format(lower, upper))


print('This program finds all the "Alzo" numbers between a certain range.')
print("Please enter the range below.\n")
lower = int(input("Lower bound (inclusive): "))
upper = int(input("Upper bound (inclusive): "))
print()
find_alzo(lower, upper)

"""
A number is considered "Alzo" if it meets the criteria below.

1.  First split the number in half to create two separate numbers.
    Eg: 1345 becomes -> 13 and 45

2.  If the number has an odd number of digits, then you must consider both sets of numbers separately.
    Eg: For 175 you must consider the pairs -> 17 and 5 AND 1 and 75.

3.  For the number to be Alzo, both numbers of at least one pair must both be prime.
    
    NOTE: For an odd number of digits, the two pairs of numbers are INDEPENDENT of each other.
    If both numbers from the first pair are prime but both numbers from the second pair are not prime,
    then only the first pair is considered moving forward.
    Eg: 1 and 75 are not both prime, but 17 and 5 are, so 175 could still be Alzo (spoiler, it is!)

4.  Next take your two prime numbers and find their sum.
    Eg: 17 + 5 = 22

5.  Now split this number into two numbers as well.
    Eg: 22 becomes -> 2 and 2

6.  Finally, find the sum of these final two numbers. If the sum is a square number then the original number is Alzo!
    
    NOTE: At this stage, these numbers DO NOT need to be prime.
    It would actually be impossible to have an Alzo number if this was the case, as prime sums are all even.

And that is Alzo!
"""
