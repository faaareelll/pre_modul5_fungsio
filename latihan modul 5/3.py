import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([4, 5, 9, 2])  # Garis ketiga

# Membuat plot untuk garis y1, y2, dan y3 dengan warna dan corak yang berbeda
plt.plot(y1, label='Garis 1', color='blue', linestyle='dashed', marker='o')
plt.plot(y2, label='Garis 2', color='green', linestyle='dotted', marker='s')
plt.plot(y3, label='Garis 3', color='purple', linestyle='dashdot', marker='^')

# Menambahkan judul dan label sumbu
plt.title('Percobaan 3')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

# Menambahkan keterangan (legend)
plt.legend()

# Menampilkan plot
plt.show()