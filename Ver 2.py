import random

def SmoothUp(SubTreeSize, LeftSubTreeSize):
    temp = SubTreeSize + LeftSubTreeSize + 1
    LeftSubTreeSize = SubTreeSize
    SubTreeSize = temp
    return SubTreeSize, LeftSubTreeSize


def SmoothDown(SubTreeSize, LeftSubTreeSize):
    temp = SubTreeSize - LeftSubTreeSize - 1
    SubTreeSize = LeftSubTreeSize
    LeftSubTreeSize = temp
    return SubTreeSize, LeftSubTreeSize


def SwapItems(Array, index1, index2):
    temp = Array[index1]
    Array[index1] = Array[index2]
    Array[index2] = temp
    return Array


def SmoothShift(Array, NodeIndex, SubTreeSize, LeftSubTreeSize):
    ChildIndex = 0

    while(SubTreeSize >= 3):
        ChildIndex = NodeIndex - SubTreeSize + LeftSubTreeSize
        if(Array[ChildIndex] <= Array[NodeIndex - 1]):
            ChildIndex = NodeIndex - 1
            SubTreeSize, LeftSubTreeSize = SmoothDown(SubTreeSize, LeftSubTreeSize)
        if(Array[NodeIndex] >= Array[ChildIndex]):
            SubTreeSize = 1
        else:
            Array = SwapItems(Array, NodeIndex, ChildIndex)
            NodeIndex = ChildIndex
            SubTreeSize, LeftSubTreeSize = SmoothDown(SubTreeSize, LeftSubTreeSize)


def SmoothTrinkle(Array, NodeIndex, LeftRightTreeAddress, SubTreeSize, LeftSubTreeSize):
    ChildIndex = 0
    PreviousCompleteTreeIndex = 0

    while(LeftRightTreeAddress > 0):
        while(LeftRightTreeAddress % 2 == 0):
            LeftRightTreeAddress = LeftRightTreeAddress / 2
            SubTreeSize, LeftSubTreeSize = SmoothUp(SubTreeSize, LeftSubTreeSize)
        
        PreviousCompleteTreeIndex = NodeIndex - SubTreeSize
        
        if((LeftRightTreeAddress == 1) or (Array[PreviousCompleteTreeIndex] <= Array[NodeIndex])):
            LeftRightTreeAddress = 0
        else:
            LeftRightTreeAddress = LeftRightTreeAddress - 1
            if(SubTreeSize == 1):
                Array = SwapItems(Array,NodeIndex,PreviousCompleteTreeIndex)
                NodeIndex = PreviousCompleteTreeIndex
            elif(SubTreeSize >= 3):
                ChildIndex = NodeIndex - SubTreeSize + LeftSubTreeSize
                if(Array[ChildIndex] <= Array[NodeIndex - 1]):
                    ChildIndex = NodeIndex - 1
                    SubTreeSize, LeftSubTreeSize = SmoothDown(SubTreeSize, LeftSubTreeSize)
                    LeftRightTreeAddress = LeftRightTreeAddress * 2
                if(Array[PreviousCompleteTreeIndex] >= Array[ChildIndex]):
                    Array = SwapItems(Array, NodeIndex, PreviousCompleteTreeIndex)
                    NodeIndex = PreviousCompleteTreeIndex
                else:
                    Array = SwapItems(Array, NodeIndex, ChildIndex)
                    NodeIndex = ChildIndex
                    SubTreeSize, LeftSubTreeSize = SmoothDown(SubTreeSize, LeftSubTreeSize)
                    LeftRightTreeAddress = 0

    SmoothShift(Array, NodeIndex, SubTreeSize, LeftSubTreeSize)


def SmoothSemiTrinkle(Array, NodeIndex, LeftRightTreeAddress, SubTreeSize, LeftSubTreeSize):
    IndexTopPreviousCompleteHeap = 0
    IndexTopPreviousCompleteHeap = NodeIndex - LeftSubTreeSize
    if(Array[IndexTopPreviousCompleteHeap] > Array[NodeIndex]):
        Array = SwapItems(Array, NodeIndex, IndexTopPreviousCompleteHeap)
        SmoothTrinkle(Array, IndexTopPreviousCompleteHeap, LeftRightTreeAddress, SubTreeSize, LeftSubTreeSize)
    

def smoothSort(Array):
    OneBasedIndex = 1
    NodeIndex = 0
    LeftRightTreeAddress = 1
    SubTreeSize = 1
    LeftSubTreeSize = 1

    while(OneBasedIndex < len(Array)):
        if(LeftRightTreeAddress % 8 == 3):
            SmoothShift(Array,NodeIndex, SubTreeSize, LeftSubTreeSize)
            LeftRightTreeAddress = (LeftRightTreeAddress + 1) / 4
            SubTreeSize, LeftSubTreeSize = SmoothUp(SubTreeSize, LeftSubTreeSize)
            SubTreeSize, LeftSubTreeSize = SmoothUp(SubTreeSize, LeftSubTreeSize)
        elif(LeftRightTreeAddress % 4 == 1):
            if(OneBasedIndex + LeftSubTreeSize < len(Array)):
                SmoothShift(Array, NodeIndex, SubTreeSize, LeftSubTreeSize)
            else :
                SmoothTrinkle(Array, NodeIndex, LeftRightTreeAddress, SubTreeSize, LeftSubTreeSize)
            
            while(True):
                SubTreeSize, LeftSubTreeSize = SmoothDown(SubTreeSize, LeftSubTreeSize)
                LeftRightTreeAddress = LeftRightTreeAddress * 2
                if (SubTreeSize == 1):
                    break

            LeftRightTreeAddress = LeftRightTreeAddress + 1
            
        OneBasedIndex = OneBasedIndex + 1
        NodeIndex = NodeIndex + 1
    
    SmoothTrinkle(Array, NodeIndex, LeftRightTreeAddress, SubTreeSize, LeftSubTreeSize)

    while(NodeIndex > 1):
        OneBasedIndex = OneBasedIndex - 1
        if(SubTreeSize == 1):
            NodeIndex = NodeIndex - 1
            LeftRightTreeAddress = LeftRightTreeAddress - 1
            while (LeftRightTreeAddress % 2 == 0):
                LeftRightTreeAddress = LeftRightTreeAddress / 2
                SubTreeSize, LeftSubTreeSize = SmoothUp(SubTreeSize,LeftSubTreeSize)

        elif(SubTreeSize >= 3):
            LeftRightTreeAddress = LeftRightTreeAddress - 1
            NodeIndex = NodeIndex + LeftSubTreeSize - SubTreeSize
            if(LeftRightTreeAddress > 0):
                SmoothSemiTrinkle(Array, NodeIndex, LeftRightTreeAddress, SubTreeSize, LeftSubTreeSize)

            SubTreeSize, LeftSubTreeSize = SmoothDown(SubTreeSize, LeftSubTreeSize)
            LeftRightTreeAddress = LeftRightTreeAddress * 2 + 1
            NodeIndex = NodeIndex + LeftSubTreeSize
            SmoothSemiTrinkle(Array, NodeIndex, LeftRightTreeAddress, SubTreeSize, LeftSubTreeSize)
            SubTreeSize, LeftSubTreeSize = SmoothDown(SubTreeSize, LeftSubTreeSize)
            LeftRightTreeAddress = LeftRightTreeAddress * 2 + 1


Array = list(range(1,10))
random.shuffle(Array)
print("Sebelum Urut")
print(Array)
smoothSort(Array)
print("Setelah Di Sort")
print(Array)
