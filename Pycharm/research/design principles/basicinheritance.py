#Author: OMKAR PATHAK
# Date: 8/4/2017

class Data(object):
    def __init__(self, data):
        self.data = data

    def getData(self):
        print('Data:',self.data)

class Time(Data):           #Inhertiting from Data class
    def getTime(self):
        print('Time:',self.data)

if __name__ == '__main__':
    data = Data(10)
    time = Time(20)     #inherited Class -> Value passed to __init__of Data (Base class)

    time.getTime()
    data.getData()
    time.getData()

    print(Time.mro())

# Another code example I have found on GitHub. It shows the use of inheritance simply and this has helped me grasp
# the concept much easier.
# The output of this code is: Time: 20 - Data: 10 - Data: 20
# The output shows that for the first call statement of time.getTime(), the compiler uses the def getTime() method
# in the child class with the given input.
# The second call statement of data.getData() uses the def getData() method in the parent class with the given input.
# The last call is what helps me understand inheritance the best. The child class is called, but with the superclasses
# method, which it directly inherits. The input is the 20 that was given in line 17. But the method that is called
# is the parent class method itself, but with the input of the child class. This is what inheritance is all about.