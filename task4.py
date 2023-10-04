string = "foofelshmerts"
if string.count("f") == 1:
    print(string.find("f"))
    res1 = string.find("f")
    res2 = string.rfind("f")
elif string.count("f") > 1:
    res1 = string.find("f")
    res2 = string.rfind("f")
    print(res1, res2)
else:
    print("")
