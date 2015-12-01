
#!usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt


Wqi_1=0 # The waiting time for the first customer. Since he is the first 
  #customer, he doesnt have to wait in the que, as there is no one ahead of
 # him """

Ti_1=0 # """ Assuming that the time at which the first customer arrived at time
    # 0.Also there is no inter-arrival time for first customer """

Total=0
cus=np.arange(1,10,1)
wait=np.arange(0,5,10)
def interarrivaltimes():
	lamda=1
	u=np.random.uniform(0,1)
	x=-np.log2(u/lamda)
	return x

def interarrivaltimes1(): # this function calculates the inter-arrival times exponentially
	lamda=1
	tau=np.random.exponential(1)
	return tau
def servicetimes(): # this function calculates the service times exponentially
	X=np.random.exponential(2/3.0)
	return X
fra_time=0
k=30 # no of customers
res=[0.0]
res1=[0.0]
no_arrivals=[0]
no_departures=[]
timee1=[]
timee=[0]
count=0
inst=[]

kk=range(0,k-1) 


for i in range(2,k):# iterating from second customer till the last customer
	 
	TAUi=interarrivaltimes1()#inter arrival time for ith customer
	
	Ti=TAUi+Ti_1 #arrival time of ith customer

	
	Xi_1=servicetimes()#service time of i-1th customer
	
	
	""" Calculating waiting times """
	
	if Ti>=Ti_1+Wqi_1+Xi_1: #if the ith customer arrives after i-1th customers time spent in system, waiting time of ith customer is 0
		Wqi=0	 
	else:
		Wqi=Ti_1+Wqi_1+Xi_1-Ti 
	#if the ith customer arrives before i-1th customers time in system, he has to wait for Wqi time
	res.append(Wqi)# appending each customers actial waiting time to a list
	Total=Total+Wqi#finding the total waiting time for all customers
	Awq=Total/i#finding the average waiting time for all the customers
	res1.append(Awq)#appending average waiting times for each customer to a list
	
	if Wqi==0:#necessary condition to find the fraction of time when the system is empty
		inst_time=Ti-(Ti_1+Wqi_1+Xi_1)
		times_when_sys_empty=Ti-inst_time
		inst.append(times_when_sys_empty)
		fra_time=fra_time+(Ti-(Ti_1+Wqi_1+Xi_1))#arrival time of ith customer - time spent by i-1th customer in the system
	count=count+1
	timee.append(Ti)#appending all the arrival times to a list
	no_arrivals.append(count)# appending no of arrivals to a list
	no_departures.append(count)
	time_dep_i_1=Ti_1+Wqi_1+Xi_1
	timee1.append(time_dep_i_1)
	Ti_1=Ti
	Wqi_1=Wqi
	
customer_no=1
print "Customer -> Waiting Time"
print "========================"
for ww in res:
        print "%d\t->\t%f"%(customer_no,ww)
        customer_no=customer_no+1
average_waiting_time=sum(res1)/len(res1)#calculating average waiting time
print "the average waiting time in the queue is %f"%(average_waiting_time)
print Ti
print fra_time
f=fra_time/Ti#calculates the fraction of time when the system is empty

print "The fraction of time when the system is empty is %f"%(f)


for instances in inst:
	print "time instances when the system is empty %f"%(instances)

plt.figure(1)
plt.plot(kk,res,'g',label='waiting time')#plots waiting time with respect to no of customers
plt.hold(True)
plt.plot(kk,res1,'b',label='average time')#plots average customers vs no of customers
plt.xlabel("Customers(k)")
plt.ylabel("Waiting time")
plt.title("Plot of waiting time and average waiting time")
plt.legend()

plt.figure(2)
plt.step(timee,no_arrivals,'g',label="no of arrivals")
plt.hold(True)
plt.step(timee1,no_departures,'b',label="no of departures")
plt.xlabel("Time")
plt.ylabel("No of arrivals and departures")
plt.title("plot of no of arrivals and departures")
plt.legend()
plt.show()



