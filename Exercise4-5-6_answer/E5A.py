import numpy as np

def plotter(func):
    def wrapper(*args, **kwargs):
        
        func(*args, **kwargs)
        end_time = time.time()        
        elapsed_time = end_time - start_time
        return f"Elapsed time: {elapsed_time} seconds"
    return wrapper

@plotter
def sin1(N):
    x = np.linspace(0,5,20)
    return np.sin(x)

def sin1(N):
    x = np.linspace(0,5,20)
    return np.sin(x)