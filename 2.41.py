s = 'Suan'
print(s)

def string_plus(s1, s2):
    s = s1 + s2
    return s

print(s)
s = string_plus('Suan', 'Lab')
print(s)

def global_plus(s1, s2):
    gs = s + s1 + s2
    return gs

print(s)
s = global_plus('Suan', 'Lab')
print(s)
