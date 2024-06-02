from p_of_ngrowths_module import CreateGs
from p_of_ngrowths_module import NumberOfMicrostates

n = 4
Nm = NumberOfMicrostates(n)
print(Nm)

list_of_Gs = CreateGs(n, Nm)
