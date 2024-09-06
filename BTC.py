try:
    from win10toast import ToastNotifier
    import matplotlib.pyplot as plt
    import requests
    import datetime
    import time
    import os

    #Version V1.0
    print('BTC Cotação V1.0')

    #Verificação
    print('Verificando', end='')
    pastas = ['Config', 'Cache', 'Dados']
    pastas_nao = []
    for c in range(0, 3):
        try:
            pas = open(f'{pastas[c]}.txt', 'r')
        except FileNotFoundError as erro:
            erro = str(erro)
            #print(f'{erro[37:]} Nao Encontrado!!')
            print('.', end='')
            o = open(f'{pastas[c]}.txt', 'a')
            o.close()
            time.sleep(5)
            pass
    print(f'{'OK':>10}')
    #temino
    #Codigo
    try:
        pri = open('Config.txt', 'r')
        lin1 = pri.readline(10)
        lin2 = pri.readline(10)
        lin3 = pri.readline(10)
        lin4 = pri.readline(10)

        if 'BTC-BRl' in lin1:
            pri.close()
            pass

        if 'BTC-BRL' not in lin1:
            print(f'\n{"Opções":^30}\n{"BTC-BRL [1] Suport/Relatar Erro [2] Sair [3]":^30}\n{"-" * 30}')
            user = int(input('Qual Moeda Acompanhar? '))

            pri = open('config.txt', 'a')

            if user == 1:
                pri.write('BTC-BRL')
                pri.write('\n')
                pri.write('BTCBRL')

                '''toaster = ToastNotifier()
                toaster.show_toast(
                    f'Dados Alterados',
                    f'Reinicie o Codigo\nCodigo Encerrado!!',
                    threaded=True,
                    icon_path=None,
                    duration=300
                )'''
                time.sleep(2)
                pri.close()

                toaster = ToastNotifier()
                toaster.show_toast(
                    f'Importante!',
                    f'Para Desativar, Vá para Config.txt!!',
                    threaded=True,
                    icon_path=None,
                   duration=600
                )
                pri.write('Para Desativar Troque True por False no arquivo de texto config.txt')

            elif user == 2:
                site = 'https://docs.google.com/forms/d/e/1FAIpQLSfr7_JZzv9PGKSNoRxXKYXQYiZvqyrtpU_DcnRpkWacrcwbkA/viewform'
                print(f'Suport {site}')
                pri.close()
                exit()

            elif user == 3:
                pri.close()
                exit()
            pri.close()
    #2_Verificação
    except FileNotFoundError as erro:
        for c in range(0, 3):
            try:
                pas = open(f'{pastas[c]}.txt', 'r')
            except FileNotFoundError as erro:
                erro = str(erro)
                print(f'{erro[37:]} Nao Encontrado!!')
                o = open(f'{pastas[c]}.txt', 'a')
                o.close()
                time.sleep(10)
                pass
    #Fim
    #Requisição/Entrada De Dados
    while True:
        fecha = datetime.datetime.now()
        fecha2 = fecha.strftime('%H')
        if lin2 == 'BTCBRL':
            link = requests.get(f'https://economia.awesomeapi.com.br/last/BTC-BRL')
            requisição = link.json()
            btc = requisição[lin2]['name']
            alta = requisição[lin2]['high']
            baixa = requisição[lin2]['low']
            data = requisição[lin2]['create_date']
        #Fim Entrada De Dados

        dia = fecha.strftime('%A')
        #print(requisição)
        #print(dolar, dolar2)
        #Reset Lista

        arquivo1 = open('Cache.txt', 'r+')
        texto = arquivo1.read()
        if len(texto) > 40000:
            texto = arquivo1.truncate(0)
            arquivo1.close()
            #Fim Reset Lista

        #Notificação Padrão
        #if int(fecha2) >= 10 and int(fecha2) < 18:
        arquivo3 = open('Cache.txt', 'a')
        data2 = datetime.datetime.now()
        data2 = data2.strftime('%d/%m/%y %H:%M')
        arquivo3.write(data2)
        arquivo3.write('\n')
        arquivo3.write(f'{str(btc)} Alta R${alta:.4} Baixa R${baixa:.4}')
        arquivo3.write('\n')
        arquivo3.close()

        toaster = ToastNotifier()
        toaster.show_toast(
            btc,
            f'📈 Alta R${alta:.3} 📉 Baixa R${baixa:.3} 💱',
            threaded=True,
            icon_path=None,
            duration=400
        )
        #Fim Notificação Padrão
        time.sleep(1800)
        if int(fecha2) >= 18 or int(fecha2) < 10:
            data3 = datetime.datetime.now()
            data3 = data3.strftime('%d/%m/%y %H:%M')
            if int(fecha2) >= 18:
                #Dados do Grafico

                arquivo4 = open('Dados.txt', 'r+')
                texto2 = arquivo4.read()
                texto2 = texto2.split()

                num2 = 0
                for num, dado in enumerate(texto2):
                    if num % 2 == 0:
                        if f'{data3:.2}' == dado:
                            num2 = num2 + 1
                            # print(dado, num2)
                        else:
                            pass
                    elif num % 2 == 1:
                        pass
                if num2 == 1:
                    pass
                elif num2 == 0:
                    #print(f'{alta:.4}')
                    arquivo5 = open('Dados.txt', 'a')
                    arquivo5.write(f'{data3:.2} {alta:.4}')
                    arquivo5.write('\n')
                    arquivo5.write('\n')
                    arquivo5.close()

                #Fim Dados

                #Grafico
                arquivo7 = open('Dados.txt', 'r+')
                texto3 = arquivo7.read()
                texto3 = texto3.split()

                grafi = datetime.datetime.now()
                day = grafi.strftime('%d %m %y')

                if len(texto3) >= 10:
                    info = open('config.txt', 'r')
                    info_text1 = info.readline()
                    info_texto2 = info.readline()
                    info_texto2 = str(info_texto2)

                    print(f'{versão}   Teste')
                    dias = []
                    cotação = []
                    for e, dados in enumerate(texto3):
                        if e % 2 == 0:
                            dias.append(dados)
                        elif e % 2 == 1:
                            cotação.append(float(dados))

                    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
                    ax.plot(dias, cotação, label='linear')
                    ax.set_xlabel('Dias')
                    ax.set_ylabel(info_texto2)
                    ax.set_title(f"Cotação {info_texto2}")
                    plt.savefig(f'Grafico Dia {day}.pdf')
                    #plt.show()

                    toaster = ToastNotifier()
                    toaster.show_toast(
                        btc,
                        f'Grafico Gerado!!',
                        f'Grafico Dia {day}.pdf',
                        threaded=True,
                        #icon_path=None,
                        duration=300
                    )
                    info.close()
                    arquivo8 = open('Dados.txt', 'r+')
                    texto4 = arquivo8.read()
                    arquivo8.truncate(0)
                    arquivo8.close()
                    print('Um Grafico Foi Gerado!!')
                    #Fim Grafico

            #Fechamento Do Dia
            data4 = datetime.datetime.now()
            data4 = data4.strftime('%d/%m/%y %H:%M')
            arquivo10 = open('Cache.txt', 'r')
            info = arquivo10.read()
            if f'Fechamento Do Dia {data4:.5}' in info:
                print('Fechamento Ja Adicionado!!')
                pass
            elif f'Fechamento Do Dia {data4:.5}' not in info:
                arquivo9 = open('Cache.txt', 'a')
                arquivo9.write('\n')
                arquivo9.write(f'Fechamento Do Dia {data4}')
                arquivo9.write('\n')
                arquivo9.write(f'{btc} Alta R${alta:.4} Baixa R${baixa:.4}')
                arquivo9.write('\n')
                arquivo9.write('\n')
                arquivo9.close()

            toaster = ToastNotifier()
            toaster.show_toast(
                btc,
                f'Fechamento do Dia {data}\n'
                f'💲 Alta R${alta:.4} Baixa R${baixa:.4}\nO Programa Será Encerrado ❗❗ 💤',
                threaded=True,
                icon_path=None,
                duration=300
            )
            #Fim Do Fechamento Do Dia
            break
except ModuleNotFoundError as erro:
    Erro = str(erro)
    print(f'A Biblioteca {Erro[16:]} não Encontrada\nInstale as Bibliotecas'
          f' Win10toast, Requests e matplotlib\nO Programa Será Encerrado ❗❗ 💤')
    time.sleep(10)
    exit()
except requests.exceptions.ConnectionError as erro:
    print('Erro de Conexão!!\nVerifique A Conexão Com a Internet')
    time.sleep(3600)
