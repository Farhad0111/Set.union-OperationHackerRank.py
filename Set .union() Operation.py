class Farhad:
    def __init__(self):
        self.i=int(input())
        self.a=set(input().split())
        self.j=int(input())
        self.b=set(input().split())
    def faru(self):
        print(len(self.a.union(self.b)))

farhad=Farhad()
farhad.faru()