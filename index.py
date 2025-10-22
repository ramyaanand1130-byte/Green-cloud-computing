# Green Cloud Computing Simulation
# Energy Efficient Task Scheduling

import random
import matplotlib.pyplot as plt

# simulate tasks with random energy consumption
tasks = [random.randint(50, 200) for _ in range(10)]  # 10 tasks energy usage (in watts)
print("Task Energy Requirements:", tasks)

# Traditional method: random assignment to servers
servers = [0, 0, 0]  # 3 servers
for task in tasks:
    servers[random.randint(0, 2)] += task
print("\nTraditional Server Load:", servers)
print("Total Energy (Traditional):", sum(servers))

# Green method: assign tasks to least loaded server (energy-efficient)
servers_green = [0, 0, 0]
for task in tasks:
    min_server = servers_green.index(min(servers_green))
    servers_green[min_server] += task
print("\nGreen Scheduling Server Load:", servers_green)
print("Total Energy (Green):", sum(servers_green))

# Compare results
saving = sum(servers) - sum(servers_green)
print(f"\nEnergy Saved by Green Scheduling: {saving} watts")

# Bar chart comparison
labels = ['Traditional', 'Green']
energy = [sum(servers), sum(servers_green)]
plt.bar(labels, energy)
plt.ylabel('Total Energy (Watts)')
plt.title('Green Cloud Computing Energy Comparison')
plt.show()
