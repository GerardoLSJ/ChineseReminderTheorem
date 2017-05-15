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

# print(inverso(2, 7))
#print(teoremaChino([2, 3, 2], [3, 5, 7]))


#Agregar GCD(x, y)
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


from operator import mul
import functools

def GCD(a,b):
	a_primes = prime_factors(a)
	b_primes = prime_factors(b)
	max_a = a_primes[len(a_primes)-1]
	max_b = b_primes[len(b_primes)-1]
	max_global = max(max_a,max_b)
	factors_p = []
	print(a_primes)
	print(b_primes)
	for i in range(2,max_global+1):
		a_ocu = a_primes.count(i)
		b_ocu = b_primes.count(i)
		x = min(a_ocu, b_ocu)
		#print('x: ' + str(x))
		#print('i: ' + str(i))
		factors_p.append(pow(i,x))
		#print(factors_p)

	print(functools.reduce(mul, factors_p, 1))


GCD(1921,9639)


def min(x, y): 
	if x < y: return x
	else: return y













