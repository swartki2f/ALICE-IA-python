'''
introduction à NumPy.....

la bibliothèque Numpy permet  d'effectuer des calculs 
numeriques
avec Python. Elle introduit une gestion facilitée 
des tableaux de nombres

Pour utiliser numpy vous devez au préalable vous 
placer dans un environnemnet  qui comprend cette bibliothèque 

il faut au départ importer le package numpy avec l'instruction suivante:

import numpy as np


'''

import numpy as np 

#variable pi 
#numpy permet d'obtenir la valeur de pi 

np.pi
print(np.pi)

#tableau
#numpy.array()

#creation

'''
    les tableaux (en anglais array) peuvent être créés avec
    numpy.array(). On utilise des crochets pour délimiter les listes
    d'éléments dans les tableaux 
'''

a = np.array([1,2,3,4])

#affichage 
print(a)
print(type(a)) #numpy.ndarray


#accès aux élément d'un tableau 

print(a[0])

'''
Tableau de 2D: il est possible de créer un tableau 
2D en utilisant une liste 
de listes au moyen de croches imbriqués. les listes internes
correspondent à des lignes du tableau

'''
b = np.array([[1,2,3],[4,5,6]])
print(b)

#accès aux  éléments d'un tabeau 2D

print(b[0,2])

#tableau à 3D :trois lignes 

c=np.array([[1,2,3],[6,8,9],[0,7,4]])
print(c)
print(type(c))

#la fonction arange()
#numpy.arange()

m= np.arange(3,15,2)
print(m) #type m : numpy.ndarray

#range est different de arange
n= range(3,15,2)
print(n)

u=[3,7,10]#u est une liste : type > list

#il est possible d'obtenir des listes en combinant list et range()

list(range(3,15,2)) 

#la fonction numpy.arange() accepte des arguments qui ne sont
pas des entiers 

s = np.arange(0,11*np.pi,np.pi)
print(s)

'''
la fonction numpy.linspace() permet d'obtenir 
un tableau 1D allant d'une valeur de départ à une valeur de fin
avec un nombre donné d'éléments.

'''
t= np.linspace(3,4,5)
print(t)





#Action d’une fonction mathématique sur un tableau

#NumPy dispose d’un grand nombre de fonctions mathématiques qui peuvent être appliquées directement à un tableau. Dans ce cas, la fonction est appliquée à chacun des éléments du tableau.

x = np.linspace(-np.pi/2, np.pi/2, 3)
print(x)
y = np.sin(x)
print(y)