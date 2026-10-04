import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("dataset/Crop_recommendation.csv")

# Remove the label column
data = data.drop("label", axis=1)

# Calculate correlation
correlation = data.corr()

# Plot heatmap
plt.figure(figsize=(8,6))

plt.imshow(correlation, cmap="coolwarm", interpolation="nearest")

plt.colorbar()

plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)

plt.yticks(range(len(correlation.columns)), correlation.columns)

plt.title("Correlation Matrix")

plt.tight_layout()

plt.savefig("Correlation_Matrix.png")

plt.show()