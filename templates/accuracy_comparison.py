import matplotlib.pyplot as plt

# Models
models = [
    "Decision Tree",
    "KNN",
    "Naive Bayes",
    "Random Forest"
]

# Accuracy values
accuracy = [
    96.48,
    92.96,
    97.18,
    97.89
]

plt.figure(figsize=(7,5))

bars = plt.bar(models, accuracy)

plt.title("Accuracy Comparison of Machine Learning Models")

plt.xlabel("Models")

plt.ylabel("Accuracy (%)")

plt.ylim(90,100)

# Display values on bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.2,
        f"{height:.2f}%",
        ha="center"
    )

plt.tight_layout()

plt.savefig("Accuracy_Comparison.png", dpi=300)

plt.show()

print("Accuracy Comparison Graph generated successfully!")