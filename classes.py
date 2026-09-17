import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

class Consultas:
    def __init__(self, URL):
        self.df = pd.read_csv(URL, sep=';', encoding='latin1')


    def Mostrar_Hospitais(self, estado:str = 'sp', limite_hospitais:int = 10):
        '''
        :param estado: Estado que os hospitais residem
        :param limite_hospitais: quantidade de hospitais que serão mostrados, caso nada seja passado, 10 hospitais serão mostrados
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
            print(temp_df[['NOME_ESTABELECIMENTO', 'NU_TELEFONE', 'NU_ENDERECO', 'NO_BAIRRO', 'NO_EMAIL']][temp_df['UF'] == estado].head(limite_hospitais))
