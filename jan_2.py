# # # # Datatypes in Python:
# # # """
# #
# #
# # integer
# # a=565454656565465654646546468568456846545641265252365123123123
# # float
# # b=3.14565412369846846541268412368413+6984126874
# # complex
# # i=1
# # a=1

# # ab=7j+1j+2
# # ba=5+1j
# # a=str(ab)
# # print(type(a))
# # # Numeric: int, float, complex
# # a = 7 + 3j
# # b = 5 + 7j
# # print(a,b)
# # (7 + 3j)(5 + 7j)
# # #
# # #
# # # a = 7 + 3j
# # # b = 5 + 7j
# # # print(a * b)
# # #
# # #

# # strings
# # list
# # tuple
# # dictionary
# # set

# # # collections:
# # # string: Ordered & Immutable Collection Of Characters

# # # """
# s1='Students of this batch are going to rock the INDIAN software industry!'
# # # # index: 	 0123456789..................
# # # # -ve index
# # # # :	 ......................................................987654321

# # print(s1[0])
# # print(s1[-2])
# # # # print(type(s1))
# # # print(s1)
# # s1[0]='1'
# # print(s1)

# # a='12333'
# # print(len(12333))
# s1='Students of this batch are going to rock the INDIAN software industry!'
# # print(s1[59])
# # print(s1[len(s1)-12])
# # print(s1[-2:-1:-1])
# s2=s1[-69:-69:69]
# print(s2)
# # # s2=s1[:7:2]
# # # print(s1[:7:2])
# # # print(s1)
# # # print(s2)
# # s1="1=====100 fesfsrsdfcfghdre"
# #
# # # print(s1[:100])
# # # s1[0]='1'
# # # print(s1)
# # # # # slicing
# # # s2 = s1[9 : 69]
# # # print(s1)	# Slicing will always return new data
# # # print(s2)
# #
# # # print(s1[600])
# # # print(s1[12 : 600])
# # # print(s1[12 : ])
# # # print(s1[ : 60])
# # # print(s1[ : ])
# #
# # # print(s1[60])
# # # print(s1[-3])
# # """
# # print(s1[0])
# #
# # print(s1[30 : 3])
# # print("The end")
# # print(s1[-25 : -5])
# # print(s1[-30 : 50])
# # print(s1[30 : -3])
# #
# # print(s1[4 : -3])
# #
# #
# # print(s1[3 : 55 : 3])
# # print(s1[55 : 3 : -1])
# # print(s1[ : : -1])
# # print(s1[ : : -3])
# # print(String[1:5:2])
# # """
# #
# # # methods vs. functions
# # # function_name(oprand)
# # # oprand.method_name(arguments)
# #
# # # Case related methods:
# # #slice
# # s1='ROYAL TECHNOSOFT limited'
# # # s1[]
# # ROYAL
# # TECHNOSOFT
# # limited
# # ROYAL limited


# #
# #
# #
# #
# #
# #
# #
# # # s2=s1[:5]
# # # s3=s1[-7:]
# # # print(f"{s2[:3]} {s3[6:}")
# # # Output:
# #
# #
# #
# #
# # # *****New task to perform********
# #
# s1='strings are IMMUTABLE so, methods of strings cannot change the original string. Instead'
# #
# # Output:- 1) print IMMUTABLE using slicing
# #          2) print Instead using slicing
# #          3) skip alternate character and print the new string
# #                 4) print methods using slicing
# #
# # # print(s1[12:22])
# # # print(s1[-7:])
# # # print(s1[::2])
# #
# #
# # # 'Royal Technosoft Limited'
# # # 'I am learning python'
# #
# # # print(s2)
# #
# # # indian
# # # royal
# # # technosoft
# # 'Students of this batch are going to rock the INDIAN software industry!'
# s1='students .of this batch are going to rock the INDIAN software industry!'

# # type(s1)
# # s1.capitalize()


# output: s1 bdha first letters capitilize
#         indian in lower case
#         all the s1 string should in upper case
#         all the s1 string should be in lower case
#         software industry  in uppercase


# # # indian
# #
# # # s1[5]='abc'
# # print(s1)
# s1='students .of this batch are going to rock the INDIAN software industry!'
# print(s1.capitalize())
# # # print(len(s1))
# # # # print(s2)	# strings are immutable so, methods of strings cannot change the original string. Instead, they will return a new string.
# # # print( s1.capitalize())
# # # # # print( s1[5].capitalize())
# print(s1.upper())
# print(s1.lower())
# print(s1.swapcase())
# print(s1.title())


# # len(s1)
# # print()
# # input()
# # type()