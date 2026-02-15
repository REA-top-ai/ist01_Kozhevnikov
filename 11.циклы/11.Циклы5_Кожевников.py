scoops_sold=0
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
for i in sales_data:
    for sales in i:
        scoops_sold+=sales
print(scoops_sold)