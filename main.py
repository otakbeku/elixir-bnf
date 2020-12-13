# Test parser class
from Parser import ElixirParser as ps
from Contoh_Symbols import contoh1, contoh2, contoh3
from docstring_extractor import print_docstrings

ep1 = ps(contoh1[2])
print('='*10)
print("Parsing Contoh 1")
ep1.parse()

ep2 = ps(contoh2[2])
print('='*10)
print("Parsing Contoh 2")
ep2.parse()

ep3 = ps(contoh3[2])
print('='*10)
print("Parsing Contoh 3")
ep3.parse()
   
with open("Parser.py") as fp:
    print_docstrings(fp, save=True)