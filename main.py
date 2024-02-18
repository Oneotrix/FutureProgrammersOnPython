C=15
D=2
result =C+D
print(result)


K = int(input("Введи число K: "))
N = int(input("Введи число N: "))

if K<N :
    for i in range(K + 1, N):
        print(i)
else:
    for i in range(N + 1, K):
        print(i)