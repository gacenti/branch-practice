# Get integer from user
user_num = int(input('Hello, there! Enter positive integer: '))

# Iteration
for i in range(1, user_num+1):
    if i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    else:
        print(f'{i}')
