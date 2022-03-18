# ex 2 - Second exercise: Check odd/even
import random

def odd_evens(l):
    odd = [num for num in l if num %2]
    even = [num for num in l if not num %2]
    print("\nNumber of odds: ", len(odd))
    print("\nNumber of evens: ", len(even))
    return len(odd), len(even)


def separate_list(l):
    odd = [num for num in l if num %2]
    even = [num for num in l if not num %2]
    print("\nlist of only odds: ", odd)
    print("\nlist of only evens: ", even)
    return odd, even

if __name__ == '__main__':
    l = [random.randint(1, 100) for i in range(100)]
    print(l)
    odd_evens(l)
    separate_list(l)
