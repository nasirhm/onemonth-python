# Taking Bill Price as Input, Typecasting it to Float to Replacing '$' to ''
bill_price = float(input("Please Enter the Bill Amount (in $) : ").replace("$", ""))
# Or You can use .strip('$') removes $ Sign
# Percantage of (15%, 18%, 20%)
percent_15 = (bill_price * 15) / 100
percent_18 = (bill_price * 18) / 100
percent_20 = (bill_price * 20) / 100

#Printing
print(f"Here are Recommended Tips of 15% : {percent_15}, for 18 % : {percent_18} and for 20 % {percent_20}")

print(f"The Total amount would be of 15 % : {bill_price+percent_15}, for 18 % : {bill_price + percent_18}, and for 20 % : {bill_price + percent_20}")
print("Thank You Very Much Sir for Using our Tip Calculator")