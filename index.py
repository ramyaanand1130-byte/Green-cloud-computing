import random
import matplotlib.pyplot as plt
tasks = [random.randint(50, 200) for _ in range(10)]  
print("Task Energy Requirements:", tasks)
servers = [0, 0, 0]  # 3 servers
for task in tasks:
    servers[random.randint(0, 2)] += task
print("\nTraditional Server Load:", servers)
print("Total Energy (Traditional):", sum(servers))
servers_green = [0, 0, 0]
for task in tasks:
    min_server = servers_green.index(min(servers_green))
    servers_green[min_server] += task
print("\nGreen Scheduling Server Load:", servers_green)
print("Total Energy (Green):", sum(servers_green))
saving = sum(servers) - sum(servers_green)
print(f"\nEnergy Saved by Green Scheduling: {saving} watts")
labels = ['Traditional', 'Green']
energy = [sum(servers), sum(servers_green)]
plt.bar(labels, energy)
plt.ylabel('Total Energy (Watts)')
plt.title('Green Cloud Computing Energy Comparison')
plt.show()
