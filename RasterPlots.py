import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Load the behavior bouts from a CSV file
csv_file = input("What is the file's path?\n")
df = pd.read_csv(csv_file)

# Convert frame numbers to time in minutes (assuming 30 fps)
frame_rate = 30
bouts_in_minutes1 = [(row['manual t0'] / (frame_rate * 60), row['manual t1'] / (frame_rate * 60)) for index, row in df.iterrows()]
bouts_in_minutes2 = [(row['JAABA t0'] / (frame_rate * 60), row['JAABA t1'] / (frame_rate * 60)) for index, row in df.iterrows()]
bouts_in_minutes3 = [(row['Matebook t0'] / (frame_rate * 60), row['Matebook t1'] / (frame_rate * 60)) for index, row in df.iterrows()]

# Create a figure and a set of subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 6), sharex=True, gridspec_kw={'hspace': 0})  # No vertical space between subplots

# Function to plot vertical raster plots
def plot_raster(ax, bouts, color):
    for start, end in bouts:
        ax.plot([start, end], [0.5, 0.5], color=color, lw=2)  # Draw horizontal lines for duration
        ax.plot([start, start], [0.2, 0.8], color=color, lw=2)  # Adjusted y-values for better visibility
        ax.plot([end, end], [0.2, 0.8], color=color, lw=2)      # Adjusted y-values for better visibility
    ax.set_ylim(0, 1)
    ax.set_xlim(0, 15)

# Plot each set of behavior bouts in its respective subplot
plot_raster(axs[0], bouts_in_minutes1, (0/255, 192/255, 0/255))
plot_raster(axs[1], bouts_in_minutes2, (249/255, 64/255, 64/255))
plot_raster(axs[2], bouts_in_minutes3, (85/255, 160/255, 251/255))

# Set labels and title for each subplot
axs[2].set_xlabel('Time (minutes)', fontsize=22)  # Reduced font size

# Remove y-axis ticks and labels, and keep y-axis boundaries visible
for ax in axs:
    ax.set_yticks([])
    ax.set_yticklabels([])
    ax.spines['left'].set_visible(True)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)  # Hide top spine
    ax.spines['bottom'].set_visible(False)  # Hide bottom spine for middle and top plots

# Keep the bottom spine visible for the last subplot
axs[2].spines['bottom'].set_visible(True)

# Set x-axis ticks and reduced font size
xticks = np.arange(0, 16, 5)
axs[2].set_xticks(xticks)
axs[2].tick_params(axis='x', labelsize=22)  # Reduced font size for x-axis ticks

# Hide x-axis for the top subplots
for ax in axs[:-1]:
    ax.xaxis.set_visible(False)

# Extract base name and directory from the CSV file path
base_name = os.path.splitext(os.path.basename(csv_file))[0]
input_directory = os.path.dirname(csv_file)

# Set the plot subtitle
plt.suptitle(f'{base_name} - Wing Extension Bouts', fontsize=24)  # Reduced font size

# Add a big rectangle covering all subplots
rect = patches.Rectangle((0, 0), 15, 3, linewidth=1, edgecolor='black', facecolor='none', transform=fig.transFigure)
fig.patches.append(rect)

# Adjust layout
plt.subplots_adjust(hspace=0, wspace=0, top=0.92, bottom=0.1, left=0.1, right=0.9)  # Adjust layout to remove gaps

# Save the plot as an image in the same directory as the input CSV file
image_file = os.path.join(input_directory, f"{base_name}_raster_plot.png")
plt.savefig(image_file)

# Display the plot
plt.show()
