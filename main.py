# Importando as bibliotecas a serem utilizadas neste estudo.
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker 
import seaborn as sns

# Lendo o arquivo csv extraido do Kaggle
df = pd.read_csv('\energy_dataset_.csv')

# Checando as medidas resumo das variáveis presentes na base de dados
df.describe()

# Checando valores duplicados
df.duplicated().sum()

# Checando valores faltanntes
df.isnull().sum()

# Ajustando os labels para as variáveis qualitativas do tipo de energia e origem dos fundos de investimento
df['Type_of_Renewable_Energy'] = df['Type_of_Renewable_Energy'].astype(str)
 
mapping = {
    '1': 'Solar',
    '2': 'Wind',
    '3': 'Hydroelectric',
    '4': 'Geothermal',
    '5': 'Biomass',
    '6': 'Tidal',
    '7': 'Wave'
}

 
df['Type_of_Renewable_Energy'] = df['Type_of_Renewable_Energy'].map(mapping)

df['Funding_Sources'] = df['Funding_Sources'].astype(str)
 
funding_mapping = {
    '1': 'Government',
    '2': 'Private',
    '3': 'Public-Private Partnership'
}
 
df['Funding_Sources'] = df['Funding_Sources'].map(funding_mapping)

# Checando se as transformações estão corretas
df.head()

# Criando duas variáveis de agregaçao para  "Type_of_Renewable_Energy" e "Funding_Sources"
energy_production = df.groupby('Type_of_Renewable_Energy')['Energy_Production_MWh'].sum().reset_index()
funding_investments = df.groupby('Funding_Sources')['Initial_Investment_USD'].sum().reset_index()

# Criando gráficos de pizza para as variáveis acima.
fig, ax = plt.subplots(1, 2, figsize=(14, 7))

ax[0].pie(energy_production['Energy_Production_MWh'], labels=energy_production['Type_of_Renewable_Energy'], autopct='%1.1f%%', startangle=140)
ax[0].set_title('Energy Production by Renewable Energy Types')

ax[1].pie(funding_investments['Initial_Investment_USD'], labels=funding_investments['Funding_Sources'], autopct='%1.1f%%', startangle=140)
ax[1].set_title('Initial Investments by Funding Sources')

plt.tight_layout()
plt.show()

# Gerando gráficos de barras para as demais variaveis
sns.set_style('whitegrid') 

plt.figure(figsize=(10, 18)) 

plt.subplot(3, 1, 1)
df_jobs = df.groupby('Type_of_Renewable_Energy')['Jobs_Created'].mean().reset_index()
sns.barplot(x='Type_of_Renewable_Energy', y='Jobs_Created', data=df_jobs, palette='coolwarm')
plt.title('Average Jobs Created by Type of Renewable Energy')

# Emissão de gases do efeito estufa
plt.subplot(3, 1, 2)
df_ghg = df.groupby('Type_of_Renewable_Energy')['GHG_Emission_Reduction_tCO2e'].mean().reset_index()
sns.barplot(x='Type_of_Renewable_Energy', y='GHG_Emission_Reduction_tCO2e', data=df_ghg, palette='viridis')
plt.title('Average GHG Emission Reduction (tCO2e) by Type of Renewable Energy')

# Reduçao na poluição do ar
plt.subplot(3, 1, 3)
df_air = df.groupby('Type_of_Renewable_Energy')['Air_Pollution_Reduction_Index'].mean().reset_index()
sns.barplot(x='Type_of_Renewable_Energy', y='Air_Pollution_Reduction_Index', data=df_air, palette='magma')
plt.title('Average Air Pollution Reduction Index by Type of Renewable Energy') 

plt.xticks(rotation=45) 

plt.tight_layout() 

plt.show()

# Sumarizando os dados de "Type_of_Renewable_Energy" para as próximas análises
df_ed = df.groupby('Type_of_Renewable_Energy')[['Energy_Production_MWh','Energy_Consumption_MWh', 'Energy_Storage_Capacity_MWh']] .mean().reset_index()              
df_ed

ax = df_ed.plot(x='Type_of_Renewable_Energy', kind='bar', stacked=False, figsize=(10, 6)) 

ax.set_title('Average Energy Metrics by Type of Renewable Energy')
ax.set_xlabel('Type of Renewable Energy')
ax.set_ylabel('Average MWh') 

ax.legend(title='Metrics') 

plt.show()

# Extraindo a média da variável 'Initial_Investment_USD' e 'Financial_Incentives_USD' para as próximas análises
df_fd = df.groupby('Type_of_Renewable_Energy')['Initial_Investment_USD' ].mean().reset_index()
df_fd2 = df.groupby('Type_of_Renewable_Energy')['Financial_Incentives_USD'].mean().reset_index()

sns.set_style('whitegrid')

# Criando subplots
fig, ax = plt.subplots(2, 1, figsize=(14, 14))

# Apresentado o investimento médio inicial em USD
sns.barplot(x='Initial_Investment_USD', y='Type_of_Renewable_Energy', data=df_fd, ax=ax[0], palette='viridis')
ax[0].set_title('Average Initial Investment (USD)')
ax[0].set_xlabel('Average Investment (USD)')
ax[0].set_ylabel('Type of Renewable Energy') 

ax[0].xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))

# Apresentando os incentivos médios em USD
sns.barplot(x='Financial_Incentives_USD', y='Type_of_Renewable_Energy', data=df_fd2, ax=ax[1], palette='viridis')
ax[1].set_title('Average Financial Incentives (USD)')
ax[1].set_xlabel('Average Incentives (USD)')
ax[1].set_ylabel('Type of Renewable Energy') 

ax[1].xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:,.0f}')) 

plt.tight_layout() 

plt.show()

