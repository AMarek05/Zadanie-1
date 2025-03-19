import random
import time

def manual():
    # Zwraca listę (n <= 10) wprowadzonych liczb całkowitych
    nums = []
    done = False
    for i in range(10):
        while not done:
            wpr = input(f"Wprowadź element {i + 1} lub \'x\' by zakończyć wprowadzanie: ")
            if wpr == 'x':
                if len(nums) == 0:
                    print("Nie wprowadzono żadnych liczb. Proszę ponowić próbę.")
                else:
                    done = True
            else:
                try:
                    wpr = int(wpr)
                    nums.append(wpr)
                    break
                except ValueError:
                    print("Nie wprowadzono liczby całkowitej lub \'x\'. Proszę ponowić próbę.")
            print()
        if done:
            break
    return nums

def losowa(n):
    return [random.randint(1, 10 * n) for _ in range(n)]

def gen(algo):
    # Wyprowadza 10 posortowanych tablic w.g zaleceń
    n = int(input("Wprowadź n -- Liczbę elementów w każdej tablicy: "))
    match wyb_los():
        case 1:
            for i in range(10):
                print(f"{i}.")
                posort(algo, losowa(n))
        case 2:
            for i in range(10):
                print(f"{i}.")
                posort(algo, sorted(losowa(n)))
        case 3:
            for i in range(10):
                print(f"{i}.")
                posort(algo, sorted(losowa(n), reverse=True))
        case 4:
            for i in range(10):
                print(f"{i}.")
                lista = losowa(n)
                lista = sorted(lista)

                środ = len(lista) // 2
                l = lista[:środ]
                p = lista[środ:]

                p.reverse()
                tab = l + p
                posort(algo, tab)
        case 5:
            for i in range(10):
                print(f"{i}.")
                lista = losowa(n)
                lista = sorted(lista)

                środ = (len(lista) - 1) // 2
                l = lista[:środ + 1][::-1]
                p = lista[środ + 1:]

                tab = l + p
                posort(algo, tab)
    print()
    global czasy
    print(f"Średnia wyniosła {round(sum(czasy)/len(czasy), 5)} milisekund")

def wyb_los():
    print("Wybierz ułożenie: \n\n1. Losowe \n2. Rosnące \n3. Malejące \n4. A-kształtne \n5. V-kształtne\n")
    while True:
        try:
            los = int(input("Wprowadź wybór (1-5): "))
            if not 1 <= los <= 5:
                print("Wybór nieprawidłowy, ponów wybór\n")
            else:
                return los
        except ValueError:
            print("Nie wprowadzono liczby całkowitej, ponów próbę")

def wyb_algo():
    # Podaje odpowiedni typ algorytmu (1-5)
    print("Wybierz algorytm sortowania: \n\n1. Shell Sort \n2. Merge Sort \n3. Heap Sort \n4. Quick Sort Rekurencyjny \n5. Quick Sort Iteracyjny\n")
    while True:
        try:
            algo = int(input("Wprowadź wybór (1-5): "))
            if not 1 <= algo <= 5:
                print("Wybór nieprawidłowy, ponów wybór\n")
            else:
                return algo
        except ValueError:
            print("Nie wprowadzono liczby całkowitej, ponów próbę")

def wyb_met():
    print("Wybierz sposób wprowadzania danych: \n\n1. Ręcznie \n2. Generator\n")
    while True:
        try:
            typ = int(input("Wprowadź wybór (1 - 2): "))
            if not 1 <= typ <= 2:
                print("Wybór nieprawidłowy, ponów wybór\n")
            else:
                return typ
        except ValueError:
            print("Nie wprowadzono liczby całkowitej, ponów próbę")

def insertion_sort_g(tab, gap):
    n = len(tab)
    for i in range(gap, n):
        temp = tab[i]
        j = i
        # Stosujemy insertion sort
        while j >= gap and tab[j - gap] < temp:
            tab[j] = tab[j - gap]
            j -= gap
        tab[j] = temp

def shell_sort(tab):
    n = len(tab)
    gaps = []
    k = 1
    while(2**k - 1) < n:
        gaps.append(2**k - 1)
        k += 1

    for gap in reversed(gaps):
        # Stosujemy odwrotne insertion sort
        print(f"Wartość przyrostu: {gap}")
        insertion_sort_g(tab, gap)
    return tab

def merge_sort(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        left = tab[:mid]
        right = tab[mid:]

        merge_sort(left)
        merge_sort(right)
        
        merge(tab, left, right)
    return tab

merge_count = 0
def merge(tab, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            tab[k] = left[i]
            i += 1
        else:
            tab[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        tab[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        tab[k] = right[j]
        j += 1
        k += 1

    global merge_count
    merge_count += 1

def heapify(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] < arr[smallest]:
        smallest = l

    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        # Najmniejszy na przód
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        # Elementy większe od pivota
        if arr[j] > pivot:
            i += 1
            # zamieniamy
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_rec(arr, low, high):
    if low < high:
        part = partition(arr, low, high)

        quick_sort_rec(arr, low, part - 1)
        quick_sort_rec(arr, part + 1, high)

def quick_sort_inter(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]
    while stack:
        p, r = stack.pop()

        if p < r:
            part = partition(arr, p, r)
            stack.append((p, part - 1))
            stack.append((part + 1, r))

    return arr
czasy = []
def posort(algo, tab):
    global merge_count, czasy
    merge_count = 0
    print()
    print("Wprowadzono:", *tab)
    sort = []
    start = time.time()

    match algo:
        case 1:
            sort = shell_sort(tab)
        case 2:
            sort = merge_sort(tab)
            print(f"Zcalono {merge_count} razy")
        case 3:
            sort = heap_sort(tab)
        case 4:
            quick_sort_rec(tab, 0, len(tab) - 1)
            sort = tab
        case 5:
            sort = quick_sort_inter(tab)
    stop = time.time()
    czas = (stop - start)*1000
    czasy.append(czas)
    print(f"Zliczono: {round(czas, 2)} milisekund.")
    print("Wyprowadzono:", *sort)
    print()

def main():
    algo = wyb_algo()
    metoda = wyb_met()
    tablica = []
    if metoda == 1:
        tablica = manual()
        posort(algo, tablica)
    else:
        gen(algo)

if __name__ == "__main__":
    main()
