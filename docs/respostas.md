# Respostas Escritas

## Questão 1

### 1.1. Cada vez que tentássemos criar um objeto da classe e o ```__new__``` fosse chamado, logo em seguida, o ```__init__``` também seria chamado. Então, mesmo que na prática não foi criado um novo objeto, ele pode inicializá-lo novamente.

### 1.2. O Python só executa um arquivo importado na primeira vez. Nas importações seguintes, ele reaproveita o que já está na memória. Logo, variáveis globais em um arquivo ```.py``` funcionam como um Singleton nativo.

### 1.3. Qualquer parte do código pode alterar os dados de forma invisível. Isso causa bugs difíceis de rastrear e faz com que os testes interfiram uns nos outros.

## Questão 2

### 2.1. A classe OrderBuilder atua como o Builder e a classe Order é o objeto final construído.

### 2.2. O construtor direto funciona no Python por causa dos parâmetros nomeados e opcionais. A vantagem do Builder é permitir a construção em etapas, enquanto o construtor exige todos os dados de uma vez só na hora de instanciar.

## Questão 3

### 3.1. 

### 3.2. 

### 3.3. 

## Questão 4

### 4.1.

### 4.2. 

### 4.3. 

## Questão 5

### 5.1.

### 5.2. 

## Questão 6

### 6.1.

### 6.2. 

### 6.3. 

## Questão 7

### 7.1.

### 7.2. 

### 7.3. 

## Questão 8

### 8.1.

### 8.2. 

### 8.3. 

### 8.4. 

### 8.5. 