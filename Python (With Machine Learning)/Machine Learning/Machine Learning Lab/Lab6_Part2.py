import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.decomposition import PCA
from sklearn.metrics import roc_curve
from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

dataset = pd.read_csv("winequalityN-lab6.csv")

dataset = dataset.drop(['type'], axis=1)

dataset.loc[dataset['quality']<6,'quality']=0
dataset.loc[dataset['quality']>5,'quality']=1

X = dataset.iloc[:, 1:-1] #Data
Y = dataset.iloc[:, -1]  #Labels

labels = dataset.iloc[:, -1]
data = dataset.iloc[:, :-1]

X_train, X_test, Y_train, Y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, random_state=0)

sc = StandardScaler()
l_reg = LogisticRegression(max_iter=10000)
pca = PCA(n_components=2)

pca_pipe = make_pipeline(sc, pca)

X_train_pca = pca_pipe.fit_transform(X_train)
X_test_pca = pca_pipe.fit_transform(X_test)

clf = make_pipeline(l_reg)

clf.fit(X_train_pca, Y_train)

y_pred_pca = clf.predict(X_test_pca)

disp = DecisionBoundaryDisplay.from_estimator(
    clf, X_train_pca, response_method="predict",
    xlabel='X1', ylabel='X2',alpha=0.5
)
disp.ax_.scatter(X_train_pca[:, 0], X_train_pca[:, 1], c=Y_train)
plt.show()

acc = accuracy_score(Y_test, y_pred_pca)
print('Accuracy is ', acc)