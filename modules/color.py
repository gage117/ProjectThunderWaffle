modifiers = {
    "END" : "\033[0m",

    "BOLD"       : "\033[1m",
    "DIM"        : "\033[2m",
    "UNDERLINED" : "\033[4m",
    "BLINK"      : "\033[5m",
    "REVERSE"    : "\033[7m",
    "HIDDEN"     : "\033[8m",

    "DEFAULT"      : "\033[39m",
    "BLACK"        : "\033[30m",
    "RED"          : "\033[31m",
    "GREEN"        : "\033[32m",
    "YELLOW"       : "\033[33m",
    "BLUE"         : "\033[34m",
    "PURPLE"       : "\033[35m",
    "CYAN"         : "\033[36m",
    "LIGHTGRAY"    : "\033[37m",
    "DARKGRAY"     : "\033[90m",
    "LIGHTRED"     : "\033[91m",
    "LIGHTGREEN"   : "\033[92m",
    "LIGHTYELLOW"  : "\033[93m",
    "LIGHTBLUE"    : "\033[94m",
    "LIGHTPURPLE"  : "\033[95m",
    "LIGHTCYAN"    : "\033[96m",
    "WHITE"        : "\033[97m",

    "BACKGROUNDDEFAULT"      : "\033[49m",
    "BACKGROUNDBLACK"        : "\033[40m",
    "BACKGROUNDRED"          : "\033[41m",
    "BACKGROUNDGREEN"        : "\033[42m",
    "BACKGROUNDYELLOW"       : "\033[43m",
    "BACKGROUNDBLUE"         : "\033[44m",
    "BACKGROUNDPURPLE"       : "\033[45m",
    "BACKGROUNDCYAN"         : "\033[46m",
    "BACKGROUNDLIGHTGRAY"    : "\033[47m",
    "BACKGROUNDDARKGRAY"     : "\033[100m",
    "BACKGROUNDLIGHTRED"     : "\033[101m",
    "BACKGROUNDLIGHTGREEN"   : "\033[102m",
    "BACKGROUNDLIGHTYELLOW"  : "\033[103m",
    "BACKGROUNDLIGHTBLUE"    : "\033[104m",
    "BACKGROUNDLIGHTPURPLE"  : "\033[105m",
    "BACKGROUNDLIGHTCYAN"    : "\033[106m",
    "BACKGROUNDWHITE"        : "\033[107m",
}
def modifyText(text, modifier):
  if isinstance(text, str) or isinstance(text, int):
    return modifiers[modifier.upper()] + str(text) + modifiers['END']
  elif isinstance(text, list) or isinstance(text, tuple):
    modified_arr = []
    for i in text:
      modified_arr.append(modifyText(i, modifier))
    return modified_arr
