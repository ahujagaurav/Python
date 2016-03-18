

a = {'Name': 'gaurav', 'balance': 2755,'A/C':1}
b = {'Name': 'Akshay', 'balance': 2734,'A/C':2}
c = {'Name': 'Nikhil', 'balance': 2772,'A/C':3}
d = {'Name': 'Aditya', 'balance': 2712,'A/C':4}
final = {
	1:a,
	2:b,
	3:c,
	4:d,
	
}


loginchoice = raw_input("Enter your choice")


if loginchoice=='login':
    choice = input("What is your username? ")
    choice2 = input("What is your password? ")
    if choice==choice2:
        print final[choice]
    else:
        print "The username or password you entered is incorrect. Please try again or register."
elif loginchoice=='exit':
	print "You choose to exit! Bye Bye"
elif loginchoice=='Transfer':
	transfer= int (input("Enter the amount you want to transfer"))
	account= int (input("Enter your user Account Number"))
	if account not in final:
		print "Wrong account number"
	elif account in final:
		a=final['Bal']-transfer
		b=final[account]['Bal']+transfer
		print "Transaction Successfull "

	else:
		print "Wrong account! Please try again" 

else :
	print "The choice you entered is wrong! Please try again"	

#!/usr/bin/python
