class Person:
    """ Print the person full name and if he/she is an adult"""
    def __init__(self, fn, ln, age):
        self.fn = fn
        self.ln = ln
        self.age = age

    def full_name(self):
        return f"{self.fn} {self.ln}"

    def is_adult(self):
        return self.age >= 18
