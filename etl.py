import pandas as pd

class ETLProcess:
    def __init__(self, fonte_dados):
        self.fonte_dados = fonte_dados

    def extrair_dados(self):
        raise NotImplementedError("Metodo extrair dados deve ser implementado nas classes filhas")
    
    def transformar_dados(self, dados):
        raise NotImplementedError("Metodo transformar dados deve ser implementado nas classes filhas")
    
    def carregar_dados(self, dados_transformados):
        raise NotImplementedError("Metodo carregar dados deve ser implementado nas classes filhas")
    
    def executar_etl(self):
        dados_extraidos = self.extrair_dados()
        dados_transformados = self.transformar_dados(dados_extraidos)
        self.carregar_dados(dados_transformados)
        
class ETLcsv(ETLProcess):
    def extrair_dados(self):
        return  pd.read_csv(self.fonte_dados)
    
    def transformar_dados(self, dados):
        # exemplo simples de transformacao: converter todas as letras em maiusculas
        return dados.applymap(lambda x: x.upper() if isinstance(x, str) else x)
    
    def carregar_dados(self, dados_transformados):
        # aqui voce pode implementar a logica para carregar os dados transformados para onde desejar
        print("dados transformados:")
        print(dados_transformados)


class ETLxls(ETLProcess):
    def __init__(self, fonte_dados):
        super().__init__(fonte_dados)

    def extrair_dados(self):
        print("all")    # exemplo, so para dizer que eu tenho liberdade de implementar como eu quisar aqui
        return super().extrair_dados()
    def transformar_dados(self, dados):
        return super().transformar_dados(dados)
    

    # exemplo de uso

if __name__ == __main__:
    fonte_csv = "dados.csv"    # substitua dados.csv pelo caminho do seu arquivo csv
    etl_csv = ETLcsv(fonte_csv)
    etl_csv.executar_etl()

