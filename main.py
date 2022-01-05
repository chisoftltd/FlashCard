from tkinter import *
import os

#   --------------------------------------- CONSTANTS -----------------------------------------------
FONT_NAME = "Ariel"
BACKGROUND_COLOR = "#B1DDC6"


#   --------------------------------------- UI SETUP ------------------------------------------------
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_image = PhotoImage(file="images/card_front.png")
canvas_card = Canvas(width=800, height=526)
canvas_card.create_image(400, 263, image=card_image)
canvas_card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_card.create_text(400, 150, text="Title", fill="black", font=(FONT_NAME, 40, "italic"))
canvas_card.create_text(400, 300, text="Word", fill="black", font=(FONT_NAME, 60, "bold"))
canvas_card.grid(row=0, column=0, columnspan=2)

good_image = PhotoImage(file="images/right.png")
canvas_good = Button(image=good_image, highlightthickness=0)
canvas_good.grid(row=1, column=1)

x_image = PhotoImage(file="images/wrong.png")
canvas_x = Button(image=x_image, highlightthickness=0)
canvas_x.grid(row=1, column=0)

window.mainloop()
