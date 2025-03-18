print("Wybierz algorytm sortowania: \n\n1. Shell Sort \n2. Merge Sort \n3. Heap Sort \n4. Quick Sort Rekurencyjny \n5. Quick Sort Iteracyjny\n")
algo = int(input("Wprowadź wybór (1-5): "))
while (not 1 <= algo <= 5):
    algo = int(input("Wprowadź wybór (1-5): "))
    print("Wybór nieprawidłowy, ponów wybór\n")
print()
print("Wybierz sposób wprowadzania danych: \n\n1. Ręcznie \n2. Generator\n")
typ = int(input("Wprowadź wybór (1, 2): "))
while (not 1 <= typ <= 2):
    print("Wybór nieprawidłowy, ponów wybór\n")

print("Wybrano:", algo, typ)

