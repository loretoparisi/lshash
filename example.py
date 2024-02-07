# -*- coding: utf-8 -*-

from lshashpy3 import LSHash

# create 6-bit hashes for input data of 8 dimensions:
k = 6 # hash size
L = 5  # number of tables
d = 8 # Dimension of Feature vector
lsh = LSHash(hash_size=k, input_dim=d, num_hashtables=L)

# index vector
lsh.index([2,3,4,5,6,7,8,9])

# get the binary hash for an input point by iterating through all tables
binary_hashes = lsh.get_hashes([2,3,4,5,6,7,8,9])
print("hash representation", binary_hashes)

# checking that each table stores the same input vector with different keys
for key, table in zip(binary_hashes, lsh.hash_tables):
    print(key, table.get_list(key))

# index vector and extra data
lsh.index([10,12,99,1,5,31,2,3], extra_data="vec1")
lsh.index([10,11,94,1,4,31,2,3], extra_data="vec2")

# query a data point
top_n = 1
nn = lsh.query([1,2,3,4,5,6,7,7], num_results=top_n, distance_func="euclidean")
print("query (euclidean):", nn)

# query a data point
top_n = 1
nn = lsh.query([1,2,3,4,5,6,7,7], num_results=top_n, distance_func="hamming")
print("query (hamming):", nn)

# unpack vector, extra data and vectorial distance
# distance_func can be "euclidean", "true_euclidean", "centred_euclidean", "cosine", "l1norm".
top_n = 3
nn = lsh.query([10,12,99,1,5,30,1,1], num_results=top_n, distance_func="euclidean")
for ((vec,extra_data),distance) in nn:
    print(vec, extra_data, distance)

# InMemoryStorage
lsh = LSHash(hash_size=k, input_dim=d, num_hashtables=L,
    storage_config={ 'dict': None }, matrices_filename='weights.npz', overwrite=False)

# local storage for numpy uniform random planes, overwrite matrix file
lsh = LSHash(hash_size=k, input_dim=d, num_hashtables=L,
    storage_config={ 'dict': None },
    matrices_filename='weights.npz', 
    hashtable_filename='hash.npz', 
    overwrite=True)

lsh.index([10,12,99,1,5,31,2,3], extra_data="vec1")
lsh.index([10,11,94,1,4,31,2,3], extra_data="vec2")

top_n = 3
nn = lsh.query([10,12,99,1,5,30,1,1], num_results=top_n, distance_func="euclidean")
print("query (euclidean):", nn)

# save hash table to disk 
lsh.save()

# local storage for numpy uniform random planes, overwrite matrix file
lsh = LSHash(hash_size=k, input_dim=d, num_hashtables=L,
    storage_config={ 'dict': None },
    matrices_filename='weights.npz', 
    hashtable_filename='hash.npz', 
    overwrite=True)

# execute a query loading hash table from local file system
top_n = 3
nn = lsh.query([10,12,99,1,5,30,1,1], num_results=top_n, distance_func="euclidean")
print("query from disk (euclidean):", nn)