# # # # # creating a dictionary
# # # # # my_dict = {"name":"jay" , "age": 18 , "city ":" purnia"}
# # # # # print(my_dict)
# # # # # name_in_dict = my_dict["name"]
# # # # # print(name_in_dict)
# # # # # my_dict["email"] = "jaykumarkbp@gmail.com"
# # # # # print(my_dict)
# # # # # del my_dict['email']
# # # # # print(my_dict)
# # # # # #check for keys
# # # # # my_dict = {"name":"jay" , "age": 18 , "city ":" purnia"}
# # # # # if "name" in my_dict:
# # # # #     print(my_dict['name'])
# # # # # try:
# # # # #     print(my_dict["age"])
# # # # # except KeyError:
# # # # #     print("no found ")
# # # # #     # lopping in dictionary
# # # # # for dict in my_dict:
# # # # #     print(dict, my_dict[dict])
# # # # #
# # # # #
# # # #
# # # #
# # # # dict_org = {"name":"sarswati", "age":"28389", "city":"heaven"}
# # # # dict_copy = dict_org
# # # # print(dict_copy)
# # # # dict_copy["name"] = "Jay"
# # # # print(dict_org)
# # # # print(dict_copy)
# # # # dict_org = {"name":"sarswati", "age":"28389", "city":"heaven"}
# # # # dict_copy = dict_org.copy() #if we are using the copy() arguments then dict.org is not copy dict_org is still remain .
# # # # dict_copy['name'] = "Jay"
# # # # print(dict_org)
# # # # print(dict_copy)
# # # dict_org = {"name":"sarswati", "age":"28389", "city":"heaven"}
# # # dict_org2 = {"name":"jay" , "age":"18", "city":"purnia"}
# # # dict_org.update(dict_org2)
# # # print(dict_org)
# # # my_dict = {3:9, 9:12, 12:18}
# # # print(my_dict[3], my_dict[9], my_dict[12])
# # # nested_dict = { "dictA": dict_org,
# # #                 "dictB": dict_org2}
# # # print(nested_dict)
# #
# #
# #
# # # my_set = []
# # # print(type(my_set))
# # # a = set()
# # # # print(type(a))
# # # my_set = {"apple", "banana" , "cherry"}
# # # # print(my_set)
# # # my_set_2 = set(["one", "two", "three"])
# # # my_set_2 = set(("one" , "two ", "three"))
# # #
# # # print(my_set_2)
# # # my_set_3 = set("aadsfasdjfdsljafkhuodhsifjjdifajufewjkijfjkdhjdjfj eruurtuyr4t843ut7iefjhfuhj")
# # # print(my_set_3)
# # # # my_set = set()
# # # my_set.add("Hello")
# # # my_set.add("Jay")
# # # my_set.add(7328)
# # # print(my_set)
# # # my_set.remove("Jay")
# # # print(my_set)
# # my_set = {"apple", "banana" , "cherry"}
# # for set in my_set:
# #     print(set)
# #
# # odds = {1,3,5,7,9}
# # evenss = {0, 2 ,4 ,6 ,8 }
# # primes = {2, 3, 5, 7}
# #
# # f = odds.union(evenss)
# # print(f)
# # f = odds.intersection(evenss)
# # print(f)
# # g = evenss.intersection(odds)
# #
# # print(g)
# # g = evenss.union(odds)
# #
# # print(g)
# # g = primes.intersection(evenss)
# # print(g)
# # g  = primes.union(odds)
# #
# # print(g)
#
# setA = {1,2,3,4,5,6,7,8,9,0}
# setB = { 1,3,5, 38}
# #---------symmetric difference returns  a set with all the elements that are in setA but not have in setB
#
# diff_set = setA.symmetric_difference(setB)
# print(diff_set)
# setB.symmetric_difference_update(setA)
# print(setB)
