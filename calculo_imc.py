from colorama import Fore, Style, init

init(autoreset=True)

#definições de cores
amarelo = Fore.YELLOW
verde = Fore.GREEN
azul = Fore.BLUE
vermelho = Fore.RED
ciano = Fore.CYAN
resetar = Style.RESET_ALL

def calculo_peso():
	while True:
		try:
			peso = float(input(f'{azul}Digite o seu peso (kg): {resetar}'))
			altura = float(input(f'{azul}Digite a sua altura (m): {resetar}'))
			imc = peso / (altura ** 2)
			print(f'{ciano}O IMC dessa pessoa é {imc:.2f}')
			if imc < 18.5:
				print(f'{amarelo}Você está ABAIXO DO PESO!!{resetar}')
			elif 18.5 <= imc < 25:
				print(f'{verde}Você esta no PESO IDEAL!!{resetar}')
			elif 25 <= imc < 30:
				print(f'{amarelo}Você está SOBREPESO!!{resetar}')
			elif 30 <= imc < 40:
				print(f'{amarelo}Você está em OBESIDADE!!{resetar}')
			elif imc >= 40:
				print(f'{vermelho}Você está em OBESIDADE MÓRBIDA! CUIDADO!!{resetar}')
		except ValueError:
			print(f'{vermelho}ERRO!! digite novamente: {resetar}')
calculo_peso()
