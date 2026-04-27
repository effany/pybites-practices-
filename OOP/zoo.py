class Animal:
    list_animals = []
    def __init__(self, name):
        self.name = name
        self.initial_num = 10000
        index_animal = (len(self.list_animals) + 1) + self.initial_num
        self.list_animals.append(f"{index_animal}. {self.name.capitalize()}")

    def __str__(self):
        status, index = self.has_animal(self.name)
        if status == 'True':
             print(self.list_animals[index])
             return self.list_animals[index]

    @classmethod
    def zoo(cls):
        return '\n'.join(cls.list_animals)
    
    @classmethod
    def has_animal(cls, name):
        for index, item in enumerate(cls.list_animals):
             if item.split(". ", 1)[1].lower() == name.lower():
                  return ['True', index]

        
animals_dict = {}
for animal in 'dog cat fish lion mouse'.split():
        animals_dict[animal] = Animal(animal)

print(Animal.zoo())
print(str(animals_dict['cat']))