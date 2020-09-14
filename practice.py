#get the three test score and assign them to the
#test1, test2, and test3 variables

test1 = float(input('enter the first test score:'))
test2 = float(input('enter the second test score:'))
test3 = float(input('enter the third test score:'))


#Calculate the average of test scores

#assign the result to the average variable
average = (test1 + test2 + test3) / 3.0

#display the average 
print ("the average score is:", average)




#get number of seconds from users
total_seconds = float(input('enter a number of seconds:'))

# get the number of hours 
hours = (total_seconds // 60) % 60 

# get the number of remianing minutes 
minutes = total_seconds % 60

# get the number of remianing seconds 
seconds = total_seconds % 60

#display the results 
print ('here is the time in hours, minutes, and seconds:')

print ('hours:', hours)
print ("minutes:", minutes)
print ('seconds:', seconds)

