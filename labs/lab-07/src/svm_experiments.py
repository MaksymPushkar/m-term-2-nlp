from sklearn.svm import LinearSVC

def run_linear_svc(X_train, y_train, balanced=False):

    if balanced:
        model = LinearSVC(class_weight="balanced")
    else:
        model = LinearSVC()

    model.fit(X_train, y_train)

    return model