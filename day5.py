#construction of  nested loop 
name=input("enter your name ")
print("welcome ",name,'\n')
starting_message="""
plz choose your option:
type---> 1 for  check the balance
type---> 2 for  deposite the amount
type---> 3 for withdrwal amount
"""
print(starting_message)
task=int(input("enter the option from above"))
if task>=1 and task<=3:
    if task==1:
        ## code to check balance
        available_balance=5000
        print("your available balance is ",available_balance)
        print('thank you for visiting our bank')
        
    elif task==2:
        
        deposit_amount=int(input("plz enter the  amount to be deposit :"))
         
        if deposit_amount>500:
              
            print("your amount is deposited in account successfully",deposit_amount)
            av=5000+deposit_amount
            print("available balance is ==",av)
            print("thank you for visiting")
        else:
            print("increase the amount of limit")
    else:
        
        ##code to be withdrawl
        withdrawl_balance=int(input("enter the amount to be withdrawl===="))
        
        if withdrawl_balance>5000 and withdrawl_balance<1:
            print("insufficent balance in your account  or  wrong withdrawl")
        else:
            
            withdrawl=5000-withdrawl_balance
            print("amount is debit=",withdrawl_balance)
            print("your available balance==== ",withdrawl)
        
                

            
        
    
                
    
else:
    print("wrong input is select in b/w 1--3")
    
    




