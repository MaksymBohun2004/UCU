from typing import List
def sieve_flavius(n: int) -> List[int]:
    """
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
    """
    numbers = [i for i in range(1,n)]
    timed_numbers = numbers.copy()
    num = 1
    for i in timed_numbers:
        try:
            if i == 1:
                continue
            if i in numbers:
                timed = 0
                for j in range(1,len(timed_numbers)):
                    del numbers[j * i - 1 - timed]
                    timed += 1
                    if j == len(timed_numbers):
                        num += 1
        except: continue
    return numbers