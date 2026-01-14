#problem1

def selection_sort(list):
    for i in range(len(list)):
        smallest = i
        for j in range(i+1, len(list)):
            if list[j] < list[smallest]:
                smallest = j
        list[i], list[smallest] = list[smallest], list[i]
        
#can you implement this with selection sort with recursion?


#problem2

def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2 #round down
        left = list[:mid]
        right = list[mid:]
        
        merge_sort(left)
        merge_sort(right)
    
        """todo : merge left & right in the list    """

        i = j = k = 0 #셋다 0부터 시작
        
        # left, right 두 리스트를 비교하며 작은 값을 원본 리스트로 덮어쓰기
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else : # len(left) > len(right)
                list[k] = right[j]
                j += 1
            k += 1
            
        #한쪽 리스트가 먼저 끝나면, 남은 값들을 덮어씀
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    


