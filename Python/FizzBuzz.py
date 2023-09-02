print('Check if your number is Fizz, Buzz or Fizzbuzz!')

guess = int(input('Enter a number to check if it is fizzbuzz'))

if (guess%3 == 0 and guess%5 == 0):
    print ("FizzBuzz")
elif guess%3 == 0:
    print ("Fizz")
elif guess%5 == 0:
    print ("Buzz")
else:
    print ("that number is not fizz or buzz")

