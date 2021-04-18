#include <cmath>
#include <iostream>
const int n = 3;

struct ArrayStruct {
    double mat[n][n]{};
    double vec[n][1]{};
};

ArrayStruct func(double x, double y, double z) {
    ArrayStruct funcVec{0};
    funcVec.vec[0][0] = x + y + z - 3;
    funcVec.vec[1][0] = x * x + y * y + z * z - 5;
    funcVec.vec[2][0] = std::exp(x) + x * y - x * z - 1;
    return funcVec;
}

ArrayStruct jacobian(double x, double y, double z) {
    ArrayStruct jacobMat{0};
    double J[n][n] = {{1, 1, 1},
                      {2 * x, 2 * y, 2 * z},
                      {std::exp(x) + y - z, x, -x}};

    for (int i{0}; i < n; i++) {
        for (int j{0}; j < n; j++) {
            jacobMat.mat[i][j] = J[i][j];
        }
    }
    return jacobMat;
}

ArrayStruct inverse(ArrayStruct matrix) {
    double augmentedMatrix[n][2 * n]{0};
    ArrayStruct inverseJacob{0};

    //Copying Jacobian matrix to the augmented matrix
    for (int i{0}; i < n; i++) {
        for (int j{0}; j < n; j++) {
            augmentedMatrix[i][j] = matrix.mat[i][j];
        }
    }

    // Creating an augmented matrix on n*2n size
    for (int i{0}; i < n; i++) {
        for (int j{0}; j < (2 * n); j++) {
            if (j == (i + n)) {
                augmentedMatrix[i][j] = 1;
            }
        }
    }

    // Interchanging rows for partial pivoting
    for (int i{n - 1}; i > 0; i--) {
        if (augmentedMatrix[i - 1][0] < augmentedMatrix[i][0]) {
            for (int j{0}; j < (2 * n); j++) {
                double d = augmentedMatrix[i][j];
                augmentedMatrix[i][j] = augmentedMatrix[i - 1][j];
                augmentedMatrix[i - 1][j] = d;
            }
        }
    }

    // Replace a row by sum of itself and a
    // constant multiple of another row of the matrix
    for (int i{0}; i < n; i++) {
        for (int j{0}; j < n; j++) {
            if (j != i) {
                double factor = augmentedMatrix[j][i] / augmentedMatrix[i][i];
                for (int k{0}; k < (2 * n); k++) {
                    augmentedMatrix[j][k] -= (augmentedMatrix[i][k] * factor);
                }
            }
        }
    }

    // Multiply each row by a nonzero integer.
    // Divide row element by the diagonal element
    for (int i{0}; i < n; i++) {
        double alpha = augmentedMatrix[i][i];
        for (int j{0}; j < (2 * n); j++) {
            augmentedMatrix[i][j] /= alpha;
        }
    }

    //Slicing the augmented Matrix to recover inverse matrix
    for (int i{0}; i < n; i++) {
        for (int j{n}; j < (2 * n); j++) {
            inverseJacob.mat[i][j - n] = augmentedMatrix[i][j];
        }
    }
    return inverseJacob;
}

int main() {
    double x{};
    double y{};
    double z{};

    ArrayStruct J_inverse{};
    ArrayStruct function{};

    std::cout << "Enter initial values of x,y,z in order" << '\n';
    std::cin >> x;
    std::cin >> y;
    std::cin >> z;

    for (int iter{0}; iter < 20; iter++) {
        function = func(x, y, z);                //Calculates function vector
        J_inverse = inverse(jacobian(x, y, z));  // Calulates inverse of Jacobian
        double J_inv_func[n][1]{0};

        //Multiply J_inverse matrix with function vector to get vector
        for (int i{0}; i < n; i++) {
            for (int j{0}; j < n; j++) {
                J_inv_func[i][0] += J_inverse.mat[i][j] * function.vec[j][0];
            }
        }

        //Updating the values
        x -= J_inv_func[0][0];
        y -= J_inv_func[1][0];
        z -= J_inv_func[2][0];

        // std::cout << x << ' ' << y << ' ' << z << '\n';
    }

    std::cout << "The solution of system of non linear equation is as follows " << '\n';
    std::cout << "x: " << x << '\n';
    std::cout << "y: " << y << '\n';
    std::cout << "z: " << z << '\n';

    return 0;
}
