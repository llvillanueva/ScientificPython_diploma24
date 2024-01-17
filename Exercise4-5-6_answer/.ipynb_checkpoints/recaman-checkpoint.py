def recaman(N):
    a = []
    a.append(0)
    for n in range(1, N):
        if a[n-1] - n > 0 and (a[n-1] - n) not in a:
            a.append(a[n-1] - n)
        else:
            a.append(a[n-1] + n)
    return a

def recaman2(N):
    a = [0]
    b = {0}
    for n in range(1, N):
        if a[n-1] - n > 0 and (a[n-1] - n) not in b:
            a.append(a[n-1] - n)
            b.add(a[n-1] + n)
        else:
            a.append(a[n-1] + n)
            b.add(a[n-1] + n)
    return a

if __name__ == "__main__":
    print("Script is running directly")
    recaman(N)

if __name__ == "__main__":
    print("Script is running directly")
    recaman2(N)