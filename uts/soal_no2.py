import sympy as sp

# Definisikan variabel simbolik
n, x = sp.symbols('n x')

# Definisikan suku dari deret
a_n = (3**n * x**(n-1)) / (2*n**2 + 1)

# Hitung rasio a_(n+1) / a_n
a_n1 = (3**(n+1) * x**n) / (2*(n+1)**2 + 1)
ratio = sp.simplify(a_n1 / a_n)

# Hitung limit dari rasio saat n mendekati tak hingga
limit_ratio = sp.limit(ratio, n, sp.oo)

# Cetak hasil rasio dan limitnya
print(f"Rasio a_(n+1) / a_n: {ratio}")
print(f"Limit rasio saat n mendekati tak hingga: {limit_ratio}")

# Tentukan interval konvergensi berdasarkan limit rasio
interval_convergence = sp.solve(limit_ratio < 1, x)

# Cetak interval konvergensi
print(f"Interval konvergensi: {interval_convergence}")

