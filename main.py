from typing import Union
from fastapi import FastAPI
import time
import random
import numpy as np

app = FastAPI()

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

@app.get("/add-large-arrays")
def add_large_arrays():
    execution_time = add_arrays(10 ** 4, generate_random_array_with_randint)
    return {
        "execution_time": execution_time
    }
    
@app.get("/add-large-arrays-choices")
def add_large_arrays_choices():    
    execution_time = add_arrays(10 ** 4, generate_random_array_with_choices)
    return {
        "execution_time": execution_time
    }

def generate_random_array_with_randint(N):
    return [random.randint(0, 100) for _ in range(N)]

def generate_random_array_with_choices(N):
    return random.choices(range(101), k=N)

def add_arrays(N, generate_random_array):
    a = generate_random_array(N)
    b = generate_random_array(N)
    
    start_time = time.time()
    res = list(map(sum, zip(a, b)))
    end_time = time.time()
    
    return end_time - start_time