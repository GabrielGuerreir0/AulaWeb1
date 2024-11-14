import util

def ler_dados_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    return linhas

def processar_dados_clientes(linhas):
    idades = []
    rendas = []

    for linha in linhas:
        dados = linha.strip().split(';')
        if len(dados) == 4:  
            try:
                idade = int(dados[2])
                renda = float(dados[3])
                idades.append(idade)
                rendas.append(renda)
            except ValueError:
                print(f"Erro ao converter dados: {linha}")

    return idades, rendas

def main():
    nome_arquivo = 'clientes.txt'
    linhas = ler_dados_arquivo(nome_arquivo)
    idades, rendas = processar_dados_clientes(linhas)

    media_idade = util.calcular_media(idades)
    media_renda = util.calcular_media(rendas)

    print(f"Média de idade dos clientes: {media_idade:.2f} anos")
    print(f"Média de renda mensal dos clientes: R$ {media_renda:.2f}")

if __name__ == '__main__':
    main()
