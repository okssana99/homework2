# Задача 1
def find_apartment(floor_count, apartments_per_floor, target_apartment):

    total_apartments = floor_count * apartments_per_floor

    staircase = (target_apartment - 1) // apartments_per_floor + 1

    floor = (target_apartment - 1) % apartments_per_floor + 1
    
    return (staircase, floor)

floor_count = 10
apartments_per_floor = 4
target_apartment = 25

staircase, floor = find_apartment(floor_count, apartments_per_floor, target_apartment)
print(f"To reach apartment {target_apartment}, go to staircase {staircase} and climb to floor {floor}.")
