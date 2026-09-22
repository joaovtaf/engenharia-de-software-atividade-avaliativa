# Respostas Escritas

## Questão 1

### 1.1. Cada vez que tentássemos criar um objeto da classe e o ```__new__``` fosse chamado, logo em seguida, o ```__init__``` também seria chamado. Então, mesmo que na prática não foi criado um novo objeto, ele pode inicializá-lo novamente.

### 1.2. O Python só executa um arquivo importado na primeira vez. Nas importações seguintes, ele reaproveita o que já está na memória. Logo, variáveis globais em um arquivo ```.py``` funcionam como um Singleton nativo.

### 1.3. Qualquer parte do código pode alterar os dados de forma invisível. Isso causa bugs difíceis de rastrear e faz com que os testes interfiram uns nos outros.

## Questão 2

### 2.1. A classe OrderBuilder atua como o Builder e a classe Order é o objeto final construído.

### 2.2. O construtor direto funciona no Python por causa dos parâmetros nomeados e opcionais. A vantagem do Builder é permitir a construção em etapas, enquanto o construtor exige todos os dados de uma vez só na hora de instanciar.

## Questão 3

### 3.1. O Creator é o PaymentProcessor, que define o fluxo process_order sem saber qual pagamento vai usar. Cada processor concreto (PixProcessor, CreditCardProcessor, BoletoProcessor) é o Concrete Creator, porque implementa o create_payment() decidindo qual classe instanciar. O Product é a classe abstrata Payment, com o método pay, e o Concrete Product é cada implementação dela: PixPayment, CreditCardPayment e BoletoPayment.

### 3.2. Um if/elif escolhendo a classe concreta deixa essa decisão espalhada em qualquer lugar do código que precisa criar um pagamento, e toda forma nova exige mexer nesse trecho. O Factory Method separa essa escolha, colocando ela dentro de um método que cada subclasse do Creator implementa por conta própria. Assim quem usa o processor, no caso o process_order, nunca fica sabendo qual pagamento concreto foi criado.

### 3.3. Só precisa criar a nova classe de Payment com o método pay e a classe de Processor correspondente com o create_payment dela. O PaymentProcessor e o process_order continuam iguais, porque eles não conhecem as classes concretas de pagamento.

## Questão 4

### 4.1. Checkout e Notification formam uma família porque cada canal precisa de uma versão compatível dos dois. O checkout do canal Web mostra o pedido de um jeito e a notificação do canal Web avisa o cliente de um jeito parecido, então dá pra pensar nos dois como uma dupla que pertence ao mesmo canal. Misturar o checkout de um canal com a notificação de outro não faz sentido dentro da loja.

### 4.2. A Abstract Factory resolve o problema de garantir que checkout e notificação combinam entre si sem quem usa a fábrica precisar saber qual canal está ativo. O código que processa o pedido só chama create_checkout() e create_notification() da fábrica que recebeu, então não corre o risco de montar um checkout de um canal com a notificação de outro, porque isso fica garantido dentro da própria fábrica.

### 4.3. Porque canal e forma de pagamento variam de forma independente, o próprio enunciado já deixa isso claro dizendo que WEB pode usar PIX e MOBILE pode usar cartão. Se o pagamento estivesse dentro da ChannelFactory, cada combinação de canal com forma de pagamento ia precisar da própria fábrica, tipo uma WebPixFactory e uma WebCartaoFactory, e isso cresce rápido demais. Deixando o pagamento de fora, a fábrica do canal cuida só do que realmente é responsabilidade dela.

## Questão 5

### 5.1. Pra adicionar o KIOSK criei só um arquivo novo, src/kiosk.py, com KioskCheckout, KioskNotification e KioskFactory, e no final desse arquivo chamei o registro dessa fábrica no dicionário que o get_channel_factory usa. Não precisei alterar src/channel.py nem nenhum trecho que já usava Checkout ou Notification.

### 5.2. É compatível com o OCP porque a extensão inteira aconteceu adicionando um arquivo, sem tocar em código já existente e testado. O get_channel_factory e o resto do sistema continuam trabalhando só com as abstrações ChannelFactory, Checkout e Notification, então nem precisam saber que o KIOSK existe, só enxergam mais uma fábrica registrada.

## Questão 6

### 6.1. O AppConfig guarda a configuração compartilhada da aplicação. O OrderBuilder monta o pedido aos poucos e o Order guarda os dados dele e calcula o total. Quem decide qual pagamento usar e executa ele é o PaymentProcessor com as subclasses de pagamento. Já o ChannelFactory e as subclasses de canal (Web, Mobile, Kiosk) criam o checkout e a notificação certos pra cada canal, sendo que o Checkout mostra o resumo do pedido pro cliente e o Notification avisa que o pedido foi processado. O EventLogger fica só com o registro de que o pedido passou pelo fluxo, e o OrderService fica no meio de tudo isso coordenando a ordem das chamadas, sem fazer o trabalho de nenhum desses colaboradores sozinho.

### 6.2. Trocar como a notificação é enviada, tipo email por SMS, fica restrito à classe de Notification do canal. A regra de cálculo do total, por exemplo aplicar desconto de cupom, é uma mudança que só deveria mexer no método total() de Order. E se o log precisar ir pra um arquivo em vez de aparecer só no console, isso é problema exclusivo do EventLogger, o resto do sistema nem percebe a troca.

### 6.3. Uma decisão que dava pra ser diferente é registrar os canais usando string (WEB, MOBILE, KIOSK) em vez de um Enum do Python. Com Enum, um erro de digitação no nome do canal apareceria na hora de rodar o código, em vez de só quando o get_channel_factory não encontrasse a fábrica. Mas usando string fica mais fácil registrar um canal novo vindo de fora do código, tipo de um arquivo de configuração, sem precisar editar uma classe de Enum toda vez.

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