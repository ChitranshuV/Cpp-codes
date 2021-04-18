import math


def func1(x, y1, y2):
    return (3*y1 + 2*y2)


def func2(x, y1, y2):
    return (2*y1 + 3*y2)


def RK_ODE(x_0, y1_0, y2_0, x, h):
    n = int((x - x_0)//h + 1)
    y1 = y1_0
    y2 = y2_0
    for i in range(1, n+1):
        k11 = func1(x_0, y1, y2)
        k12 = func2(x_0, y1, y2)
        k21 = func1(x_0 + 0.5*h, y1 + 0.5*h*k11, y2 + 0.5*h*k12)
        k22 = func2(x_0 + 0.5*h, y1 + 0.5*h*k11, y2 + 0.5*h*k12)
        k31 = func1(x_0 + 0.5*h, y1 + 0.5*h*k21, y2 + 0.5*h*k22)
        k32 = func2(x_0 + 0.5*h, y1 + 0.5*h*k21, y2 + 0.5*h*k22)
        k41 = func1(x_0 + h, y1 + h*k31, y2 + h*k32)
        k42 = func2(x_0 + h, y1 + h*k31, y2 + h*k32)

        k1_avg = (h/6)*(k11 + 2*k21 + 2*k31 + k41)
        k2_avg = (h/6)*(k12 + 2*k22 + 2*k32 + k42)

        y1 = y1 + k1_avg
        y2 = y2 + k2_avg
        x_0 = x_0 + h
        print(f"The values of k's are {[k11,k12,k21,k22,k31,k32,k41,k42]}")
        print(f"The value of k1_avg = {k1_avg}\t k2_avg = {k2_avg}")
        print(
            f"For {i}th iteration with x = {round(x_0,3)},\t y1 = {y1},\t y2 = {y2}\n")
        print("=========================================")
    print("*** 4th order Runge Kutta with 2 ODEs ***")
    print("#############################################")


def main():
    x_0 = 0
    y1_0 = 1
    y2_0 = 0
    x = 0.3
    h = 0.1
    RK_ODE(x_0, y1_0, y2_0, x, h)


if __name__ == "__main__":
    main()
