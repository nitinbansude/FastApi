from typing import List
from multiprocessing import Pool
def makeaddition(list):
    with Pool() as pool:
        result = pool.map(sum, list)
    return result

# def add_lists(list):
#     return [sum(lst) for lst in list]