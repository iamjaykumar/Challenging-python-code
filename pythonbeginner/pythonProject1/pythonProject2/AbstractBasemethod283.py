# # from abc import ABC , abstractmethod
# # class shape(ABC):
# #     @abstractmethod
# #     def printarea(self):
# #         return 0
# # class Rectangle(shape):
# #     type = "Rectangle"
# #     sides = 4
# #     def __init__(self):
# #         self.lenth = 6
# #         self.breadth = 23
# #     def printarea(self):
# #         return self.lenth * self.breadth
# #
# # rect1  = Rectangle()
# # print(rect1.printarea())
# # #---------------------------#---------------------
# from abc import ABC , abstractmethod
# class shape(ABC):
#     @classmethod
#     def printarea(cls):
#         return 0
# class Square(shape):
#     type = "Shape"
#     sides = 4
#     def __init__(self):
#         side = 4
#         side = 0
#     def printarea(cls):
#         return cls.sides * cls.sides
# sq = Square()
# print(sq.printarea())
