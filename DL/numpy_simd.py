'''
    1. 파이썬 리스트 & 넘파이
        1) 넘파이 배열
            - 형샹(shape) : 차원 결정
'''

import numpy as np

a = np.array([2,3,4])
print(a.shape)
print(a.ndim)
print(a.dtype)
print(a.itemsize)
print(a.size)

store_a = [20,10,30]
store_b = [70,90,70]

list_sum = store_a + store_b
print(list_sum)