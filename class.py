class Student(object):

    def __init__(self, name, score, gender):
        self.name = name
        self.score = score
        self.__gender = gender

    def print_score(self):
        print('%s: %s: %s' % (self.name, self.score, self.__gender))


    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if 0 <= gender <= 100:
            self.__gender = gender
        else:
            print('bad gender')

lisa = Student('Lisa', 99, 1)
bart = Student('Bart', 59, 2)

print(lisa.name)
print(lisa.print_score())

print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())

print(lisa.get_gender())
lisa.__gender = 2
print(lisa.get_gender())
lisa.set_gender(2)
print(lisa.get_gender())
lisa.set_gender(200)
print(lisa.get_gender())


class Student2(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student2()
s.score = 60    # OK，实际转化为s.set_score(60)
print(s.score)  # OK，实际转化为s.get_score()
#s.score = 9999



class Student3(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name=%s)' % self.name

    def __call__(self):
        print('My name is %s.' % self.name)

print(Student3('Michael'))
t = Student3('Michael')
print(t)
t = Student3("Michael")
print(t())

test = 7.6

#print(int('7.6'))
print(int('88'))
print(int(test))

print('99 + 88 + 7.6 =', 99 + 88 + 7.6)

from functools import reduce

def str2num(s):
    if '.' in s:
        return float(s)
    else:
        return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()