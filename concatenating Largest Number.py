#Question:

'''
Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers.
 
Note: Assume that all the numbers are two digit numbers.
 

Sample Input	23,34,55

Expected Output	553423


'''

#Answer:

#lex_auth_012693795044450304151

def create_largest_number(number_list):
    number_list.sort()
    number_list.reverse()
    concatNumber = ""
    for number in number_list:
        concatNumber += str(number)
    return int(concatNumber)

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)