# Numerical Methods
The following repository consists of various solvers which are helpful in optimization and solving ODE using numerical methods
- `Gauss-Elimination.cpp` is a C++ implementation of Gaussian Elimination for solving a system of linear equations. The program allows 2 ways to compute Forward Elimination. One is through 3 nested for loops for updating values of matrix. The second implementation uses outer product calculation for updating values. The program is made for matrix A of size n*n with entries as a(ij) = max(i,j) and the vector b is a unit vector of length n. The program is tested for multiple values of n and the results are written in a file.
- `non_linear_root.py` consists of solvers like Bisection method, RegulaFalsi Method and Newton Raphson method etc. to solve a non-linear algebraic equation.
- `Numerical_Method_ODE.py` consists of solvers like Runge-Kutta method, Midpoint Method, Huen Method, Euler Method to solve an ODE equation.
- `Newton_Raphson_system.cpp` is a C++ implementation for solving a system of Non-Linear Equation. One has to write Jacobian themselves in this program and recompile and run for other system of non-linear equation.
- `RK-4-ODE system.py` is an ODE system solver which uses order 4 Runge-Kutta Method. The program is only made for equation of the form : d(y1)/d(x) = f1(x,y1,y2) and d(y2)/d(x) = f2(x,y1,y2)
