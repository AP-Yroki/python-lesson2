string = "lovehbananahs"
arg1 = string.find('h')
arg2 = string.rfind('h')
arg3 = string[arg1:arg2 + 1]
result = string.replace(arg3, "")
print(result)