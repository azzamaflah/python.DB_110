import tkinter as tk
import sqlite3

def prediksi_prodi():
    nilai_biologi = int(biologi_entry.get())
    nilai_fisika = int(fisika_entry.get())
    nilai_inggris = int(inggris_entry.get())

    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        hasil_prediksi = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        hasil_prediksi = "Teknik"
    else:
        hasil_prediksi = "Bahasa"

    hasil_prediksi_siswa.config(text=f"Hasil Prediksi: {hasil_prediksi}")

def submit_nilai_siswa():
    nama_siswa = nama_siswa_entry.get()
    nilai_biologi = int(biologi_entry.get())
    nilai_fisika = int(fisika_entry.get())
    nilai_inggris = int(inggris_entry.get())

    # Menyimpan data ke database SQLite
    simpan_data_ke_database(nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris)

    prediksi_prodi()

def simpan_data_ke_database(nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris):
    connection = sqlite3.connect('data_siswa.db')
    cursor = connection.cursor()

    # Membuat tabel jika belum ada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            nilai_biologi INTEGER,
            nilai_fisika INTEGER,
            nilai_inggris INTEGER
        )
    ''')

    # Menyimpan data nilai siswa ke database
    cursor.execute('INSERT INTO nilai_siswa (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris) VALUES (?, ?, ?, ?)',
                   (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris))

    # Commit dan menutup koneksi
    connection.commit()
    connection.close()

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

# Menambahkan entry untuk input nilai siswa
nama_siswa_label = tk.Label(root, text="Nama Siswa:")
nama_siswa_label.grid(row=0, column=0, padx=10, pady=5)

nama_siswa_entry = tk.Entry(root)
nama_siswa_entry.grid(row=0, column=1, padx=10, pady=5)

biologi_label = tk.Label(root, text="Nilai Biologi:")
biologi_label.grid(row=1, column=0, padx=10, pady=5)

biologi_entry = tk.Entry(root)
biologi_entry.grid(row=1, column=1, padx=10, pady=5)

fisika_label = tk.Label(root, text="Nilai Fisika:")
fisika_label.grid(row=2, column=0, padx=10, pady=5)

fisika_entry = tk.Entry(root)
fisika_entry.grid(row=2, column=1, padx=10, pady=5)

inggris_label = tk.Label(root, text="Nilai Inggris:")
inggris_label.grid(row=3, column=0, padx=10, pady=5)

inggris_entry = tk.Entry(root)
inggris_entry.grid(row=3, column=1, padx=10, pady=5)

# Menambahkan tombol untuk submit nilai siswa
button_submit = tk.Button(root, text="Submit Nilai Siswa", command=submit_nilai_siswa)
button_submit.grid(row=4, column=0, columnspan=2, pady=10)

# Menambahkan label hasil prediksi siswa
hasil_prediksi_siswa = tk.Label(root, text="Hasil Prediksi: ")
hasil_prediksi_siswa.grid(row=5, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()
