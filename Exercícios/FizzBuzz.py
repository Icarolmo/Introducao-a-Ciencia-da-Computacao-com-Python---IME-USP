def fizzbuzz (n):
    div3 = n % 3
    div5 = n % 5
    if ( div3 == 0 and div5 == 0):
        return ('FizzBuzz')
    elif (div3 == 0):
         return ('Fizz')
    elif (div5 == 0):
        return ('Buzz')
    else:
        return n


