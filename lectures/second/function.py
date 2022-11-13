def mul(_a,_b):
    return _a * _b

def new_string(_symbol, _count = 3):
    return _symbol *  _count

def concatenation(*params):
    res: str = ""
    for item in params:
        res += item
    return res