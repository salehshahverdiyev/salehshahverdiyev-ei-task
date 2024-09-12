import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean


das_data = pd.read_csv('Section 3 data.csv')
print(das_data.describe())


'''
Plotting heatmap of the data to visualize spatiotemporal patterns
'''
plt.figure(figsize=(10, 6))
sns.heatmap(das_data, cmap="viridis")
plt.title("Spatiotemporal Data Heatmap")
plt.xlabel("Time (minutes)")
plt.ylabel("Depth (meters)")
plt.show()


'''
Plotting histograms for a few random depths
'''
depth_indices = [10, 100, 500]
for depth in depth_indices:
    plt.figure(figsize=(8, 4))
    das_data.iloc[depth].plot(kind='hist', bins=50)
    plt.title(f"Histogram of Signal Values at Depth {depth} meters")
    plt.xlabel("Signal Value")
    plt.ylabel("Frequency")
    plt.show()









'''
Step 1: Adjust the Canny edge detection thresholds
Step 2: Lower the Hough Line threshold
'''
das_image = das_data.to_numpy()
edges = cv2.Canny(das_image.astype(np.uint8), 30, 100)

plt.imshow(edges, cmap='gray')
plt.title('Edge Detection Output')
plt.show()

lines = cv2.HoughLines(edges, 1, np.pi/180, 100)
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        plt.plot([x1, x2], [y1, y2], color='red')

    plt.imshow(das_image, cmap='gray')
    plt.title('Detected Lines Using Hough Transform')
    plt.show()
else:
    print("No lines were detected.")


'''Example'''
depth1 = das_data.iloc[10].to_numpy()
depth2 = das_data.iloc[50].to_numpy()

distance, path = fastdtw(depth1, depth2, dist=euclidean)
print(f"DTW distance between depth 10 and depth 50: {distance}")
