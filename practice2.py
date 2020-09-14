# spaces
print('one', end=" ")
print ('two', end= " ")
print ('three')

#line separators 
print('one','two', 'three', sep=" ")
print('one','two', 'three', sep="*")

# escape characters
print('one\ntwo\nthree')
print('one\ttwo\tthree')
print('one\\two\\three')

# string conventration 
print('enter the amount of ' +
'sales for each day'+'press enter')

print(format(123456.6789, '.2f'))

print (format(12345.66667, ".3f"))

#demonstrates the floating number
amount_due = 5000.2
monthly_payment = amount_due/12.0

print('the monthly payment is',
format(monthly_payment,'.2f'))

print(format(123456.6789,'.2e'))






