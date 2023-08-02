# Manga Downloader
O Manga Downloader é um programa em Python que permite baixar automaticamente as imagens dos capítulos de mangás a partir de links fornecidos. O programa é capaz de criar pastas específicas para cada capítulo baixado, garantindo uma organização eficiente das imagens.
**Título do Projeto: Manga Downloader**

**Descrição:**
O Manga Downloader é um programa em Python que permite baixar automaticamente as imagens dos capítulos de mangás a partir de links fornecidos. O programa é capaz de criar pastas específicas para cada capítulo baixado, garantindo uma organização eficiente das imagens.

**Recursos:**
- Baixar imagens de capítulos de mangás a partir de links fornecidos.
- Criar pastas individuais para cada capítulo baixado, garantindo organização e facilidade de acesso.
- Interface simples e intuitiva, facilitando o uso para qualquer usuário.

**Como Usar:**
1. Clone este repositório em sua máquina local.
2. Certifique-se de ter o Python instalado em sua máquina.
3. No terminal ou prompt de comando, navegue até o diretório onde o repositório foi clonado.
4. Execute o programa digitando o seguinte comando:
   ```
   python manga_downloader.py
   ```
5. O programa solicitará que você informe o link do capítulo do mangá que deseja baixar. Insira o link e pressione Enter.
6. O Manga Downloader irá baixar automaticamente as imagens do capítulo e criará uma pasta com o número do capítulo para armazenar as imagens.
7. Repita o processo para baixar outros capítulos de mangás.

**Observações:**
- Certifique-se de ter uma conexão estável com a internet para o correto funcionamento do programa.
- O Manga Downloader não hospeda nem fornece links para mangás, apenas baixa as imagens a partir de links fornecidos pelo usuário.
- O programa funciona e foi testado para o site **https://mangahost4.com/**, para demais site é preciso fazer modificações no código (principalmente na função capítulos que faz o web scraping dos links das imagens).

**Requisitos:**
- Python 3.x
- Biblioteca BeautifulSoup (para fazer a análise do HTML e extração dos links das imagens)
- Biblioteca requests (para fazer as requisições HTTP para baixar as imagens)
- Biblioteca os (para criar os diretórios)

**Licença:**
Este projeto está licenciado sob a licença GNU General Public License (GPL). Sinta-se à vontade para usá-lo, modificá-lo e distribuí-lo de acordo com os termos da licença.

**Contribuições:**
Contribuições para a melhoria do programa são bem-vindas! Se você encontrou algum bug ou tem alguma ideia para adicionar novos recursos, sinta-se à vontade para abrir uma issue ou um pull request neste repositório.

**Autor:**
[Thiago Lopes]

**Contato:**
[Thiagolopesalmeida1230@gmail.com]
