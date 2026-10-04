import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("dataset/Crop_recommendation.csv")

# Features and target
X = data.drop("label", axis=1)
y = data["label"]

# Train Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Feature importance
importance = model.feature_importances_

# Create DataFrame
feature_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
})

# Sort values
feature_df = feature_df.sort_values(by="Importance", ascending=False)

# Plot
plt.figure(figsize=(8,5))
plt.bar(feature_df["Feature"], feature_df["Importance"])
plt.title("Feature Importance using Random Forest")
plt.xlabel("Input Features")
plt.ylabel("Importance Score")
plt.xticks(rotation=45)
plt.tight_layout()

# Save graph
plt.savefig("feature_importance.png", dpi=300)

plt.show()

print("Feature Importance graph generated successfully.")