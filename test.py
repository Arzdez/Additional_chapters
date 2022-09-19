from numpy import empty
from sympy import Symbol, pprint, powsimp
from matplotlib.pyplot import scatter, show
import time
#Функция запрашивает степень полинома и его коэфициенты
def  Request_coef():
    #Переменные для вывода полинома
    x = Symbol('x')
    s = 0
    
    #Запрос степени полинома
    pprint("Input polinom degree.\n(P(x) = Σ С_i*(x**i), i = 0,1,....,n. n - degree of polinom ")
    degree_of_polynomial = int(input("==> "))+1
    
    Coef_of_polinom = empty(degree_of_polynomial)
    
    #Ввод коэфициентов полинома
    for i in range(degree_of_polynomial):
        print(f"input {i} coeficient")
        Coef_of_polinom[i] = int(input("==> "))
        
        #Заполнение переменной для вывода плученного полинома
        s+= powsimp(Coef_of_polinom[i]*x**i,combine='base',force=True)
    
    #Вывод полинома
    print("-------------------------")
    print("Your polinom") 
    pprint(s)
    print("-------------------------")
    
    return Coef_of_polinom

#С коэфициентами предыдущей фнукции вычисляет P(x) с данным x
def Polinomial_Answer(coeficients,X):
    
    Degree = len(coeficients)
    Answer = 0
    
    for i in range(Degree):
        Answer+= coeficients[i]*(X**i)
    
    return Answer


#Проверяет функцию на транзитивность и биективность
def Chek_Bijectiv_Tranzitiv():

    Coef_of_polinom = Request_coef()
    
    #Массивы хранящие кольцо вычетов по модулю 4 и 8 соответственно
    Massiv_mod4 = [i for i in range(4)]
    Massiv_mod8 = [i for i in range(8)]
    
    #Массивы хранящие вычеты функции по модулю 4 и 8 соответственно
    Funk_deduction_mod4 = []
    Funk_deduction_mod8 = []
    
    #Начальное значение с которого начинать проверку
    x0 = 0
    
    #Расчёт значения полинома в данной точке и вычисление вычета по модулю 4
    while x0 not in Funk_deduction_mod4:
        Funk_deduction_mod4.append(x0)
        x0 = Polinomial_Answer(Coef_of_polinom,x0)%4
        
    #Проверка являются ли полученные вычеты перестановкой вычетов по модулю 4
    if sorted(Funk_deduction_mod4) == Massiv_mod4:
        print("-------------------------")
        print("Funktion is Bijective")
        print("Ring modulo 4\n", Massiv_mod4)
        print("Funk deduction modulo 4\n", Funk_deduction_mod4)
        print("-------------------------")
        
    else:
        print("Funktion is not Bijective")
        print("Ring modulo 4\n", Massiv_mod4)
        print("Funk deduction modulo 4\n", Funk_deduction_mod4)
    
    
    #Аналогичные операции по модулю 8
    while x0 not in Funk_deduction_mod8:
        Funk_deduction_mod8.append(x0)
        x0 = Polinomial_Answer(Coef_of_polinom,x0)%8
        
  
    if sorted(Funk_deduction_mod8) == Massiv_mod8:
        print("-------------------------")
        print("Funktion is Tranzitive")
        print("Ring modulo 8\n", Massiv_mod8)
        print("Funk deduction modulo 8\n", Funk_deduction_mod8)
        print("-------------------------")
        
    else:
        print("Funktion is not Tranzitive")
        print("Ring modulo 8\n", Massiv_mod8)
        print("Funk deduction modulo 8\n", Funk_deduction_mod8)  

def Graph_Plot():
    

    Coef_of_polinom = Request_coef()
    
    #Запрашиваем число разрядов k
    digit = int(input("Input digit\n==> "))
    
    #Генерируем все k-разрядные строки 
    Kdigit_strings = [i for i in range( 2**digit )]
    
    #Генерируем массив рациональных чисел вида: l/p**k , l = {0,1,...,(p**k)-1)}
    Rational_number_for_Kstring = [ i / ( 2**digit )  for i in Kdigit_strings]
    
    #Генерируем массив рациональных чисел вида: ( f(l) mod p**k ) / ( p**k )
    Funk_deduction_module = [ ( ( Polinomial_Answer( Coef_of_polinom , i ) % ( 2**digit )  ) / ( 2**digit ) ) for i in Kdigit_strings ]

    #Рисуем граффик
    scatter(Rational_number_for_Kstring,Funk_deduction_module,s=1)
    show()
    
    
    
    
    
    
    


if __name__ == '__main__':
    Graph_Plot()

