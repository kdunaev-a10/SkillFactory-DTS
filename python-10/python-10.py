
import numpy as np

data = np.array([4, 9, -4, 3, -5])
roots = np.sqrt(data)
print(roots)
print(sum(roots))
print()

print(np.isnan(roots))
print(sum(np.isnan(roots)))
print()

print(roots[np.isnan(roots)])
roots[np.isnan(roots)] = 0
print(roots)
print(sum(roots))


simplelist = [19, 242, 14, 152, 142, 1000]
mystery = np.array(simplelist)
print(np.min(mystery))
print(np.mean(mystery))
print(np.median(mystery))
print(np.std(mystery))