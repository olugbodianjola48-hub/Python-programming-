import matplotlib.pyplot as mp
year =[1990, 1991, 1992, 1993]
sales = [20, 50, 70, 75]
mp.title("Annual Sales Growth")
mp.xlabel("year")
mp.ylabel("sales")
mp.bar(year, sales,label="sales") # for bar chart
#mp.plot(year,sales,marker=0,label="sales") # for line chart
mp.legend()
mp.grid(False)
mp.show()