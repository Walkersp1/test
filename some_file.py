print('First')
print('Second')


def say_something(number: int, word: str) -> str:
   word = word.capitalize()
   return word * number


say_something(8,'hello')
