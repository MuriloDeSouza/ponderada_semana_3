# Ponderada_Sem_3_Murilo_Prianti (robo.ts)

Este é um script em TypeScript que interage com um robô controlado por meio de uma porta serial. O robô pode ser manipulado para realizar diferentes movimentos e ações, proporcionando uma interface de usuário interativa.

## Pré-requisitos
Certifique-se de que você atende aos seguintes requisitos antes de executar o script:
- Node.js instalado no seu sistema.
- Módulos necessários instalados. Você pode instalá-los executando `npm install inquirer typer yaspin`.

## Uso
Para usar o script, siga as etapas abaixo:

1. Execute o script `robo.ts` no seu terminal usando o TypeScript Compiler (`tsc`) ou usando Node.js diretamente se estiver usando um ambiente Node.js.
2. Escolha a porta serial à qual o robô está conectado.
3. Selecione a operação desejada a partir do menu interativo.

## Operações Disponíveis
- **Home:** Move o robô para a posição inicial.
- **Ligar Ferramenta:** Liga a ferramenta do robô.
- **Desligar Ferramenta:** Desliga a ferramenta do robô.
- **Posição Atual:** Exibe a posição atual do robô.
- **Vá até (x, y, z, r):** Move o robô para uma posição específica (X, Y, Z, R).
- **Qual eixo você quer mexer?:** Move o robô ao longo de um eixo específico (X, Y, Z, R).
- **Sair:** Encerra a execução do script.

**Observação:** Certifique-se de confirmar se deseja continuar após cada operação.

## Contribuição
Sinta-se à vontade para contribuir para este projeto através de sugestões, relatórios de problemas ou envio de solicitações pull.

## Autor
Este script foi desenvolvido por Murilo de Souza Prianti Silva.
