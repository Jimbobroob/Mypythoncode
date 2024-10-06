import tkinter as tk
import random

window = tk.Tk()
window.title("Rock Paper Scissors")

def paper_function():
    rand=['R','P', 'S']
    computer_choice = random.choice(rand)
    if computer_choice == 'R':
        result1 = tk.Label(text="You Win")
        result1.pack()
    elif computer_choice == 'P':
        result2 = tk.Label(text="Tie")
        result2.pack()
    elif computer_choice == 'S':
        result3 = tk.Label(text="You Lose")
        result3.pack()   
        
def rock_function():
    rand=['R','P', 'S']
    computer_choice = random.choice(rand)
    if computer_choice == 'R':
        result2 = tk.Label(text="Tie")
        result2.pack()
    elif computer_choice == 'P':
        result3 = tk.Label(text="You Lose")
        result3.pack()
    elif computer_choice == 'S':
        result1 = tk.Label(text="You Win")
        result1.pack()           
        
def scissors_function():
    rand=['R','P', 'S']
    computer_choice = random.choice(rand)
    if computer_choice == 'R':
        result3 = tk.Label(text="You Lose")
        result3.pack()
    elif computer_choice == 'P':
        result2 = tk.Label(text="You Win")
        result2.pack()
    elif computer_choice == 'S':
        result1 = tk.Label(text="Tie")
        result1.pack()  

greeting = tk.Label(text="My Rock Paper Scissors Game")
greeting.pack()

button1 = tk.Button(text="Rock", width=25, height=5, bg="grey", fg="white", command= rock_function)
button1.pack() 

button2 = tk.Button(text="Scissors", width=25, height=5, bg="grey", fg="white", command= scissors_function) 
button2.pack() 

button3 = tk.Button(text="Paper", width=25, height=5, bg="grey", fg="white", command= paper_function)
button3.pack()  


    
window.mainloop()