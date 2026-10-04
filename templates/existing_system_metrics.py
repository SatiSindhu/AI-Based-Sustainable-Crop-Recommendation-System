import numpy as np
import matplotlib.pyplot as plt

# Metrics on X-axis
metrics = ["Accuracy", "Precision", "Recall", "F1-Score"]

# Existing system models
decision_tree = [96.48, 96.59, 96.48, 96.47]
knn = [92.96, 92.27, 92.96, 92.56]
naive_bayes = [97.18, 96.63, 97.18, 96.87]

x = np.arange(len(metrics))
width = 0.25

plt.figure(figsize=(8,5))

bars1 = plt.bar(x - width, decision_tree, width, label="Decision Tree")
bars2 = plt.bar(x, knn, width, label="KNN")
bars3 = plt.bar(x + width, naive_bayes, width, label="Naive Bayes")

# Add values on top of bars
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.15,
            f"{height:.2f}",
            ha="center",
            va="bottom",
            fontsize=8
        )

plt.xticks(x, metrics)
plt.xlabel("Evaluation Metrics")
plt.ylabel("Performance (%)")
plt.title("Existing System Performance Comparison")
plt.ylim(90, 100)
plt.legend()

plt.tight_layout()

plt.savefig("Existing_System_Comparison.png", dpi=300)

plt.show()

print("Existing System Comparison Graph generated successfully!")

