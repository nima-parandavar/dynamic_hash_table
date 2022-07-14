# Dynamic Hash Table
### A linear dynamic hash table
### You can change hash function to any _'hash function'_:
----
### h(k) = h(k * k)
----
###    k = k1, k2, k3, k4, ….., kn
###    s = k1+ k2 + k3 + k4 +….+ kn
####    h(K)= s
####    Here,
####    __s__ is obtained by adding the parts of the key k
-----
###  h(K) = floor (M (kA mod 1))

####  Here,
####  M is the size of the hash table.
####  k is the key value.
####  A is a constant value
