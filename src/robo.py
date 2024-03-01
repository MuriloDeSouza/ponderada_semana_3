# robo.py

# Traz a ferramenta serial para apresentar quais portas estão disponíveis
from serial.tools import list_ports
import inquirer
import pydobot
from yaspin import yaspin
import typer
import time

#Instância de aplicação
app = typer.Typer()

# Traz o spinner para apresentar uma animação enquanto o robô está se movendo
spinner = yaspin(text="Processando...", color="white")

# Listas as portas seriais disponíveis
available_ports = list_ports.comports()

# Pede para o usuário escolher uma das portas disponíveis
porta_escolhida = inquirer.prompt([
    inquirer.List("porta", message="Escolha a porta serial", choices=[x.device for x in available_ports])
])["porta"]

# Cria uma instância do robô
robo = pydobot.Dobot(port=porta_escolhida, verbose=False)

@app.command()
def movimentos():
    # realiza lista de perguntas para o usuário
    perguntas = [
        inquirer.List("movimento", message="Qual movimento você deseja que o robô faça?", choices=["Home", "Ligar_Ferramenta","Desligar_Ferramenta","Posição_Atual","Vá_até: ", "Sair", "Mover em X:", "Sair", "Mover em Y:", "Sair", "Mover em Z:"])
    ]
    continuar = True
    while continuar:
        # realiza a leitura das respostas
        respostas = inquirer.prompt(perguntas)
        # chama a funcao que processa a operação e exibe uma spinner para o usuário
        spinner = yaspin(text="Processando...", color="yellow")
        # realiza a operação
        saida = processar(respostas)
        # exibe o resultado
        print(saida)
    continuar = typer.confirm("Deseja continuar?")

# Função que processa a operação
def processar(dados):
    operacao = dados["movimento"]

    if operacao == "Home":
        robo.speed(100, 100)
        spinner.start()
        robo.move_to(238, -11, 150, 0, wait=True)
        posicao_atual = robo.pose()
        print(f"Posição atual: {posicao_atual}")
        spinner.stop()

    elif operacao == "Ligar_Ferramenta":
        spinner.start()
        robo.suck(True)
        spinner.stop()

    
    elif operacao == "Desligar_Ferramenta":
        spinner.start()
        robo.suck(False)
        spinner.stop()

    elif operacao == "Posição_Atual":
        posicao_atual = robo.pose()
        print(f"Posição atual: {posicao_atual}")
        spinner.stop()


    elif operacao == "Vá_até: ":
        x = typer.prompt("Digite o valor de X", type=float)
        y = typer.prompt("Digite o valor de Y", type=float)
        z = typer.prompt("Digite o valor de Z", type=float)

        spinner.start()
        robo.move_to(x, y, z, 0, wait=True)
        posicao_atual = robo.pose()
        spinner.stop()
    
    elif operacao == "Mover em X:":
        x = typer.prompt("Digite o valor de X", type=float)
        spinner.start()
        robo.move_to(x, 0, 0, 0, wait=True)
        posicao_atual = robo.pose()
        spinner.stop()
    
    elif operacao == "Mover em Y:":
        x = typer.prompt("Digite o valor de Y", type=float)
        spinner.start()
        robo.move_to(0, y, 0, 0, wait=True)
        posicao_atual = robo.pose()
        spinner.stop()
    
    elif operacao == "Mover em Z:":
        x = typer.prompt("Digite o valor de Z", type=float)
        spinner.start()
        robo.move_to(0, 0, z, 0, wait=True)
        posicao_atual = robo.pose()
        spinner.stop()

    elif operacao == "Sair":
        continuar = False
        quit()

        
#Ele executa a aplicação    
if __name__ == "__main__":
    app()

robo.close()
quit()
