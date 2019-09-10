import tkinter as tk
import random

window = tk.Tk()
window.title("Password Genarator")
window.geometry("1000x1000")

def eight_length():
	word = ['a','b','c','d','e','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','-','_','+','=',',','.','/','?','"',':',';','`','[',']','{','}','|']
	name = str(entry1.get())
	return name + " your Password Is :  "  + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)]  


def eight_display():
	eight = eight_length()

	eightdisplay = tk.Text(master=window, height=10,width=80)
	eightdisplay.grid(column=10,row=10)
	eightdisplay.insert(tk.END,eight)

def nine_length():
	word = ['a','b','c','d','e','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','-','_','+','=',',','.','/','?','"',':',';','`','[',']','{','}','|']
	name = str(entry1.get())
	return name + " your Password Is :  "  + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)]  


def nine_display():
	nine = nine_length()

	ninedisplay = tk.Text(master=window, height=10,width=80)
	ninedisplay.grid(column=10,row=10)
	ninedisplay.insert(tk.END,nine)

def ten_length():
	word = ['a','b','c','d','e','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','-','_','+','=',',','.','/','?','"',':',';','`','[',']','{','}','|']
	name = str(entry1.get())
	return name + " your Password Is :  "  + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)]  


def ten_display():
	ten = ten_length()

	tendisplay = tk.Text(master=window, height=10,width=80)
	tendisplay.grid(column=10,row=10)
	tendisplay.insert(tk.END,ten)

def eleven_length():
	word = ['a','b','c','d','e','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','-','_','+','=',',','.','/','?','"',':',';','`','[',']','{','}','|']
	name = str(entry1.get())
	return name + " your Password Is :  "  + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)]  


def eleven_display():
	eleven = eleven_length()

	elevendisplay = tk.Text(master=window, height=10,width=80)
	elevendisplay.grid(column=10,row=10)
	elevendisplay.insert(tk.END,eleven)

def twelve_length():
	word = ['a','b','c','d','e','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','-','_','+','=',',','.','/','?','"',':',';','`','[',']','{','}','|']
	name = str(entry1.get())
	return name + " your Password Is :  "  + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)]  


def twelve_display():
	twelve = twelve_length()

	twelvedisplay = tk.Text(master=window, height=10,width=80)
	twelvedisplay.grid(column=10,row=10)
	twelvedisplay.insert(tk.END,twelve)

def thirteen_length():
	word = ['a','b','c','d','e','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','-','_','+','=',',','.','/','?','"',':',';','`','[',']','{','}','|']
	name = str(entry1.get())
	return name + " your Password Is :  "  + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)] + word[random.randint(1,90)]  


def thirteen_display():
	thirteen = thirteen_length()

	thirteendisplay = tk.Text(master=window, height=10,width=80)
	thirteendisplay.grid(column=10,row=10)
	thirteendisplay.insert(tk.END,thirteen)





label1 = tk.Label(text="Password generator",font=("Arial Black",20))
label1.grid(column=3, row=0)

label2 = tk.Label(text="Select your choice",font=("Arial Black",15))
label2.grid(column=1,row=1)

label3 = tk.Label(text="Enter your name :",font=("Arial Black",10))
label3.grid(column=2,row=2)

entry1 = tk.Entry()
entry1.grid(column=3,row=2)

button1 = tk.Button(text="8 length password",command=eight_display,bg="green")
button1.grid(column=1,row=3)

button2 = tk.Button(text="9 length password",command=nine_display,bg="yellow")
button2.grid(column=3,row=4)

button3 = tk.Button(text="10 length password",command=ten_display,bg="green")
button3.grid(column=1,row=5)

button4 = tk.Button(text="11 length password",command=eleven_display,bg="yellow")
button4.grid(column=3,row=6)

button5 = tk.Button(text="12 length password",command=twelve_display,bg="green")
button5.grid(column=1,row=7)

button6 = tk.Button(text="13 length password",command=thirteen_display,bg="yellow")
button6.grid(column=3,row=8)

window.mainloop()