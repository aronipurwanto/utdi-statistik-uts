import sympy as sp

# Definisikan variabel simbolik
x = sp.symbols('x')

# Definisikan fungsi f(x)
f = sp.sin(x)**2

# Hitung deret Maclaurin dari f(x)
maclaurin_series = sp.series(f, x, 0, 6)
# 6 adalah ordo maksimum deret yang kita inginkan

# Cetak hasil deret Maclaurin
print(maclaurin_series)

