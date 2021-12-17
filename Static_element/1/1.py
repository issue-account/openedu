# # 1.1  очень легко 
# # 1.2  решение на сайте https://planetcalc.ru/485/
# N = float(input("Введите число полученное на сайте: "))
# print(round(N,3))
# # 1.3
print("Введите проценты фирм по очереди")
P = [int(input("Введите значение:")) for i in range(3)]
print("Введите количество ошибок по очереди: ")
Q = [int(input("Введите значение:")) for i in range(3)]
H_1 = (P[0]*(Q[0]))/10000
H_2 = (P[1]*(Q[1]))/10000
H_3 = (P[2]*(Q[2]))/10000
Sum_H = H_1 + H_2 + H_3
print(round(Sum_H,3))
H = H_1/Sum_H
print(round(H,3))
#X = [5,5,6,2,2,1,2,5,1,4]
# X =[1,4,1,4,3,1,4,1,3,1]
# #[6,5,2,3,3,4,5,1,1]
X = [5,4,4,3,6,2,1,2,2,2,2,1,2,2]
print(len(X))
# #https://math.semestr.ru/math/expectation-discrete.php
# p
2 ^ 2*0.73+4 ^ 2*0.27-2.54 ^ 2
