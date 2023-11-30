import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]

# Modifikasi dengan variasi baru:
plt.scatter(x, y, c='yellow', marker='o', s=100, alpha=0.8, edgecolors='orange', linewidths=1.5, label='(X, Y)')  # Menambahkan variasi warna, marker, ukuran marker, transparansi, warna tepi, dan ketebalan tepi
plt.title('Percobaan 4')  # Menambahkan judul
plt.xlabel('Nilai x')  # Menambahkan label sumbu x
plt.ylabel('Nilai y')  # Menambahkan label sumbu y
plt.legend()  # Menambahkan legenda

# Menampilkan plot
plt.show()