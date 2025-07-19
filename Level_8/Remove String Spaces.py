s = 'sdfa asdf adasdf    adsfafda'
no_space = lambda s: s.replace(' ', '')
print(no_space(s))

no_space2 = lambda s: ''.join(filter(lambda ch: not ch == ' ', s))