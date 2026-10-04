import numpy as np
import matplotlib.pyplot as plt

# Metrics on X-axis
metrics = ["Accuracy", "Precision", "Recall", "F1-Score"]

# Existing Models
decision_tree = [96.48, 96.59, 96.48, 96.47]
knn = [92.96, 92.27, 92.96, 92.56]
naive_bayes = [97.18, 96.63, 97.18, 96.87]

# Proposed Model
random_forest = [97.89, 97.25, 97.89, 97.56]

x = np.arange(len(metrics))
width = 0.2

plt.figure(figsize=(10,6))

bars1 = plt.bar(x - 1.5*width, decision_tree, width, label="Decision Tree")
bars2 = plt.bar(x - 0.5*width, knn, width, label="KNN")
bars3 = plt.bar(x + 0.5*width, naive_bayes, width, label="Naive Bayes")
bars4 = plt.bar(x + 1.5*width, random_forest, width, label="Random Forest (Proposed)")

# Display values on bars
for bars in [bars1, bars2, bars3, bars4]:
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.12,
            f"{height:.2f}",
            ha="center",
            va="bottom",
            fontsize=8
        )

plt.xticks(x, metrics)

plt.xlabel("Evaluation Metrics")
plt.ylabel("Performance (%)")

plt.title("Comparison of Existing System and Proposed System")

plt.ylim(90,100)

plt.legend()

plt.grid(axis='y', linestyle='--', alpha=0.4)

plt.tight_layout()

plt.savefig("Existing_vs_Proposed_System.png", dpi=300)

plt.show()

print("Existing vs Proposed System graph generated successfully!")