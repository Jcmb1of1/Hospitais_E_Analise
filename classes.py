import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

class Consultas:
    def __init__(self, url):
        self.df = pd.read_csv(url, sep=';', encoding='latin1')


    def mostrar_estabelecimentos(self, estado:str = 'sp', limite_estabelecimentos:int = 10):
        '''
        :param estado: Estado que os hospitais residem
        :param limite_estabelecimentos: quantidade de hospitais que serão mostrados, caso nada seja passado, 10 hospitais serão mostrados
        '''
        estado = estado.upper()
        temp_df = self.df.copy()
        #aqui verifica se o estado está na tabela
        if estado not in self.df['UF'].values:
            print('Estado não encontrado')
        else:
            #SUbstituindo os itens que faltam por não encontrados.
            temp_df['NU_ENDERECO'] = temp_df['NU_ENDERECO'].replace('S/N', 'Endereço não encontrado')
            temp_df = temp_df.fillna({'NU_ENDERECO': 'Endereço não informado', 'NU_TELEFONE': 'Telefone não informado', 'NO_EMAIL': 'Email não encontrado'})

            #Informações mostradas
            print(temp_df[['NOME_ESTABELECIMENTO', 'NU_TELEFONE', 'NU_ENDERECO', 'NO_BAIRRO', 'NO_EMAIL']][temp_df['UF'] == estado].head(limite_estabelecimentos))


class Analise:
    def __init__(self, url):
        self.df = pd.read_csv(url, sep=';', encoding='latin1')

    def estabelecimentos_por_estado(self):
        novo_df = self.df.copy()
        df_temp = novo_df.groupby(['UF']).nunique()['CNES']
        estados, quant = [*df_temp.index], [*df_temp.values]
        plt.barh(estados, quant)
        plt.xlabel('Quantida de estabelecimentos')
        plt.ylabel('Estados')
        plt.title('Estabelecimentos de sáude por estado.')
        plt.show()

