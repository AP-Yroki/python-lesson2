string = "htesthtesth"
h1 = string.find('h')
h2 = string.rfind('h')
distance_remove = string[h1 + 1:h2]
result = distance_remove.replace('h', 'H')
print(result)