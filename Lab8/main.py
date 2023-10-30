import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

'''
Parte 1
'''

'''
Ejercicio 1
'''
df = pd.read_csv('titanic_MD.csv')
# Reemplace los valores de "?" con NaN
df.replace('?', np.nan, inplace=True)

# Identificar columnas con valores faltantes y contarlos
missing_data = df.isnull().sum()

# Imprimir el resultado
print("Columnas con valores faltantes y su cantidad:")
print(missing_data)

'''
Ejercicio 2
Sex: Imputacion por moda. Al ser categorías conviene aplicar la más común
Age: bins. Al ser edades se pueden agrupar por rangos.
SibSp: Eliminación. La cantidad de missing data es muy reducida
Parch: Imputación por moda. Al ser categorías conviene aplicar la más común
Fare: Eliminación. La cantidad de missing data es muy reducida
Embarked: Imputación por moda. Al ser categorías conveien aplicar la más común
'''

'''
Ejercicio 3
'''
missing_data = df.isnull().sum()

# Filtrar las columnas que no tienen valores faltantes
columns_with_no_missing_data = missing_data[missing_data == 0]

# Mostrar las columnas sin valores faltantes
print("Columnas sin valores faltantes:")
print(columns_with_no_missing_data.index.tolist())

'''
Ejercicio 4
'''

# Imputar valores faltantes en todo el DataFrame con la moda
df_imputacion_moda = df.fillna(df.mode().iloc[0])
print(df_imputacion_moda)

# Imputar valores faltantes en todo el DataFrame con la media
df_imputacion_media = df.fillna(df.mean())
print(df_imputacion_media)

#Imputar valores faltantes en todo el DataFrame con la mediana
df_imputacion_mediana = df.fillna(df.median())
print(df_imputacion_mediana)

df['Sex'] = df['Sex'].replace({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].replace({'C': 0, 'S': 1, 'Q': 2})
columnas_a_excluir = ['PassengerId', 'Name', 'Ticket', 'Cabin']

df_copy = df.copy()
df_copy=df_copy.drop(columnas_a_excluir, axis=1)
# Rellenar las columnas de las variables independientes con imputacion por moda o mediana
mode_age = df_copy['Age'].mean()
mode_sibsp = df_copy['SibSp'].median()
mode_parch = df_copy['Parch'].median()
mode_embarked = df_copy['Embarked'].mode()[0]
mode_fare = df_copy['Sex'].mode()[0]

df_copy['Age'].fillna(mode_age, inplace=True)
df_copy['SibSp'].fillna(mode_sibsp, inplace=True)
df_copy['Parch'].fillna(mode_parch, inplace=True)
df_copy['Embarked'].fillna(mode_embarked, inplace=True)
df_copy['Sex'].fillna(mode_fare, inplace=True)

#Regresión lineal para la variable Sex

train_data = df_copy.dropna()  # Eliminar filas con valores faltantes
test_data = df_copy[df_copy['Fare'].isna()]  # Filas con valores faltantes en 'Sex'

# Definir las variables independientes (características) y la variable dependiente (objetivo)
X_train = train_data[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Sex', 'Embarked']]
y_train = train_data['Fare']
X_test = test_data[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Sex', 'Embarked']]

model = LinearRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicciones para los valores faltantes en 'Sex'
predictions = model.predict(X_test)

# Asignar las predicciones a las filas con valores faltantes en 'Sex' en df_copy
df_copy.loc[df_copy['Fare'].isna(), 'Fare'] = predictions
print('Regresión lineal')
print(df_copy)
#Outliers percentile approach

def remove_outliers(df, column_name):
    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[column_name] >= lower_bound) & (df[column_name] <= upper_bound)]
    return df
df_outliers=remove_outliers(df,'Sex')
print(df_outliers)
df_outliers=remove_outliers(df,'SibSp')
print(df_outliers)
df_outliers=remove_outliers(df,'Parch')
print(df_outliers)
df_outliers=remove_outliers(df,'Embarked')
print(df_outliers)
df_outliers=remove_outliers(df,'Age')
print(df_outliers)
df_outliers=remove_outliers(df,'Fare')
print(df_outliers)

'''
Ejercicio 5

El método que más se acerca a la realidad para las variables categóricas como Sex o Embarked es el de imputación por moda,
pues al ser menos categorías se acercan más a la realidad.
Por otro lado, las variables númericas como Fare o Age el método que más se acerca a la realidad es el de regresión lineal,
pues este toma en cuenta las variables y trata de hacer una aproximación, además que es posible que los datos
se hayan encontrado relacionados entre sí.
'''

'''
Ejercicio 6
En conclusión, el metodo de regresión lineal es mas util si tienes datos relacionados, puedes utilizar la regresión 
para predecir los valores faltantes en función de las demás variables. Este enfoque es útil cuando los datos tienen 
una estructura más compleja.

La imputación por moda puede reemplazar los valores faltantes por la moda (el valor más común) de la columna respectiva.
Esto es útil para datos categóricos.

Por último, El enfoque de percentiles para outliers se basa en identificar valores atípicos mediante los percentiles Q1 y Q3, 
y suele ser útil cuando se necesita una detección rápida y sencilla de outliers en un contexto univariado y se prefiere un 
enfoque estadísticamente robusto.
'''


'''
Parte 2
'''
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MaxAbsScaler
'''
Ejercicio 1
'''
df1= pd.read_csv('titanic.csv')
df1=df1.drop(columnas_a_excluir,axis=1)
df1['Sex'] = df1['Sex'].replace({'male': 0, 'female': 1})
df1['Embarked'] = df1['Embarked'].replace({'C': 0, 'S': 1, 'Q': 2})

scaler = StandardScaler()
# Ajustar el escalador a los datos y transformar el DataFrame
df_scaled = pd.DataFrame(scaler.fit_transform(df_copy), columns=df_copy.columns)
df_scaled1= pd.DataFrame(scaler.fit_transform(df1), columns=df1.columns)
# df_scaled ahora contiene las columnas normalizadas
print('Standarization')
print(df_scaled)

scaler = MinMaxScaler()
# Ajustar el escalador a los datos y transformar el DataFrame
df_scaled = pd.DataFrame(scaler.fit_transform(df_copy), columns=df_copy.columns)
df_scaled1= pd.DataFrame(scaler.fit_transform(df1), columns=df1.columns)
# df_scaled ahora contiene las columnas normalizadas
print(df_scaled)

scaler = MaxAbsScaler()
# Ajustar el escalador a los datos y transformar el DataFrame
df_scaled = pd.DataFrame(scaler.fit_transform(df_copy), columns=df_copy.columns)
df_scaled1= pd.DataFrame(scaler.fit_transform(df1), columns=df1.columns)

# df_scaled ahora contiene las columnas normalizadas
print(df_scaled)

'''
Ejercicio 2

El método que más se acerco fue el de MinMaxScaling

El metodo de Standarization es útil cuando trabajas con algoritmos sensibles a la magnitud 
y varianza de las características, como la regresión lineal, SVM y k-means.

El método MaxMinScaling es útil cuando Útil cuando deseas que todos los valores estén dentro 
de un rango específico (por defecto, [0, 1]).

El método MaxAbsScaler conviene cuando deseas mantener la magnitud relativa de los valores, 
sin preocuparte por los signos.
'''