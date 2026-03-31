from sklearn.linear_model import LogisticRegression

def run_logreg_baseline(X_train, y_train):

    model = LogisticRegression(max_iter=2000)
    model.fit(X_train, y_train)

    return model