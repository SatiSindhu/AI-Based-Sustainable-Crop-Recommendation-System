import matplotlib.pyplot as plt

# Metrics
metrics = ["Accuracy", "Precision", "Recall", "F1-Score"]

# Random Forest (Proposed System)
random_forest = [97.89, 97.25, 97.89, 97.56]

plt.figure(figsize=(7,5))

bars = plt.bar(metrics, random_forest, width=0.5, label="Random Forest")

# Display values on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.15,
        f"{height:.2f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.xlabel("Evaluation Metrics")
plt.ylabel("Performance (%)")
plt.title("Proposed System Performance (Random Forest)")
plt.ylim(90, 100)

plt.legend()

plt.tight_layout()

plt.savefig("Proposed_System_Comparison.png", dpi=300)

plt.show()

print("Proposed System Graph generated successfully!")