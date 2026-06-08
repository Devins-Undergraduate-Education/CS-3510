# NAME THE FILE Integral.py
import math
import random
# apparently, we can't import sys.... BOOOOOOOOOOOOOOO

def parse_bound(s, limit=10.0):
    if s == 'INF':
        return limit
    elif s == '-INF':
        return -limit
    else:
        return float(s)

def monte_carlo_integral(a, b, N=1000000):
    total = 0.0
    for _ in range(N):
        x = random.uniform(a, b)
        total += math.exp(-x**2)
    average = total / N
    return average * (b - a)

def main():
    limit = 10.0  # Approximation for infinity
    try:
        a_input = input().strip()
        b_input = input().strip()
    except EOFError:
        a_input = '-INF'
        b_input = 'INF'
        
    a = parse_bound(a_input, limit)
    b = parse_bound(b_input, limit)
        
    integral = monte_carlo_integral(a, b, N=1000000)
    
    print(f"{integral}")

if __name__ == "__main__":
    main()