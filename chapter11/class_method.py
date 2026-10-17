class A:
    a=24
    @classmethod
    def show(cls):
        print(f"class instant is {cls.a}")
c=A()
c.a=12
c.show()