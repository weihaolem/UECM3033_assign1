import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans


def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate((x-x**2)**4/(1+x**2), (x,0,1))
    return ans


def my_solution():
    A = np.array( [[3,1,5,4,8,9,4,6,2,8], [1,2,8,7,1,6,2,5,4,9], 
                   [9,7,1,5,4,8,2,6,3,1], [4,3,5,6,7,2,8,4,5,7], 
                   [4,7,1,5,2,4,8,6,3,1], [3,4,8,5,7,1,2,2,4,1],
                   [1,7,4,6,10,15,4,8,3,1],[5,6,8,2,7,4,3,9,1,5],
                   [9,7,2,4,6,1,5,3,8,4],[6,4,7,5,8,3,2,1,5,4]] )
    b = np.array([2,5,6,4,5,8,1,2,5,6])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1302054
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
