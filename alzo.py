def is_prime(n):
    if n < 2 or n % 2 == 0: return False
    if n == 2 or n == 3: return True
    
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False

    return True

def is_square(n):
    if n<1:
        return False
    else:
        for i in range(int(n/2)+1):
            if (i*i)==n:
                return True
        return False

def split_number(_n):
    n = str(_n)
    L = len(n)
        
    if L % 2 == 0:
        mid = L // 2
        
        half1 = n[:mid]
        half2 = n[mid:]

        return int(half1), int(half2)
            
    else:
        mid1 = (L // 2)
        mid2 = mid1 + 1
        
        half11 = n[:mid1]
        half21 = n[mid1:]
        
        half12 = n[:mid2]
        half22 = n[mid2:]

        return int(half11), int(half21), int(half12), int(half22)

def get_prime_sum(n):
    if len(str(n)) % 2 == 0:
        half1, half2 = split_number(n)
        
        if not (is_prime(half1) and is_prime(half2)): return None
        
        return half1 + half2
    else:
        half11, half21, half12, half22 = split_number(n)

        if not (is_prime(half11) and is_prime(half21)): return None
        if not (is_prime(half12) and is_prime(half22)): return None
        
        return (half11 + half21), (half12 + half22)

def is_alzo(n):
    s1 = get_prime_sum(n)
    s2 = get_prime_sum(s1)
    
    if not is_square(s2): return False
    
    return True

def find_alzo(upper):
    for i in range(10,upper):
        if is_alzo(i):
            print("N: {}".format(n))

find_alzo(100)
