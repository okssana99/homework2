list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

result = zip(list1, list2)

print(list(result))  
def my_zip(*args):
  
    min_length = min(len(seq) for seq in args)
    result = []
    for i in range(min_length):
        tuple_ = tuple(seq[i] for seq in args)
        result.append(tuple_)
    
    return result

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

result = my_zip(list1, list2)
print(result)  
