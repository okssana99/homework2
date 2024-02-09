#Задача3
def check_line(line):
    parts = line.split(';')
    nums1 = list(map(int, parts[0].split()))
    nums2 = list(map(int, parts[1].split()))
    
    expected_sum = sum(nums1) // len(nums1)
    remainder = sum(nums1) % len(nums1)
    
    if remainder != 0:
        expected_sum += 1
    return expected_sum == sum(nums2)
with open('numbers.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if check_line(line):
            print(line, "True")
        else:
            print(line, "False")


