import numpy as np
import matplotlib.pyplot as plt

n = 1000
p_edge = 0.8
p_sample = 0.5
num_samples = 10000000

A = np.zeros((n, n))
for i in range(n):
    for j in range(i + 1, n):
        if np.random.rand() < p_edge:
            A[i, j] = 1
            A[j, i] = 1

counts = np.zeros(num_samples)
for t in range(num_samples):
    u = (np.random.rand(n) < p_sample)
    counts[t] = int(u @ A @ u) // 2

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

axes[0].hist(counts, bins=600, color='#1b365d')
axes[0].set_title("large scale")
axes[0].set_xlabel("e(U)")
axes[0].set_ylabel("count")

lo = int(counts.mean()) - 2500
hi = int(counts.mean()) + 2500
window = (counts >= lo) & (counts <= hi)
axes[1].hist(counts[window], bins=np.arange(lo, hi + 1), color='#1b365d')
axes[1].set_title("small scale")
axes[1].set_xlabel("e(U)")
axes[1].set_ylabel("count")
axes[1].margins(x=0)

plt.tight_layout()
plt.savefig("figures/two-scale.png", dpi=150)