from django.db import models

# Create your models here.
class Cat():
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

cats = [
  Cat('Lolo', 'tabby', 'foul little demon', 3),
  Cat('Jerry', 'tortoise shell', 'he is really chunky', 6),
  Cat('Raven', 'black tripod', '3 legged cat', 4)
]