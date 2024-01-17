def check_empty_array(func):
    def wrapper(*args, **kwargs):
        if not args and not kwargs:
            return "Array is empty. Function not called."
        else:
            return func(*args, **kwargs)
    return wrapper

@check_empty_array
def array(arr):
    print("Array:", arr)