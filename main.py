print('Enter your name:')
x = input()
words = x.split(' ')
capitalized = ' '.join([word.capitalize() for word in words])
print('Hello, ' + capitalized)