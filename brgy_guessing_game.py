import turtle
import pandas
screen = turtle.Screen()

screen = turtle.Screen()
screen.title('District 4 QC Baranggays')
screen.setup(width=1600, height=1062)
img_background = 'resized.gif'
# img_background = 'new_4th_dist.gif'
# img_background = 'samsung.gif'
screen.addshape(img_background)
turtle.shape(img_background)
district4_df = pandas.read_csv('final_brgy_list.csv')

# print(district4_df)
# print(district4_df.brgys_in_lowercase.to_list())
# print(type(district4_df.brgys_in_lowercase.to_list()))

remaining_guess = 10
t = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

list_of_guesses = []
correct_guesses = []
game_on = True
while remaining_guess != 0:
    user_input = screen.textinput(title='Type a Baranggay', prompt='name').lower().strip()
    list_of_guesses.append(user_input)
    if user_input in district4_df.brgys_in_lowercase.to_list():
        correct_guesses.append(user_input)
        print('okay')
        idx = district4_df.brgys_in_lowercase.to_list().index(user_input)
        print(idx)
        print(district4_df.iloc[idx][2], district4_df.iloc[idx][3])
        # t.hideturtle()
        t.penup()
        t.shape('circle')
        t.goto(district4_df.iloc[idx][2], district4_df.iloc[idx][3])
        t.write(user_input.title(), align='center', font=('Arial', 15, 'bold'))

        t3.clear()
        t3.penup()
        t3.hideturtle()
        t3.goto(-250.0, 350.0)
        t3.write(f'{len(correct_guesses)} out of 37 correct', font=('Arial', 20, 'bold'))

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
print(list_of_guesses)
print(correct_guesses)

missed_brgys = []
for each_brgy in district4_df.brgys_in_lowercase.to_list():
    if each_brgy not in  list_of_guesses:
        missed_brgys.append(each_brgy)
        # print(each_brgy,district4_df.brgys_in_lowercase.to_list().index(each_brgy), district4_df.iloc[
        #     district4_df.brgys_in_lowercase.to_list().index(each_brgy)][2],district4_df.iloc[
        #     district4_df.brgys_in_lowercase.to_list().index(each_brgy)][3])
# print(missed_brgys)

t4 = turtle.Turtle()
for brgy_missed in missed_brgys:
    print(brgy_missed)
    t4.hideturtle()
    t4.penup()
    t4.color('red')
    t4.goto(district4_df.iloc[
            district4_df.brgys_in_lowercase.to_list().index(brgy_missed)][2],district4_df.iloc[
            district4_df.brgys_in_lowercase.to_list().index(brgy_missed)][3])
    t4.write(brgy_missed,align='center',font=('Arial', 15, 'normal'))

t5 = turtle.Turtle()
t5.hideturtle()
t5.penup()
t5.goto(150,-200)
t5.write('These are the baranggays that you have missed', font=('Arial', 20, 'bold'))


# t3.penup()
# t3.hideturtle()
# t3.goto(0,0)
# t3.write(missed_brgys,align='center',font=('Arial', 20, 'bold'))

# screen.exitonclick()
turtle.mainloop()