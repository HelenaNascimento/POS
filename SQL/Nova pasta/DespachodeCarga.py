import sqlite3
from datetime import datetime

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# Função para listar portos
def listar_portos():
    cursor.execute("SELECT Id_Porto, Nome_Porto, Localizacao FROM Porto")
    portos = cursor.fetchall()
    return portos

# Função para inserir carga
def inserir_carga( Destino, Peso, Dat_Max, Obs, Dat_Validade, Tem_Max):
    cursor.execute('''
    INSERT INTO Carga ( Destino, Peso, Dat_Max, Obs, Dat_Validade, Tem_Max)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', ( Destino, Peso, Dat_Max, Obs, Dat_Validade, Tem_Max))
    conn.commit()
    print("Carga inserida com sucesso!")

# Função principal para inserir uma nova carga
def main():
    # Listar portos disponíveis
    portos = listar_portos()
    if not portos:
        print("Nenhum porto disponível.")
        return

    # Mostrar portos disponíveis
    print("Portos disponíveis:")
    for porto in portos:
        print(f"{porto[0]}: {porto[1]}")

    # Selecionar porto de destino
    porto_destino = int(input("Selecione o código do porto de destino: "))

    # Verificar se o porto selecionado é válido
    if porto_destino not in [porto[0] for porto in portos]:
        print("Código de porto inválido.")
        return

    # Coletar dados da carga
    peso = float(input("Insira o peso da carga (kg): "))
    data_maxima_desembarque = input("Insira a data máxima para desembarque (YYYY-MM-DD): ")
    data_validade = input("Insira a data de validade (YYYY-MM-DD) ou deixe em branco se não for perecível: ")
    temperatura_maxima = input("Insira a temperatura máxima (Celsius) ou deixe em branco se não for sensível: ")

    # Validar datas
    try:
        datetime.strptime(data_maxima_desembarque, "%Y-%m-%d")
        if data_validade:
            datetime.strptime(data_validade, "%Y-%m-%d")
    except ValueError:
        print("Formato de data inválido.")
        return

    # Inserir a nova carga no banco de dados
    inserir_carga(porto_destino, peso, data_maxima_desembarque, data_validade or None, temperatura_maxima or None)

if __name__ == "__main__":
    main()
    conn.close()
