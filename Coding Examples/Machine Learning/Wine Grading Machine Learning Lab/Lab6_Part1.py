import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
#from sklearn.inspection import DecisionBoundaryDisplay
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
clf = make_pipeline(sc, l_reg)

clf.fit(X_train, Y_train)

y_pred = clf.predict(X_test)
y_clf_prob = clf.predict_proba(X_test)

acc = accuracy_score(Y_test, y_pred)
print('Accuracy is ', acc)
recall = recall_score(Y_test, y_pred)
print('Recall is ', recall)

cm = confusion_matrix(Y_test, y_pred)
cm_display = ConfusionMatrixDisplay(cm).plot()

f1 = f1_score(Y_test, y_pred)
print('F1 Score is ', f1)

fpr, tpr, _ = roc_curve(Y_test, y_clf_prob[:, 1], pos_label=clf.classes_[1])
roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr).plot()

plt.show()

auc = roc_auc_score(Y_test, y_clf_prob[:,1])
print('AUC is ', auc)

