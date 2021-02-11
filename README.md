# Web Crawler Nerdstore
Este repositório foi criado com o intuito de testar o [`Scrapy`](https://scrapy.org/), um framework Python de Scraping e Web Crawling.  
O programa irá acessar o site [nerdstore](https://nerdstore.com.br/), entrar em cada categoria e acessar a página de cada produto anúnciado.  
Dentro da página do produto, irá coletar o nome, preço, descrição, especificações e a url da página e armazenar em banco de dados [`SQLite3`](https://sqlite.org/index.html).

## Pré-requisitos
Para você rodar o software é necessário tem instalado em sua máquina o `Python3.6.+` e o `Scrapy`.  
## Começando
Clone o projeto em sua máquina com o seguinte comando:
```
git clone https://github.com/igor-taconi/web-crawling-nerdstore.git
```
## Virtualenv
Recomendo não instalar nada em sua máquina e criar uma virtualenv para não quebrar algum possível projeto. Mas, fique a fontade.
### Criando o virtualenv com Python3
Entre no diretório clonado e execute o comando.
```
python -m venv .venv
```
### Ativando o virtualenv
```
source .venv/bin/activate
```
## Para instalar o `Scrapy`
Com o virtualenv já criado e ativado (ou não), basta instalar o Scrapy.
 ```
pip install Scrapy==2.4.1
```
## Executar
Para rodar o projeto
```
cd nerd_store 
scrapy crawl nerdstore
```
Após o script terminar sua execução aparecerá um arquivo nerdstore_products.db.  
Você pode entrar no site [SQL Online IDE](https://sqliteonline.com/) para visualizar o arquivo, baixar o [DB Browser for SQLite](https://sqlitebrowser.org/dl/) em sua máquina ou usar os dados da forma que melhor lhe convir.
## Contribuindo
Sinta-se à vontade para enviar pull requests.
