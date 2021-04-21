import requests
import requests_cache
from bs4 import BeautifulSoup

def main():
    print("Digite 1 para requisitar uma página, 2 para sair: ")
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        requests_cache.install_cache('banco')
        pagina = input("Digite o link da página: ")
        cont = 0
        cont2 = 0
        response = requests.get(pagina)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.select("a")
            lista = links[:10]

            for i in lista:
                cont += 1
                print(f"{cont} = ", i["href"])
        
            numero = int(input("Digite o número do link desejado: "))
            palavra_chave = input("Digite a palavra-chave: ")

            for i in lista:
                cont2 += 1
                if cont2 == numero:
                    busca_link(i["href"], palavra_chave)

        else:
            print(response.status_code)



def busca_link(link, palavra):
    cont_palavra = 0
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        ocorrencia = soup.get_text()
        for i in ocorrencia.split():
            if palavra in i:
                cont_palavra += 1
        
        print(f"A palavra {palavra} ocorre {cont_palavra} vezes")

    else:
        print(response.status_code)

    main()


main()