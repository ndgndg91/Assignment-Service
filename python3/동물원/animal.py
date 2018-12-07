class Animal():
    def __init__(self, name, species, groups):
        self.name = name
        self.species = species
        self.groups = groups

    def __str__(self):
        return "{}\t{}".format(self.name, self.species)