#Write a program to implement abstraction on animal class (base class). The abstract method will be move that is for displaying what subclasses can do.

from abc import ABC

#abstract class
class animal(ABC):
    #abstract method 
    def move(self):
        pass

class human(animal):
     def move(self):
         return"i can walk and run "
     
     
class snake(animal):
    def move(self):
        return"i can crawl"
    
class lion(animal):
     def move(self):
         return"i can roar"
     
class cat(animal):
    def move(self):
        return"i can meow"
    

h=human()
print(h.move())

s=snake()
print(s.move())

l=lion()
print(l.move())

c=cat()
print(c.move())
        