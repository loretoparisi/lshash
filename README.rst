LSHash
======

:Version: 0.0.9
:Python: 3.11.5

A fast Python implementation of locality sensitive hashing with persistance
support.

Based on original source code https://github.com/kayzhu/LSHash

Highlights
==========

- Python3 support
- Load & save hash tables to local disk
- Fast hash calculation for large amount of high dimensional data through the use of `numpy` arrays.
- Built-in support for persistency through Redis.
- Multiple hash indexes support.
- Built-in support for common distance/objective functions for ranking outputs.

Installation
============
``LSHash`` depends on the following libraries:

- numpy
- bitarray (if hamming distance is used as distance function)

Optional
- redis (if persistency through Redis is needed)

To install from sources:

.. code-block:: bash

    $ git clone https://github.com/loretoparisi/lshash.git
    $ python setup.py install
    
To install from PyPI:

.. code-block:: bash

    $ pip install lshashpy3
    $ python -c "import lshashpy3 as lshash; print(lshash.__version__);"

Quickstart
==========
To create 6-bit hashes for input data of 8 dimensions:

.. code-block:: python

 # create 6-bit hashes for input data of 8 dimensions:
 lsh = LSHash(6, 8)
 
 # index vector
 lsh.index([2,3,4,5,6,7,8,9])

 # index vector and extra data
 lsh.index([10,12,99,1,5,31,2,3], extra_data="vec1")
 lsh.index([10,11,94,1,4,31,2,3], extra_data="vec2")

 # query a data point
 top_n = 1
 nn = lsh.query([1,2,3,4,5,6,7,7], num_results=top_n, distance_func="euclidean")
 print(nn)

 # unpack vector, extra data and vectorial distance
 top_n = 3
 nn = lsh.query([10,12,99,1,5,30,1,1], num_results=top_n, distance_func="euclidean")
    for ((vec,extra_data),distance) in nn:
        print(vec, extra_data, distance)
        
        
To save hash table to disk:

.. code-block:: python

 lsh = LSHash(hash_size=k, input_dim=d, num_hashtables=L,
     storage_config={ 'dict': None },
     matrices_filename='weights.npz', 
     hashtable_filename='hash.npz', 
     overwrite=True)

 lsh.index([10,12,99,1,5,31,2,3], extra_data="vec1")
 lsh.index([10,11,94,1,4,31,2,3], extra_data="vec2")
 lsh.save()

To load hash table from disk and perform a query:

.. code-block:: python

 lsh = LSHash(hash_size=k, input_dim=d, num_hashtables=L,
     storage_config={ 'dict': None },
     matrices_filename='weights.npz', 
     hashtable_filename='hash.npz', 
     overwrite=True)

 top_n = 3
 nn = lsh.query([10,12,99,1,5,30,1,1], num_results=top_n, distance_func="euclidean")
 print(nn)

API
==============

- To initialize a ``LSHash`` instance:

.. code-block:: python

 k = 6 # hash size
 L = 5  # number of tables
 d = 8 # Dimension of Feature vector
 LSHash(hash_size=k, input_dim=d, num_hashtables=L,
    storage_config={ 'dict': None },
    matrices_filename='weights.npz', 
    hashtable_filename='hash.npz', 
    overwrite=True)

parameters:

``hash_size``:
    The length of the resulting binary hash.
``input_dim``:
    The dimension of the input vector.
``num_hashtables = 1``:
    (optional) The number of hash tables used for multiple lookups.
``storage = None``:
    (optional) Specify the name of the storage to be used for the index
    storage. Options include "redis".
``matrices_filename = None``:
    (optional) Specify the path to the .npz file random matrices are stored
    or to be stored if the file does not exist yet
``hashtable_filename = None``:
    (optional) Specify the path to the .npz file hash table are stored
    or to be stored if the file does not exist yet
``overwrite = False``:
    (optional) Whether to overwrite the matrices file if it already exist

- To index a data point of a given ``LSHash`` instance, e.g., ``lsh``:

.. code-block:: python

    lsh.index(input_point, extra_data=None):

parameters:

``input_point``:
    The input data point is an array or tuple of numbers of input_dim.
``extra_data = None``:
    (optional) Extra data to be added along with the input_point.

- To query a data point against a given ``LSHash`` instance, e.g., ``lsh``:

.. code-block:: python

    lsh.query(query_point, num_results=None, distance_func="euclidean"):

parameters:

``query_point``:
    The query data point is an array or tuple of numbers of input_dim.
``num_results = None``:
    (optional) The number of query results to return in ranked order. By
    default all results will be returned.
``distance_func = "euclidean"``:
    (optional) Distance function to use to rank the candidates. By default
    "euclidean" distance function will be used. Distance function can be 
    "euclidean", "true_euclidean", "centred_euclidean", "cosine", "l1norm".
    

- To save the hash table currently indexed:

.. code-block:: python

    lsh.save():
