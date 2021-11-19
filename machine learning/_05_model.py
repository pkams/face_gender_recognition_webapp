from pycaret.classification import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd
import joblib

x = np.load('../data/data_pcafeat_100x100.npy')
y = np.load('../data/data_normalized_100x100.npz')['arr_1']
print(x.shape, y.shape)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, stratify=y)
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

df_train = pd.DataFrame(x_train)
df_train['label'] = y_train
df_test = pd.DataFrame(x_test)
df_test['label'] = y_test

setup(df_train, 'label', silent=True)
model = compare_models()
model = tune_model(model)
model = finalize_model(model)
joblib.dump(model, '../model/best_model.joblib')

y_pred = predict_model(model, data=df_test)['Label']
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))



