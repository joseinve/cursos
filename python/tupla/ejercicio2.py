alfabeto = (
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
)
numletra=round(float(input("ingrese un valor entre 1 y 26:")))
if(numletra>-1 and numletra<27):
    print(alfabeto[numletra-1])
elif(numletra<1):
    print("EL numero no debe ser menor a 1")
elif(numletra>26):
    print("EL numero no debe ser mayor a 26")