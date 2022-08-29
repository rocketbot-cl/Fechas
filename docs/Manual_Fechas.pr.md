# Data
  
Módulo para gerenciar datas  

*Read this in other languages: [English](Manual_Fechas.md), [Portugues](Manual_Fechas.pr.md), [Español](Manual_Fechas.es.md).*
  
![banner](imgs/Banner_fechas.png)
## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  



## Descrição do comando

### Formato de data
  
Alterar o formato de uma data
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Data |Data para a qual o formato será alterado|19/10/2000|
|Resultado |Variável onde o resultado será armazenado|data|
|Formato de entrada|Formato que tem a data inserida|dd/mm/yyyy|
|Formato de saída |Formato que terá a data de recebimento|dd/mm/yyyy|
|Entrada personalizada |Se o formato da data for diferente das opções acima, deve ser informado neste campo.|%d/%m/%y|
|Saída personalizada |Caso o formato da data a ser recebida seja diferente das opções anteriores, deve ser informado neste campo.|%d/%m/%y|

### Obter dia da semana
  
Obtém o dia da semana da data inserida
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Data |Campo para ingresso na data.|19/10/2000|
|Formato de entrada|Formato que tem a data inserida.|dd/mm/yyyy|
|Resultado |Variável onde o resultado será salvo.|data|

### Adicionar e subtrair entre datas
  
Adicionar e subtrair entre datas
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Data |Data a ser usada no cálculo|19/10/2000|
|Formato de entrada|Formato que tem a data inserida.|dd/mm/yyyy|
|Resultado |Variável onde o resultado será armazenado|data|
|Valor a ser subtraído ou adicionado|Número que será subtraído ou adicionado da data inserida.|3|
|Tipo de data|Tipo de data que você deseja subtrair ou adicionar|days|

### Obter número da semana
  
Obter número da semana
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Data |Data a partir da qual você deseja obter o número da semana|19/10/2000|
|Formato de entrada|Formato que tem a data inserida.|dd/mm/yyyy|
|Resultado |Variável onde o resultado será armazenado|data|

### Comparação de datas
  
Comparação de datas
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Data 1 |Data 1 para comparar|19/10/2000|
|Operação|Operação a ser realizada entre as datas inseridas.|<|
|Data 2 |Data 2 para comparar|19/10/2000|
|Resultado |Variável onde o resultado será armazenado|resultado|
|Formato de entrada|Formato que tem a data inserida|dd/mm/yyyy|
|Entrada personalizada|Preencha caso queira usar outro formato de data.|%d/%m/%y|
