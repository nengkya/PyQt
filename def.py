
class c(object):
    def a():
        print('1')

    def b(self):
        a()
        print('2')

d = c()

d.b
