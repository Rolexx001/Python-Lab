# Student Name : Aman Sagar
# Roll_Number : 2024ug3015
# Course : CD-2101-Python Programming Lab
# Experiment-2-Task_05 : Analyzing Monthly Sales Data

import matplotlib.pyplot as plt #importing matplotlib for plotting

sales_data = [25,89,28,2,12,23,78,23,31,53,64,63]
total_sales = 0

for i in sales_data: 
  total_sales += i #calculating total sales

print("Total yearly sales: ", total_sales)

average_sales = total_sales/12 #calculating average sales
print("Average yearly sales: ", average_sales)

highest_sales = 0
for i in sales_data: #finding highest sales
    if(highest_sales<i):
      highest_sales=i

print("Highest Sales: ", highest_sales)

plt.plot(sales_data,marker='x')
plt.xticks(range(1,len(sales_data)+1)) #setting x-ticks from 1 to 12
plt.xlabel("Month") 
plt.ylabel("sales")
plt.title("MONTH WISE EARLY SALES OF 2024")
plt.show()