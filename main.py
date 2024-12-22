def bill_calc(t_bill, tip_per):
    per_amount=t_bill*(tip_per/100)
    total=t_bill+per_amount
    print("please pay your total bill of ", total)
t_bill=float(input("enter the bill amount "))
tip_per=float(input("enter tip percentage "))
bill_calc(t_bill, tip_per)