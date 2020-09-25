import time

def measure_func_execution_time(func):
    def wrapper():
        st = time.perf_counter()
        res = func()
        execution_time = time.perf_counter() - st
        print('execution_time >> ', execution_time)
        return res
    return wrapper

@measure_func_execution_time
def generate_huge_list():
    res = []
    for i in range(100000):
        res.append(i)
    return res

generate_huge_list()
