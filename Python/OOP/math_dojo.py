class MathDojo(object):
    def __init__(self):
        self.val = 0

    def add(self, *args):
        for i in args:
            if type(i) == int:
                self.val += i
            elif type(i) == list:
                for j in i:
                    self.val += j
            elif type(i) == tuple:
                for j in i:
                    self.val += j                
        return self

    def sub(self, *args):
        for i in args:
            if type(i) == int:
                self.val -= i
            elif type(i) == list:
                for j in i:
                    self.val -= j
            elif type(i) == tuple:
                for j in i:
                    self.val -= j
        return self

    def result(self):
        print 'result:', self.val
        return self

md = MathDojo()

md.add(2).add(2,5).sub(3,2).result()

mr = MathDojo()

mr.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).sub(2, [2,3], (1.1,2.3)).result()