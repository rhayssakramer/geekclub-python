   # Declaração de variáveis
dinheiro, resultado, hora, lanche, outrolanche, refri, outrorefri = "", "", "", "", "", "", ""
valortempo, valorcomida, outracomida, valorbebida, outrabebida = 0.0, 0.0, 0.0, 0.0, 0.0
opcao, tempo, opcaocomida, opcaobebida, comida, maiscomida, bebida, maisbebida, pagamento, escolhafim = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
total = 0.0
    
while True:
        print("                              ")
        print("Seja Bem-Vindo ao Geek Club!")
        print("                              ")
        print("Somos um novo conceito de Park Tech, líder na América Latina com vários ambientes temáticos do mundo Nerd!")
        print("------------------------------")
        print("Vamos juntos embarcar nessa aventura cheia de diversões? VEM COMIGO!")
        print("Nesse mês de Dezembro estamos trazendo muito entretenimento, com valores promocionais, especialmente para vocês.")
        print("                              ")
        print("Para adquirir sua passagem para o mundo da diversão, você terá que escolher um entretenimento, o tempo que deseja se divertir, e poderá também escolher o que deseja comer e beber.")
        print("------------------------------")
        print("APROVEITE SUA EXPERIÊNCIA!")
        print("                               ")

        # Escolha as opções de entretenimento
        while True:
            print("Comece escolhendo para qual diversão você deseja se aventurar hoje:")
            print(" 1: Salão de Games.")
            print(" 2: Boliche.")
            print(" 3: Pista de Patinação.")
            print(" 4: Sair do Menu.")
            opcao = int(input("Opção escolhida: "))
            
            if opcao == 1:
                resultado = "Salão de Games"
                break
            elif opcao == 2:
                resultado = "Boliche"
                break
            elif opcao == 3:
                resultado = "Pista de Patinação"
                break
            elif opcao == 4:
                resultado = "Sair do Menu."
                print("Você escolheu a opção Sair do Menu. Obrigado pela visita e volte sempre!")
            else:
                print("Você escolheu uma opção inválida!")
        
        print(f"Que legal! A sua escolha de hoje para se divertir foi {resultado}")

        # Escolha as opções de tempo de diversão
        while True:
            print("Agora escolha qual o tempo que você deseja se divertir conosco hoje:")
            print(" 1: 2 horas.")
            print(" 2: 5 horas.")
            print(" 3: Diária.")
            print(" 4: Sair do Menu.")
            tempo = int(input("Opção escolhida: "))
            
            if tempo == 1:
                hora = "2 horas"
                valortempo = 35.0
                break
            elif tempo == 2:
                hora = "5 horas"
                valortempo = 75.0
                break
            elif tempo == 3:
                hora = "Diária"
                valortempo = 100.0
                break
            elif tempo == 4:
                hora = "Sair do Menu."
                print("Você escolheu a opção Sair do Menu. Obrigado pela visita e volte sempre!")
            else:
                print("Você escolheu uma opção inválida!")
        
        print(f"Que Massa! A sua opção de tempo escolhida foi {resultado} por {hora}")

        # Escolha as opçõe de comida
        while True:
            print("Agora escolha qual comida você quer pedir hoje:")
            print(" 1: Batata Frita.")
            print(" 2: Hambuguer.")
            print(" 3: Hot-Dog.")
            print(" 4: Nenhuma das opções acima.")
            print(" 5: Sair do Menu.")
            comida = int(input("Opção escolhida: "))
            
            if comida == 1:
                lanche = "Batata Frita"
                valorcomida = 20.0
                break
            elif comida == 2:
                lanche = "Hambuguer"
                valorcomida = 25.0
                break
            elif comida == 3:
                lanche = "Hot-Dog"
                valorcomida = 15.0
                break
            elif comida == 4:
                lanche = "Nenhuma das opções."
                print("Você escolheu a opção Nenhuma das opções. Anotado, vamos seguir!")
                break
            elif comida == 5:
                lanche = "Sair do Menu."
                print("Você escolheu a opção Sair do Menu. Obrigado pela visita e volte sempre!")
            else:
                print("Você escolheu uma opção inválida!")
        
        print(f"Que delícia, excelente escolha! A sua comida escolhida para hoje foi {lanche}")
        
        # Escolha a opção de mais comida
        while True:
            print("Você deseja incluir mais algum item na opção de comida? Responda abaixo:")
            print(" 1: Sim.")
            print(" 2: Não")
            opcaocomida = int(input("Opção escolhida: "))
            
            if opcaocomida == 1:
                while True:
                    print("Escolha outra opção de comida que você deseja pedir hoje:")
                    print(" 1: Batata Frita.")
                    print(" 2: Hambuguer.")
                    print(" 3: Hot-Dog.")
                    print(" 4: Nenhuma das opções acima.")
                    maiscomida = int(input("Opção escolhida: "))
                    
                    if maiscomida == 1:
                        outrolanche = "Batata Frita"
                        outracomida = 20.0
                        break
                    elif maiscomida == 2:
                        outrolanche = "Hambuguer"
                        outracomida = 25.0
                        break
                    elif maiscomida == 3:
                        outrolanche = "Hot-Dog"
                        outracomida = 15.0
                        break
                    elif maiscomida == 4:
                        outrolanche = "Nenhuma das opções."
                        print("Você escolheu a opção Nenhuma das opções. Anotado, vamos seguir!")
                        break
                    else:
                        print("Você escolheu uma opção inválida!")
                break
            elif opcaocomida == 2:
                break
            else:
                print("Você escolheu uma opção inválida!")
        
        print(f"Que delícia, excelente escolha! A sua comida escolhida para hoje foi {lanche} e {outrolanche}")

        # Escolha as opções de bebidas
        while True:
            print("Por fim, escolha qual bebida você quer pedir hoje:")
            print(" 1: Coca-cola.")
            print(" 2: Suco.")
            print(" 3: Água.")
            print(" 4: Nenhuma das opções acima.")
            print(" 5: Sair do Menu.")
            bebida = int(input("Opção escolhida: "))
            
            if bebida == 1:
                refri = "Coca-Cola"
                valorbebida = 10.0
                break
            elif bebida == 2:
                refri = "Suco"
                valorbebida = 8.0
                break
            elif bebida == 3:
                refri = "Água"
                valorbebida = 5.0
                break
            elif bebida == 4:
                refri = "Nenhuma das opções."
                print("Você escolheu a opção Nenhuma das opções. Anotado, vamos seguir!")
                break
            elif bebida == 5:
                refri = "Sair do Menu."
                print("Você escolheu a opção Sair do Menu. Obrigado pela visita e volte sempre!")
            else:
                print("Você escolheu uma opção inválida!")
        
        print(f"Excelente escolha! A sua bebida escolhida para hoje foi {refri}")
        
        # Escolha a opção de mais bebida
        while True:
            print("Você deseja incluir mais algum item na opção de bebida? Responda abaixo:")
            print(" 1: Sim.")
            print(" 2: Não")
            opcaobebida = int(input("Opção escolhida: "))
            
            if opcaobebida == 1:
                while True:
                    print("Escolha outra opção de bebida que você deseja pedir hoje:")
                    print(" 1: Coca-cola.")
                    print(" 2: Suco.")
                    print(" 3: Água.")
                    print(" 4: Nenhuma das opções acima.")
                    maisbebida = int(input("Opção escolhida: "))
                    
                    if maisbebida == 1:
                        outrorefri = "Coca-Cola"
                        outrabebida = 10.0
                        break
                    elif maisbebida == 2:
                        outrorefri = "Suco"
                        outrabebida = 8.0
                        break
                    elif maisbebida == 3:
                        outrorefri = "Água"
                        outrabebida = 5.0
                        break
                    elif maisbebida == 4:
                        outrorefri = "Nenhuma das opções."
                        print("Você escolheu a opção Nenhuma das opções. Anotado, vamos seguir!")
                        break
                    else:
                        print("Você escolheu uma opção inválida!")
                break
            elif opcaobebida == 2:
                break
            else:
                print("Você escolheu uma opção inválida!")
        
        print(f"Excelentes escolhas! Sua bebida escolhida para hoje foi {refri} e {outrorefri}")
        
        total = valortempo + valorcomida + valorbebida + outracomida + outrabebida
        print("------------------------------")
        print("Fica ligado! Segue os seus itens escolhidos para a sua aventura de hoje:")
        print(f"Para entretenimento: {resultado}")
        print(f"Para tempo: {hora} | R$ {valortempo}")
        print(f"Sua comida: {lanche} e {outrolanche} | R$ {valorcomida} | R$ {outracomida}")
        print(f"Sua bebida: {refri} e {outrorefri} | R$ {valorbebida} | R$ {outrabebida}")
        
        print("------------------------------")
        print(f"O valor total dos itens escolhidos foram R$ {total}")
        
        # Escolha o método de pagamento
        while True:
            print("Então, qual a sua forma de pagamento dos itens escolhidos?")
            print(" 1: Dinheiro.")
            print(" 2: Pix.")
            print(" 3: Débito.")
            print(" 4: Crédito.")
            print(" 5: Sair do Menu.")
            pagamento = int(input("Opção escolhida: "))
            
            if pagamento == 1:
                dinheiro = "Dinheiro."
                break
            elif pagamento == 2:
                dinheiro = "PIX"
                break
            elif pagamento == 3:
                dinheiro = "Débito."
                break
            elif pagamento == 4:
                dinheiro = "Crédito."
                break
            elif pagamento == 5:
                dinheiro = "Sair do Menu."
                print("Você escolheu a opção Sair do Menu. Obrigado pela visita e volte sempre!")
            else:
                print("Você escolheu uma opção inválida!")
        
        print(f"Sua forma de pagamento escolhida foi {dinheiro}")
        print("------------------------------")
        print("Muito bom! Obrigada por nos escolher, tenha um excelente dia e experiência no Geek Club!")
        
        while True:
            print("------------------------------")
            print("Você deseja incluir mais alguma coisa? Responda abaixo:")
            print(" 1: Sim.")
            print(" 2: Não")
            escolhafim = int(input("Opção escolhida: "))
            
            if escolhafim == 1:
                print("------------------------------")
                print("Vamos voltar ao menu inicial!")
                break
            elif escolhafim == 2:
                print("Você escolheu a opção Não, você deseja sair do menu. Obrigado pela visita e volte sempre!")
                exit()
            else:
                print("Você escolheu uma opção inválida!")