def remove_chars(_s):
    return _s[1:-1:]
    # try:
    #     _s = _s[1::]
    #     _s = _s[:-1:]
    #     return _s
    # except (Exception):
    #     return Exception


print(remove_chars('hello world'))
print(remove_chars('ld'))
print(remove_chars('d'))
print(remove_chars(''))