# Create a Classic User Interface using only "print" and "f() string"
# class fg:
#     BLACK   = '\033[30m'
#     RED     = '\033[31m'
#     GREEN   = '\033[32m'
#     YELLOW  = '\033[33m'
#     BLUE    = '\033[34m'
#     MAGENTA = '\033[35m'
#     CYAN    = '\033[36m'
#     WHITE   = '\033[37m'
#     RESET   = '\033[39m'

# class bg:
#     BLACK   = '\033[40m'
#     RED     = '\033[41m'
#     GREEN   = '\033[42m'
#     YELLOW  = '\033[43m'
#     BLUE    = '\033[44m'
#     MAGENTA = '\033[45m'
#     CYAN    = '\033[46m'
#     WHITE   = '\033[47m'
#     RESET   = '\033[49m'

# class style:
#     BRIGHT    = '\033[1m'
#     DIM       = '\033[2m'
#     NORMAL    = '\033[22m'
#     RESET_ALL = '\033[0m'


def fg(color):
  if color == "red":
    return("\033[31m")
  elif color == "green":
    return("\033[32m")
  elif color == "blue":
    return("\033[34m")
  elif color == "yellow":
    return("\033[33m")
  elif color == "cyan":
    return("\033[36m")
  elif color == "magenta":
    return("\033[35m")
  else:
    return("\033[0m")

text1 = fg("red")+"="+fg("white")+"="+fg("blue")+"="+fg("yellow")+" Music App "+fg("blue")+"="+fg("white")+"="+fg("red")+"="
text2 = "🔥▶ " + fg("white") + "RadioGaga"
text3 = fg("yellow") + "Queen"
print (text1.center(100))
print(text2)
print(text3)



