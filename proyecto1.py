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
print(teoremaChino([2, 3, 2], [3, 5, 7]))


#Agregar GCD(x, y)

def min(x, y): 
	if x < y: return x
	else: return y













