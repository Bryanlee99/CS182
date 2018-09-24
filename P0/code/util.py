##### Filename: util.py
##### Author: Bryan Lee
##### Date: 9/14/18
##### Email: bryanlee@college.harvard.edu

import copy

class Util:

    ## Problem 1
    def matrix_multiply(self, x, y):
        out = []
        for i in range(len(x)):
            out.append([])
        for i in range(len(x)):
            for k in range(len(y[0])):
                temp = 0
                for j in range(len(y)):
                     temp += x[i][j] * y[j][k]
                out[i].append(temp)
        return out

    ## Problem 2, 3
    class MyQueue:
        def __init__(self):
            self.q = []
        def push(self, val):
            self.q.append(val)
        def pop(self):
            if(len(self.q) == 0):
                return None
            return self.q.pop(0)
        def __eq__(self, other):
            if (len(other.q) != len(self.q)):
                return False
            for i in range(len(other.q)):
                if (other.q[i] != self.q[i]):
                    return False
            return True
        def __ne__(self, other):
            if(len(other.q) != len(self.q)):
                return True
            for i in range(len(other.q)):
                if(other.q[i] != self.q[i]):
                    return True
            return False
        def __str__(self):
            return "Name"

    class MyStack:
        def __init__(self):
            self.s = []
        def push(self, val):
            self.s.append(val)
        def pop(self):
            if (len(self.s) == 0):
                return None
            return self.s.pop()
        def __eq__(self, other):
            if (len(other.s) != len(self.s)):
                return False
            for i in range(len(other.s)):
                if (other.s[i] != self.s[i]):
                    return False
            return True
        def __ne__(self, other):
            if(len(other.s) != len(self.s)):
                return True
            for i in range(len(other.s)):
                if(other.s[i] != self.s[i]):
                    return True
            return False
        def __str__(self):
            return "Name"

    ## Problem 4
    def add_position_iter(self, lst, number_from=0):
        out = []
        for i in range(len(lst)):
            out.append(lst[i] + i + number_from)
        return out

    def add_position_recur(self, lst, number_from=0):
        if not lst:
            return
        out = lst[:]
        ans = self.add_position_recur(out[1:], number_from + 1)
        if ans:
            out[1:] = ans
        out[0] += number_from
        return out

    def add_position_map(self, lst, number_from=0):
        return map(lambda (i, x): x + number_from + i, enumerate(lst))

    ## Problem 5
    def remove_course(self, roster, student, course):
        if student in roster:
            if course in roster[student]:
                roster[student].remove(course)
                return roster
        print "Student or class not in roster"
        return None

    ## Problem 6
    def copy_remove_course(self, roster, student, course):
        roster_copy = copy.deepcopy(roster)
        if student in roster_copy:
            if course in roster_copy[student]:
                roster_copy[student].remove(course)
                return roster_copy
        print "Student or class not in roster"
        return None

util = Util()
s = util.MyStack()
s.push(2); s.push(3);
a = util.MyStack()
a.push(2); a.push(3)
print s.__ne__(a)