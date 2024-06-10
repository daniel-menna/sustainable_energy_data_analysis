## Introdução

Investir em energias renováveis é crucial, considerando as mudanças climáticas atuais, pois reduz as emissões de gases de efeito estufa, mitigando o aquecimento global e os eventos climáticos extremos. As energias renováveis, como solar e eólica, fornecem fontes de energia sustentáveis e de baixo carbono, diminuindo a dependência de combustíveis fósseis e aumentando a segurança energética. Além disso, estimulam o crescimento econômico por meio da criação de empregos e da inovação. A transição para as energias renováveis é vital para proteger os ecossistemas, a saúde pública e garantir um planeta habitável para as futuras gerações.

Este estudo tem o objetivo de entender os tipos de energia renovável disponíveis, sua capacidade e também os investimentos feitos em cada uma delas. Através de uma Análise Exploratória de Dados (AED), vamos explorar essas informações e encontrar alguns insights relevantes.

## Base de Dados e Bibliotecas utilizadas

Para realizar esta análise de dados, usaremos Python e algumas bibliotecas, portanto, é necessário garantir que as seguintes bibliotecas estejam instaladas e importá-las:

- Plotly Express;
- Matplotlib Pyplot;
- Matplolib Ticker
- Pandas;
- Seaborn.

A base de dados utilizada está disponível no [Kaggle](https://www.kaggle.com/datasets/girumwondemagegn/dataset-for-renewable-energy-systems/data).

### Schema da Base de Dados

A base de dados é composta pelas seguintes variáveis:
- Tipo_de_Energia_Renovável: Código numérico representando o tipo de fonte de energia renovável (1: Solar, 2: Eólica, 3: Hidrelétrica, 4: Geotérmica, 5: Biomassa, 6: Maré, 7: Onda).
- Capacidade_Instalada_MW: Capacidade instalada em megawatts (MW).
- Produção_de_Energia_MWh: Produção anual de energia em megawatt-hora (MWh).
- Consumo_de_Energia_MWh: Consumo anual de energia em megawatt-hora (MWh).
- Capacidade_de_Armazenamento_de_Energia_MWh: Capacidade de armazenamento de energia em megawatt-hora (MWh).
- Eficiência_do_Armazenamento_Porcentagem: Eficiência dos sistemas de armazenamento de energia em porcentagem.
- Nível_de_Integração_à_Rede: Código numérico representando o nível de integração à rede (1: Totalmente Integrado, 2: Parcialmente Integrado, 3: Integração Mínima, 4: Microrede Isolada).
- Investimento_Inicial_USD: Custos de investimento inicial em USD.
- Fontes_de_Financiamento: Código numérico representando a fonte de financiamento (1: Governo, 2: Privado, 3: Parceria Público-Privada).
- Incentivos_Financeiros_USD: Incentivos financeiros em USD.
- Redução_de_Emissões_de_GEE_tCO2e: Redução nas emissões de gases de efeito estufa em toneladas de CO2 equivalente (tCO2e).
- Índice_de_Redução_da_Poluição_do_Ar: Índice de redução da poluição do ar.
- Empregos_Criados: Número de empregos criados.

## Questões de negócio

### Quais são os tipos de energia renovaveis presentes no estudo e os seus investimentos?
De acordo com a fonte de dados, podemos ver que a produção de energia em MWh por tipo é muito semelhante. Além disso, de acordo com o valor investido, as fontes de financiamento também investiram quantias semelhantes.

<img src="pics/1.png" width=800>

### Quais tipos de energia renovável criaram mais empregos?
Para esta análise, o número de funcionários envolvidos nesses investimentos é semelhante, embora o tipo eólico tenha o maior valor, com 5.530.174 funcionários.

<img src="pics/2.png" width=800>

### Quail das energiais possui maior potencial de redução nas emissões dos gases do efeito estufa?
De acordo com os resultados deste estudo, a Biomassa, em média, tem o maior potencial de redução com 25.645,694359 tCO2e.

<img src="pics/3.png"  width=800>

### Qual a capacidade de produção e o consumo das energias renovaveis?
Para todos os tipos de fontes, a capacidade atual é maior que a demanda. Portanto, há espaço para adoção com a capacidade atual. Também é possível verificar que a Eólica tem a maior capacidade.

<img src="pics/4.png" width=800>

### Em média, quais foram as fontes de energia com maior investimento e, também, as que receberam maiores subsidios?
De acordo com este estudo, em média, a energia das marés recebeu mais investimentos.

<img src="pics/5.png"  width=800>

Além disso, em relação ao financiamento utilizado para apoiar esses investimentos, a energia eólica está recebendo maiores recursos.

<img src="pics/6.png"  width=800>

## Conclusões e sugestões para análise futuras
Para este projeto, nosso principal objetivo foi encontrar insights a partir dos dados. Aqui estão algumas descobertas principais:

- **Fonte de Financiamento:** A principal fonte de financiamento é a parceria público-privada, representando 33,6% do total.
- **Emprego:** A energia das marés emprega muitas pessoas, criando uma média de 2.519 empregos.
- **Redução de Emissões de GEE:** A biomassa lidera na redução de emissões de GEE, com uma redução média de 25.645,69 tCO2e.
- **Redução da Poluição do Ar:** A energia solar tem o maior índice de redução da poluição do ar, com uma média de 51,61.
- **Produção de Energia:** A energia geotérmica tem a maior produção média de energia, com 252.893,83 MWh.
- **Consumo de Energia:** A energia hidrelétrica tem o menor consumo médio de energia, com 221.711,58 MWh.
- **Capacidade de Armazenamento de Energia:** A biomassa lidera na capacidade de armazenamento de energia, com uma média de 5.066,70 MWh.
- **Investimento Inicial:** A energia das marés tem o menor investimento inicial, com uma média de $247.874.200.
- **Incentivos Financeiros:** A energia eólica recebe os maiores incentivos financeiros, com uma média de $10.232.840.

Para estudos futuros, a sugestão é explorar a relação entre:
- Emissões de GEE e o custo dos investimentos para definir o melhor cenário;
- Potencial de redução das emissões com os fundos disponíveis;
- O impacto social e econômico que seria criado considerando os novos empregos que seriam gerados.

No entanto, para completar esta análise, é importante verificar a possibilidade de coletar dados adicionais sobre a geografia e a disponibilidade de fontes de energia. Isso impactará a definição dependendo do país, por exemplo.



