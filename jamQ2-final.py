'''
######################################################################

Author: Srikanth Peetha
Date: 05-30-2017
About: Google code jam qualification round 2017

Question (B)

######################################################################
'''

#~~~ Begin: function to create tidy Number
def tidyNumber_create(numArray, num_length):
	limit = num_length -1
	for k in range(0, limit):	
		if numArray[k] > numArray[k+1]:
			numArray[k] = numArray[k] - 1
			for k in range(k+1, num_length):
				numArray[k] = 9
	return numArray
#~~~ End: create tidy function



#~~~ Begin: function to check if a number is tidy or not
def tidyNumber_check(numArray, num_length):
	limit = num_length -1

	count_check = []
	del count_check[:]

	compare = []
	del compare[:]

	k = 0
	for k in range(0, limit):
		compare.append(0) # a tidy array = array of zeros
		if numArray[k] > numArray[k+1]:
			count_check.append(1)


		if numArray[k] <= numArray[k+1]:
			count_check.append(0)

	if count_check == compare:
		return 1 #number is tidy
	else:
		return 0 #number is untidy

#~~~ Tidy number check is complete



def main():
	import string
	arr = []
	array = []
	#input_file = open("B-small-practice.in", 'r') # small input
	input_file = open("B-large-practice.in", 'r') # large input

	output_file = open("Q2-B-large.txt", 'w') # large output

	i = 0
	for  line in input_file.readlines():
		numbers = map(int, string.split(line) ) [0]
		arr.append(numbers)
		i=i+1
	
	j = 0
	for i in range(0,100):
		j =i+1
		array.append( arr[j] )


	#### Creating array of the Tidy number ####

	a = 0
	print "Input"+ 15*' '+"Output"
	array_length = len(array)



	#~~~Begin While loop
	#while(a<array_length):
	while(a<100):
		#~~~ Creating an array of individual numbers
			numArray = []
			num1 = array[a]
			num_length = len(str(num1))
			rem = 10 #some non-zero number
			i = 1
			quot = num1
			while(num_length>0):
				rem = quot%10
				quot = quot/10
				numArray.append(rem)
				num_length = num_length - 1
				i = i+1	
			numArray.reverse()
			#print numArray
		#~~~ Array is Creation for numbers is done

		#~~~ Finding the tidy number
			num_length = len(str(num1))
		   	#~~~ if the length of the number = 1
			if num_length==1:
				garbage_num = 1

		   	#~~~ if length of the number is > 1
			else:
				count = 0

				while count != 5:
					check_tidy = tidyNumber_check(numArray, num_length)
					if(check_tidy == 0): #~~~ NUmber is untidy
						tidyNumber_create(numArray, num_length)
						count = 0

					if(check_tidy == 1): #~~~ NUmber is Tidy
						count = 5
		#~~~ Found the Tidy number


		#~~~ Convert the array back to an integer.
			num_length = len(str(num1))
			limit = num_length

			power = num_length - 1
			number_conv = 0

			for j in range(0, limit):
				number_conv = number_conv + ( 10**power * numArray[j] )
				power = power - 1
			#print number_conv
		#~~~ Converted the array into a integer.

		#~~~ output printing
			itr = a+1
			spaces_act = 20
			spaces_gen = spaces_act - limit #~~~ limit = length of the array number
			#print "Case #"+str(itr)+": "+ str(number_conv) + (spaces_gen*' ') + str(num1)
			output_file.write("Case #"+str(itr)+": "+str(number_conv)+"\n")# + (spaces_gen*' ') + str(num1) + "\n")

		#~~~ printed output 
			a = a+1 #~~~ Condition to repeat the while loop
	print "done"
	output_file.close() #~~~ Close the output file
main()









