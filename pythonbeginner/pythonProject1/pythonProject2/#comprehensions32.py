#      WITHOUT USING COMPREHENSIONS ---------------
# listA = []
# for a in range(50):
#     if a%5 ==0:
#         listA.append(a)
#     print(a)
# lstA = [a for a in range(50) if a%5 ==0]
# print(lstA)
# Normaldict = {
#     0: "item 0",
#     1: "item 1",
#     2: "item 2",
#     3: "item 3",
#     4: "item 4"
# }
# print(Normaldict)

# dict1 = { i:f"Item {i}" for i in range(5)}
# print(dict1)
#--------------without comprehension in generator -----------------------#
# def gener(n):
#     for i in range(n):
#         yield i
# a = gener(5)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# =============== with comprehension for generator ====================#
# gener = (i for i in range(5))
# print(gener.__next__())
# print(gener.__next__())
# print(gener.__next__())