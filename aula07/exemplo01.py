import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# Conectando os dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    # 'utf-8', 'iso-8859-1', latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    # print(df_ocorrencias.head())

    # Delimitando as variáveis
    df_roubo_veiculo = df_ocorrencias[['munic','roubo_veiculo']]

    # agrupando e quantificando  // reset_index() para aparecer o número das linhas
    df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()
    print(df_roubo_veiculo.head())

except Exception as e:
    print(f'Erro ao obter dados {e}')

# Obter informações do padrão de roubos de veículos
try:
    print('Obter informações do padrão de roubos de veículos')

    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

    # medidas de tendência central
    media = np.mean(array_roubo_veiculo)
    mediana = np.median(array_roubo_veiculo)
    distancia_media_mediana = ((media - mediana) / mediana) * 100

    print(f'\nDados de Medida Central')
    print(f'Média: {media:.2f}')
    print(f'Mediana: {mediana:.2f}')
    print(f'Distância Média e Mediana: {distancia_media_mediana:.2f}')

except Exception as e:
    print(f'Erro ao obter informações...{e}')

# Obtendo medidas estatísticas
try:

    q1 = np.quantile(array_roubo_veiculo, .25)
    q2 = np.quantile(array_roubo_veiculo, .50)
    q3 = np.quantile(array_roubo_veiculo, .75)

    print('\nMedidas de posição:')
    print(50*'-')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')

    # menores
    df_roubo_veiculo_menores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < q1]

    # maiores
    df_roubo_veiculo_maiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > q3]

    print('\nMenores')
    print(50*'-')
    print(df_roubo_veiculo_menores.sort_values(by='roubo_veiculo'))

    print('\nMaiores')
    print(50*'-')
    print(df_roubo_veiculo_maiores.sort_values(by='roubo_veiculo', ascending=False).head(5))

    # Medidas de dispersão
    maximo = np.max(array_roubo_veiculo)
    minimo = np.min(array_roubo_veiculo)
    amplitudetotal = maximo - minimo

    print('\nMedidas de dispersão: ')
    print(50*'-')
    print(f'Máximo: {maximo}')
    print(f'Mínimo: {minimo}')
    print(f'Amplitude total: {amplitudetotal}')

    # Calculo do Intervalo Inter Quartil o iqr
    iqr = q3 - q1
    print(50*'-')
    print('\nIntervalo Inter Quartil')
    print(f'O iqr é: {iqr}')

    # Limite inferior
    limite_inferior = q1 - (1.5 * iqr)
    
    # Limite superior
    limite_superior = q3 + (1.5 * iqr)

    print('\nLimite Inferior')
    print(50*'-')
    print(f'O limite inferior é: {limite_inferior}')
    
    print('\nLimite Superior')
    print(50*'-')
    print(f'O limite inferior é: {limite_superior}')

    # Outliers Inferiores
    df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior]
    
    # Outliers Superiores
    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior]

    print('\nOutliers Inferiores: ')
    print(50*'-')
    if len(df_roubo_veiculo_outliers_inferiores) == 0:
        print(50*'-')
        print('Não há outliers inferiores')
    else:
        print(50*'-')
        print(df_roubo_veiculo_outliers_inferiores.sort_values(by='roub_veiculo', ascending=True))
    
    print('\nOutliers Superiores: ')
    print(50*'-')
    if len(df_roubo_veiculo_outliers_superiores) == 0:
        print(50*'-')
        print('Não há outliers superiores')
    else:
        print(50*'-')
        print(df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=False))


except Exception as e:
    print(f'Erro ao obter informações {e}')

try:
    # pip install matplotlib
    print('Visualizando dados...')

    plt.subplots(2,2, figsize=(16, 7))
    plt.suptitle('Análise do Boxplot')

    plt.subplot(2, 2, 1)
    plt.boxplot(array_roubo_veiculo, vert=False, showfliers=False, showmeans=True)
    plt.title('Gráfico BoxPlot')


    plt.subplot(2, 2, 2)
    plt.boxplot(array_roubo_veiculo, vert=False, showmeans=True)
    plt.title('Gráfico BoxPlot')
    print('Posição 2')
    
    
    plt.subplot(2, 2, 3)
    print('Posição 3')
    
    
    plt.subplot(2, 2, 4)
    print('Posição 4')

    plt.show()

except Exception as e:
    print(f'Erro de plotagem de dados {e}')