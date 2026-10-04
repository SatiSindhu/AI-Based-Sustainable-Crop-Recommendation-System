import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("dataset/Crop_recommendation.csv")

# -------- Nitrogen Distribution --------
plt.figure(figsize=(6,4))
plt.hist(data["N"], bins=10)
plt.title("Distribution of Nitrogen")
plt.xlabel("Nitrogen (N)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Nitrogen_Distribution.png")
plt.close()

# -------- Temperature Distribution --------
plt.figure(figsize=(6,4))
plt.hist(data["temperature"], bins=10)
plt.title("Distribution of Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Temperature_Distribution.png")
plt.close()

# -------- Rainfall Distribution --------
plt.figure(figsize=(6,4))
plt.hist(data["rainfall"], bins=10)
plt.title("Distribution of Rainfall")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Rainfall_Distribution.png")
plt.close()

print("Feature distribution graphs generated successfully!")