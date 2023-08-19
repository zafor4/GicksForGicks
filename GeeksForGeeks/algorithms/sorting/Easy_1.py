def selectionSort(array,size):
    for i in range (0,size-1):
        index_min=i
        for j in range (i+1,size):
            if (array[j]<array[index_min]):
                index_min=j
        if (index_min!=i):        
            array[i],array[index_min]=array[index_min],array[i]

array=[2,5,2,8,5,6,8,8]
size=len(array)
frq=[0,0,0,0,0,0,0,0,0]
selectionSort(array,size)
for i in range (0,size):
    value=array[i]
    k=i
    count=1
    for j in range (1,size):
        if array[k]==array[j]:
            count+=1
            k+=1
    frq[i]=count 

print(frq)

