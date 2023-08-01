import requests
from bs4 import BeautifulSoup
import os

#serve para pegar o url das imagem de cada capítulo
def capitulos(url, posicao, header):
    endereco = url.format(posicao)
    response = requests.get(endereco, headers=header)
    if response.status_code == requests.codes.OK:
        content = response.content #pega o conteúdo do request
        site = BeautifulSoup(content, 'html.parser') #transforma no formato que dá para manipular
        # print(site.prettify())
        #prettify organiza a formatação
        chapters = site.findAll("picture") #procura a tag picture
        # chapter = site.findAll('div', attrs={'class':"img_class"}) #procura todas as div com a class img_class
        url_caps = [] # arrya onde vai salvar os link das imagens
        for chapter in chapters:
            url_caps.append(chapter.source['srcset']) #especifica a tag source dentro do picture, pegando o link da imagem que está no srcset
        return url_caps #retorna o array apenas com os links das imagens
    else:
        print("Erro ao acessar a página:", response.status_code)

#baixa as imagem
def baixar_arquivos(url_img, local_save, header, stream=True):
    #gravando o que vier do request da url para a variável
    #abrir o arquivo no formato que desejar e usar o w = write e b = binário
    try:
        response =  requests.get(url_img, headers=header)
        if response.status_code == 200: #verifica o status do request
            with open(local_save, "wb") as novo_arquivo: 
                #salvando o conteúdo do arquivo
                novo_arquivo.write(response.content)
                print("Download Finalizado. Salvo em {}".format(local_save))
        else:
            print("Erro ao baixar a imagem. Status code:", response.status_code)
    except Exception as e:
        print("Erro ao baixar a imagem:", e)

#cria a pasta
def criar_pasta(BASE_PATH, posicao):
    try:
        os.mkdir(BASE_PATH + str(posicao)) #cria a pasta 
    except OSError:
        print("Pasta já criada ou Erro")
         
#função principal 
if __name__ == "__main__":
    #esse código funciona para o site: https://mangahost4.com/, para outros sites precisa fazer algumas modificações principalmente na função capitulos
    BASE_PATH = r'local_onde_quer_salvar' #local onde quer salvar, vai ser aqui também que ele vai criar a pasta para salvar as imagens baixadas
    BASE_URL = "caminho_da_url{:02d}" #exemplo "https://mangahost4.com/manga/zombie-100-zombie-ni-naru-made-ni-shitai-100-no-koto-mh34679/{:02d}"
    #{:02d} é a numeração do capítulo no formato com dois dígitos (01,02...)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'} #necessário para não ter o erro 403 ao usar o request
    #j é quantidade de capitulos
    for j in range (35, 36): #a numeração é os capítulos, define a quantidade de capítulos que quer baixar
        #retorna o valor específico das imagem para ser usado quando for baixar
        value = capitulos(BASE_URL, j, header)
        criar_pasta(BASE_PATH, j) #chama função criar pasta onde vai ser salva as imagens
        #path é o local da pasta que foi criada para salvar as imagens
        path = os.path.join(BASE_PATH + str(j)) #o local + a posição 
        # # i é a quantidade de imagens que tem por capítulo
        for i in range(len(value)): #vê a quantidade de imagens necessárias para baixar
            try:
                #nome_arquivo vai juntar o local + mais a posição da imagem e no formato jpg
                nome_arquivo = os.path.join(path , str(i)+".jpg")
                #baixar arquivos passa o parâmetro value com o indice, o nome_arquivo que vai ser onde vai ser salvo e o formato, header que é necessário no request
                baixar_arquivos(value[i], nome_arquivo, header)
            except:
                print("Download Concluído ou Erro Verificar")


        

    
