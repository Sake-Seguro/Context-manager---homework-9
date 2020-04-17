

import datetime


class MyTimer():

  def __init__(self, file_path, mode, encode):
    self.file_path = file_path
    self.mode = mode
    self.encode = encode
    self.time_start = datetime.datetime.now()

  def __enter__(self):
    self.file = open(self.file_path, self.mode, encoding=self.encode)
    return self.file

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.file.close()
    self.time_stop = datetime.datetime.now()

    print(f'\n\nThe program began its work at: {self.time_start}.')
    print(f'\nThe program finished its work: {self.time_stop}.')
    print(f'\nThe program was executed within: {self.time_stop - self.time_start} sec.')


def Polish_notation():

  print('\nFor two positive integers you could play with the Polish notation.')

  your_input = list(input('\n\nEnter your Polish notation: one arythmetic symbol followed by two positive integers separated with spaces to start the game,\n e.g. + 2 9: ').split(' '))

  operation_sym = your_input[0]

  number_1 = int(your_input[1])
  number_2 = int(your_input[2])

  operation_symbols = ['+', '-', '*', '/']

  result = 0

  assert operation_sym in operation_symbols, 'Incorrect symbol of arithmetic operations. Please, check and try again.'

  assert number_1 >= 0 and number_2 >= 0, 'The number you entered is not a positive integer, Please, check and try again.'

  try:

    if operation_sym == '+':
      result = number_1 + number_2
    elif operation_sym == '-':
      result = number_1 - number_2
    elif operation_sym == '*':
      result = number_1 * number_2
    elif operation_sym == '/':
      result = number_1 / number_2

    print(f'\nThe result of your Polish notation is {result}.')


  except ZeroDivisionError:
    print('\nIt is impossible to divide by 0.')
  except ValueError:
    print('\nThe meanings you tried to use are incorrect.')
  except UnboundLocalError:
    print('\nIt seems you tried to apply some incorrect command.')
  except Exception as e:
    print(f'\nYour error is {e}.')

  else:
    print('\nWe did this exercise in a good manner :).')


if __name__ == '__main__':
  
  with MyTimer('mylogger.txt', 'w', 'UTF-8') as file:

    start_time = datetime.datetime.now()
    file.write(f'\nThe program started its work at {start_time}.\n')
    
    Polish_notation()
    
    stop_time = datetime.datetime.now()
    file.write(f'\nThe program finished its functioning at {stop_time}.\n')
    
    calc_time = stop_time - start_time
    file.write(f'\nThe duration of its functioning is {calc_time}.\n')
    
