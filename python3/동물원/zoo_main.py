from tkinter import *


def categorize(animal_list):
    mammal = []
    bird = []
    aquatic = []
    reptile = []
    insect = []
    for i in animal_list:
        if i.groups == 'Mammal':
            mammal.append(i)
        elif i.groups == 'Bird':
            bird.append(i)
        elif i.groups == 'Aquatic':
            aquatic.append(i)
        elif i.groups == 'Reptile':
            reptile.append(i)
        elif i.groups == 'Insect':
            insect.append(i)
    return mammal, bird, aquatic, reptile, insect


def main():
    while True:
        print('''**************************************************
Korea Zootopia
--------------------------------------------------
1. Show Zoo Animals Catalog.
2. Display Zoo Animals Charts.
3. Generate Zoo Animals Text Files
4. Add Animal
5. Delete Animal
6. Quit
**************************************************
Enter your choice:''')
        choice = int(input())
        if choice == 1:
            animals = parsing()
            mammal, bird, aquatic, reptile, insect = categorize(animals)
            choice_1(mammal, bird, aquatic, reptile, insect)
        elif choice == 2:
            animals = parsing()
            mammal, bird, aquatic, reptile, insect = categorize(animals)
            choice_2(mammal, bird, aquatic, reptile, insect)
        elif choice == 3:
            animals = parsing()
            mammal, bird, aquatic, reptile, insect = categorize(animals)
            choice_3(mammal, bird, aquatic, reptile, insect)
        elif choice == 4:
            choice_4()
        elif choice == 5:
            choice_5()
        elif choice == 6:
            break


def parsing():
    animal_object = []
    animals_txt = open('./animal.txt', 'r')
    contents = animals_txt.read()
    animal_list = contents.split('\n')
    for i in range(len(animal_list)):
        animal = animal_list[i].split()
        if not animal:
            continue
        else:
            a = Animal(animal[0], animal[1], animal[2])
            animal_object.append(a)

    return animal_object


def choice_5():
    index = 1
    contents = []

    f = open('animal.txt', mode='rt', encoding='utf-8')
    for line in f:
        contents.append(line)
        print(str(index)+'. '+line)
        index += 1
    f.close()

    f = open('animal.txt', mode='wt', encoding='utf-8')
    delete_line = int(input('''Which row do you want to delete? '
    select number : 1 ~ ''' + str(index - 1) + ' : ')) - 1
    try:
        contents[delete_line] = ''
    except IndexError:
        print('You must enter the number between 1 and '+str(index - 1))
    for line in contents:
        f.write(line)
    f.close()


def choice_4():
    animals = open('animal.txt', 'a', encoding='utf-8')
    name = input('Enter a new Animal name : ')
    name += '\n' + name + ' '
    species = input('Enter a new Animal species : ')
    species += ' '
    groups = input('Enter a new Animal groups : ')
    groups += ' '
    new_row = name + species + groups
    animals.write(new_row)
    animals.close()


def choice_3(mammal, bird, aquatic, reptile, insect):
    mammal_txt = open('mammal.txt', 'w', encoding='utf-8')
    bird_txt = open('bird.txt', 'w', encoding='utf-8')
    aquatic_txt = open('aquatic.txt', 'w', encoding='utf-8')
    reptile_txt = open('reptile.txt', 'w', encoding='utf-8')
    insect_txt = open('insect.txt', 'w', encoding='utf-8')

    for i in range(len(mammal)):
        mammal_txt.write(str(i + 1) + '.' + mammal[i].name + '\t' + mammal[i].species + '\n')
    for i in range(len(bird)):
        bird_txt.write(str(i + 1) + '.' + bird[i].name + '\t' + bird[i].species + '\n')
    for i in range(len(aquatic)):
        aquatic_txt.write(str(i + 1) + '.' + aquatic[i].name + '\t' + aquatic[i].species + '\n')
    for i in range(len(reptile)):
        reptile_txt.write(str(i + 1) + '.' + reptile[i].name + '\t' + reptile[i].species + '\n')
    for i in range(len(insect)):
        insect_txt.write(str(i + 1) + '.' + insect[i].name + '\t' + insect[i].species + '\n')

    mammal_txt.close()
    bird_txt.close()
    aquatic_txt.close()
    reptile_txt.close()
    insect_txt.close()


def choice_2(mammal, bird, aquatic, reptile, insect):
    T = Tk()
    C = Canvas(T, width=700, height=400)
    T.geometry('700x400')
    T.title('')

    C.create_line(10, 10, 690, 10)
    C.create_text(300, 30, text='            Korea Zootopia Animals Bar Chart            ')
    C.create_line(10, 50, 690, 50)
    y = 100
    text = ['Mammal', 'Bird', 'Aquatic', 'Reptile', 'Insect']
    for i in range(5):
        C.create_text(75, y, text=text[i])
        y += 50
    y2 = 90
    y3 = 115
    data = [len(mammal), len(bird), len(aquatic), len(reptile), len(insect)]
    fill_color = ['green', 'navy', 'yellow', 'orange', 'pink']
    for i in range(5):
        C.create_rectangle(120, y2, 120 + data[i] * 50, y3, fill=fill_color[i])
        y2 += 50
        y3 += 50
    C.create_line(10, 390, 690, 390)
    C.pack()
    T.mainloop()


def choice_1(mammal, bird, aquatic, reptile, insect):
    x = 15
    y = 100
    index = 1
    T = Tk()
    C = Canvas(T, width=520, height=650)
    T.geometry('520x650')
    T.title('')
    C.create_line(10, 10, 500, 10)
    C.create_text(260, 30, text='Korea Zootopia Animals Catalog')
    C.create_line(10, 50, 500, 50)
    C.create_text(x, 70, text='Mammal', anchor=W)

    for i in mammal:
        C.create_text(x, y, text=str(index) + '. ' + i.name + '\t' + i.species, anchor=W)
        index += 1
        y += 20
    C.create_line(10, y, 500, y)
    y += 20
    C.create_text(x, y, text='Bird', anchor=W)
    index = 1
    for i in bird:
        y += 20
        C.create_text(x, y, text=str(index) + '. ' + i.name + '  ' + i.species, anchor=W)
        index += 1
    y += 20
    C.create_line(10, y, 500, y)
    y += 20
    C.create_text(x, y, text='Aquatic', anchor=W)
    index = 1
    for i in aquatic:
        y += 20
        C.create_text(x, y, text=str(index) + '. ' + i.name + '  ' + i.species, anchor=W)
        index += 1
    y += 20
    C.create_line(10, y, 500, y)
    y += 20
    C.create_text(x, y, text='Reptile', anchor=W)
    index = 1
    for i in reptile:
        y += 20
        C.create_text(x, y, text=str(index) + '. ' + i.name + '  ' + i.species, anchor=W)
        index += 1
    y += 20
    C.create_line(10, y, 500, y)
    y += 20
    C.create_text(x, y, text='Insect', anchor=W)
    index = 1
    for i in insect:
        y += 20
        C.create_text(x, y, text=str(index) + '. ' + i.name + '  ' + i.species, anchor=W)
        index += 1
    y += 20
    C.create_line(10, y, 500, y)
    C.pack()
    T.mainloop()


class Animal:
    def __init__(self, name, species, groups):
        self.name = name
        self.species = species
        self.groups = groups

    def __str__(self):
        return "{}\t{}".format(self.name, self.species)


if __name__ == '__main__':
    main()
