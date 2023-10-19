# **DataGrid**

Este é um módulo que implementa a lógica de negócios de um DataGrid utilizando algoritmos aprendidos na disciplina Projeto e Análise de Algoritmos (FGV EMAp). O trabalho foi avaliado com nota 9.

## **Manual de Instruções**

A classe DataGrid foi pensada especificamente para ser utilizada em conjuntos de dados que sigam o seguinte padrão:

Coluna | Tipo do dado | Tipo de busca | Extra 
--- | --- | --- | ---
id | integer | exato | único
owner_id | string | exato | Exatamente 5 caracteres alfanuméricos
creation_date | string | intervalo | Formato: AAAA-MM-DD hh:mm:ss
count | integer | intervalo |
name | string | contém | Tamanho máximo de 20 caracteres
content | string | contém | 

Cada registro no DataGrid é considerado um $\texttt{Event}$.

Para inicializar a classe DataGrid, basta importar o módulo e instanciar a classe. Certifique-se de que seu script consegue acessar a pasta na qual se encontra o módulo DataGrid, por exemplo:

```python
import sys
sys.path.append('src/')

from datagrid import DataGrid
```

Inicialize a classe DataGrid com:

```python
datagrid = DataGrid()
```

A classe DataGrid possui os seguintes métodos:

- `read_csv(file, sep = ',', encoding = 'utf-8')`: popula o datagrid a partir dos dados no arquivo CSV cujo caminho é passado como
parâmetro, considerando o separador e o encoding definidos;

- `show(start=0, end=100, prints = False, returns = True)`: exibe as entradas do DataGrid, limitando a exibição ao intervalo definido pelos parâmetros. $\texttt{returns=True}$ retorna a lista de objetos da classe $\texttt{Event}$ entre $\texttt{start}$ e $\texttt{end}$, e o $\texttt{prints=True}$ faz o display do conteúdo desses objetos. Apresenta a tabela no seu estado atual de ordenação. 

- `insert_row(row)`: insere novos eventos no DataGrid. Recebe um dicionário contendo os dados do evento a ser inserido e cria uma instância de $\texttt{Event}$ a partir desses dados. O dicionário deve ter como chaves os nomes das colunas e como valores os dados a serem inseridos, conforme o padrão descrito na tabela acima.

- `delete_row(column, value)`: remove eventos do DataGrid. Recebe o nome da coluna e o valor a ser buscado nessa coluna. Remove todos os eventos que possuem o valor buscado na coluna especificada. Se `column = 'positions'`, remove elementos de acordo com a posição (índice) na tabela. Nesse caso, `value` pode ser tanto um intervalo identificado por uma tupla `(start, end)` ou um único valor inteiro positivo.

- `search(column, value)`: busca eventos no DataGrid. Recebe o nome da coluna e o valor a ser buscado nessa coluna. Retorna uma lista de objetos da classe $\texttt{Event}$ que possuem o valor buscado na coluna especificada.

- `sort(column, direction = 'asc')`: ordena o DataGrid. Recebe o nome da coluna e a direção da ordenação. Para ordenar em ordem decrescente, basta passar `direction = 'desc'`. 

- `select_count(i, j, how = 'median-of-medians')`: retorna a lista de objetos da classe $\texttt{Event}$ entre as posições $i$ e $j$ da tabela considerando a coluna `count` ordenada de forma crescente. A operação não altera a estrutura interna do DataGrid. Também é possível passar o parâmetro `how = 'quickselect'` ou `how = 'heapsort'` para escolher qual algoritmo será utilizado para realizar a operação.

O arquivo [`demo.ipynb`](demo.ipynb) contém um exemplo de uso da classe DataGrid utilizando dados gerados aleatoriamente pelo arquivo [`dataGenerator.py`](dataGenerator.py). Os comentários sobre as operações realizadas no notebook dizem respeito aos resultados utilizando o arquivo [`fake_data_100.csv`](data/fake_data100.csv), com 100 linhas.

## **Geração de dados aleatórios**

Caso deseje gerar dados aleatórios para testar o módulo DataGrid, basta executar o arquivo [`dataGenerator.py`](dataGenerator.py). Lembre-se de alterar o(s) valor(es) da lista `n`, ao final do arquivo, para definir quantos arquivos deseja gerar e quantas linhas cada um deles deve conter.
