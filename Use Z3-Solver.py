from z3 import Solver,Int,add,model,check

S = Solver()
x = Int("x")
y = Int("y")
hasil = Int('hasil')

s.add((7*x)+(4*y) == 1)
s.add ((5*x)+(2*y) == -1)
s.add(x+y == hasil)
s.check()
print(s.model())
