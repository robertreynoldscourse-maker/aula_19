import pandas as pd 
import numpy as np

# Obtendo os dados com PANDAS

try:
    print('Obtendo os dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # iso-8859-1 | utf-8 | latin1 | cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep = ';', encoding = 'iso-8859-1')
    
    # Delimitar as variáveis
    df_roubo_vehiculo = df_ocorrencias[['munic', 'roubo_veiculo']]

    # Agrupando e quantificando as variáveis quantitativas
    df_roubo_vehiculo = df_roubo_vehiculo.groupby('munic', as_index=False)['roubo_veiculo'].sum()

    # Ordenando em decrescente:
    df_roubo_vehiculo = df_roubo_vehiculo.sort_values(by='roubo_veiculo', ascending=False)

    print(df_roubo_vehiculo)



    #print(df_ocorrencias)

except Exception as e:
    print(f'Erro ao obter os dados: {e}')

# Obtendo informações com NUMPY
try:
    print('Obtendo informações a cerca dos roubos de veiculos... ')
    array_roubo_veiculo = np.array(df_roubo_vehiculo['roubo_veiculo'])

    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    distancia = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo * 100) # *100 para ter em porcentagem

    print('\nMEDIDAS DE TENDÊNCIA CENTRAL')
    print(40*'=')
    print(f'A media é : {media_roubo_veiculo:.2f}')
    print(f'A mediana é : {mediana_roubo_veiculo:.2f}')
    print(f'Distância entre a media e mediana: {distancia:.2f}%')
    ## Distancia entre 0 e 10, a tendencia é simétrica
    ## Distancia entre 10 e 25, a tendencia é simétrica moderado, a media pode estar sofrendo influencia dos extremos
    ### a media ainda pode ser utilizado como medida central representativa.
    ## Distancia maior a 25, a tendencia é asimétrica (dados altamente heterogéneos)
    ### a media não é uma medida central representativa (confiável) porque os dados são completamente asimétricos.
    
    ## Obtendo os quartis
    print('\nMEDIDAS DE POSIÇÃO')
    print(40*'=')
    q1 = np.quantile(array_roubo_veiculo, 0.25)
    print(f'Primer quartil: {q1:.2f}')
    q2 = np.quantile(array_roubo_veiculo, 0.5)
    print(f'Segundo quartil: {q2:.2f}')
    q3 = np.quantile(array_roubo_veiculo, 0.75)
    print(f'Terceiro quartil: {q3:.2f}')

    # MENORES
    df_roubo_veiculo_menores = df_roubo_vehiculo[df_roubo_vehiculo['roubo_veiculo'] < q1]

    # MAIORES
    df_roubo_veiculo_maiores = df_roubo_vehiculo[df_roubo_vehiculo['roubo_veiculo'] > q3]
    # Ordem crescente
    print('\nMunicípios com Menos Roubos')
    print(40*'=')
    print(df_roubo_veiculo_menores.sort_values(by = 'roubo_veiculo', ascending = True))
    # Ordem decrescente
    print('\nMunicipios com Mais Roubos')
    print(40*'=')
    print(df_roubo_veiculo_maiores)


except Exception as e:
    print(f'Erro ao calcular as informações... ')

