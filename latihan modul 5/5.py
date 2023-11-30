import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Membuat sampel data dari distribusi normal
sample = np.random.normal(loc=50, scale=5, size=1000)

# Menampilkan histogram dari sampel data
plt.figure(figsize=(5,4))
plt.hist(sample, bins=10, density=True)
plt.show()

# Menghitung rata-rata dan standar deviasi dari sampels
sample_mean = np.mean(sample)
sample_std = np.std(sample)
print('Mean=%.3f \nStandart Deviation=%.3f' % (sample_mean, sample_std))

# Membuat distribusi normal baru dengan rata-rata dan standar deviasi dari sampel
dist = norm(sample_mean, sample_std)

# Menentukan nilai-nilai untuk distribusi probabilitas
values = np.arange(30, 70)
probabilities = [dist.pdf(value) for value in values]

# Menampilkan distribusi probabilitas dan histogram data sampel
plt.hist(sample, bins=10, density=True, alpha=0.7, label='Sample Data')
plt.plot(values, probabilities, label='Probability Distribution')
plt.legend()
plt.show()