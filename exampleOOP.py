class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} is {self.age} years old"

class Employee(Person):
  def __init__(self, name, age, salary):
    super().__init__(name, age)
    self.salary = salary
  def __str__(self):
    return f"{super().__str__()} and receives {self.salary} dollars per month"

if __name__ == '__main__':
  person = Person('John', 36)
  print(person.name)
  print(person)
  student = Employee('Todor', 36, 20000)
  print(student)

  osobe = [person, student]
  for person in osobe:
    print(person)

class EmptyClass:
  pass