import time
from functools import lru_cache
lru_cache(maxsize=32)
def some__work(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work ")
    some__work(3)
    some__work(1)
    some__work(6)
    some__work(2)
    print("Done... Calling again .")
    input()
    some__work(3)
    print("Called again")


