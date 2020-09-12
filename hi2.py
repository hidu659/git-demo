#this program gets an items orginal price 
#calculate its sales price with 20% discount

#get the items orginal price 
original_price = float(input('enter the items original price:'))

#calculate the amount of the discount 
discount = original_price * 0.2 

# calculate the sale price 
sale_price = original_price - discount 

#Display sales price 
#Print the sale price 
print("the sales price is:", sale_price)
