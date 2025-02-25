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
    creation_time, addition_time = add_arrays(10 ** 6, generate_random_array_with_randint)
    return {
        "creation_time": creation_time,
        "addition_time": addition_time
    }
    
@app.get("/add-large-arrays-choices")
def add_large_arrays_choices():    
    creation_time, addition_time = add_arrays(10 ** 6, generate_random_array_with_choices)
    return {
        "creation_time": creation_time,
        "addition_time": addition_time
    }

def generate_random_array_with_randint(N):
    return [random.randint(0, 100) for _ in range(N)]

def generate_random_array_with_choices(N):
    return random.choices(range(101), k=N)

def add_arrays(N, generate_random_array):
    start_time = time.time()
    a = generate_random_array(N)
    b = generate_random_array(N)
    end_time = time.time()
    array_creation_time = end_time - start_time
    
    start_time = time.time()
    res = list(map(sum, zip(a, b)))
    end_time = time.time()
    addition_time = end_time - start_time
    
    return (array_creation_time, addition_time)