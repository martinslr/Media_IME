import PySimpleGUI as sg


class NotasIME:

    def __init__(self, ve1=0, ve2=0, vc=0, vf=0):
        self.ve1 = ve1
        self.ve2 = ve2
        self.vc = vc
        self.vf = vf

    def media_final(self):
        return float(self.ve1)*(0.125) + float(self.ve2)*(0.125) + float(self.vc)*(0.25) + float(self.vf)*(0.5)

    def quanto_precisa_vf(self):
        return 10 - (float(self.ve1)+float(self.ve2)+2*float(self.vc))/4


layout = [
    [sg.Text("---------------------------- Bem vindo a plataforma de médias! ------------------------------")],
    [sg.Text("=> Entre com os valores de suas notas, se não houver, entre com o valor 0.")],
    [sg.Text('')],
    [sg.Text('Nota da VE1:'), sg.InputText(key='nota_ve1')],
    [sg.Text('Nota da VE2:'), sg.InputText(key='nota_ve2')],
    [sg.Text('Nota da VC:  '), sg.InputText(key='nota_vc')],
    [sg.Text('Nota da VF:  '), sg.InputText(key='nota_vf')],
    [sg.Text('')],
    [sg.Text(' ', key='saida_final')],
    [sg.Button("Calcular Minha Média"), sg.Button("Quanto Preciso na VF")]
]

janela = sg.Window("Plataforma de Médias - IME XXVI", layout)

while True:

    evento, valores = janela.read()

    if evento == sg.WIN_CLOSED:
        break

    if evento == 'Calcular Minha Média':
        ve1 = float(valores['nota_ve1'])
        ve2 = float(valores['nota_ve2'])
        vc = float(valores['nota_vc'])
        vf = float(valores['nota_vf'])
        sem1 = NotasIME(ve1, ve2, vc, vf)
        jan_saida = janela['saida_final']
        jan_saida.update(f"Sua média é {sem1.media_final()}.")

    if evento == "Quanto Preciso na VF":
        ve1 = float(valores['nota_ve1'])
        ve2 = float(valores['nota_ve2'])
        vc = float(valores['nota_vc'])
        sem1 = NotasIME(ve1, ve2, vc, 0)
        jan_saida = janela['saida_final']
        jan_saida.update(
            f'Voce precisa de {sem1.quanto_precisa_vf()} para passar direto!')

janela.close()
