class Beta:
    def fun1(self):
        x=100
        self.items = []
    def fun2(self):
        self.items.append(33)
    def fun3(self):
        print(self.items)
        # print(x) error
b1 = Beta()
b1.fun1()
b1.fun2()
b1.fun3()