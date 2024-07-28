import pandas as pd

dataframe = pd.read_excel('./dataframe.xlsx')

###### Verificação de importação de dados: 
print(dataframe)

## Imprimir as primeiras linhas:
print("Primeiras linhas:")
print(dataframe.head())

## Imprimir as últimas linhas:
print("Últimas linhas:")
print(dataframe.tail())

### Cópia do conjunto de dados original:
new_dataframe = dataframe.copy()

### Substituindo os valores NaN da coluna Calories e imprimindo o resultado:
for index, calories in new_dataframe['Calories'].items():
    if pd.isna(calories):
        new_dataframe.at[index, 'Calories'] = 0
        
print(new_dataframe)

### Substituindo os valores NaN da coluna Date, imprimindo o resultado e transformando a string em data:
for index, date in new_dataframe['Date'].items():
    if pd.isna(date):
        new_dataframe.at[index, 'Date'] = '1900/01/01'
    
    new_dataframe.at[index, 'Date'] = pd.to_datetime(new_dataframe.at[index, 'Date'])
        
print(new_dataframe)

### Substituindo a data 1900/01/01 por nulo e imprimindo o resultado:
new_dataframe.loc[new_dataframe['Date'] == pd.Timestamp('1900-01-01 00:00:00'), 'Date'] = pd.NaT

print(new_dataframe)

### Removendo os registros que contenham valores nulos em Date:
new_dataframe = new_dataframe.dropna(subset=['Date'])
print(new_dataframe)