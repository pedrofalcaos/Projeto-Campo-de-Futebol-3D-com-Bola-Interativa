Documentação do Projeto: Campo de Futebol 3D com Bola Interativa
Descrição
Este projeto cria um campo de futebol em 3D usando Python, onde uma bola pode ser movida pelo usuário. Quando a bola ultrapassa a linha do gol entre as três traves, é marcado um gol, e a bola retorna automaticamente ao centro do campo. Se a bola sair das quatro linhas do campo em qualquer outra direção, será considerada "fora". As mensagens de "Gol no Sport" e "Bola fora" são exibidas no terminal. O projeto também inclui uma função que exibe um pop-up ao fechar a aplicação, perguntando se o "Sport perdeu".

Tecnologias Utilizadas
Python 3
Bibliotecas:
numpy: para manipulação de matrizes e cálculo de posições.
matplotlib: para visualização gráfica em 3D do campo e da bola.
tkinter: para exibir mensagens de confirmação na saída do programa.
Estrutura do Código
Classe CampoFutebol3D: Gerencia o campo de futebol 3D, incluindo a configuração do campo, a detecção de gol ou bola fora, e o movimento da bola.
Métodos principais:
__init__: Inicializa o campo, a bola e o gol com suas posições.
mover_bola: Controla o movimento da bola e verifica se foi gol ou fora.
mostrar_grafico: Cria e exibe o gráfico em 3D.
atualizar_grafico: Atualiza a posição da bola no gráfico.
on_key_press: Recebe as teclas pressionadas pelo usuário para mover a bola.
on_close: Exibe um pop-up ao fechar o programa, solicitando confirmação.
