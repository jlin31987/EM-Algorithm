import numpy as np

x = np.array([6.6123, 18.6543, 11.351, 8.7254, 6.9369, 8.7147, 14.0346, 13.7268, 11.6965, 15.7425])

mu1, mu2 = 6, 10

iterations = 2
sigma = 1

for iteration in range(iterations):
    numerator1 = (1 / np.sqrt(2 * np.pi * sigma**2)) * np.exp(-0.5 * ((x - mu1)**2) / sigma**2)
    numerator2 = (1 / np.sqrt(2 * np.pi * sigma**2)) * np.exp(-0.5 * ((x - mu2)**2) / sigma**2)
    denominator = numerator1 + numerator2

    w1 = numerator1 / denominator
    w2 = numerator2 / denominator

    mu1 = np.sum(w1 * x) / np.sum(w1)
    mu2 = np.sum(w2 * x) / np.sum(w2)

    print(f"Iteration {iteration + 1}:")
    print(f"  Estimated Mean 1: {mu1}")
    print(f"  Estimated Mean 2: {mu2}")


