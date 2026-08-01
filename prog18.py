'''A semiconductor manufacturer sells three types of microprocessors: 8-bit, 16-bit and 32-bit. It
differentiates between three types of customer: industry, government, and university. It has the
following discount policy that depends on the type of microprocessor, the amount of order, and the
type of customer:
For 32-bit microprocessor, if the order is for less than Rs. 50,000, allow 5% discount to industrial
customers and 6.5% discount to the government agencies. If the order is Rs. 50,000 or more, a
discount of 7.5 % and 8.5 % respectively it given to the industrial customers and the government
agencies. A discount of 10 % is given to both industrial customers and government agencies if the
order is more than Rs.1,00,000. universities get a discount of 7.5 % irrespective of the amount of
order.
For 16-bit microprocessors, no discount is given for orders less than Rs. 10.000. For orders of Rs.
10,000 or more, 5 % discount is given to the industrial customers and universities, and 6 % discount
is given to the government agencies.
For 8-bit microprocessors, a flat discount of 10 % is given to all the three types of customers for any
order.
Write a program that reads the type of customer, the type of the product, the amount of the order,
and prints of the net amount payable by the customer.'''

# Program to find discount on Microprocessor sales
micro = int(input("type of microprocessor:8, 16, 32"))
cust = input("type of customer:G, U, I")
ord = int(input("ordered amount:"))
if micro == 32:
    if cust =='U':
        dis = 7.5
    elif cust == 'I':
        if ord < 50000:
            dis = 5
        else:
            dis = 7.5
            if ord > 100000:
                dis = 7.5
                if (cust == "G"):
                    if ord <50000:
                        dis = 6,5
                    else:
                        dis = 8.5
                        if ord > 100000:
                            dis = 10
                            if micro == 16:
                                if(ord>10000):
                                    if(cust =="U" or cust == "I"):
                                        dis = 5
                                    else:
                                        dis = 6
                                        if micro == 8:
                                            dis = 10
                                            amt = ord*(100-dis)/100
                                            print ("cust,micro,orderant")
                                            print("payable amt after dis",amt)