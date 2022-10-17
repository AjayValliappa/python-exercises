#Question
'''
Given a list of integer values. Write a python program to check whether it contains same number in adjacent position. Display the count of such adjacent occurrences

Sample Input

Expected Output

[1,1,5,100,-20,-20,6,0,0]

3

[10,20,30,40,30,20]

0

[1,2,2,3,4,4,4,10]

3

'''

#Answer

def get_count(num_list):
    count=0
    n=0
    while((len(num_list)-1)>(n)):
        if (num_list[n]==num_list[n+1]):
            count+=1
            n+=1
        else:
            n+=1
    return count

#provide different values in list and test your program
num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))