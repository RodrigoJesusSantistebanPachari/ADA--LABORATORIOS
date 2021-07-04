import random
from math import log

def GenerateRandom(n):
  A = []
  for i in range(n):
    A.append(random.randint(-99999999,99999999))
  return A;

def AlgoritmoMaximo(A):
  cont = 0
  max = A[0]
  for i in range(len(A)):
    if(A[i]> max):
      cont += 1;
      max = A[i]
  return cont

def Promedio_200_Veces(n):
  promedio = 0
  for i in range(200):
    A = GenerateRandom(n)
    cont = AlgoritmoMaximo(A)
    promedio += cont
  promedio /= 200
  return promedio

n = 2**8
while(n<=2**20):
  print("----------------------------------")
  print("    n    |   ", n)
  print("Promedio |   ",Promedio_200_Veces(n))
  print("1+ln(n)  |   ", 1+log(n))

  n*=2