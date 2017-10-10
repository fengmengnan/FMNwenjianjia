def BinSearch(array, key, low, high):
    mid = int((low+high)/2)
    if key == array[mid]:  
        return array[mid]
    if low > high:
        return False

    if key < array[mid]:
        return BinSearch(array, key, low, mid-1)  
    if key > array[mid]:
        return BinSearch(array, key, mid+1, high)



if __name__ == "__main__":
    array = [1,2,3,4,5]
    ret = BinSearch(array, 3, 0, len(array)-1) 
    print(ret)
