import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import itertools


# -----------------------------------------
# 1️⃣ Connect to DagsHub MLflow
# -----------------------------------------
mlflow.set_tracking_uri(
    "https://dagshub.com/asifuzzaman-lasker/experiment-tracking-lab.mlflow"
)

mlflow.set_experiment("Hyperparameter_Tuning_RF")


# -----------------------------------------
# 2️⃣ Load Dataset
# -----------------------------------------
data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)


# -----------------------------------------
# 3️⃣ Hyperparameter Grid
# -----------------------------------------
n_estimators_list = [50, 100, 200]
max_depth_list = [None, 5, 10]

best_accuracy = 0
best_params = {}


# -----------------------------------------
# 4️⃣ Run Multiple Experiments
# -----------------------------------------
for n_estimators, max_depth in itertools.product(n_estimators_list, max_depth_list):

    with mlflow.start_run():

        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=42
        )

        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)

        # Log parameters
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)

        # Log metric
        mlflow.log_metric("accuracy", acc)

        # Log model
        mlflow.sklearn.log_model(model, "model")

        # -----------------------------------------
        # Log Confusion Matrix as Artifact
        # -----------------------------------------
        cm = confusion_matrix(y_test, preds)

        plt.figure()
        plt.imshow(cm, interpolation='nearest')
        plt.title("Confusion Matrix")
        plt.colorbar()
        plt.xlabel("Predicted")
        plt.ylabel("True")
        plt.tight_layout()

        plt.savefig("confusion_matrix.png")
        mlflow.log_artifact("confusion_matrix.png")
        plt.close()

        print(f"Run → n_estimators={n_estimators}, max_depth={max_depth}, accuracy={acc}")

        # Track best model
        if acc > best_accuracy:
            best_accuracy = acc
            best_params = {
                "n_estimators": n_estimators,
                "max_depth": max_depth
            }

print("\n🔥 Best Accuracy:", best_accuracy)
print("🔥 Best Parameters:", best_params)
