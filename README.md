# Web Crawler Nerdstore
Este repositório foi criado com o intuito de testar o [`Scrapy`](https://scrapy.org/), um framework Python de Scraping e Web Crawling.  
O programa irá acessar o site [nerdstore](https://nerdstore.com.br/), entrar em cada categoria e acessar a página de cada produto anúnciado.  
Dentro da página do produto, irá coletar o nome, preço, descrição, especificações e a url da página e armazenar em banco de dados [`SQLite3`](https://sqlite.org/index.html).
## Começando
Clone o projeto em sua máquina com o seguinte comando:
```
git clone https://github.com/igor-taconi/web-crawling-nerdstore.git
```
## Pré-requisitos
Para você rodar o software é necessário tem instalado em sua máquina o `Python3.x.` e o `scrapy`.  
### Para instalar o `scrapy`
 ```
pip install scrapy
```
## Executar
Para rodar o projeto
```
cd nerd_store 
scrapy crawl nerdstore
```
Após o script terminar sua execução aparecerá um arquivo nerdstore_products.db.  
Você pode entrar no site [SQL Online IDE](https://sqliteonline.com/) para visualizar o arquivo ou baixar o [DB Browser for SQLite](https://sqlitebrowser.org/dl/) em sua máquina
## Contribuindo
Sinta-se à vontade para enviar pull requests.
