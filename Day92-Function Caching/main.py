#Function caching is a technique for improving the performance of a program by storing the results of a function call so that you can reuse the results instead of recomputing them every time the function is called. 
#program maintains a cache
import functools
import time

@functools.lru_cache(maxsize=None) 
#if using lru_cache the output will be memoize which means store result so that it can be subsequesntly retrieved without repeating the computation.
def fx(n):
    time.sleep(2)
    return n*5
#lru_cache is also taking memory -> the cache is maintained in a single run of a program at that instant
#only throughout the program running time the lru_cache is maintained

print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")

print("-------------------------")

print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")
#use caching if only you know there are small number of data requests.
#dont use when you know the same values wont repeat everytime as the cache may take unwanted memory locations.


