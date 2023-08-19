def insertionSort(array):
    for i in range (1,len(array)):
        item=array[i]
        j=i-1
        while (j>=0 and array[j]>item):
            array[j+1]=array[j]
            j=j-1
        array[j+1]=item
a=[0,1,2,0,1,2]
insertionSort(a) 
print(a)           