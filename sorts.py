#INSERTION SORT
# Funcion principal 
def insertionSort(arr):  
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # en base a l se dividen los elementos para hacer el sort 
        j = i-1
        while j >=0 and key > arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
# codigo de test
arr = [10,4,6,9,8,7,1,12] 
insertionSort(arr) 

#QUICK SORT
#funcion principal de quick sort, toma el ultimo elemento como pivote
def partition(arr, low, high): 
    i = (low-1)          
    pivot = arr[high]
    #el de arriba es el pivote
    
    for j in range(low, high): 
  
        # aqui revisa el el elemento es igual al pivote
        
        if arr[j] <= pivot: 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1) 
  
  
# QUICK SORT
#funcion principal
def quickSort(arr, low, high): 
    if len(arr) == 1: 
        return arr 
    if low < high: 
  
        # pi es el elemento que corta, en caso de que este ordenado ya se guarda
        pi = partition(arr, low, high) 
  
        # se hace el sort por separado para hacer el ordenamiento rápido
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
  
# codigo de prueba (tienen que ser iguales los dos o algo anda mal)

arr = [10,4,6,9,8,7,1,12] 
n = len(arr) 
quickSort(arr, 0, n-1) 



