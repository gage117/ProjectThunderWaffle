from os import system, name as os_name

### Clears the console
def clear():
  if os_name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

def wait_for_read(what_to_print):
  print(what_to_print)
  input("> ")

def clear_and_wait(what_to_print):
  clear()
  wait_for_read(what_to_print)