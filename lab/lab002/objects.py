# class Student:
#     pass

# s1 = Student()
# print(s1)

###

# class Student:
#     def __init__(self, name):
#         self.name = name
    
#     def __str__(self):
#         return f'My name is {self.name}. James {self.name}.'

#     def print_my_name(self):
#         print(f'{self.name = }')

# s1 = Student('Bożydar')
# print(s1)
# print(s1.name)
# s1.print_my_name()

###

# class Student:
#     classes = []

#     def __init__(self, name):
#         self.name = name
    
#     def __str__(self):
#         return f'My name is {self.name}. James {self.name}.'

#     def print_my_name(self):
#         print(f'{self.name = }')

#     def print_classes(self):
#         print(self.classes)
#     def add_class(self, cl):
#         self.classes.append(cl)

# s1 = Student('Bożydar')
# s1.add_class('PwZN')
# s1.add_class('WdPRiR')
# s1.add_class('FK')
# s1.add_class('FS')
# s1.print_classes()
# s2 = Student('Ziemowit')
# s2.print_classes()

###

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.classes = []
    
#     def __str__(self):
#         return f'My name is {self.name}. James {self.name}.'

#     def print_my_name(self):
#         print(f'{self.name = }')

#     def print_classes(self):
#         print(self.classes)
#     def add_class(self, cl):
#         self.classes.append(cl)

# s1 = Student('Bożydar')
# s1.add_class('PwZN')
# s1.add_class('WdPRiR')
# s1.add_class('FK')
# s1.add_class('FS')
# s1.print_classes()
# s2 = Student('Ziemowit')
# s2.print_classes()

###

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.classes = []
    
#     def __str__(self):
#         return f'My name is {self.name}. James {self.name}.'

#     def print_my_name(self):
#         print(f'{self.name = }')

#     def print_classes(self):
#         print(self.classes)
#     def add_class(self, cl):
#         self.classes.append(cl)

# s1 = Student('Bożydar')
# print(s1.__dict__)
# s1.nie_ma_mnie = 'lol'
# print(s1.__dict__)
# print(Student.__dict__)
# Student.__dict__['print_my_name'](s1)

###

# x = [2, 5, 3, 56, 7, 3]
# for i in x:
#     print(i)

###

# class LameList:
#     def __init__(self):
#         self._list = []

#     def add_to_list(self, element):
#         self._list.append(element)

#     def __iter__(self):
#         self._index = -1
#         return self

#     def __next__(self):
#         self._index += 1
#         if self._index < len(self._list):
#             return self._list[self._index]
#         else:
#             raise StopIteration()

# ll = LameList()
# ll.add_to_list('Bożydar')
# ll.add_to_list('Ziemowit')
# ll.add_to_list('Genowefa')

# for element in ll:
#     print(element)

###

class LameList:
    def __init__(self):
        self._list = []

    def add_to_list(self, element):
        self._list.append(element)

    def __iter__(self):
        for e in self._list:
            yield e

ll = LameList()
ll.add_to_list('Bożydar')
ll.add_to_list('Ziemowit')
ll.add_to_list('Genowefa')

for element in ll:
    print(element)