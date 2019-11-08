# REF : https://stackoverflow.com/questions/9786102/how-do-i-parallelize-a-simple-python-loop

from joblib import Parallel, delayed
import multiprocessing
from timeit import default_timer as timer

inputs = range(10000000) 
def processInput(i):
    return i * i

num_cores = multiprocessing.cpu_count()

print("num_cores : {}".format(num_cores))


start = timer()
result2 = [processInput(i) for i in inputs]
end = timer()
print("normal code time in seconds: {}".format(end - start)) # Time in seconds, e.g. 5.38091952400282

start = timer()
results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)
end = timer()
print("joblib time in seconds: {}".format(end - start)) # Time in seconds, e.g. 5.38091952400282
