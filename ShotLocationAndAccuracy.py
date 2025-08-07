import csv
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

filename = 'events.csv'

events = [{'time': '00:19', 'player': 'Player 3', 'event': '18-foot jumpshot missed', 'x': 18, 'y': 8},
    {"time": "00:15", "player": "Player 1", "event": "22-foot jumpshot missed", "x": 22, "y": 8},
    {"time": "00:47", "player": "Player 2", "event": "Layup made", "x": 5, "y": 25},
    {"time": "01:10", "player": "Player 3", "event": "18-foot jumpshot made", "x": 18, "y": 12},
    {"time": "01:32", "player": "Player 4", "event": "Three-point jumpshot missed", "x": 23, "y": 22},
    {"time": "02:01", "player": "Player 5", "event": "Fastbreak layup missed", "x": 6, "y": 24},
    {"time": "02:25", "player": "Player 6", "event": "Corner three made", "x": 25, "y": 6},
    {"time": "02:44", "player": "Player 1", "event": "20-foot jumpshot made", "x": 20, "y": 10},
    {"time": "03:11", "player": "Player 2", "event": "Turnaround jumper missed", "x": 15, "y": 16},
    {"time": "03:45", "player": "Player 3", "event": "Putback dunk made", "x": 8, "y": 25},
    {"time": "04:03", "player": "Player 4", "event": "Fadeaway three missed", "x": 24, "y": 21}]
          
# Write data from list to CSV
with open(filename, mode = 'w', newline='', encoding = 'utf-8') as event_csv:
    file_headers = ['time', 'player', 'event', 'x', 'y']
    writer = csv.DictWriter(event_csv, fieldnames = file_headers)
    writer.writeheader()
    for row in events:
        writer.writerow(row)

# Set up canvas

fig, ax = plt.subplots(figsize=(10, 9))
ax.set_xlim(0, 47)
ax.set_ylim(0, 50)

# Draw basic court elements
# Hoop
hoop = plt.Circle((23.5, 5), radius=0.75, linewidth=2, color='orange', fill=False)
# Paint
paint = plt.Rectangle((17, 0), width=13, height=19, fill=False, linewidth=2)
# Backboard
backboard = plt.Line2D([21, 26], [4], color="black", linewidth=3)
# Three-point arc
arc = Arc((23.5, 5), 44, 44, theta1=0, theta2=180, linewidth=2)

# Add the court elements
ax.add_patch(hoop)
ax.add_patch(paint)
ax.add_line(backboard)
ax.add_patch(arc)

# Plot each shot
for shot in events:
    x = shot['x']
    y = shot['y']
    result = 'made' if 'made' in shot['event'].lower() else 'missed'
    color = 'green' if result == 'made' else 'red'
    marker = 'o' if result == 'made' else 'x'
    ax.plot(x, y, marker=marker, color=color, markersize=10, label=result)

plt.title('Shot Chart')
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor('#f5f5f5')
plt.grid(False)
plt.show()