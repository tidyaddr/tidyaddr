import regex
class Match:
    """"Holds a match string, a left, and right index
    also holds functionality to produce matches
    """""
    def __init__(self,str,left,right):
        self.str = str
        self.left = left
        self.right = right
        self.length = self.right - self.left

    def left_of(self,x,inclusive=False):
        """"Is the Match to left of an index i?"""""
        if isinstance(x,Match):
            x = x.left
        if inclusive:
            return self.right <= x
        else:
            return self.right < x

    def right_of(self,x,inclusive=False):
        """"Is the match to right of an index i?"""""
        if isinstance(x,Match):
            x = x.right
        if inclusive:
            return self.left >= x
        else:
            return self.left > x

    def is_between(self,lbound,rbound,l_inclusive=False,r_inclusive=False):
        return self.right_of(lbound,l_inclusive) and self.left_of(rbound,r_inclusive)

    def is_outside(self,lbound,rbound,l_inclusive=False,r_inclusive=False):
        return self.left_of(lbound,l_inclusive) or self.right_of(rbound,r_inclusive)

    @staticmethod
    def substring_between_matches(s,left_match,right_match):
        return s[left_match.right:right_match.left]
    @staticmethod
    def substring_rightof_match(s,match):
        return s[match.right:]
    @staticmethod
    def substring_leftof_match(s,match):
        return s[:match.left]


    @staticmethod
    def findall_p_in_s(p,s):
        """"returns a series of matches for a pattern (p) in a str (s)"""""
        match_strs = regex.findall(p,s)
        #get pairs of left and right indexes
        match_indexes = [(i.start(0),i.end(0)) for i in regex.finditer(p,s)]
        all_p_in_s = [Match(match_strs[i],match_indexes[i][0],match_indexes[i][1]) for i in range(0,len(match_strs))]
        return all_p_in_s

    @staticmethod
    def findall_patterns_in_s(patterns,s,unique=True):
        matches = [Match.findall_p_in_s(p,s) for p in patterns]
        #unnest list of lists
        matches =  [item for sublist in matches for item in sublist]
        if unique:
            matches = list(set(matches))
        return matches


    def __repr__(self):
        return "M(" + self.__str__() + ")"

    def __str__(self):
        return self.str + ", " +  str(self.left) + ", " + str(self.right)

    def __eq__(self,other):
        if(isinstance(other,Match)):
            return self.str == other.str and self.left == other.left and self.right == other.right
        else:
            return False

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self.__repr__())
