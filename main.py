while True:
    choice:str = input("Do you want to start the game? (yes or no ?):").strip().lower()

    if choice in ["no"]:
       print("goodbye!, see you later")
       break
    elif choice in ["yes"]:
        question: list[tuple[str,list[str],str]]=[
        ("what your name?",["A:sara", "B:zizi", "C:ali" , "D:abas"],"B"),
        ("how old are you?",["A:20", "B:21", "C:22" , "D:23"],"A"),
        ("what your favorite color?",["A:black", "B:blue", "C:pink" , "D:red"],"C")
         ]
    score=0
    BONUS= 10
    PENALTY=3
    correct=0
    for qu,opt,ans in question:
        print(qu)
        for op in opt:
         print(op)
    useranswer:str = input("your choice:").strip().upper()
    if useranswer == ans:
        print("correct!!")
        score += BONUS
        correct +=1
    else:
        print("incorrect")
        score -= PENALTY
    print(f"your final score :{score}")
    print(f"your answered:{correct}")
    print(f"percentage:{correct / len (qu)*100}")

    
