import matplotlib.pyplot as plt
import numpy as np

def I(n):
	return 4*2**(n-1)

nmax = 50

n = np.arange(1,nmax+1)

bytes_per_kB = np.full(n.size,1024)
bytes_per_MB = bytes_per_kB * 1024
bytes_per_GB = bytes_per_MB * 1024
bytes_per_TB = bytes_per_GB * 1024
bytes_per_PB = bytes_per_TB * 1024
bytes_per_EB = bytes_per_PB * 1024

plt.semilogy(n,I(n),label='I(n)')
plt.semilogy(n,bytes_per_kB,'b-.',label='1 kB')
plt.semilogy(n,bytes_per_MB,'r-.',label='1 MB')
plt.semilogy(n,bytes_per_GB,'g-.',label='1 GB')
plt.semilogy(n,bytes_per_TB,'y-.',label='1 TB')
plt.semilogy(n,bytes_per_PB,'m-.',label='1 PB')
plt.semilogy(n,bytes_per_EB,'c-.',label='1 EB')

plt.xlabel('n')
plt.ylabel('number of Bytes')
plt.title('Memory Required for a Brute-force Solution of Leetcode 779')

plt.xlim(1,50)

xmarks = [1,10,20,30,40,50]

plt.xticks(xmarks)

plt.legend()

plt.show()
