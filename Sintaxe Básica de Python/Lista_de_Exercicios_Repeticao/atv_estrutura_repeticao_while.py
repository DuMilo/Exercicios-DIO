while True:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n>> 0"));

    if opcao == 1:
        print("Sacando...");
    elif opcao == 2:
        print("Exibindo o extrato...");
    else:
        print("Obrigado por usar nosso sistema bancário, até logo!");
        break;
