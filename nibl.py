import numpy as np
import matplotlib.pyplot as plt

rate = 9.48
time = 7.5

def cmpd_interest(principal,rate,time):
    cmpINT = principal * (pow((1 + rate/100),time))
    return cmpINT

def double_amount(principal):
    return 2*principal

maxMoney = int(input("Enter the amount: "))
principal = range(0,maxMoney)

x = []
y = []
z = []
for amounts in principal:
    cmpd = cmpd_interest(amounts,rate,time)
    double = double_amount(amounts)
    difference = double-cmpd

    x.append(cmpd)
    y.append(double)
    z.append(difference)

plt.figure(figsize=(10,10))
plt.plot(x,'r-',label='Compounded Rates')
plt.plot(y,'b-',label='Doubled Rates')
plt.plot(z,'g-',label='Difference in Rates at 7.5 years')

plt.xticks(np.arange(0,maxMoney,maxMoney/10))
plt.yticks(np.arange(0,2*maxMoney,maxMoney/5))

plt.legend()

plt.text(0,maxMoney*1.65,"Given Amount: "+str(maxMoney))
plt.text(0,maxMoney*1.55,"Difference between two Skims: "+str(max(z)))

plt.title("The Amounts and their values at 7 years Duration")

print("kkkk")
plt.show()
