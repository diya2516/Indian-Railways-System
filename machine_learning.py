import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
a={'Train Names':pd.Series(['Tamilnadu Express','Grand Trunk Express','NZM Kranthi Express','Janasatpadhi Express','Duronto Express','Sangmitra Express','Kerala Express','AP Express','PDY NDLS Express','Vande Bharat Express']),
   'Train Numbers':pd.Series([12621,12615,12651,12078,22203,12295,12625,20805,22403,20708]),
   'Technical Supervisor (locopilot)':pd.Series(['Neha sood','Geeta Singh','Akash Kumar','Sartak sinha','Shiv Kumar','Mihir Krishnan','Asif pathan','Amit singh','Khvathi Kumari','Hashitha kaur']),
   'Station names':pd.Series(['Vijayawada','Delhi','Nizamudin','Guntur','Vijayawada','Danapur','Nagpur','Bhopal','Agra','Secundrabad']),
   'Payments':pd.Series([480,825,725,375,450,1780,970,520,800,1060]),
   'PNR':pd.Series([7823547901,9572456700,6305623899,7689087654,9876098334,8902357483,7843902365,9331122009,5367822309,8754632107]),
   'User Feedback':pd.Series([5,4,3,2,4,3,4,4,5,4])}
b=pd.DataFrame(a)
print(b)
print()
print("-----------Training Data--------------")
print()
print("--------Training Data One--------------")
print()
train1=b.sample(frac=.65)
print(train1)
print()
print("--------Training Data Two--------------")
print()
train2=b.sample(n=3)
print(train2)
print()
print("----------- Bias AD vs TD ----------------")
print()
bias=b['Payments'].subtract(train1['User Feedback'])
print(bias)
print() 
tbias=bias.sum()
abias1=(tbias/3)
print("Total Bias    : ",abias1)
print()
print()
print("----------- Variance AD vs TD ----------------")
print()
var2=((abias1)**2)
print("Total Variance    : ",var2)
print()
print("----------- Bias TD1 vs TD2 ----------------")
print()
bias=train1['Payments'].subtract(train2['User Feedback'])
print(bias)
print()
tbias=bias.sum()
abias2=(tbias/3)
print("Total Bias    : ",abias2)
print()
print("----------- Variance TD1 vs TD2 ----------------")
print()
var1=((abias2)**2)
print("Total Variance    : ",var1)

print()
print("-----------Graphical Representtaion---------")
print()
x = b['Train Names'][:5]
payments = b['Payments'][:5]
feedback = b['User Feedback'][:5]

# Line Graph
plt.figure(figsize=(10,5))
plt.plot(x, payments, marker='o', linewidth=2, label='Payments')
plt.plot(x, feedback, marker='s', linewidth=2, label='User Feedback')
plt.title("Train Payments and User Feedback")
plt.xlabel("Train Names")
plt.ylabel("Values")
plt.xticks(rotation=20)
plt.legend()
plt.grid(True)
plt.show()

# Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(payments, feedback)
plt.title("Payments vs User Feedback")
plt.xlabel("Payments")
plt.ylabel("User Feedback")
plt.grid(True)
plt.show()
