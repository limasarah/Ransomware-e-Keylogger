from cryptography.fernet import Fernet
import os


def carregar_chave():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    chave_path = os.path.abspath(os.path.join(script_dir, "..", "chave.key"))
    with open(chave_path, "rb") as chave_file:
        return chave_file.read()


def descritografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados_encriptografados = file.read()
    dados_descritografados = f.decrypt(dados_encriptografados)
    with open(arquivo, "wb") as file:
        file.write(dados_descritografados)


def encontrar_arquivos(diretorio):
    lista = []
    nome_script = os.path.basename(__file__)
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != nome_script and not nome.endswith(".key"):
                lista.append(caminho)
    return lista


def main():
    chave = carregar_chave()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    arquivos = encontrar_arquivos(script_dir)
    for arquivo in arquivos:
        descritografar_arquivo(arquivo, chave)
    print("arquivos restaurados com sucesso!")


if __name__ == "__main__":
    main()