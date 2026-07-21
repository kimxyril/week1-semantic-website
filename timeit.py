import timeit
import matplotlib.pyplot as plt

# --- TASK 1: Big O Functions ---
def o1(n): return n*2                  # O(1)
def ologn(n):
    c=0
    while n>1: n//=2; c+=1; return c    # O(log n)
def on(n):
    c=0
    for _ in range(n): c+=1; return c   # O(n)
def onlogn(n):
    c=0
    for _ in range(n):
        t=n
        while t>1: t//=2; c+=1
    return c                            # O(n log n)
def on2(n):
    c=0
    for _ in range(n):
        for _ in range(n): c+=1
    return c                            # O(n²)

funcs = [("O(1)",o1), ("O(log n)",ologn), ("O(n)",on), ("O(n log n)",onlogn), ("O(n²)",on2)]

# --- TASK 2: Timeit ---
ns = [100,1000,10000]
times = {name:[] for name,_ in funcs}
for n in ns:
    print(f"\nn={n}")
    for name,f in funcs:
        t = timeit.timeit(lambda:f(n), number=5)/5
        times[name].append(round(t,8))
        print(f"{name:<12} {t:.8f}s")

# --- TASK 3: Plot ---
for name,t in times.items():
    plt.plot(ns,t,marker='o',label=name)
plt.xlabel("n");plt.ylabel("Time");plt.legend();plt.grid();plt.show()

# --- TASK 4: Optimize O(n²)→O(n) ---
def orig(arr):
    s=0
    for i in arr:
        for j in arr: s+=i+j
    return s
def opt(arr): return 2*len(arr)*sum(arr)

arr=list(range(200))
print(f"\nOrig: {orig(arr)} | Opt: {opt(arr)}")
print(f"Orig time: {timeit.timeit(lambda:orig(arr),number=10):.6f}s")
print(f"Opt time: {timeit.timeit(lambda:opt(arr),number=10):.6f}s")