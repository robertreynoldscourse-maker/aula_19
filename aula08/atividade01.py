import pandas as pd 
import numpy as np

# Obtendo os dados com PANDAS

try:
    print('Obtendo os dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # iso-8859-1 | utf-8 | latin1 | cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep = ';', encoding = 'iso-8859-1')
    
    # Delimitar as variáveis
    df_estelionato = df_ocorrencias[['mes_ano', 'estelionato']] ##Variável qualitativa: mes_ano, variavel quantitativa: estelionato

    # Agrupando e quantificando as variáveis quantitativas
    df_estelionato = df_ocorrencias.groupby(['mes_ano'], as_index = False)['estelionato'].sum()

    # Ordenando em decrescente:
    #df_estelionato_anual = df_roubo_vehiculo.sort_values(by='roubo_veiculo', ascending=False)

    #print(df_estelionato.head(15))
    

except Exception as e:
    print(f'Erro ao obter os dados: {e}')
    #exit() opcional para sair do programa se não dar certo

# Obtendo informações com NUMPY
# CALCULANDO MEDIDAS ESTATISTICAS

try:
    print('Obtendo informações a cerca dos estelionatos... ')
    array_estelionato = np.array(df_estelionato['estelionato'])
    #array_mes_ano = np.array(df_estelionato['mes_ano']) não é necessário
    '''
    total_geral = np.sum(array_estelionato)
    idx_maior = np.argmax(array_estelionato)
    idx_menor = np.argmin(array_estelionato)

    mes_maior = df_estelionato_mensal['mes_ano'].iloc[idx_maior]
    mes_menor = df_estelionato_mensal['mes_ano'].iloc[idx_menor]

    
    print(f'Maior: {idx_maior}, mes: {mes_maior}')
    print(f'Menor: {idx_menor}, mes: {mes_menor}')
    print(f'O total de estelionatos é: {total_geral}')

    
    pct_maior = (array_estelionato[idx_maior] / total_geral) * 100
    pct_menor = (array_estelionato[idx_menor] / total_geral) * 100
    print(45*'=')
    print('Comparação dos periodos com o total de registros.')
    print(f'Porcentagem maior: {pct_maior:.2f}')
    print(f'Porcentagem menor: {pct_menor:.2f}')
    '''   
    
    ## Obtendo os quartis
    print('\nMEDIDAS DE POSIÇÃO')
    print(40*'=')
    #q1 = np.quantile(array_estelionato, 0.25, method = 'weibull')
    q1 = np.quantile(array_estelionato, 0.25)
    print(f'Primer quartil: {q1:.2f}')
    #q2 = np.quantile(array_estelionato, 0.5) #CORRESPONDE A MEDIANA
    #print(f'Segundo quartil: {q2:.2f}')
    q3 = np.quantile(array_estelionato, 0.75)
    print(f'Terceiro quartil: {q3:.2f}')

    # MENORES
    df_estelionato_menores = df_estelionato[df_estelionato['estelionato'] < q1]

    # MAIORES
    df_estelionato_maiores = df_estelionato[df_estelionato['estelionato'] > q3]
    # Ordem crescente
    print('\nMes_ano com Menos Estelionatos')
    print(40*'=')
    print(df_estelionato_menores.sort_values(by = 'estelionato', ascending = False).head(30))
    # Ordem decrescente
    print('\nMes_ano com Mais Estelionatos')
    #print(40*'=')
    print(df_estelionato_maiores.sort_values(by = 'estelionato', ascending = True).head(30))
    


    print('\nMEDIDAS DE TENDÊNCIA CENTRAL')
    media_estelionato = np.mean(array_estelionato)
    mediana_estelionato = np.median(array_estelionato)
    distancia = abs((media_estelionato - mediana_estelionato) / mediana_estelionato * 100) # *100 para ter em porcentagem

    print(40*'=')
    print(f'A media é : {media_estelionato:.2f}')
    print(f'A mediana é : {mediana_estelionato:.2f}')
    print(f'Distância entre a media e mediana: {distancia:.2f}%')
    ## Distancia entre 0 e 10, a tendencia é simétrica
    ## Distancia entre 10 e 25, a tendencia é simétrica moderado, a media pode estar sofrendo influencia dos extremos
    ### a media ainda pode ser utilizado como medida central representativa.
    ## Distancia maior a 25, a tendencia é asimétrica (dados altamente heterogéneos)
    ### a media não é uma medida central representativa (confiável) porque os dados são completamente asimétricos.

except Exception as e:
    print(f'Erro ao calcular as informações... ')


########caso o git não queira subir a gente tem que digitar o seguinte comando
    ## depois de git init sempre digitar
    ## git pull origin main 