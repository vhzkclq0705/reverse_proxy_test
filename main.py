from typing import Union
from fastapi import FastAPI
import time
import random
import numpy as np

app = FastAPI()
n = 10 ** 5

@app.get("/")
def read_root():
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    result = list(map(sum, zip(a, b)))
    return {"Hello": result}

@app.get("/two-dimensional-array")
def two_dimensional_array():
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    b = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    result = [list(map(sum, zip(a[i], b[i]))) for i in range(len(a))]
    
    return {"result": result}

@app.get("/add-large-arrays-numpy")
def add_large_arrays_numpy():
    creation_time, execution_time = add_arrays(n, generate_random_array_with_numpy_randint, True)
    return {
        "creation_time": creation_time,
        "execution_time": execution_time
    }

@app.get("/add-large-arrays")
def add_large_arrays():
    creation_time, execution_time = add_arrays(n, generate_random_array_with_randint, False)
    return {
        "creation_time": creation_time,
        "execution_time": execution_time
    }
    
@app.get("/add-large-arrays-choices")
def add_large_arrays_choices():    
    creation_time, execution_time = add_arrays(n, generate_random_array_with_choices, False)
    return {
        "creation_time": creation_time,
        "execution_time": execution_time
    }
    
def generate_random_array_with_numpy_randint(N):
    return np.random.randint(1, 101, size=N)

def generate_random_array_with_randint(N):
    return [random.randint(0, 100) for _ in range(N)]

def generate_random_array_with_choices(N):
    return random.choices(range(101), k=N)

def add_arrays(N, generate_random_array, is_numpy):
    c_start_time = time.time()
    a = generate_random_array(N)
    b = generate_random_array(N)
    c_end_time = time.time()
    
    e_start_time = time.time()
    res = a + b if is_numpy else list(map(sum, zip(a, b)))
    e_end_time = time.time()
    
    return c_end_time - c_start_time, e_end_time - e_start_time