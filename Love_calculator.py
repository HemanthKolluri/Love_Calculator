
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

c=0
name1=name1.lower()
name2=name2.lower()
z=name1+name2

c=c+z.count("t")
c=c+z.count("r")
c=c+z.count("u")
c=c+z.count("e")

n=0
n=n+z.count("l")
n=n+z.count("o")
n=n+z.count("v")
n=n+z.count("e")
T=str(c)+str(n)
T=int(T)
print(f"Your score is {T}.")
