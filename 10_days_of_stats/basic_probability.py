import numpy as np

die=np.arange(1,6.1,1)

results=np.zeros((6,6))

results+=die

results+=results.T

prob=(results<=9.1).sum()/36.

print(prob)
