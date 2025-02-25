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
    n = 10 ** 6
    a = [random.randint(1, 100) for _ in range(n)]
    b = [random.randint(1, 100) for _ in range(n)]
    
    start_time = time.time()
    result_1 = list(map(sum, zip(a, b)))
    end_time = time.time()
    
    n_a = np.random.randint(1, 100, size=n)
    n_b = np.random.randint(1, 100, size=n)
    
    n_start_time = time.time()
    result_2 = np.add(n_a, n_b)
    n_end_time = time.time()
    
    return {
        "list_comprehension": end_time - start_time,
        "numpy": n_end_time - n_start_time
    }
    
@app.get("/add-large-arrays-choices")
def add_large_arrays_choices():
    n = 10**6
    
    c_start_time = time.time()
    a = random.choices(range(101), k=n)
    b = random.choices(range(101), k=n)
    c_end_time = time.time()
    
    s_start_time = time.time()
    result = list(map(sum, zip(a, b)))
    s_end_time = time.time()
    
    return {
        "choice_time": c_end_time - c_start_time,
        "execution_time": s_end_time - s_start_time
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}