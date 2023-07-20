import pyautogui
import time

print ('A mensagem que sera enviada por padrão é: \n1º"Boa noite!" \n2º"Estou sem sono, e vc foi sortiado(a) a contar carnerinho comigo :)" \n3º"1 carnerinho..." \n4º"Obg por ma fazer companhia."')
print ('OBS:Já deixe no contato que ira receber a mensagem')

resposta = input('deseja mododificar algo?[S/N]')
resposta = resposta.upper()

while (resposta != 'S') and (resposta != 'N'):
    print ('Palavra invalida.')
    resposta = input('deseja mododificar algo?[S/N]')
    resposta = resposta.upper()

if (resposta == 'S'):
    confirmacao = 'N'
    while (confirmacao == 'N'):
        print('=' * 50)
        txt1 = input('Informe a 1º frase:')
        txt2 = input('Informe a 2º frase:')
        laco = input('Informe a frase a ser repetida:')
        txt3 = input('Informe a frase final:')
        print('=' * 50)

        print('A frase foi modificada para: \n1º"{}" \n2º"{}" \n3º"{}" \n4º"{}"' .format(txt1, txt2,laco,txt3))

        confirmacao = input('Esta correto?[S/N]')
        confirmacao = confirmacao.upper()

        while (confirmacao != 'S') and (confirmacao != 'N'):
            print('Palavra invalida.')
            confirmacao = input('Esta correto?[S/N]')
            confirmacao = confirmacao.upper()
    
    cont_laco = int(input('Quantas vezes vou contar o "{}"?' .format(laco)))

    while (cont_laco < 0):
        print('Número invalido.')
        cont_laco = int(input('Quantas vezes vou contar o "{}"?' .format(laco)))

    whataspp = input('Onde o whataspp vai ser aberto?[web/app]')
    whataspp = whataspp.lower()

    while (whataspp != 'web') and (whataspp != 'app'):
        print('Palavra invalida.')
        whataspp = input('Onde o whataspp vai ser aberto?[web/app]')
        whataspp = whataspp.lower()

    if (whataspp == 'web'):
        print('Abra o whatsApp e deixe no contato que deseja enviar a mensagem.')
        janela = int(input('Informe em qual posição na barra de aplicativos esta o seu navegador:'))

        while (janela <= 0):
            print('Número invalido.')
            janela = int(input('Informe em qual posição na barra de aplicativos esta o seu navegador:'))

        for cont in range (1, janela+1):
            pyautogui.hotkey('win', 't')
            time.sleep(0.1)
        pyautogui.press('enter')

        time.sleep(2)
        pyautogui.write(txt1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write(txt2)
        pyautogui.press('enter')
        time.sleep(1)

        for cont in range (1, cont_laco + 1):
            pyautogui.write(laco)
            pyautogui.press('enter')
            time.sleep(1)
        
        pyautogui.write(txt3)
        pyautogui.press('enter')
        time.sleep(2)
    else:
        janela = int(input('Informe em qual posição na barra de aplicativos esta o WhatsApp:'))

        while (janela <= 0):
            print('Número invalido.')
            janela = int(input('Informe em qual posição na barra de aplicativos esta o whatsApp:'))

        for cont in range (1, janela + 1):
            pyautogui.hotkey('win', 't')
            time.sleep(0.1)
        pyautogui.press('enter')

        time.sleep(2)
        pyautogui.write(txt1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write(txt2)
        pyautogui.press('enter')
        time.sleep(1)

        for cont in range (1, cont_laco + 1):
            pyautogui.write(laco)
            pyautogui.press('enter')
            time.sleep(1)
        
        pyautogui.write(txt3)
        pyautogui.press('enter')
    time.sleep(2)
else:
    cont_carnerinhos = int(input('Quantas vezes vou contar os carnerinhos?'))

    while (cont_carnerinhos < 0):
        print('Número invalido.')
        cont_carnerinhos = int(input('Quantas vezes vou contar os carnerinhos?'))

    whataspp = input('Onde o whataspp vai ser aberto?[web/app]')
    whataspp = whataspp.lower()

    while (whataspp != 'web') and (whataspp != 'app'):
        print('Palavra invalida.')
        whataspp = input('Onde o whataspp vai ser aberto?[web/app]')
        whataspp = whataspp.lower()

    if (whataspp == 'web'):
        print('Abra o whatsApp e deixe no contato que deseja enviar a mensagem.')
        janela = int(input('Informe em qual posição na barra de aplicativos esta o seu navegador:'))

        while (janela <= 0):
            print('Número invalido.')
            janela = int(input('Informe em qual posição na barra de aplicativos esta o seu navegador:'))

        for cont in range (1, janela + 1):
            pyautogui.hotkey('win', 't')
            time.sleep(0.1)
        pyautogui.press('enter')

        time.sleep(2)
        pyautogui.write('Boa noite!')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write('Estou sem sono, e vc foi sortiado a contar carnerinho comigo :)')
        pyautogui.press('enter')
        time.sleep(1)
        
        for cont in range(1, cont_carnerinhos+1):
            pyautogui.write('{} carnerinho' .format(cont))
            pyautogui.press('enter')
            time.sleep(0.2)

        pyautogui.write('Obg por me fazer companhia!')
        pyautogui.press('enter')
        time.sleep(2)
    else:
        janela = int(input('Informe em qual posição na barra de aplicativos esta o whatsApp:'))

        while (janela <= 0):
            print('Número invalido.')
            janela = int(input('Informe em qual posição na barra de aplicativos esta o whatsApp:'))
    
        for cont in range (1, janela+1):
            pyautogui.hotkey('win', 't')
            time.sleep(0.1)
        pyautogui.press('enter')

        time.sleep(2)
        pyautogui.write('Boa noite!')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write('Estou sem sono, e vc foi sortiado a contar carnerinho comigo :)')
        pyautogui.press('enter')
        time.sleep(1)
        
        for cont in range(1, cont_carnerinhos+1):
            pyautogui.write('{} carnerinho' .format(cont))
            pyautogui.press('enter')
            time.sleep(0.2)

        pyautogui.write('Obg por me fazer companhia!')
        pyautogui.press('enter')
        time.sleep(2)