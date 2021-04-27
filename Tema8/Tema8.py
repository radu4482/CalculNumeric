import math
import random


def approximate_derivative(point, function, h=10 ** (-5)):
    return (3 * function(point) - 4 * function(point - h) + function(point - 2 * h)) / 2 * h


def approximate_derivative_2(point, function, h=10 ** (-5)):
    return (-1 * function(point + 2 * h) + 8 * function(point + h) - 8 * function(point - h) + function(
        point - 2 * h)) / 12 * h


def get_second_derivative(point, function, h=10 ** (-5)):
    return ((-1 * function(point + 2 * h)) + 16 * function(point + h) - 30 * function(point) + 16 * function(
        point - h) - function(point - 2 * h)) / 12 * h * h


def get_z(function, point):
    up = math.ceil(approximate_derivative_2(point, function, 10 ** (-5)))
    up = up * up
    g_k = approximate_derivative_2(point, function)
    down = approximate_derivative_2(point + g_k, function) - g_k

    return point + (up / down)


def get_delta(function, point):
    g_k = approximate_derivative_2(point, function)
    z = get_z(function, point)

    up = g_k * (approximate_derivative_2(z, function) - g_k)
    down = approximate_derivative_2(point + g_k, function) - g_k

    return up / down


def dehghan_hajarian(function, x_0, eps=10 ** (-12)):
    x_k = x_0
    g_k = approximate_derivative_2(x_k, function)
    print(g_k)
    down = approximate_derivative_2(x_k + g_k, function) - g_k
    print(down)
    delta_x = 0

    for i in range(0, int(10 ** 8)):
        if (abs(down) <= eps):
            return x_k
        delta_x = get_delta(function, x_k)
        print(delta_x)

        x_k = x_k - delta_x

        if (abs(delta_x) > 10 ** 8):
            break
        if (abs(delta_x) < eps):
            break

    if abs(delta_x) < eps:
        return x_k
    else:
        return "Divergent"



sin_f = lambda x: x * x + math.sin(x)
first_f = lambda x: 1 / 3 * math.pow(x, 3) - 2 * math.pow(x, 2) + 2 * x + 3
third_f = lambda x: math.pow(x, 4) - 6 * math.pow(x, 3) + 13 * math.pow(x, 2) + 4

x_0 = random.random() * random.randint(0, 100)
print(x_0)

sin_result = dehghan_hajarian(sin_f, x_0)
first_result = dehghan_hajarian(first_f, x_0)
third_result = dehghan_hajarian(third_f, x_0)

if(type(sin_result) != str):
    print(get_second_derivative(sin_result, sin_f) > 0)
if(type(first_result) != str):
    print(get_second_derivative(first_result, first_f) > 0)
if(type(third_result) != str):
     print(get_second_derivative(third_result, third_f) > 0)
