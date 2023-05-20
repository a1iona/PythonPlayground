name = input('please enter your name')
surname = input ('please enter your surname')
age = int (input ('please enter your age'))
height = float (input ('please enter your height'))
city = input ('please enter your city')
weight = int(input ('please enter your weight'))

print (f'name: {name} surname: {surname} age {age} height {height} city {city} BMI: {height * 703 / weight * weight}')