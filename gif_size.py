import turtle
import pandas
from guess_update import Update_Guess
import time
import tkinter
screen = turtle.Screen()

# window = tkinter.Tk()
# window.title('Baranggay')
# frame = tkinter.Frame(window)
# frame.pack()
# brgy_frame = tkinter.LabelFrame(frame, text='Guess a baranggay')
# brgy_frame.grid(row=0, column=0, padx=20,pady=20,sticky='news')
# brgy_guess = tkinter.Label(brgy_frame, text='Type a baranggay')
# brgy_guess.grid(row=0, column=0, padx=5,pady=5,sticky='news')
# brgy_entry = tkinter.Entry(brgy_frame)
# brgy_entry.grid(row=1, column=0, padx=1,pady=1,sticky='news')
# player_guess = brgy_entry.get()
# print(player_guess)
# # button = tkinter.Button(brgy_frame,text='Check Baranggay', command=Check_Baranggay)
# button = tkinter.Button(brgy_frame,text='Check Baranggay')
# button.grid(row=2, column=0, sticky='news')

screen = turtle.Screen()
screen.setup(width=800, height=800)
# img_background = 'new_4th_dist.gif'
img_background = 'resized.gif'
screen.addshape(img_background)
turtle.shape(img_background)
district4_df = pandas.read_csv('district4_csv.csv')

# print(district4_df)
# print(district4_df.iloc[36][0], district4_df.iloc[36][1], district4_df.iloc[36][2])
# print(type(district4_df.iloc[1][0]))
# print(district4_df.iloc[1][1])
# print(type(district4_df.iloc[1][1]))
# print(district4_df.iloc[1][2])
# print(len(district4_df))
# for i in range(37):
#     print(district4_df.iloc[i][0], district4_df.iloc[i][1], district4_df.iloc[i][2])
# print(district4_df.Baranggay)
# print(type(district4_df.Baranggay.to_list()))

remaining_guess = 10
t = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
# remaining_guess = Update_Guess()
list_of_guesses = []
game_on = True
while remaining_guess != 0:

    user_input = screen.textinput(title='Input Baranggay', prompt='Type guess')
    list_of_guesses.append(user_input)
    if user_input in district4_df.Baranggay.to_list():
        print('okay')
        idx = district4_df.Baranggay.to_list().index(user_input)
        print(idx)
        print(district4_df.iloc[idx][1], district4_df.iloc[idx][2])
        # t.hideturtle()
        t.penup()
        t.shape('circle')
        t.goto(district4_df.iloc[idx][1], district4_df.iloc[idx][2])
        t.write(user_input, align='center', font=('Arial', 20, 'bold'))

    else:
        remaining_guess -= 1
        t2.hideturtle()
        t2.clear()
        t2.penup()
        t2.goto(-273.0, 439.0)
        t2.write(f'remaining guesses = {remaining_guess}', font=('Arial', 20, 'bold'))
        if remaining_guess == 0:
            game_on = False
            break
        else:
            # remaining_guess.update_guess()
            t1.hideturtle()
            t1.clear()
            t1.penup()
            t1.goto(-243.0, 400.0)
            t1.write(f'{list_of_guesses[len(list_of_guesses) - 1]} does not belong in the 4th District of QC, '
                     f'check spelling or take another guess', font=('Arial', 20, 'bold'))





# -253.0,439.0
# def get_mouse_click_coor(x, y):
#     print(f'{x},{y}')
#     turt = turtle.Turtle()
#     turt.penup()
#     turt.goto(x,y)
# turtle.onscreenclick(get_mouse_click_coor)

# def get_mouse_click_coor(x, y):
#     print(f'x={x}, y={y}')
# turtle.onscreenclick(get_mouse_click_coor)

# sample = [[-39.0, 41.0], [250.0, 205.0]]
# print(sample)
# print(type(sample))
# for samp in sample:
#     print(samp[0],samp[1])

# screen.exitonclick()
turtle.mainloop()


# def get_mouse_click_coor(x, y):
#     print(f'x={x}, y={y}')
# turtle.onscreenclick(get_mouse_click_coor)


# from PIL import Image, ImageSequence
#
# im = Image.open("new_4th_dist_python.jpg")
# im = im.resize((im.size[0] // 1, im.size[1] // 1), Image.ANTIALIAS)  # decreases width and height of the image
# im.save("conv1.jpg", optimize=True, quality=100)  # decreases its quality

# from PIL import Image, ImageSequence
#
# im = Image.open("new_4th_dist_python.jpg")
# im = im.resize((im.size[0] // 1, im.size[1] // 1), Image.ANTIALIAS)  # decreases width and height of the image
# im.save("conv1.jpg", quality=100)  # decreases its quality