def ELIZA():
    run = True
    while run:
        topic = input("Ask me something")
        print(f"{topic} is cool! tell me more")
        exit = input("do you want to exit?")
        if exit in ["yes", "Yes", "y"]:
            run = False

ELIZA()