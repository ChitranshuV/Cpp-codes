# Trigonometric solution for three real roots
# https://en.wikipedia.org/wiki/Cubic_equation#Trigonometric_and_hyperbolic_solutions
# we will reduce our cubic equation to depressed cubic and use François Viète formula to find the roots.
# This formula works only if all roots of the cubic equation are real.
import math


def depressed_cubic(a, b, c, d):
    p = (3*a*c - b**2)/(3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*d*a**2)/(27*a**3)
    return p, q


def viete_formula(p, q):
    assert (4*p**3 + 27*q**2) < 0, "This cubic equation has complex roots"
    assert p != 0

    d = {}
    for k in range(3):
        d["t_"+str(k)] = 2*math.sqrt(-p/3) * \
            math.cos(math.acos(3*q*math.sqrt(-3/p)/(2*p))/3 - (2*math.pi*k/3))
    return d


def main():
    print("Please enter the coefficients for cubic equation of form ax^3 + bx^2 + cx + d = 0.")
    a = float(input("Enter coefficient a= "))
    b = float(input("Enter coefficient b= "))
    c = float(input("Enter coefficient c= "))
    d = float(input("Enter coefficient d= "))
    x = []
    p, q = depressed_cubic(a, b, c, d)
    t = viete_formula(p, q)
    for i in t:
        x.append(t[i] - (b/3*a))
    print(
        f"The 3 real roots of this cubic equation are {x[0]} \t {x[1]} \t {x[2]}")


if __name__ == "__main__":
    main()
