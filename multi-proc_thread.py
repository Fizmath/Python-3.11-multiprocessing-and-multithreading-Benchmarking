from multiprocessing import Process
import threading
from time import time, sleep
import random
import sys
from functools import wraps
lock = threading.Lock()


def nested( MM : int) : 
    """
    generates two nested lists A  with random float elements and B with random int 

    does matrix multiplication A.B

    sums column elements 
    
    returns a one dimensional list 

    """
    dim = MM*MM

    arand =  [random.uniform(1,1000) for _ in range(dim)]
    A = list(map(lambda x: arand[MM*x:(x+1)*MM], range(MM)))

    brand  = list(random.sample(range(0, dim), dim))
    B = list(map(lambda x: brand[MM*x:(x+1)*MM], range(MM)))

    mult = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

    assert len(list(map(sum, zip(*mult)))) == MM



def madmatrix(MM):
    """
    prolongs the process by mutating the matrix by adding 100*100 elements in each consecutive loop
    """
    num_MM = 5
    for i in range(num_MM):
        lock.acquire()
        nested(MM)
        lock.release()
        print(f'Matrix size {MM*MM} .... done!')
        MM += 100
    pass    


final = [f'py{sys.version[0:6]}']

def timeit(func):
    @wraps(func)
    def call(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        total_time = end - start
        final.append(f'{func.__name__}{args} -> {total_time:.4f} s')
        print(final[-1])
        return result
    return call


@timeit
def NO_thread():
    """
    default matrix dimension  100*100 

    """
    madmatrix(100)


threads = []
@timeit
def Threads(iter):
    """
    iter :  the number of independent threads to  spawn
    """ 
    for _ in range(iter):
            H = threading.Thread(target=madmatrix, args=(100,))
            H.start()
            print(H)  
            threads.append(H)

    for _ in threads:
        _.join()


processes = []
@timeit
def Processes(iter): 
    """
    iter :  the number of independent processes to launch
    """ 
    for _ in range(iter):
            P = Process(target=madmatrix, args=(100,))
            P.start()
            print(P)
            processes.append(P)

    for _ in processes:
        _.join()


NO_thread()
sleep(0.1)

Threads(5)
sleep(0.1)

Processes(5)

print(final)
