# College Algebra course with Python
import sympy
from sympy import symbols
from sympy.solvers import solve


n1 = 3
d1 = 2
n2 = 0
d2 = 16

def cross_multiply():
    if n2 == 0:
        answer = d2 * n1 / d1
        print(answer)
    if d2 == 0:
        answer = n2 * d1 / n1
        print(answer)
cross_multiply()


mixedNum = 1 + 2 / 3
mixedNum_2 = 3 + 4 / 5
num = 7
print(mixedNum + mixedNum_2 - 7)

# Solve for X, inverse the operation to cancel it out. Apply to both sides to make equal
# Equations with sympy
# x = symbols('x')
# eq = 2*x - 4
# print(solve(eq,x))

# Multiple Solutions
x = symbols('x')
eq = 2*x - 4
solution = solve(eq,x)
for s in solution:
    print("x = ", s)
