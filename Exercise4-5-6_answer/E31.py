import sympy as sp

def taylor(N):
    x=sp.symbols('x')
    a = sp.symbols('a')
    func = sp.sin(x)
    n = 0
    series = 0
    for n in range(N):
        series = series + sp.diff(func, x, n).subs(x,a)*(x-a)**n/sp.factorial(n)
    return series + sp.O(sp.Pow(x-a, N))

#need to update the code so that 'sp.Pow(x-a, N)' doesnt get evaluated

if __name__ == "__main__":
    print("Script is running directly")
    my_function()