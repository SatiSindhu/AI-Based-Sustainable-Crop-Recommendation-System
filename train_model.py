import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("dataset/Crop_recommendation.csv")

# Features and Label
X = data.drop("label", axis=1)
y = data["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Models
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "Naive Bayes": GaussianNB(),
    "Random Forest": RandomForestClassifier(random_state=42)
}

results = []

print("\n==============================")
print("MODEL EVALUATION")
print("==============================")

for name, model in models.items():

    # Train model
    model.fit(X_train, y_train)

    # Prediction
    prediction = model.predict(X_test)

    # Metrics
    accuracy = accuracy_score(y_test, prediction)

    precision = precision_score(
        y_test,
        prediction,
        average="weighted",
        zero_division=0
    )

    recall = recall_score(
        y_test,
        prediction,
        average="weighted",
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        prediction,
        average="weighted",
        zero_division=0
    )

    # Store results
    results.append([name, accuracy, precision, recall, f1])

    # Print Results
    print("\n------------------------------")
    print(name)
    print("------------------------------")
    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    # Confusion Matrix
    labels = sorted(y.unique())
    cm = confusion_matrix(
        y_test,
        prediction,
        labels=labels
    )

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=labels
    )

    disp.plot(xticks_rotation=90)

    plt.title(f"{name} Confusion Matrix")

    plt.tight_layout()

    plt.savefig(f"{name}_ConfusionMatrix.png")

    plt.close()

    # Individual Bar Graph
    metrics = ["Accuracy", "Precision", "Recall", "F1-Score"]

    values = [accuracy, precision, recall, f1]

    plt.figure(figsize=(6,5))

    plt.bar(metrics, values)

    plt.ylim(0,1)

    plt.ylabel("Score")

    plt.title(f"{name} Performance Metrics")

    plt.tight_layout()

    plt.savefig(f"{name}_Metrics.png")

    plt.close()

# Comparison Table
results_df = pd.DataFrame(
    results,
    columns=[
        "Model",
        "Accuracy",
        "Precision",
        "Recall",
        "F1-Score"
    ]
)

print("\n==============================")
print("COMPARISON TABLE")
print("==============================")
print(results_df)

# Save CSV
results_df.to_csv("Model_Comparison.csv", index=False)

# Save Random Forest Model
joblib.dump(
    models["Random Forest"],
    "model/crop_model.pkl"
)

print("\nRandom Forest model saved successfully!")
print("Model comparison saved as Model_Comparison.csv")
print("Graphs generated successfully.")