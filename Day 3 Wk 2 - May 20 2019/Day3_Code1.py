##name='joshua'
##relationship='friends'
##original_price=4000
##discount=0.15
##print('hello',name,'because we are',relationship,'i will drop the price from',original_price,'to',original_price-(original_price*discount),'at a discount of',discount*100,'%')

##here the + was used to replace commas and the string, 'str()' was used to embed the calculations into the sentences
##name='joshua'
##relationship='friends'
##original_price=4000
##discount=0.15
##sentence='hello'+name+'because we are'+relationship+'i will drop the price from'+str(original_price)+'to'+str(original_price-(original_price*discount))+'at a discount of'+str(discount*100)+'%'
##print(sentence)

##here the spaces are added into strings to prevent them from being joined to variables
name='joshua'
relationship='friends'
original_price=4000
discount=0.15
sentence='hello '+name+' because we are '+relationship+' i will drop the price from '+str(original_price)+' to '+str(original_price-(original_price*discount))+' at a discount of '+str(discount*100)+'%'
print(sentence)