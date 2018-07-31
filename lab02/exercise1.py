class NameList:
    def __init__(self):
        self.index = {}

    def add(self, key1, value1):
        self.index[key1] = value1

    def find(self, key1):
        try:
            print(self.index[key1])
        except KeyError:
            print('Index not existed.')
        else:
            return self.index[key1]

    def order(self):
        dict = sorted(self.index.items(), key=lambda d: d[0])
        print('Roll number Ascending:')
        for (k, v) in dict:
            print("No.", k, " " + "Name:", v)


class BetterNameList(NameList):
    def order(self):
        dict_new = sorted(self.index.items(), key=lambda d: -1*d[0])
        print('Roll number descending:')
        for (k, v) in dict_new:
            print("No.", k, " " + "Name:", v)


a = NameList()
a.add(121, 'example')
a.add(122, 'super')
a.add(120, 'real')
a.find(120)
a.find(124)
a.order()

b = BetterNameList()
b.add(121, 'example')
b.add(122, 'super')
b.add(120, 'real')
b.find(120)
b.find(124)
b.order()
