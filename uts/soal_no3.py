import sympy as sp

# Definisikan variabel simbolik
x = sp.symbols('x')

# Definisikan fungsi f(x)
f = 1 / (4*x + 8)

# Hitung deret Taylor dari f(x) di sekitar a=2
taylor_series = sp.series(f, x, 2, 6)
# 6 adalah ordo maksimum deret yang kita inginkan

# Cetak hasil deret Taylor
print(taylor_series)

