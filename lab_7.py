import turtle

n=10
def countdown():
    global n
    if n == 0:
        print("blast off")
        return
    print(n)
    n=n-1
    turtle.ontimer(countdown,1000)
    

countdown()
