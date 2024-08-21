import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

palavras = list()

with open('texto.txt', 'r') as arquivo:
    for linha in arquivo:
        palavras.extend(linha.split())

bubble_sort_palavras = palavras.copy()
inicio = time.time()
bubble_sort(bubble_sort_palavras)
fim = time.time()
tempo_bubble_sort = fim - inicio

selection_sort_palavras = palavras.copy()
inicio = time.time()
selection_sort(selection_sort_palavras)
fim = time.time()
tempo_selection_sort = fim - inicio

sort_palavras = palavras.copy()
inicio = time.time()
sort_palavras.sort()
fim = time.time()
tempo_sort = fim - inicio

print("Resultado da ordenação usando Bubble Sort:")
print(bubble_sort_palavras)
print(f"Tempo de execução: {tempo_bubble_sort:.6f} segundos\n")

print("Resultado da ordenação usando Selection Sort:")
print(selection_sort_palavras)
print(f"Tempo de execução: {tempo_selection_sort:.6f} segundos\n")

print("Resultado da ordenação usando o método nativo sort:")
print(sort_palavras)
print(f"Tempo de execução: {tempo_sort:.6f} segundos\n")

metodo_mais_eficiente = min(tempo_bubble_sort, tempo_selection_sort, tempo_sort)
if metodo_mais_eficiente == tempo_bubble_sort:
    palavras_ordenadas = bubble_sort_palavras
elif metodo_mais_eficiente == tempo_selection_sort:
    palavras_ordenadas = selection_sort_palavras
else:
    palavras_ordenadas = sort_palavras

with open('palavras_ordenadas.txt', 'w') as arquivo:
    for palavra in palavras_ordenadas:
        arquivo.write(palavra + '\n')

print("Palavras ordenadas salvas no arquivo 'palavras_ordenadas.txt'.")