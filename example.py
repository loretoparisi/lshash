# -*- coding: utf-8 -*-

from lshash import LSHash

# create 6-bit hashes for input data of 8 dimensions:
lsh = LSHash(6, 8)
lsh.index([1,2,3,4,5,6,7,8])
lsh.index([2,3,4,5,6,7,8,9])
lsh.index([10,12,99,1,5,31,2,3])
lsh.query([1,2,3,4,5,6,7,7])