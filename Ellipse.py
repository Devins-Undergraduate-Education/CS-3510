# NAME THE FILE Ellipse.py
import math
import random

def read_coefficients():
    coefficients = []
    for _ in range(6):
        line = input().strip()
        coefficients.append(float(line))
    return coefficients  # [A, B, C, D, E, F]

def find_center(A, B, C, D, E, F):
    # solve for the center (h, k) of the ellipse
    det = 4*A*C - B**2
    h = (B*E - 2*C*D) / det
    k = (B*D - 2*A*E) / det
    return h, k

def rotate_coefficients(A, B, C, D, E, F, h, k):
    # shift to center
    F_shifted = F + A*h**2 + B*h*k + C*k**2 + D*h + E*k
    # calculate rotation angle
    if B != 0:
        phi = 0.5 * math.atan2(B, A - C)
    else:
        phi = 0
    cos_phi = math.cos(phi)
    sin_phi = math.sin(phi)
    # rotate coefficients
    A_prime = A*cos_phi**2 + B*cos_phi*sin_phi + C*sin_phi**2
    C_prime = A*sin_phi**2 - B*cos_phi*sin_phi + C*cos_phi**2
    F_prime = F_shifted
    return A_prime, C_prime, F_prime, phi

def get_semi_axes(A_prime, C_prime, F_prime):
    # standard form: (x')^2/a^2 + (y')^2/b^2 = 1
    a = math.sqrt(-F_prime / A_prime)
    b = math.sqrt(-F_prime / C_prime)
    return a, b

def estimate_perimeter(a, b, N=1000000):
    total = 0.0
    for _ in range(N):
        theta = random.uniform(0, 2 * math.pi)
        dx = -a * math.sin(theta)
        dy = b * math.cos(theta)
        ds = math.hypot(dx, dy)
        total += ds
    average_ds = total / N
    perimeter = average_ds * (2 * math.pi)
    return perimeter

def main():
    A, B, C, D, E, F = read_coefficients()
    h, k = find_center(A, B, C, D, E, F)
    A_prime, C_prime, F_prime, phi = rotate_coefficients(A, B, C, D, E, F, h, k)
    a, b = get_semi_axes(A_prime, C_prime, F_prime)
    perimeter = estimate_perimeter(a, b)
    print(perimeter)

if __name__ == "__main__":
    main()