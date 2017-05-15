'''
Función inverso
Parámetros: x, mod
x es el número del cuál se quiere sacar el inverso
mod es el módulo que se empleará
Regresa una cadena con el inverso multiplicativo si es que existe y con un mensaje de error en caso contrario
'''

def inverso(x, mod):
	existeInverso = False
	inverso = 0
	#Itera desde 0 hasta el módulo
	for a in range(0, mod):
		#Si se cumple la igualdad, existe el inverso
		if ((x*a) % mod) == 1: 
			return a

	return "No se encontró el inverso"

def teoremaChino(elements, modules):
	m = 1
	M = list()
	I = list()
	sol = 0
	index = 0
	for module in modules: 
		m = m * module
	for module in modules: 
		M.append(int(m/module))
		I.append(inverso(M[index], modules[index]))
		sol = sol + (elements[index] * M[index] * I[index])
		index = index + 1

	# print(M)
	# print(I)
	# print(sol)
	return sol

def factores(num): #diccionario de numero de veces de factores primos L{factor1: veces, ..., factorn,]
	div = 2
	L = {}
	while(num >= div):
		if(num % div == 0):
			L[div] = 0
			while(num % div ==0):
				L[div] += 1
				num = num / div

		div = div + 1
	return L

def minimo(A, B): 
	minimos = {}
	#print(A)
	#print(B)
	if(len(A) >= len(B)):
		for p in A.items():
			if(B.get( p[0] ) != None):
				minimos[ p[0] ] = min(p[1], B[p[0]])
	
	else:
		for p in B.items():
			if(A.get( p[0] ) != None):
				minimos[ p[0] ] = min(p[1], A[p[0]])
	
	#print(minimos)
	return minimos

def maximo(A, B): 
	maximos = {}
	#print(A)
	#print(B)
	if(len(A) >= len(B)):
		maximos = A
		for p in B.items():
			if(maximos.get( p[0] ) != None):
				maximos[ p[0] ] = max(p[1], maximos[p[0]])
			else:
				maximos[p[0]] = p[1]
	else:
		maximos = B
		for p in A.items():
			if(maximos.get( p[0] ) != None):
				maximos[ p[0] ] = max(p[1], maximos[p[0]])
			else:
				maximos[p[0]] = p[1]
	#print(maximos)
	return maximos

def gcd(x, y):
	#print(factores(x))
	#print(factores(y))
	result = 1;
	valores = minimo(factores(x),factores(y))
	#print(valores)
	for p in valores.items():
		result = result * pow(p[0], p[1])

	return result

def lcm(x, y):
	result = 1;
	valores = maximo(factores(x),factores(y))
	#print(valores)
	for p in valores.items():
		result = result * pow(p[0], p[1])

	return result



a = 1921
b = 9639
x = lcm(a,b)
y = gcd(a,b)
print("valores:    a = "+str(a) + "       b = " + str(b))
print("maximo comun divisor: " + str(y))
print("minimo comun multiplo: " + str(x))
print("se comprueba el teorema a*b = lcm(a,b)*gcd(a,b):   " + str(a*b) + "=" + str(x*y))


# print(inverso(2, 7))
#print(teoremaChino([2, 3, 2], [3, 5, 7]))
