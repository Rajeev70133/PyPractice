# OOPS Concept - DRY Do not repeat
# Class - Template
# Object - Instance of Class

# class Student:
#     pass
#
# amit = Student()  # object 1
# Sumit = Student() # object 2
#
"""Below are the instance variable of objects of Student"""
# amit.name="Amit"
# amit.std=12
# amit.section=1
# Sumit.std=9
# print(amit.name, Sumit.std)

# ########################
# class Employee:
#     """Instance and class variable example"""
#     school_name = "papa ka school"
#     pass
# harry = Employee()
# rohan = Employee()
#
# harry.nam ="Harry"
# harry.tanqua = 500
# harry.role="Chutiyapa"
#
# rohan.nam ="Harry"
# rohan.tanqua = 500
# rohan.role="Maha Chutiyapa"
#
# print(rohan.role)
# print(rohan.school_name)
#
# Employee.school_name="Papa ki Pari ka hai"
# print(harry.school_name)
#
# rohan.school_name="Rohan k papa ka school"
#
# print(rohan.school_name)
# print(harry.school_name)
# print(rohan.__dict__)
# print(harry.__dict__)
# print(Employee.__dict__)
# print(Employee.school_name)
#########################################################
import params as params

"""__init__(self)"""
"""using @classmethod decorator we can create functions which will not call __init__(self) on every instance of that clas"""
#
#
# class Employee:
#     """Instance and class variable example"""
#     school_name = "papa ka school"
#
#     def __init__(self, name, salary, action):
#         self.nam = name
#         self.tanqua = salary
#         self.role = action
#
#     def print_details(self):
#         return f"Naam hai :{self.nam}, uska tankhwa hao {self.tanqua} or wo {self.role} hai. Wo {self.school_name}"
#
#     @classmethod
#     def chang_skol_func(cls, change_school):
#         cls.school_name = change_school
#
#     @classmethod
#     def from_str(cls, string):
#         return cls(*string.split("-"))
#         # params = string.split("-")
#         # return cls(params[0], params[1], params[2])
#
#
#
# amit = Employee("Amit Kumar", "300000", "Lad chat hai")
# sumit = Employee("Sumit Kumar", "10", "chaman Chutiya")
# ravi = Employee.from_str("Ravi-3000-Hamara")
#
# # harry = Employee()
# # rohan = Employee()
# #
# # harry.nam ="Harry"
# # harry.tanqua = 500
# # harry.role="Chutiyapa"
# #
# # rohan.nam ="Harry"
# # rohan.tanqua = 500
# # rohan.role="Maha Chutiyapa"
#
# # Employee.school_name = "Ye SUMIT & Amitt k baap ka school hai"
# amit.chang_skol_func("Krishna Public School")
# # sumit.chang_skol_func(" Budhaa School me ")
# print(amit.print_details())
# print(sumit.print_details())
# print(amit.school_name)
# print(sumit.school_name)
# print(ravi.print_details())
# print(ravi.school_name)

"""Static Method"""
# class Employee:
#     """Instance and class variable example"""
#     school_name = "papa ka school"
#
#     def __init__(self, name, salary, action):
#         self.nam = name
#         self.tanqua = salary
#         self.role = action
#
#     def print_details(self):
#         return f"Naam hai :{self.nam}, uska tankhwa hao {self.tanqua} or wo {self.role} hai. Wo {self.school_name}"
#
#     @classmethod
#     def chang_skol_func(cls, change_school):
#         cls.school_name = change_school
#
#     @staticmethod
#     def printsome(strng):
#         print("this is good : " + strng)
#
# amit = Employee("Amit Kr", 10000 , "Chutiya")
# sumit = Employee("Sumit Kr", 20000 , "ChutiyaHead")
#
#     # @classmethod
#     # def from_str(cls, string):
#     #     return cls(*string.split("-"))
#     #     # params = string.split("-")
#
# # return cls(params[0], params[1], params[2])# # sumit.chang_skol_func(" Budhaa School me ")
#
# print(amit.print_details())
# print(sumit.print_details())
# print(amit.school_name)
# print(sumit.school_name)
# # print(ravi.print_details)
# Employee.printsome("RajeevSome")
"""Abstraction & Encapsulation"""
"""Single Inheritance"""
# class Employee:
#     # """Instance and class variable example"""
#     school_name = "papa ka school"
#
#     def __init__(self, name, salary, action):
#         self.nam = name
#         self.tanqua = salary
#         self.role = action
#
#     def print_details(self):
#         return f"Naam hai :{self.nam}, uska tankhwa hao {self.tanqua} or wo {self.role} hai."
#
#     @classmethod
#     def chang_skol_func(cls, change_school):
#         cls.school_name = change_school
#
#     @staticmethod
#     def printsome(strng):
#         print("this is good : " + strng)
#
# class Programer(Employee):
#     def __init__(self, name, salary, action, Language):
#         self.no_of_bc = 10
#         self.nam = name
#         self.tanqua = salary
#         self.role = action
#         self.Language = Language
#
#
#
#
#     def print_programer(self):
#         return f"the management people nMe is {self.nam}, uski sallary hai{self.tanqua}, wo padha hai{self.school_name} anf he know {self.Language} and e {self.no_of_bc}"
#
# amit = Employee("Amit Kr", 10000 , "Chutiya")
# sumit = Employee("Sumit Kr", 20000 , "ChutiyaHeadProgramer")
#
# ravi= Programer("Ravi", 18000, "ManagerChutiya", ["abcd"])
# kavi = Programer("kavi", 77000, "LeadChutiyaProgramer", ["xyhz"])
#
#     # @classmethod
#     # def from_str(cls, string):
#     #     return cls(*string.split("-"))
#     #     # params = string.split("-")
#
# # return cls(params[0], params[1], params[2])# # sumit.chang_skol_func(" Budhaa School me ")
#
# print(amit.print_details())
# print(sumit.print_details())
# print(amit.school_name)
# print(sumit.school_name)
# # print(ravi.print_details)
# Employee.printsome("RajeevSome")
# print(kavi.print_details())
# print(kavi.print_programer())

"""Multiple Inheritance"""
# class Employee:
#     # """Instance and class variable example"""
#     school_name = "papa ka school"
#
#     def __init__(self, name, salary, action):
#         self.nam = name
#         self.tanqua = salary
#         self.role = action
#
#     def print_details(self):
#         return f"Naam hai :{self.nam}, uska tankhwa hao {self.tanqua} or wo {self.role} hai."
#
#     @classmethod
#     def chang_skol_func(cls, change_school):
#         cls.school_name = change_school
#
#     @staticmethod
#     def printsome(strng):
#         print("this is good : " + strng)
#
# class Player:
#     no_of_games = 4
#     def __init__(self, name, game):
#         self.name = name
#         self.game = game
#
#     def print_gam_details(self):
#         return f"Naam hai :{self.name}, wo {self.game} khrlta hai."
#
# class CoolPerson(Employee, Player):
#     language = "Pytnon"
#     def printLanguage(self):
#         print(self.language)
#
# amit = Employee("Amit Kr", 10000 , "Chutiya")
# sumit = Employee("Sumit Kr", 20000 , "ChutiyaHeadProgramer")
#
# ravi = Player("ravi Kr", ["Football"])
#
# kavi = CoolPerson("Kavi Kr", 880000, "Code")
#
# print(Player.print_gam_details(ravi))
# print(kavi.print_details())
# kavi.printLanguage()
"""Multilevel Inheritance"""
# class Dad:
#     game = 5
# class Son(Dad):
#     dance = 4
#     game = 2
#     def candance(self):
#         return f"Yes i can dance in {self.dance} ways and as my dad was player i also play {self.game}"
# class Grandson(Son):
#     musicalInstrument = 2
#     dance = 8
#     def candance(self):
#         return f"I can also dance in {self.dance} and can also play {self.musicalInstrument} musical instrumengt and acan also play {self.game}"
#
#
# dadag = Dad()
# betag = Son()
# potag = Grandson()
#
# print(potag.dance)
# print(betag.dance)
# print(potag.game)
# print(Grandson.candance(potag))
"""Access Specifiers, Name Angling"""
# Public
# Protected "(._VariableNam)"
# Private "(._className__variableName)"
# class Employee:
#     # """Instance and class variable example"""
#     school_name = "papa ka school"
#     var = 8
#     _abc = 10
#     __def = 20
#
#     def __init__(self, name, salary, action):
#         self.nam = name
#         self.tanqua = salary
#         self.role = action
#
#     def print_details(self):
#         return f"Naam hai :{self.nam}, uska tankhwa hao {self.tanqua} or wo {self.role} hai."
#
#     @classmethod
#     def chang_skol_func(cls, change_school):
#         cls.school_name = change_school
#
#     @staticmethod
#     def printsome(strng):
#         print("this is good : " + strng)
#
#
# amit = Employee("Amit Kr", 10000 , "Chutiya")
# sumit = Employee("Sumit Kr", 20000 , "ChutiyaHeadProgramer")
#
# # print(amit._abc)
# print(amit._Employee__def)
"""Polymorphism"""
# print(1+3)
# print("1"+"3")
# Abstraction
# Encapsulation
# inheritance
# Polymorphism
# class Employee:
#     # """Instance and class variable example"""
#     school_name = "papa ka school"
#     var = 8
#     _abc = 10
#     __def = 20
#
#     def __init__(self, name, salary, action):
#         self.nam = name
#         self.tanqua = salary
#         self.role = action
#
#     def print_details(self):
#         return f"Naam hai :{self.nam}, uska tankhwa hao {self.tanqua} or wo {self.role} hai."
#
#     @classmethod
#     def chang_skol_func(cls, change_school):
#         cls.school_name = change_school
#
#     @staticmethod
#     def printsome(strng):
#         print("this is good : " + strng)
#
#
# amit = Employee("Amit Kr", 10000 , "Chutiya")
# sumit = Employee("Sumit Kr", 20000 , "ChutiyaHeadProgramer")
# print(amit)
""""Super() & Overriding in classes, super().__init__()"""
# class A:
#     classVaribleA1 = "I am class variable in class A"
#     def __init__(self):
#         self.var1 = "Instance variable of class A constroctor"
#         self.classVaribleA1 = "Instance var in class A "
#         self.extra = "Added var"
#
# class B(A):
#     classVaribleA1 = "I am class variable in class B"
#     def __init__(self):
#         super().__init__()
#         self.var1 = "Instance variable of class B constroctor"
#         self.classVaribleA1 = "Instance var in class B "
#
# amit = A()
# satish = B()
#
# print(amit.classVaribleA1)  # insted of printing "Instance variable of class A constroctor" it has printed constroctors msg
# print(amit.var1)
#
# print(satish.classVaribleA1)
# print(satish.extra)
