import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime

# Nama file Excel dan sheet yang ingin dibaca
excel_file = 'data.xlsx'
sheet_name = 'Electric_Production'


# Fungsi untuk membaca data dari file Excel dengan validasi nama sheet
def read_excel_with_validation(excel_file, sheet_name):
    # Baca semua sheet names dalam file Excel
    sheet_names = pd.ExcelFile(excel_file).sheet_names

    # Periksa apakah sheet_name ada dalam sheet_names
    if sheet_name not in sheet_names:
        raise ValueError(f"Sheet '{sheet_name}' tidak ditemukan dalam file '{excel_file}'.")

    # Baca data dari sheet yang valid
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    return df


# Baca data dari file Excel dengan validasi
df = read_excel_with_validation(excel_file, sheet_name)

# Konversi kolom tanggal menjadi datetime
df['date'] = pd.to_datetime(df['date'])

# Set kolom tanggal sebagai index
df.set_index('date', inplace=True)

# Plot data untuk visualisasi awal
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['elektrik_production'], label='Elektrik Production')
plt.xlabel('Date')
plt.ylabel('Elektrik Production')
plt.title('Time Series of Elektrik Production')
plt.legend()
plt.show()

# Tentukan order ARIMA model (p, d, q)
# Dalam prakteknya, Anda harus menentukan p, d, q berdasarkan ACF, PACF, atau kriteria lainnya
p, d, q = 1, 1, 1

# Fit model ARIMA
model = ARIMA(df['elektrik_production'], order=(p, d, q))
model_fit = model.fit()

# Output summary dari model ARIMA
print(model_fit.summary())

# Prediksi menggunakan model ARIMA
df['forecast'] = model_fit.predict(start=0, end=len(df) - 1, typ='levels')

# Plot hasil prediksi
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['elektrik_production'], label='Actual')
plt.plot(df.index, df['forecast'], label='Forecast', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Elektrik Production')
plt.title('ARIMA Model Fit')
plt.legend()
plt.show()

# Ekstrak persamaan model
ar_params = model_fit.arparams
ma_params = model_fit.maparams
intercept = model_fit.params.get('const', 0)

print(f'AR Parameters: {ar_params}')
print(f'MA Parameters: {ma_params}')
print(f'Intercept: {intercept}')
