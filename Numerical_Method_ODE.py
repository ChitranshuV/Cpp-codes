import math


def function(x, y):
    return (-2*x-y)


def euler_explicit_1(x_0, y_0, x, h):
    n = int((x - x_0)//h + 1)
    y = y_0
    for i in range(1, n+1):
        del_y = h*function(x_0, y)
        y = y + del_y
        x_0 = x_0 + h
        print(f"y' = {function(x_0,y)}\nh*y' = {h*function(x_0,y)}")
        print(f"y for {i}th iteration with {round(x_0,3)} is {y}\n")
        print("=========================================")

    print("*** Euler Explicit Method ***")
    print("#############################################")


def euler_modified(x_0, y_0, x, h):
    n = int((x - x_0)//h + 1)
    y = y_0
    for i in range(1, n+1):
        y_p = y + h*function(x_0, y)
        initial_slope = function(x_0, y)
        final_slope = function(x_0+h, y_p)
        del_y = 0.5*h*(initial_slope + final_slope)
        y = y + del_y
        x_0 = x_0 + h

        print(
            f"Initial Slope= {initial_slope}\ny_predicted = {y_p}\nFinal Slope = {final_slope}")
        print(f"h*y'_avg = {del_y}")
        print(f"y for {i}th iteration with {round(x_0,3)} is {y}\n")
        print("=========================================")

    print("*** Euler Modified (Heun) Method ***")
    print("#############################################")

# Generic 2nd order Runge Kutta method with a=0.5, b=0.5, alpha=1, beta=1 denotes Euler Modified Method or Heun Method
# Another variation of Runge Kutta Method is explicit midpoint method


def rungeKutta_2(x_0, y_0, x, h, a=0.5, b=0.5, alpha=1, beta=1):
    n = int((x - x_0)//h + 1)
    y = y_0
    for i in range(1, n+1):
        k1 = h * function(x_0, y)
        # Generic method below is commented for now.
        # k2 = h * function(x_0 + alpha*h, y + beta*k1)
        # k_avg = a*k1 + b*k2
        # The below method is used by online solvers and is midpoint method
        k2 = h * function(x_0 + 0.5*h, y + 0.5*k1)
        k_avg = k2
        y = y + k_avg
        x_0 = x_0 + h

        print(f"h*k1 = {k1}\nh*k2 = {k2}")
        print(f"h*k_avg ={k_avg}")
        print(f"y for {i}th iteration with {round(x_0,3)} is {y}\n")
        print("=========================================")

    print("*** Runge Kutta 2nd order (midpoint method) ***")
    print("#############################################")


def rungeKutta_4(x_0, y_0, x, h):
    n = int((x - x_0)//h + 1)
    y = y_0
    for i in range(1, n+1):
        k1 = h * function(x_0, y)
        k2 = h * function(x_0 + 0.5*h, y + 0.5*k1)
        k3 = h * function(x_0 + 0.5*h, y + 0.5*k2)
        k4 = h * function(x_0 + h,     y + k3)
        k_avg = (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        y = y + k_avg
        x_0 = x_0 + h

        print(f"h*k1 = {k1}\nh*k2 = {k2}\nh*k3 = {k3}\nh*k4 = {k4}")
        print(f"h*k_avg ={k_avg}")
        print(f"y for {i}th iteration with {round(x_0,3)} is {y}\n")
        print("=========================================")

    print("*** Runge Kutta 4th order ***")
    print("#############################################")


def main():
    x_0 = 0
    y_0 = -1
    x = 0.6
    h = 0.1

    euler_explicit_1(x_0, y_0, x, h)
    #euler_modified(x_0, y_0, x, h)
    #rungeKutta_4(x_0, y_0, x, h)
    #rungeKutta_2(x_0, y_0, x, h)


if __name__ == "__main__":
    main()
