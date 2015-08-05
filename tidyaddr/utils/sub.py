import regex
from functools import reduce
class Sub():
    def __init__(self):
        pass
    @staticmethod
    def apply_subs(subs, s):
        args = list(subs.keys())
        args.insert(0,s)
        return reduce(lambda x,y: regex.sub(y,subs[y],x),args)
