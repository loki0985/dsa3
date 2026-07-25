import pandas as pd
import matplotlib.pyplot as plt

# --------------------------
# Input Data
processes = ['P1', 'P2', 'P3', 'P4']
arrival_time = [0, 1, 2, 3]
burst_time = [10, 5, 8, 6]
time_quantum = 4

# --------------------------
# FCFS Algorithm
def fcfs(processes, arrival, burst):
    n = len(processes)
    start = [0]*n
    comp = [0]*n
    wait = [0]*n
    tat = [0]*n

    start[0] = arrival[0]
    comp[0] = start[0] + burst[0]

    for i in range(1, n):
        start[i] = max(comp[i-1], arrival[i])
        comp[i] = start[i] + burst[i]

    for i in range(n):
        tat[i] = comp[i] - arrival[i]
        wait[i] = tat[i] - burst[i]

    gantt = [(processes[i], start[i], comp[i]) for i in range(n)]

    return start, comp, wait, tat, gantt

# --------------------------
# SJF Algorithm (Non-Preemptive)
def sjf(processes, arrival, burst):
    n = len(processes)
    done = [False]*n
    start = [0]*n
    comp = [0]*n
    wait = [0]*n
    tat = [0]*n

    time = 0
    completed = 0

    while completed < n:
        idx = -1
        min_bt = float("inf")

        for i in range(n):
            if arrival[i] <= time and not done[i] and burst[i] < min_bt:
                min_bt = burst[i]
                idx = i

        if idx == -1:
            time += 1
            continue

        start[idx] = time
        time += burst[idx]
        comp[idx] = time
        tat[idx] = comp[idx] - arrival[idx]
        wait[idx] = tat[idx] - burst[idx]

        done[idx] = True
        completed += 1

    gantt = [(processes[i], start[i], comp[i]) for i in range(n)]
    return start, comp, wait, tat, gantt

# --------------------------
# Round Robin Algorithm
def round_robin(processes, arrival, burst, tq):
    n = len(processes)
    rem = burst.copy()
    time = 0
    wait = [0]*n
    tat = [0]*n
    gantt = []

    while True:
        done = True
        for i in range(n):
            if rem[i] > 0:
                done = False
                start = time

                if rem[i] > tq:
                    time += tq
                    rem[i] -= tq
                else:
                    time += rem[i]
                    wait[i] = time - burst[i]
                    rem[i] = 0

                gantt.append((processes[i], start, time))

        if done:
            break

    for i in range(n):
        tat[i] = wait[i] + burst[i]

    return wait, tat, gantt

# --------------------------
# Gantt Chart Function
def plot_gantt(gantt, title):
    plt.figure(figsize=(8, 2))
    for p, s, e in gantt:
        plt.barh(1, e-s, left=s)
        plt.text((s+e)/2, 1, p, ha='center', va='center')
    plt.yticks([])
    plt.xlabel("Time")
    plt.title(title)
    plt.show()

# --------------------------
# Running Algorithms

fcfs_s, fcfs_c, fcfs_w, fcfs_t, fcfs_g = fcfs(processes, arrival_time, burst_time)
sjf_s, sjf_c, sjf_w, sjf_t, sjf_g = sjf(processes, arrival_time, burst_time)
rr_w, rr_t, rr_g = round_robin(processes, arrival_time, burst_time, time_quantum)

# --------------------------
# Display Tables

df_fcfs = pd.DataFrame({
    'Process': processes,
    'Arrival': arrival_time,
    'Burst': burst_time,
    'Start': fcfs_s,
    'Completion': fcfs_c,
    'Waiting': fcfs_w,
    'Turnaround': fcfs_t
})

df_sjf = pd.DataFrame({
    'Process': processes,
    'Arrival': arrival_time,
    'Burst': burst_time,
    'Start': sjf_s,
    'Completion': sjf_c,
    'Waiting': sjf_w,
    'Turnaround': sjf_t
})

df_rr = pd.DataFrame({
    'Process': processes,
    'Burst': burst_time,
    'Waiting': rr_w,
    'Turnaround': rr_t
})

print("\n----- FCFS -----")
print(df_fcfs)

print("\n----- SJF -----")
print(df_sjf)

print("\n----- Round Robin -----")
print(df_rr)

# --------------------------
# Averages
print("\n--- Average Times ---")
print("FCFS Waiting Time:", sum(fcfs_w)/len(processes))
print("FCFS Turnaround Time:", sum(fcfs_t)/len(processes))

print("SJF Waiting Time:", sum(sjf_w)/len(processes))
print("SJF Turnaround Time:", sum(sjf_t)/len(processes))

print("RR Waiting Time:", sum(rr_w)/len(processes))
print("RR Turnaround Time:", sum(rr_t)/len(processes))

# --------------------------
# Plot Gantt Charts
plot_gantt(fcfs_g, "FCFS Gantt Chart")
plot_gantt(sjf_g, "SJF Gantt Chart")
plot_gantt(rr_g, "Round Robin Gantt Chart")
