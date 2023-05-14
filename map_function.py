numbers = [2,3,4,5,6]

def cube_number(number):
    new_number_cubed = number*number*number
    return new_number_cubed

#normal function in map()
cubed_list = list(map(cube_number, numbers))
print(f"Using normal function {cubed_list}")

#Use of Lambda function in map() 
lambda_square_numbers = list(map(lambda x: x**2, numbers))
print(f"Using lambda function {lambda_square_numbers}")