# CMO Assignment
# Submitted By: Rohit Kumar
# M.Tech(A.I.)-20963
print("\n-----------CMO Assignment:01------------\n")

# importing libraries
import numpy as np
import subprocess


def grad_f(a):
    g = np.array([-4 * a[0] + a[1] ** 2 + 16 * a[0] ** 3, 2 * a[0] * a[1]])
    return g


def calc(x):
    someVar = subprocess.run([".\getGradients_windows", f"20963,{x}"], stdout=subprocess.PIPE).stdout.decode("utf-8")
    someVar = someVar.split(",")
    func = float(someVar[0])
    grad_func = float(someVar[1])
    return func, grad_func


def bract_t(xc, f0, grad_f0):
    i = 0
    u = -grad_f0
    t = 1
    e = 10 ** (-3)

    while i < maxIterations:
        f1, grad_f1 = calc(xc + t * u)
        if f1 <= f0 + alpha * t * grad_f0 * u:  # for single variable grad_f.T=grad_f
            return xc + t * u
        elif abs(t * u) < e:
            return xc + t * u

        t = beta * t
        i = i + 1
    else:
        return xc + t * u


def q_3b():
    print("\033[92m          ::Question No.:3b::          \n")

    testData = [[0.7, 0.005], [0.3, 0.005], [-0.1, 0.005], [-0.7, 0.005]]

    for i in range(4):
        error = float('inf')
        k = 0
        x_k = np.array(testData[i])
        x_kp = float('inf')
        while error > 10 ** (-10):
            x_kp = x_k - (0.1 / (k + 1)) * grad_f(x_k)
            error = (sum((x_kp - x_k) ** 2)) ** 0.5
            x_k = x_kp
            k += 1
        print(f"\033[93mFor x0 = {testData[i]}, K value = {k}")


def q_4a():
    print("\033[92m        ::Question No.:4a(i)::          ")
    e = 10 ** (-3)
    maxIterations = 30
    x0 = 1.0
    f, grad_f = calc(x0)
    x = x0
    k = 1

    while k <= maxIterations:
        xp = bract_t(x, f, grad_f)
        fp, grad_fp = calc(xp)

        if abs(grad_fp) < e:
            break

        if k == 1 or k == 10 or k == 20:
            print(f"\033[93mValue of f(x) at iter no.{k}= {fp}")

        x = xp
        f = fp
        grad_f = grad_fp
        k += 1

    if k < 10:
        print(f"\033[93m\nvaue of f(x) at iter no.10= -1")
    if k < 10:
        print(f"\033[93m\nvaue of f(x) at iter no.20= -1")

    print("\033[92m\n        ::Question No.:4a(ii)::          ")
    print("\033[00m           -:Final Output:-         ")
    print(f"\033[93mx = {x}")
    print(f"f(x) = {f}")
    print(f"grad f(x) = {grad_f}")

def q_4b():
    print("\033[92m        ::Question No.:4b(i)::          \n")
    gamma = 0.25
    etta = 0.5
    e = 10 ** (-3)
    x0 = 1.0

    fk, grad_fk = calc(x0)
    xk = x0
    xk_m = x0
    k = 1
    counter = 0

    while (k == 1):
        xp = xk - gamma * grad_fk + etta * (xk - xk_m)
        fp, grad_fp = calc(xp)

        if counter == 1 or counter == 3 or counter == 5:
            print(f"\033[93mValue of f(x) at iter no.{counter}= {fk}")
        xk_m = xk
        xk = xp
        fk = fp
        grad_fk = grad_fp
        counter += 1

        if abs(grad_fp) < e:
            break

    if counter < 10:
        print(f"\n\033[93mvaue of f(x) at iter no.3= -1")
    if counter < 10:
        print(f"\n\033[93mvaue of f(x) at iter no.5= -1")

    print("\n\n\033[92m        ::Question No.:4b(ii)::         ")
    print("\033[00m           -:Final Output:-         ")
    print(f"\033[93mx = {xk}")
    print(f",f(x) = {fk}")
    print(f"grad f(x) = {grad_fk}")


if __name__ == '__main__':
    alpha = 0.5
    beta = 0.1
    maxIterations = 30
    while (1):
        userInput = int(input("\033[94mChoose your question:\n"
                              "Press 1 for Qn.3b\n"
                              "Press 2 for Qn.4a\n"
                              "Press 3 for Qn.4b\n"
                              "Press 0 for exit\n"))

        if userInput == 1:
            q_3b()

        elif userInput == 2:
            q_4a()

        elif userInput == 3:
            q_4b()

        elif userInput == 0:
            break

        else:
            print("\033[00mPlease provide correct input :(\n")
            continue

print("Program ended!!!")

