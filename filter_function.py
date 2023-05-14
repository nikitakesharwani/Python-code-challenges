numbers = [1,2,4,45,6,71,8,3,12,0,32,44,]


not_divisbile_by_3_list = list(filter(lambda x : x % 3 != 0 , numbers))
print(f"List of numbers not divisible by 3: {not_divisbile_by_3_list}")

def check_divisibility(num):
    return num % 3 == 0

divisible_by_3_list = list(filter(check_divisibility , numbers))
print(f"List showing divisibility by 3: {divisible_by_3_list}")