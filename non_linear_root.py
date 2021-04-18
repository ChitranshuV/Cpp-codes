import math
epsilon = 0.000001


def function(x):
    return (x**3 - 3*x**2 + x - 3)


def derivative_f(x):
    return(3*x**2 - 6*x + 1)


def rootExistence(a, b):
    if ((function(a) * function(b)) <= 0):
        return 1
    elif ((function(a) * function(b)) > 0):
        return 0


def bisectionMethod(a, b):
    assert (rootExistence(a, b) == 1)
    step = 1
    while abs(b-a) > epsilon:
        m = (a + b)/2
        print(f"Iteration={step},\t x = {m},\t f(x) = {function(m)}")
        if function(m) == 0:
            break
        if (rootExistence(a, m)):
            b = m
        elif (rootExistence(b, m)):
            a = m
        step += 1
    print(f"The value of root by Bisection Method is = {m}")


def regulaFalsiMethod(a, b):
    assert (rootExistence(a, b) == 1)
    step = 1
    condition = True
    while condition:
        m = (a*function(b) - b*function(a))/(function(b) - function(a))
        f_m = function(m)
        print(
            f"Iteration={step},\t a = {a},\t b = {b},\t x = {m},\t f(x) = {f_m}")
        if f_m == 0:
            break
        if (rootExistence(a, m)):
            b = m
        elif (rootExistence(b, m)):
            a = m
        step += 1
        condition = abs(f_m) > epsilon
    print(f"The value of root by Regular Falsi method is = {m}")


def secantMethod(a, b, N=50):
    step = 1
    condition = True
    while condition:
        assert(function(a) != function(b))
        m = a - (b-a)*function(a)/(function(b)-function(a))
        f_m = function(m)
        print(f"Iteration={step},\t x = {m},\t f(x) = {f_m}")
        a = b
        b = m
        step += 1

        if step > N:
            print("Not convergent")
            break
        condition = abs(f_m) > epsilon
    print(f"The value of root by Secant method is = {m}")


def newtonRaphson(x, N=50):
    h = function(x) / derivative_f(x)
    step = 1
    while (abs(h) >= epsilon):
        h = function(x) / derivative_f(x)
        x -= h
        print(
            f"Iteration={step},\t x = {x},\t f(x) = {function(x)},\t Error = {abs(h)}")
        step += 1
        if step > N:
            print("Not convergent")
            break
    print(f"The value of root by Newton Raphson Method is {x}")


def main():
    regulaFalsiMethod(0, 3.6)
    # newtonRaphson(3.6)


if __name__ == "__main__":
    main()
