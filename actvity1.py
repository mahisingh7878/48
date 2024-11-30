#then , create an object for child and class and call the display method to display the name and idum=number.

#parent class 
class person:
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber=idnumber

    def display(self):
        print("name of person  ",self.name,"and id is ",self.idnumber)


#child class
class employee(person):
     def __init__(self, name, idnumber,salary,post):
         self.salary=salary
         self.post=post
         super().__init__(name,idnumber)


emp1=employee("ali",1234,15000,"intern")
emp1.display()
print("salary of ",emp1.name,"is ",emp1.salary )
        
    


     
