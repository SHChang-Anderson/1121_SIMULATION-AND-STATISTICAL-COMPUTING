import numpy as np
import scipy.stats as stats
import random
import math
import matplotlib.pyplot as plt
#指數隨機變數產生器
def generate_EXP(lambda_param):
    U = np.random.uniform(0, 1)
    X = -1/lambda_param * np.log(U)
    return X

def mm1_simulation(arrival_rate, service_rate, num_customers):
    arrival_times = [0]
    service_times = []
    sum = 0
    working = 0 
    # 產生到達時間
    for i in range(num_customers):
        tp = generate_EXP(1/arrival_rate)
        arrival_times.append(arrival_times[-1] + tp)


    
    print(arrival_times)

    # 產生隨機服務時間
    for i in range(num_customers):
        service_times.append(generate_EXP(1/service_rate))
    print(service_times)

    # 服務初始顧客
    starting_queue = [arrival_times[0]]
    departure_times = [arrival_times[0] + service_times[0]]

    # 服務顧客
    for i in range(1, num_customers): 
        starting_queue.append(max(arrival_times[i], departure_times[i-1]))
        departure_times.append(starting_queue[i] + service_times[i])
        working += service_times[i]
    wait_times = []
    # 計算等待時間
    for i in range(num_customers):
        wait_times.append(starting_queue[i] - arrival_times[i])
        

    print(f"Customer\tArrival Time\tService Start Time\tService End Time\tWait Time")
    for i in range(num_customers):
        print(f"{i+1}\t\t{arrival_times[i]:.4f}\t\t{starting_queue[i]:.4f}\t\t\t{departure_times[i]:.4f}\t\t\t{wait_times[i]:.4f}")

    average_wait_time = np.mean(wait_times)
    print(f"\nAverage Wait Time: {average_wait_time:.4f} minutes")
    utilization = working / departure_times [num_customers - 1]
    print(f"\nServer Utilization: {utilization:.4f}")

   
    return average_wait_time

arrival_rate = 6  # 顧客到達率
service_rate = 8  # 服務率
num_customers = 10  # 顧客數量

outputarr1 = []
outputarr2 = []
simutime = 1000
for i in range(simutime):
    outputarr2.append(mm1_simulation(arrival_rate, service_rate, num_customers))


# 計算信賴區間
confidence_level=0.95
average_wait_time_simu = np.mean(outputarr2)
print(average_wait_time_simu )
confidence_interval = (average_wait_time_simu - 2*np.std(outputarr2), average_wait_time_simu + 2*np.std(outputarr2))
print(f"\nConfidence Interval ({confidence_level*100}%): ({confidence_interval[0]:.4f}, {confidence_interval[1]:.4f})")

ct = 0
for  i in range(len(outputarr2)):
    if(outputarr2[i] >= (average_wait_time_simu - 2*np.std(outputarr2)) and outputarr2[i] <= (average_wait_time_simu  + 2*np.std(outputarr2)) ):
        ct += 1


print(f"\n{ct/simutime}%")


counts, bins, patches = plt.hist(outputarr2, density=True,bins= 100,   edgecolor='black')
plt.xticks(np.arange(min(outputarr2), max(outputarr2), step=2))
color_start = average_wait_time_simu - 2*np.std(outputarr2)
color_end = average_wait_time_simu + 2*np.std(outputarr2)
start_idx = np.digitize(color_start, bins)
end_idx = np.digitize(color_end, bins)
for i in range(start_idx, end_idx+1):
  patches[i].set_facecolor('red')
plt.xlabel('Avg. Waiting Times')
plt.ylabel('Proportion')
plt.title('The Distritbution of Wating Times')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()



