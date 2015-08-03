import regex
from .match import Match
class Filter():
    def __init__(self):
        pass

    @staticmethod
    def leftmost_left_index(matches):
        if matches == []: return []
        leftmost = min([m.left for m in matches])
        return [m for m in matches if m.left == leftmost]
    @staticmethod
    def leftmost_right_index(matches):
        if matches == []: return []
        leftmost = min([m.right for m in matches])
        return [m for m in matches if m.right == leftmost]
    @staticmethod
    def rightmost_left_index(matches):
        if matches == []: return []
        rightmost = max([m.left for m in matches])
        return [m for m in matches if m.left == rightmost]
    @staticmethod
    def rightmost_right_index(matches):
        if matches == []: return []
        rightmost = max([m.right] for m in matches)
        return
    @staticmethod
    def shortest(matches):
        if matches == []: return []
        shortest = min([m.length for m in matches])
        return [m for m in matches if m.length == shortest]
    @staticmethod
    def longest(matches):
        if matches == []: return []
        longest = max([m.length for m in matches])
        return [m for m in matches if m.length == longest]
    @staticmethod
    def left_of(x,matches):
        if matches == []: return []
        return [m for m in matches if m.leftof(x)]
    @staticmethod
    def right_of(x,matches):
        if matches == []: return []
        return [m for m in matches if m.right_of(x)]
    @staticmethod
    def is_between(lbound,rbound,matches):
        if matches == []: return []
        return [m for m in matches if m.is_between(lbound,rbound)]
    @staticmethod
    def is_outside(lbound,rbound,matches):
        if matches == []: return []
        return [m for m in matches if m.is_outside(lbound,rbound)]
    @staticmethod
    def is_outside_match(m,matches):
        if matches == []: return []
        return Filter.is_outside(m.left,m.right,matches)
    @staticmethod
    def does_not_match_any(exceptions,matches):
        if matches == []: return []
        return [m for m in matches if m not in exceptions]

