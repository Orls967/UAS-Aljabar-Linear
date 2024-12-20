def gauss_jordan(A, B):
    n = len(B)
    for i in range(n):
        A[i].append(B[i])
    print("\nMatriks Awal:")
    tampilkan_matriks(A)
    for i in range(n):
        pivot = A[i][i]
        for j in range(len(A[i])):
            A[i][j] /= pivot
        print(f"\nSetelah membuat pivot di baris {i + 1}:")
        tampilkan_matriks(A)
        for k in range(n):
            if k != i:
                faktor = A[k][i]
                print(f"Baris ke-{k + 1} dikurangi {faktor:.3f} kali baris ke-{i + 1}:")
                for j in range(n + 1):
                    A[k][j] -= faktor * A[i][j]
                tampilkan_matriks(A)
    print("\nMatriks Hasil Akhir:")
    tampilkan_matriks(A)
    return [A[i][-1] for i in range(n)]
def tampilkan_matriks(matriks):
    for baris in matriks:
        print("\t".join(f"{nilai:.3f}" for nilai in baris))
    print()
def input_matriks():
    print("Matriks A (3x3):")
    A = [list(map(float, input().split())) for _ in range(3)]
    print("Matriks B (3x1):")
    B = [float(input()) for _ in range(3)]
    return A, B
A, B = input_matriks()
solusi = gauss_jordan(A, B)
X, Y, Z = solusi
print(f"X: {X:.3f}%")
print(f"Y: {Y:.3f}%")
print(f"Z: {Z:.3f}%")
print(f"Jadi kontribusi data piksel sebesar {X:.3f}%, kontribusi fitur tesktur sebesar {Y:.3f}%, dan kontribusi data warna sebesar {Z:.3f}%.")