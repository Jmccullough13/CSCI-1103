#McCullough-Invoice.py
#Jeffrey McCullough
#3/22/2022
#This program will calculate the totals for the costs of books, tuition, and lab fees and print an invoice.

books = 52.99
lab_fees = 25.00
CREDIT_HOUR = 157.93
tuition = CREDIT_HOUR * 3
total = books + lab_fees + tuition
print ('*' * 50
       +'\n\tColumbus State Community College'
       +'\n\t550 East Spring Street'
       +'\n\tColumbus, OH 43215'
       +"\n"+'-'*50
       +'\n\tProduct Name:\tProduct Price:'
       +'\n\tBooks'+"\t\t"+'$'+str(books)
       +'\n\tLab Fees:'+"\t"+'$'+str(lab_fees)
       +'\n\tTuition:'+"\t"+'$'+str(tuition)
       +"\n"+'-'*50
       +"\n\t\t\t"+'Total'
       +"\n\t\t\t"+'$'+str(total)
       +"\n"+'-'*50
       +"\n\n"+'  Thank you for being a Columbus State Student'
       +"\n"+'*' * 50)

