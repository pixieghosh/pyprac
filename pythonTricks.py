
#%%
from datetime import datetime
from typing import Dict

#%%
class Person:
    def __init__(self, name, age, race):
        self.name = name 
        self.age = age 
        self.race = race
    def __str__(self): #prints specific string when print(instance) is called
        return f'my name is {self.name} and I am {self.age} years old'
    def __eq__(self,other):
        return self.age == other.age
    def __ne__(self, o):
        return self.age != o.age
    def __ge__(self,other):
        return self.age >= other.age
    def __le__(self,other):
        return self.age <= other.age
    def __gt__(self,other):
        return self.age > other.age
    def __lt__(self,other):
        return self.age < other.age
    def __hash__(self):
        return hash(self.name + self.race)
    @property
    def birthyear(self):
        return datetime.now().year - self.age
    @birthyear.setter
    def birthyear(self, val):
        self.age = datetime.now().year - val 

pix = Person('pix',22,'asian')
dad = Person('dad',54,'asian')
pix.birthyear = 11
print(pix.age)
# %%
hash('pixie')

# %%
def sum(*args):
    total = 0
    for itm in args:
        total += int(itm)
    return total 

print(sum(3,4,78,2,5,7,3,2,5,7,4))
# %%
def varArg(**kwargs):
    if 'age' in kwargs:
        return kwargs['age']*10
    else:
        return None
print(varArg(**{'name':'pix','race':'asian','age':22}))
# %%
def up(s) -> str: # shows that function returns str
    return s.upper()

def multage(p: Person): # shows that function takes person class
    return p.age

def func(d: Dict[str,int]):
    d['pix'].
# %%
def pow4(x : int) -> int:
    return x**4

print(pow4(2))
# %%
l = [2,3,4]
[pow4(i) for i in l]
print(list(map(pow4,l)))
# %%
