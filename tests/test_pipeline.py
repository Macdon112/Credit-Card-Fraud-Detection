import pandas as pd
from collections import Counter
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE


def test_smote_balances_classes_and_preserves_features():
    X, y = make_classification(
        n_samples=100,
        n_features=5,
        n_informative=3,
        n_redundant=0,
        weights=[0.9, 0.1],
        random_state=42,
    )
    feature_names = [f"f{i}" for i in range(X.shape[1])]
    df = pd.DataFrame(X, columns=feature_names)
    target = pd.Series(y)

    pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("smote", SMOTE(random_state=42)),
        ]
    )

    X_res, y_res = pipeline.fit_resample(df, target)

    counts = Counter(y_res)
    assert counts[0] == counts[1]
    assert X_res.shape[1] == len(feature_names)
