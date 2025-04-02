
# Online Python - IDE, Editor, Compiler, Interpreter

sign = [" ", "?", ",", ".", "!", "(", ")", ";"]
a = input()
b = list(sorted(a))
quantidade = 0
matriz = []
for i in b :
    if i not in sign and i not in matriz:
        quantidade += 1
        matriz.append(i)
print("Aqui está sua frase em ordem alfabetica.")
print(matriz)
print("A quanttidade de caracteres é: ")
print(quantidade)