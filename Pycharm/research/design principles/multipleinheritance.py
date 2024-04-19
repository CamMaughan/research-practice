#Author: OMKAR PATHAK


class A(object):
    def doThis(self):
        print('Doing this in A')

class B(A):
    pass

#If class C was also being derived from A then the lookup order would be D,B,C,A
class C(object):
    def doThis(self):
        print('Doing this in C')

class D(B, A):
    pass

if __name__ == '__main__':
    dObj = D()
    dObj.doThis() #A method gets called because order for lookup is D,B,A this is shown by function mro

    print(D.mro())


# The output of this code is: Doing this in A, [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>,
# <class 'object'>]
# The output shows that the method doThis() is called from class A.
# mro method stands for Method Resolution Order. Which dictates the order Python looks for methods on instances of
# a class.
# Class D is dervied from B and A, in that order. So once python looks for the method in D, it goes to B and then to A.
# I can change the order of inheritance for classes A and C to see how the output changes. Though simply, Python will
# look for the method in the first class that is inherited from. If it is not found, it will look in the next class
# and so on. If the method is not found in any of the classes, it will throw an error.
