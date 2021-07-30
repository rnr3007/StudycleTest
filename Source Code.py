Input_Data = []

# Fungsi untuk input secara khusus nilai integer
def Data_Int():
    while True:
        # Jika input int maka loop akan berhenti
        try:
            Integer = int(input("Masukkan angka:"))
            break
        # Jika input bukan int maka akan kembali di-loop
        except ValueError:
            print("Ulangi lagi dengan memasukkan nilai integer\n")
    return(Integer)

# Fungsi untuk sortir data secara ascending
def Ascend_Sort(Data):
    # Untuk menyimpan data
    Data_Holder = 0
    for i in range(len(Data)-1):
        for i in range(len(Data)-1):
            # Jika present data lebih kecil dari next data maka ditukar posisinya
            if Data[i] > Data[i+1]:
                Data_Holder = Data[i]
                Data[i] = Data[i+1]
                Data[i+1] = Data_Holder
    return(Data)

# Fungsi untuk mencari nilai rerata
def Mean_Find(Data):
    # Mendefinisikan panjang data untuk menjadi penyebut
    Data_Length = len(Data)
    # Menjumlah nilai data yang diinputkan
    Total = 0
    for i in range(Data_Length):
        Total += Data[i]
    # Menghitung rata-rata
    Mean = Total/Data_Length
    return(Mean)

# Fungsi untuk mencari nilai tengah
def Median_Find(Data):
    # Urutkan dahulu data secara ascending
    Sorted_Data = Ascend_Sort(Data)
    # Pemilihan jika panjang data genap atau ganjil
    Odd_or_Even = len(Data)%2
    # Jika genap
    if Odd_or_Even == 0:
        Median = (Data[len(Data)//2]+Data[(len(Data)//2)-1])/2
    # Jika ganjil
    elif Odd_or_Even == 1:
        Median = Data[len(Data)//2]
    return(Median)

# Fungsi untuk mencari hasil product of sum dari array
def Product_of_Sum(Data):
    # Inisialisasi perkalian dengan nilai 1 dan bukan dengan 0 agar hasil
    # akhir tidak 0
    Product = 1
    # Mengalikan menggunakan loop
    for i in range(len(Data)):
        Product *= Data[i]
    return(Product)

# Fungsi untuk menjalankan program utama
def main():
    # Input banyaknya elemen yang akan diproses
    Element = Data_Int()
    print(f"Panjang input: {Element}\n")

    # Input data yang akan diproses
    for i in range(Element):
        Input_Data.append(Data_Int())
    print(f"\nData yang digunakan: {Input_Data}")

    # Cetak hasil
    print(f"Hasil sortir data secara ascending: {Ascend_Sort(Input_Data)}")
    print(f"Hasil mencari rerata dari data: {Mean_Find(Input_Data)}")
    print(f"Hasil mencari nilai tengah dari data: {Median_Find(Input_Data)}")
    print(f"Hasil mencari perkalian dari seluruh data: {Product_of_Sum(Input_Data)}")

    # Keluar dari program ketika tombol enter ditekan
    Out = input("Tekan [Enter] untuk mengakhiri program")

# Program main dijalankan
main()



