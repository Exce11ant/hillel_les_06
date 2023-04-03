def farm():
    wr = open("requirements.txt")
    file = [i for i in wr]
    st = '<br>'.join(file)
    return st