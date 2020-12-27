import random

def sortHeads(array,tree,size,pos,node):
  heads = []
  for i in range(0,len(size)):
     if i == 0:
        heads += [tree[size[i]]-1]
     else:
        heads += [heads[i-1]+tree[size[i]]]
  min = len(heads)-1
  for i in range(0,len(heads)):
     for j in range(len(heads)-1,i,-1):
        if size[j] == 0:
           if array[heads[j]] < array[heads[j-1]]:
              array[heads[j]], array[heads[j-1]] = array[heads[j-1]], array[heads[j]]
              if j-1 < min:
                 min = j-1
        else:
           child1 = heads[j]-1
           if size[j] > 1:
              child2 = heads[j]-tree[size[j]-2]-1
           else:
              child2 = heads[j]-2
           if array[heads[j-1]] > array[child1] and array[heads[j-1]] > array[child2] and array[heads[j-1]] > array[heads[j]]:
              array[heads[j]], array[heads[j-1]] = array[heads[j-1]], array[heads[j]]
              if j-1 < min:
                 min = j-1
  while min <= pos:
     trickleDown(array,tree,size,min,heads[min])
     min += 1

def trickleDown(array,tree,size,pos,node):
  i = 1
  while i <= size[pos]:
     child1 = node -1
     if i == size[pos]:
        child2 = node -2
     else:
        child2 = node-tree[size[pos]-i-1]-1
     if array[child1] < array[child2]:
        maxchild = child2
        i += 1
     else:
        maxchild = child1
        i += 2
     if array[maxchild] > array[node]:
        array[maxchild],array[node] = array[node],array[maxchild]
        node = maxchild
     else:
        break

def smoothsort(array):
  tree = [1,3,5,9,15,25,41,67,109,177,287,465,753,1219]
  size = [0]
  pos = 0
  for i in range(1,len(array)):
     if pos > 0 and (size[pos-1] == size[pos]+1 or size[pos-1] == 0):
        size.pop()
        pos -= 1
        size[pos] += 1
     else:
        size += [0]
        pos += 1
     sortHeads(array,tree,size,pos,i)
  for i in range(len(array)-2,0,-1):
     if size[pos] == 0:
        size.pop()
        pos -= 1
     else:
        size[pos] -= 1
        if size[pos] == 0:
           size += [0]
        else:
           size += [size[pos]-1]
        pos += 1
     sortHeads(array,tree,size,pos,i)

array = list(range(1,10))
random.shuffle(array)
print("Sebelum Urut")
print(array)
smoothsort(array)
print("Setelah Urut")
print(array)
