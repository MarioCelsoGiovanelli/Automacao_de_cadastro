![Badge Concluido](http://img.shields.io/static/v1?label=STATUS&message=%20CONCLUIDO&color=GREEN&style=for-the-badge)

# :robot: Automação de cadastros

Com essa automação, vamos usar uma base de dados de clientes em um arquivo excel, para pegar as informações e cadastrar em um sistema.

Nessa automação foi usado o navegador Google Chrome, será usado um executável de acordo com o navegador.


:film_projector:

<img src=".\Animação03.gif" alt="Código funcionando" width="600px" heidth="400px">



É necessário fazer o download do executável no site **[ChromeDriver](https://chromedriver.chromium.org/home)**, deve ser usado a mesma versão do google chrome que estiver usando.

Para verificar qual versão do google chrome esta instalado: vá em **ajuda** na aba do google (fica onde tem 3 pontos) em seguida; sobre o Google Chrome. Vai abrir uma aba mostrando a versão; ex: Versão 124.0.6367.79 (Compilação oficial) (64 bits)
O importante são os 3 primeiros dígitos. Ex: 124.


:movie_camera:

<img src=".\Animação01.gif" alt="Código funcionando" width="600px" heidth="400px">



Clique em **the Chrome for Testing availability dashboard**, clique em **Stable**, escolha a versão ex: chrome | win64 | [link do arquivo](https://storage.googleapis.com/chrome-for-testing-public/124.0.6367.91/win64/chrome-win64.zip).

Escolha o caminha do Download para a pasta onde está o executável Python, se estiver usando o Anacondo, deve ser dentro da pasta Anaconda, Scripts. Se estiver usando um ambiente virtual, o arquivo deve ser extraído dentro da pasta **venv**, **Scripts** e extrair sem criar uma pasta ex: Downloads\python\projeto\venv\Scripts. Com isso facilita na hora de usar o WebDriver para não ter que ficar especificando o caminho da pasta em que ele está.

### Entendendo como funciona o Selenium:

Com o método **webdrive.Chrome()** abrimos o browser e já verificamos se o WebDriver está funcionando corretamente. Atribuímos o método a uma variável  

````python
browser = webdrive.Chrome()
````

Para que o browser seja aberto e maximizado usamos o método **maximize_window()**.

````python
browser.maximize_window()
````

Para abrir uma página de internet usamos o método **get()** e como parâmetro a url do site.

````python
browser.get(‘https://fonts.google.com/’)
````

Com a automação abrindo a pagina usamos o botão direito do mouse, opção **inspecionar** ou botão **F12**. 
Para usar a ferramenta **DevTools**. 
Usamos o seletor de elementos ou **Ctrl + Shift + C** para identificar o campo que precisamos adicionar uma informação. 
Clique com o botão direito do mouse na opção que apareceu selecionada na aba DevTools e selecione **Copy**, **Copy XPath**

:film_strip:

<img src=".\Animação02.gif" alt="Código 2 funcionando" width="600px" heidth="400px">


Utilizaremos o **XPath** passando para o **By** da seguinte forma; **By.XPATH, ‘//*[@id="input"]’**.

Criando uma variável e usando o método **find_element()** e passando o By como parâmetro.

````python
busca = browser.find_element(By.XPATH, ‘//*[@id="input"]’)
````

Com esse comando aparentemente a automação não vai fazer nada, ela só vai achar o caminho do campo no qual vamos adicionar uma informação.

Com o método **send_keys** passamos a informação para preencher o campo que a automação identificou.

````python
busca.send_keys(‘google fonts’)
````

Para a automação clicar em um botão usamos o método **click()**. Primeiro atribuímos o XPath do botão a uma variável.

````python
botao = browser.find_element(By.XPATH, ‘//*[@id="input"]’)
````
````python
botao.click()
````

Para usar o **read_excel()** do pandas, uma dependência é o **openpyxl**, ambos já vem instalado no anaconda.

Criamos uma variável para receber o arquivo excel e passamos o nome do arquivo como parâmetro para o método **read_excel()**

````python
dataframe = pandas.read_excel(‘cadastro_clientes.xlsx’)
````

Visualizar as informações do arquivo **head()**.

````python
dataframe.head()
````


|             | Nome          | E-mail  | Telefone  | 
| ------------- |:-------------:| -----:| -----:|
| 0      | Joana Cardoso      |   joana.cardoso@exemplo.com.br |    (11) 9218-5801|
| 1 | Bryan Duarte  |    bryan.duarte@exemplo.com.br | (21) 3547-3474  |
|2| Fernanda Nogueira |fernanda.nogueira@exemplo.com.br | (31) 1090-7993  |
| 3|	Juan Azevedo |	juan.azevedo@exemplo.com.br | (51) 3456-3454  |
|4	| Lucca Duarte	| lucca.duarte@exemplo.com.br | (41) 3452-3039  |



## Arquivo Requirements:

É um arquivo de texto formato **.txt** neste arquivo está especificado todos os pacotes e bibliotecas que são utilizados no projeto, isso ajuda para que garanta que se o projeto for usado por outro desenvolvedor não aconteça erros ou problemas por causa da alguma atualização na versão do pacote ou uma descontinuidade na linguagem Python.

Para instalar entre no terminal, **Ctrl + ‘** no terminal basta instalar o requirements para usar todos os pacotes na mesma versão usada no projeto. 

````python
pip install -r requirements.txt
````


## 📁 Como utilizar o código:

O arquivo **script.py** pode ser usado em um terminal:

````python
python script.py
````

## :computer: Técnicas e Tecnologias utilizadas:

- Processos com tarefas repetitivas

- Navegação em sistemas web
  
- Alimentação de sistemas

- Gerar gráfico

- Automatizar o controle do teclado e mouse

- Laço de repetição
  
- Estrutura condicional **if** - **elif**


	- **Python**
   
	- **Jupyter Notebook**


## :books: Bibliotecas:

- **Pandas**
  - pip install pandas
- **openpyxl**
  - pip install openpyxl
- **selenium**
  - pip install selenium

## :electric_plug: como usar as bibliotecas e seus modos:

- from selenium
- import webdriver
- from selenium.webdriver.common.keys
- import Keys
- from selenium.webdriver.common.by
- import By
- import pandas as pd

