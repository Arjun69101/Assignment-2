#Assignment 2


#__________________Question 1__________________


#The input string.
inp_str='Python is a case sensitive language'

#a. Finding length of string
length=len(inp_str)

#Printing length
print(length)

#b. Splitting the input
split_inp=inp_str.split()

#Reversing the input
split_inp.reverse()

#Joining the input
join_inp=" ".join(split_inp)

#Printing the reverse order
print(join_inp)

#c. Slicing input
slice_inp=inp_str[10:26]

#Printing slice string
print(slice_inp)

#d. Changing "a case sensitive" with "object oriented"
new_inp_str=inp_str.replace('a case sensitive','object oriented')

#Printing new string
print(new_inp_str)

#e. finding index of substring a
print(inp_str.find('a'))

#d. Removing white spaces
no_space_str=inp_str.strip()

#Printing string with removed whitespaces
print(no_space_str)



#__________________Question 2__________________


#Storing details in variables
name='Arjun'
SiD='21104029'
Dep_name='Electrical'
cgpa='10'

#First sentence 
Intro='Hey, {} here'.format(name)

#Second sentence
SiD_intro='My SID is {}'.format(SiD)

#Third sentence
dep_cg="I am from {} department and my CGPA is {}".format(Dep_name,cgpa)

#Printing all the sentences
print(Intro)
print(SiD_intro)
print(dep_cg)



#__________________Question 3__________________


#numbers given a=0b111000 b=0b1010
a=56
b=10

#AND operator
print(a&b)

#OR operator
print(a|b)

#XOR operator
print(a^b)

#Left shift operator
print(a<<2)
print(b<<2)

#Right shift operator
print(a>>2)
print(b>>4)



#__________________Question 4__________________


#Taking input of integers from user
num1=input('Enter an integer:')
num2=input('Enter another integer:')
num3=input('Enter a third integer:')

#Making list of user entered integers
a=[int(num1),int(num2),int(num3)]

#Sorting list
a.sort()

#Printing Largest Number
print('Your largest entered number is:',a[-1])


#__________________Question 5__________________


#Sentence input by user
inp_sen=input('Enter a sentence:')

#special word 'name'
sp_word='name'

#Check if sentence contains special word
if sp_word in inp_sen:

#print yes if true
    print('Yes, it contains the word- name')

#print no if false
else:
    print('No, it does not contain the word- name')



#__________________Question 6__________________


#Taking input of sides from user
side1=int(input('First side length:'))
side2=int(input('Second side length:'))
side3=int(input('Third side length:'))

#print yes if criteria met
if (side1+side2)>=side3 and (side2+side3)>=side1 and (side1+side3)>=side2:
    print('Yes, a triangle is possible')
else:
    print('No, a triangle is not possible')


