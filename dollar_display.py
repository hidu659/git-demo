#this programs shows how a floating-point
#number can be displayed in currency 
monthly_pay = 5000.0
annual_pay = monthly_pay * 12.0

print('your annual pay is $',
format(annual_pay, ',.2f'), 
sep='')

#sales report breaking long statements
monday = 36
tuesday = 40 
wednesday = 48

# display message
print('monday sales are', monday,
'and teusday sales are', tuesday,
'and wednesday sales are', wednesday)

# long message connected by operation + 
message = 'hello ' + 'world'

#F-string 
#display message 
print(message)

name = 'hidaya'
print(f'hello', name, sep=' ')

print(f'the value is {10+2}.')


name = 'hidaya'
print(f'my name is {name}.')

val = 133
print(f'the value of this money is, {val}.')

num = 122
print(f'{num}')

num = 122
print(f'{num:,.2f}')

discount = 0.5
print(f'{discount:.0%}')

number = 123456789
print(f'{number:,d}')

num = 12345.6789
print (f'{num:,.2e}')

#assigning field width 
num = 12345.6789
print(f'the number is {num: 12,.2f}')

# alignment of value 

number = 234
print(f'{number: < 20,.2f}')

print(f'{number: > 20,.2f}')

print(f'{number: ^ 20,.2f}')

print(f'{number: > 10,.2f}')