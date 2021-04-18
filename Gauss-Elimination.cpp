#include <fstream>
#include <iomanip>
#include <iostream>
#define N 32

/*
N = dimension of our square matrix =  {32, 128, 512, 1024}
Stack Overflows in the cases of bigger N (1024 for example).
Increase stack size of the OS or change compiler flags during compilation process to resolve this.
- For GCC:   ```-Wl,--stack,10485760``` this compiler flag changes stack size to 10MBs.
- For Linux: ```ulimit -s unlimited``` makes stack size unlimited for the current shell session
*/

void forwardElimination(double (&a)[N][N], double (&b)[N][1]) {
    //Creating temporary matrices to hold A and b values
    double a_t[N][N];
    std::copy(&a[0][0], &a[0][0] + N * N, &a_t[0][0]);  //copying a -> a_t
    double b_t[N][1];
    std::copy(&b[0][0], &b[0][0] + N * 1, &b_t[0][0]);  //copying b -> b_t

    int n{N};

    for (auto k{0}; k <= n - 2; ++k) {
        for (auto i{k + 1}; i <= n - 1; ++i) {
            for (auto j{0}; j <= n - 1; ++j) {
                auto factor{a_t[i][k] / a_t[k][k]};  //multiplication factor for elimination
                a[i][j] = a_t[i][j] - (factor * a_t[k][j]);
                b[i][0] = b_t[i][0] - (factor * b_t[k][0]);
            }
        }
        std::copy(&a[0][0], &a[0][0] + N * N, &a_t[0][0]);  //copying a -> a_t
        std::copy(&b[0][0], &b[0][0] + N * 1, &b_t[0][0]);  //copying b -> b_t
    }
}

void backwardSubstitution(double (&a)[N][N], double (&b)[N][1], double (&x)[N][1]) {
    x[N - 1][0] = b[N - 1][0] / a[N - 1][N - 1];  //Calculating the last element of x vector
    int n{N};
    for (auto i{n - 2}; i >= 0; --i) {
        double sum{0};
        for (auto j{n - 1}; j >= i + 1; --j) {
            sum += (a[i][j] * x[j][0]);
        }
        x[i][0] = (b[i][0] - sum) / a[i][i];
    }
}

double squareSum(double (&x)[N][1]) {
    double sq_sum{0};
    for (auto i{0}; i < N; ++i) {
        sq_sum += (x[i][0] * x[i][0]);  //Calculating sum of squares of elements of x vector
    }
    return sq_sum;
}

void writeToFile(double &sq_sum) {
    int n{N};
    std::ofstream output_file;
    output_file.open("result.dat", std::ios_base::app);  //opening file in append mode
    output_file << "n = " << n << '\t' << std::fixed << 1 / sq_sum << '\n';
    output_file.close();
}

void printMatrix(double arr[N][N]) {
    for (auto i{0}; i <= N - 1; ++i) {
        for (auto j{0}; j <= N - 1; ++j) {
            std::cout << arr[i][j] << " \n"[j == N - 1];
        }
    }
    std::cout << "---------------------------------\n";
}

void printVector(double vec[N][1]) {
    for (auto i{0}; i <= N - 1; ++i) {
        std::cout << vec[i][0] << ' ';
    }
    std::cout << "\n----------------------------------\n";
}

int main() {
    double a[N][N]{};  //Declaring a N*N array
    double b[N][1]{};  //Declaring a N*1 vector
    double x[N][1]{};  //Declaring x vector of the unknowns

    // Initializing both the arrays and vector
    // array a has elements aij as max(i,j), and b is a unit vector 
    for (auto i{0}; i <= N - 1; ++i) {
        for (auto j{0}; j <= N - 1; ++j) {
            a[i][j] = std::max(i + 1, j + 1);
            b[i][0] = 1;
        }
    }
    std::cout << "Initial Matrix A:\n";
    printMatrix(a);
    std::cout << "Initial Vector b:\n";
    printVector(b);
    printVector(x);

    forwardElimination(a, b);
    std::cout << "Matrix A after Forward Elimination:\n";
    printMatrix(a);
    std::cout << "Vector b after Forward Elimination:\n";
    printVector(b);

    backwardSubstitution(a, b, x);
    std::cout << "Vector x after Back Substitution:\n";
    printVector(x);

    double sq_sum{squareSum(x)};
    std::cout << "n = " << N << '\t' << "squared sum = " << sq_sum
              << '\t' << "Inverse squared sum: " << std::fixed << 1 / sq_sum << '\n';

    writeToFile(sq_sum);

    return 0;
}
