#!/usr/bin/python
#!enconding: UTF-8
import sys
import math

PI35DT = 3.14159265358979311599796346854418516
def calcular_xi (n,i):
  xi = (i - 1.0/2.0) / n 
  return xi
  
def calcular_fxi (xi):
  fxi = 4.0 / (1.0 + xi * xi)
  return fxi
  
def arccot(x, unity):
  sum = xpower = unity // x
  n = 3
  sign = -1
  while 1:
    xpower = xpower// (x*x)
    term = xpower // n
    if not term:
      break
    sum += sign * term
    sign = -sign
    n += 2
  return sum
  
def decimales_pi (digits):
  unity = 10 ** (digits + 10)
  decimal_pi = 4 * (4*arccot(5, unity) -arccot(239, unity))
  return (float(decimal_pi // 10**10) / 10**digits)
 
def calcular_pi (n):
  VALOR_PI = 3.14159265358979311599796346854418516
  ini = 0
  intervalo = 1.0 / float (n)
  sumatorio = 0.0
  for i in range (n):
    xi = 0
    fxi = 0
    xi = calcular_xi(n, i+1)
    fxi = calcular_fxi (xi)
    ini += intervalo
    sumatorio += fxi
  valor_pi = sumatorio / n
  return (valor_pi)

if (__name__=="__main__"):
  argumentos = sys.argv[1:]
  if (len(argumentos) == 2):
    n = int (argumentos[0])
    aproximaciones = int (argumentos[1])
  else:
    print "Introduzca el numero de intervalos (n > 0):"
    n = int (raw_input ());
    print "Introduzca el numero de aproximaciones:"
    aproximaciones = int (raw_input ());
  if (n > 0):
    
    intervalo = n
    lista = []
    valor = 0
    for i in range (aproximaciones):
      valor = calcular_pi (intervalo)
      lista.append (valor)
      intervalo += n
    print lista
    diferencia = []
    for i in range (aproximaciones):
      dif = abs (PI35DT - lista[i])
      diferencia.append (dif)
    print "i\tPI35DT\tlista i\tPI35DT - lista i" 
    for i in range (aproximaciones):
      print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1, PI35DT, lista [i], diferencia [i])
      
  else:
    print "El valor de los intervalos debe ser mayor que 0"
  #print "El valor aproximado de PI es:", calcular_pi (n)

  


  
  
