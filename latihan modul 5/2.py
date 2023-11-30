import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array([1, 8, 10])
ypoints = np.array([3, 10, 5])

# Menambah variasi:
plt.figure(figsize=(8, 6))  # Menambahkan ukuran figur yang lebih besar
plt.plot(xpoints, ypoints, color='red', marker='o', linestyle='-', linewidth=2, markersize=8)  # Menambahkan marker, corak, lebar garis, dan ukuran marker
plt.xlim([0, 12])  # Mengubah batas sumbu x
plt.ylim([0, 12])  # Mengubah batas sumbu y
plt.title('Percobaan 2')  # Menambahkan judul
plt.xlabel('Nilai x')  # Menambahkan label sumbu x
plt.ylabel('Nilai y')  # Menambahkan label sumbu y
plt.grid(True, linestyle='--', alpha=0.7)  # Menambahkan grid dengan garis putus-putus dan transparansi

# Menampilkan plot
plt.show()