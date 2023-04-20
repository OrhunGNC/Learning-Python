while True:
    print("Options")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Division")
    print("4.Multiply")
    commandtxt=input("Choose command: ")
    num1=float(input("First Number: "))
    num2=float(input("Second Number: "))
    if(commandtxt=="Addition"):
        rslt=num1+num2
        print(rslt)
        cnt=input("Do you want to continue? (Yes/No)")
        if(cnt=="No"):
            break
        else:
            continue
    elif(commandtxt=="Subtraction"):
        rslt=num1-num2
        print(rslt)
        cnt=input("Do you want to continue? (Yes/No)")
        if(cnt=="No"):
            break
        else:
            continue
    elif(commandtxt=="Division"):
        try:
            rslt=num1/num2
            print(rslt)
            cnt=input("Do you want to continue? (Yes/No)")
            if(cnt=="No"):
                break
            else:
                continue
        except:
            print("Num2 cannot be equal to 0!")
            cnt=input("Do you want to continue? (Yes/No)")
            if(cnt=="No"):
                break
            else:
                continue
        
    elif(commandtxt=="Multiply"):
        rslt=num1*num2
        print(rslt)
        cnt=input("Do you want to continue? (Yes/No)")
        if(cnt=="No"):
            break
        else:
            continue
    else:
        print("Wrong Command!")
        cnt2=input("Do you want to try again? (Yes/No)")
        if(cnt=="Yes"):
            continue
        else:
            break




