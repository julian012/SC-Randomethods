import numpy as np


def mean_square_method(seed, k, limit):
    n = seed ** 2
    extension = len(str(int('9' * len(str(seed))) ** 2))
    middle = int(extension / 2)
    nums = []
    ri = []
    for x in range(limit):
        n = '0' * (extension - len(str(n))) + str(n)
        n = n[middle - k: middle + k]
        n = int(n)
        nums.append(n)
        ri.append(n / 10 ** (k * 2))
        n = n ** 2
    # for i in range(len(nums)):
    #     print(nums[i], ri[i])
    return ri


def linear_congruence_method(x0, k, c, g, limit):
    a = 1 + (2 * k)
    m = 2 ** g
    xi = ((a * x0) + c) % m
    nums = [xi]
    ri = [xi / (m - 1)]
    for i in range(limit - 1):
        xi = ((a * xi) + c) % m
        nums.append(xi)
        ri.append(xi / (m - 1))
    # for i in range(len(nums)):
    #     print(nums[i], ri[i])
    return ri


def multiplicative_congruence_method(x0, t, d, limit):
    a = (8 * t) + 3
    m = 2 ** d
    xi = (a * x0) % m
    nums = [xi]
    ri = [xi / (m - 1)]
    for i in range(limit - 1):
        xi = (a * xi) % m
        nums.append(xi)
        ri.append(xi / (m - 1))
    # for i in range(len(nums)):
    #     print(nums[i], ri[i])
    return ri


def normal_distribution_method(mu, sigma, limit):
    return list(np.random.normal(mu, sigma, limit))


def uniform_distribution_method(min, max, limit):
    return list(np.random.uniform(min, max, limit))

# multiplicative_congruence_method(5, 3, 10, 15)
# linear_congruence_method(1, 4, 6, 7, 15)
# mean_square_method(5325, 2, 15)
