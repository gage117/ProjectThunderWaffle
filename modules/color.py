color = {
   'PURPLE': '\033[95m',  # Locations
   'CYAN': '\033[96m',  # Choices
   'DARKCYAN': '\033[36m',
   'BLUE': '\033[94m',
   'GREEN': '\033[92m',
   'YELLOW': '\033[93m',  # Player properties
   'RED': '\033[91m',
   'BOLD': '\033[1m',
   'UNDERLINE': '\033[4m',
   'END': '\033[0m'
}
def modifyText(text, modifier):
  if isinstance(text, str) or isinstance(text, int):
    return color[modifier.upper()] + str(text) + color['END']
  elif isinstance(text, list) or isinstance(text, tuple):
    modified_arr = []
    for i in text:
      modified_arr.append(modifyText(i, modifier))
    return modified_arr