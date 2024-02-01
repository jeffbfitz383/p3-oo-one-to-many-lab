class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner =""):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, value):
        if value not in Pet.PET_TYPES:
            raise TypeError("Pet type must be on the list of accepted pets")
        self._pet_type = value

class Owner:
    
    def __init__(self, name):
        self.name = name

    def pets(self):
        pet_list = []
        for pet in Pet.all:
            if pet.owner == self:
                pet_list.append(pet)
        return pet_list

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of pet class")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
        #new_list = []
        #for pet in Pet.all:
            #if pet.owner == self:
               # new_list.append(pet)
       # x = sorted(new_list)
       # return x