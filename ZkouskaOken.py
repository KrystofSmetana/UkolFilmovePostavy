import tkinter as tk
      
okno = tk.Tk()
okno.title("Smetana")
okno.geometry("300x300")
            
#text
label = tk.Label(okno, text="Nivniwho?")
label.pack()
            
#textové pole
vstup = tk.Entry(okno)
vstup.pack()
            
 #tlačítko
def dělej():
    print("ticho")
tlačitko = tk.Button(okno, text="Nemačkat", bg="yellow", command =dělej)
tlačitko.pack()
tlačitko2 = tk.Button(okno, text="FAKT NEMAČKAT", bg="red", command =okno.destroy)
tlačitko2.pack()

okno.mainloop()
            