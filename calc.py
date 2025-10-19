# calc.py 
def soma(a, b): 
    return a + b 
 
def subtracao(a, b): 
    return a - b 

def multiplicacao(a, b): 
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b
 
if __name__ == "__main__": 
    print("Exemplo: soma(2,3) =", soma(2, 3)) 
    print("Exemplo: subtracao(5,2) =", subtracao(5, 2)) 
    print("Exemplo: multiplicacao(3,4) =", multiplicacao(3, 4))
    print("Exemplo: divisao(10,2) =", divisao(10, 2))
