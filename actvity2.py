#Write a program to create a parent class Person (attributes - fname, lname) with a method printname to display the full name. Create a child class Student (attributes - fname, lname, year). Access the attributes of parent class in child class using super() function. Then, create an object for the child class and call the display method to display the full name. Also, print the graduation year.

class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname=lname

    def display(self):
        print("name of person  ",self.fname,"and id is ",self.lname)


#child class
class student(person):
     def __init__(self, fname, lname,year):
         self.graductionyear=year
         
         super().__init__(fname,lname)


stud1=student("mahi" ,"singh",2030)
stud1.display()
print(stud1.fname,"was graduated in the year ",stud1.graductionyear)
        
    
