# %% [markdown]
# ## Variables

# %% [markdown]
# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# %%
a = 12
print(a)

# %% [markdown]
# 2) Imprimir el tipo de dato de la constante 8.5

# %%
type(8.5)

# %% [markdown]
# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# %%
type(a)

# %% [markdown]
# 4) Crear una variable que contenga tu nombre

# %%
mi_nombre = 'juan carlos perez'

# %% [markdown]
# 5) Crear una variable que contenga un número complejo

# %%
n_complejo = 5 + 5j

# %% [markdown]
# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# %%
type(n_complejo)

# %% [markdown]
# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# %%
pi = 3.1416

# %% [markdown]
# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# %%
var1 = 'True'
var2 = True

# %% [markdown]
# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

# %%
print('La variable 1 es de tipo ', type(var1), ' y la variable 2 es de tipo ', type(var2))

# %% [markdown]
# 10) Asignar a una variable, la suma de un número entero y otro decimal

# %%
a = 5.2 + 4

# %% [markdown]
# 11) Realizar una operación de suma de números complejos

# %%
a = 3 + 1j
b = 1 + 3j
print(a + b)

# %% [markdown]
# 12) Realizar una operación de suma de un número real y otro complejo

# %%
c = a + 1.61
print(c)

# %% [markdown]
# 13) Realizar una operación de multiplicación

# %%
print(3 * 2)

# %% [markdown]
# 14) Mostrar el resultado de elevar 2 a la octava potencia

# %%
print(2**8)

# %% [markdown]
# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# %%
a = 27 / 4
print(a)

# %% [markdown]
# 16) De la división anterior solamente mostrar la parte entera

# %%
print(27 // 4)

# %% [markdown]
# 17) De la división de 27 entre 4 mostrar solamente el resto

# %%
27 % 4

# %% [markdown]
# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# %%
6 * 4 + 3

# %% [markdown]
# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# %%
var1 = 'Buenos '
var2 = 'Aires'
print(var1 + var2)

# %% [markdown]
# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# %%
2 == '2'

# %% [markdown]
# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# %%
2 == int('2')

# %% [markdown]
# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# %%
a = float('3,8')

# %% [markdown]
# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

# %%
a = -3
a -= 1
print(a)

# %% [markdown]
# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# %%
1 << 2

# %% [markdown]
# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# %%
2 + '2'

# %%
float(2) + float('2')

# %%
int(2) + int('2')

# %%
str(2) + str('2')

# %% [markdown]
# 26) Realizar una operación válida entre valores de tipo entero y string

# %%
var1 = 'este texto se repite '
var2 = 3
print(var1 * var2 + str(var2) + ' veces')


