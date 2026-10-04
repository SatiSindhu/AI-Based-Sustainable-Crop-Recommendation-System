import pandas as pd
import matplotlib.pyplot as plt

# Model evaluation metrics
data = {
    "Accuracy":  [0.964789, 0.929577, 0.971831, 0.978873],
    "Precision": [0.965927, 0.922668, 0.966339, 0.972502],
    "Recall":    [0.964789, 0.929577, 0.971831, 0.978873],
    "F1-Score":  [0.964718, 0.925575, 0.968710, 0.975610]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate correlation matrix
corr = df.corr()

# Plot heatmap
plt.figure(figsize=(6,5))

plt.imshow(corr, cmap="coolwarm", interpolation="nearest")

plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)

plt.yticks(range(len(corr.columns)), corr.columns)

# Display correlation values
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        plt.text(
            j,
            i,
            f"{corr.iloc[i, j]:.2f}",
            ha="center",
            va="center",
            color="black",
            fontsize=10
        )

plt.title("Correlation Matrix of ML Model Metrics")

plt.tight_layout()

plt.savefig("Metrics_Correlation_Matrix.png", dpi=300)

plt.show()

print("Metrics Correlation Matrix generated successfully!")