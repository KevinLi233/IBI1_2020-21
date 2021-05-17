class Grade(object):
    def __init__(self, name, code, poster, final, score):
        self.name = name
        self.code = code
        self.poster = poster
        self.final = final
        self.score = score

def Grade_calculator(self):
    '''
    Input: a grade class
    grade, name string and a number from 0  to 100
    '''
    self.score = 0 + 0.4*self.code + 0.3 *(self.poster + self.final)
    print(self.name,': ',self.score)

#example
g = Grade('Leo',80,80,80,0)
'''
input student name and grades such as g = Grade('Tom',80,80,80,0)
class difination is above
'''
Grade_calculator(g)

