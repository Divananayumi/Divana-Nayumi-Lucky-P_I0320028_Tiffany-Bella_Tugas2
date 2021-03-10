print("=====Program Menghitung Luas Persegi Panjang=====")
panjang = float(input("Masukkan panjang"))
lebar = float(input("Masukkan lebar"))
luas = panjang*lebar
print("Luas persegi panjang adalah", luas, "satuan")

print("=====Program Menghitung Luas Lingkaran=====")
phi = 3.14
jari_jari = float(input("Masukkan jari_jari"))
luas = phi*jari_jari*jari_jari
print("Luas lingkaran adalah", luas, "satuan")

print("=====Program Menghitung Luas Kubus=====")
sisi = float(input("Masukkan sisi"))
luas_permukaan = 6*sisi*sisi
print("Luas kubus adalah", luas_permukaan, "satuan")

print("=====Program Menghitung Konversi Suhu Celcius ke Farenheit=====")
celcius = float(input("Masukkan suhu celcius"))
konversi = ((9/5)*celcius)+32
print("Konversi suhu dari celcius ke farenheit adalah", konversi, "derajat")

print("=====Program Menghitung Konversi Suhu Reamur ke Kelvin=====")
reamur = float(input("Masukkan suhu reamur"))
konversi = ((5/4)*reamur)+273
print("Konversi suhu dari reamur ke kelvin adalah", konversi, "derajat")