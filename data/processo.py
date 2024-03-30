def escrever_temp(txt_file, ano, media):
    linha = f'INSERT INTO TempGlobal VALUES (0, {ano}, {media});\n'
    txt_file.write(linha)


def escrever_emissao(txt_file, ano, pais, total, solid, liquid, gas, cement, gas_flaring, per_capita, bunker):
    linha = f'INSERT INTO EmissoesCO2 VALUES (0, {ano}, {pais}, {total}, {solid}, {liquid}, {gas}, {cement}, {gas_flaring}, {per_capita}, {bunker});\n'
    txt_file.write(linha)


def escrever_idh(txt_file, pais, idh):
    linha = f'INSERT INTO IDHpaises2014 VALUES (0, {pais}, {idh});\n'
    txt_file.write(linha)


def main():
    # Nomes de arquivos a receber e gerar
    arq_gerar = 'query.txt'
    arq_recebe1 = 'annual.csv'
    arq_recebe2 = 'fossil-fuel-co2-emissions-by-nation.csv'
    arq_recebe3 = 'human-development-index-hdi-2014.csv'
    # Base de criação das tabelas
    base = '''
    -- Criação da tabela TempGlobal
    CREATE TABLE IF NOT EXISTS TempGlobal (
        id INTEGER PRIMARY KEY,
        ano INTEGER,
        media_desvio REAL
    );

    -- Criação da tabela EmissoesCO2
    CREATE TABLE IF NOT EXISTS EmissoesCO2 (
        id INTEGER PRIMARY KEY,
        ano INTEGER,
        pais TEXT,
        total(not_bunker) REAL,
        combust_solido REAL,
        combust_liquid REAL,
        combust_gas REAL,
        cimento REAL,
        queima_gas REAL,
        per_capita REAL,
        combust_bunker REAL
    );

    -- Criação da tabela IDHpaises2014
    CREATE TABLE IF NOT EXISTS IDHpaises (
        id INTEGER PRIMARY KEY,
        pais TEXT,
        idh REAL
    );\n\n'''

    # Inicializa o arquivo TXT
    with open(arq_gerar, 'w+', encoding='utf-8') as txt_file:
        txt_file.write(base)

        # Preparando a importação, contador e as variáveis dos estados
        from csv import DictReader

        # Abre o CSV de temperatura global
        with open(arq_recebe1, 'r', encoding='utf-8') as csv_file:
            leitor_csv = DictReader(csv_file)
            for linha_csv in leitor_csv:
                if linha_csv['Source'] == 'GISTEMP' and int(linha_csv['Year']) >= 1880 and int(linha_csv['Year']) <= 2014:
                    # Chama a função para escrever a linha no arquivo TXT
                    escrever_temp(txt_file, linha_csv['Year'], linha_csv['Mean'])

        # Abre o CSV de emissão de CO2
        with open(arq_recebe2, 'r', encoding='utf-8') as csv_file:
            leitor_csv = DictReader(csv_file)
            for linha_csv in leitor_csv:
                if int(linha_csv['Year']) >= 1880:
                    escrever_emissao(txt_file, linha_csv['Year'], linha_csv['Country'], linha_csv['Total'], linha_csv['Solid Fuel'], linha_csv['Liquid Fuel'], linha_csv['Gas Fuel'], linha_csv['Cement'], linha_csv['Gas Flaring'], linha_csv['Per Capita'], linha_csv['Bunker fuels (Not in Total)'])

        # Abre o CSV de IDH
        with open(arq_recebe3, 'r', encoding='utf-8') as csv_file:
            leitor_csv = DictReader(csv_file)
            for linha_csv in leitor_csv:
                escrever_idh(txt_file, linha_csv['Location'].upper(), linha_csv['Human Development Index (HDI)'])

    txt_file.close()

    print('-----------------------------------------------------------------------------------------')
    print('|                     Processo encerrado. Arquivo criado com sucesso!                     |')
    print('|                    Obrigado por usar um algoritmo de antthLuca. (^-^)                   |')
    print('-----------------------------------------------------------------------------------------')


if __name__ == "__main__":
    main()