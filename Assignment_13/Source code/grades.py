import math

def total(lst:list) -> float:
    return float(sum(lst))

def average(lst:list) -> float:
    if len(lst) == 0:
        return math.nan
    return float(sum(lst)/len(lst))

def median(lst:list) -> float:
    lst.sort()
    if len(lst) == 0:
        raise ValueError
    if len(lst) % 2 == 0:
        return (lst[(len(lst)//2)-1]+lst[len(lst)//2])/2
    return lst[math.floor(len(lst)//2)]