import numpy as np
import scipy.stats as stats

def mm1_simulation(arrival_rate, service_rate, num_customers, confidence_level=0.95):
    arrival_times = np.cumsum(np.random.exponential(1/arrival_rate, num_customers))
    service_times = np.random.exponential(1/service_rate, num_customers)

    arrival_queue = [arrival_times[0]]
    departure_times = [arrival_times[0] + service_times[0]]

    for i in range(1, num_customers):
        arrival_queue.append(max(arrival_times[i], departure_times[i-1]))
        departure_times.append(arrival_queue[i] + service_times[i])

    wait_times = np.subtract(arrival_queue, arrival_times)
    service_start_times = np.maximum(arrival_times, departure_times - service_times)

    utilization = sum(service_times) / departure_times[-1]

    print(f"Customer\tArrival Time\tService Start Time\tService End Time\tWait Time")
    for i in range(num_customers):
        print(f"{i+1}\t\t{arrival_times[i]:.4f}\t\t{service_start_times[i]:.4f}\t\t{departure_times[i]:.4f}\t\t{wait_times[i]:.4f}")

    average_wait_time = np.mean(wait_times)
    print(f"\nAverage Wait Time: {average_wait_time:.4f} minutes")

    print(f"\nServer Utilization: {utilization:.4f}")

    # 計算信心區間
    z_score = stats.norm.ppf(1 - (1 - confidence_level) / 2)
    margin_of_error = z_score * np.std(wait_times) / np.sqrt(num_customers)
    confidence_interval = (average_wait_time - margin_of_error, average_wait_time + margin_of_error)
    print(f"\nConfidence Interval ({confidence_level*100}%): ({confidence_interval[0]:.4f}, {confidence_interval[1]:.4f})")

# 使用示例
arrival_rate = 0.2  # 顧客到達率
service_rate = 0.5  # 服務率
num_customers = 10  # 顧客數量

mm1_simulation(arrival_rate, service_rate, num_customers)
