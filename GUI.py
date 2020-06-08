import tkinter as tk
import itertools

root = tk.Tk()
'''Window'''

my_canvas = tk.Canvas(root, width = "1500", height = "790", background ="BLACK")

my_canvas.pack()
'''Creating Lines'''
my_canvas.create_line(760,40,760,400,fill="green")
my_canvas.create_line(260,40,1480,40,fill="green")
my_canvas.create_line(10,40,1480,40,fill="green")
my_canvas.create_line(10,40,10,400,fill="green")
my_canvas.create_line(10,400,1480,400,fill="green")
my_canvas.create_line(1480,40,1480,400,fill="green")
my_canvas.create_oval(1135, 380, 1150, 390, width = 0, fill = 'white')
"my_canvas.create_image(20,65,image=photo,anchor = tk.NW)"
'''Labels'''

heading = tk.Label(root,text ="Autonomous Scoring Drone", font=("arial",20,"bold"),bg="black",
                fg="white").place(x=120,y=1)
photo = tk.Label(root,text ="Captured Image", font=("arial",8,"bold"),bg="black", fg="white").place(x=25,y=40)
map = tk.Label(root, text="Map", font=("arial", 10, "bold"), bg="black", fg="white").place(x=800, y=50)
question = tk.Label(root, text="How many Locations are you going ?", font=("arial", 10, "bold"), bg="black", fg="white").place(x=780, y=410)
label1 = tk.Label(root,text ="YARK", font=("arial",8,"bold"),bg="black", fg="white").place(x=10,y=770)
updateLabel = tk.Label(root,text =" Update: ", font=("arial",10,"bold"),bg="black", fg="white").place(x=200,y=700)
BaseStationLabel = tk.Label(root,text =" Base ", font=("arial",8,"bold"),bg="black", fg="white").place(x=1090,y=375)
CurrentStatusLabel = tk.Label(root,text ="Current Status: ", font=("arial",10,"bold"),bg="black", fg="white").place(x=20,y=420)
ScoreLabel = tk.Label(root,text ="Score: ", font=("arial",10,"bold"),bg="black", fg="white").place(x=20,y=370)

'''Function user input'''
def userInput():
    global entry_label1
    global submit_btn, stats_label
    global entry_label2
    global entry1Remove
    entry1Remove =[]
    global entry2Remove
    entry2Remove = []
    global removeLabel
    removeLabel = []
    global oval_label
    global locations
    global cur_label
    locations = input1.get()
    labels = "Enter longitude and latitude: "
    currentStatus(locations)
    '''Creating Locations'''
    for i in range(locations):
        oval_label = 'label' + str(i)
        location_label = 'label' + str(i)
        cur_label = tk.Label(my_canvas, text= "L" + str(i + 1), font=("arial", 6, "bold"), bg="black",
                             fg="white")
        cur_label.place(x=1440 -i*70, y= 70)
        oval_label = my_canvas.create_oval(1450 - i * 70 , 110 , 1430  - i * 70, 100, width = 0, fill = 'blue')
    '''Print labels as many times as user wants'''
    for i in range(locations):
        cur_label = 'label' + str(i)
        cur_label = tk.Label(my_canvas, text= labels, font=("arial", 10, "bold"), bg="black",
                             fg="white")
        cur_label.place(x=780, y=440 + i * 20)
        removeLabel.append(cur_label)
    '''Print Entry box as many times as user wants'''
    global longitude
    longitude = []
    latitude = []
    for i in range(locations):
        entry_label1 = tk.Entry(my_canvas, text=longitude.append(i), width = 20)
        entry_label1.place(x=980, y=440 + i * 20)
        entry1Remove.append(entry_label1)
        entry_label2 = tk.Entry(my_canvas, text=latitude.append(i), width=20)
        entry_label2.place(x=1120, y=440 + i * 20)
        entry2Remove.append(entry_label2)
    stats_label = tk.Label(my_canvas, text = "Drone is on base Station.", font = ("arial",10,"bold"),bg ="black",fg="white")
    stats_label.place(x=260, y =700 )
    stats_label = tk.Label(my_canvas, text="Enter longitude and latitude to go to " +str(locations) + " locations.", font=("arial", 10, "bold"), bg="black",
                           fg="white")
    stats_label.place(x=250, y=720)
    submit_btn = tk.Button(my_canvas, text='Go to locations (L) above', command = valueGET)
    submit_btn.place(x= 1050 , y = 440 + locations * 20)

'''Getting users longitude and latitude'''
def valueGET():
    x = []
    y = []
    a =[]
    for(a,b) in zip(entry1Remove,entry2Remove):
        x = a.get()
        y = b.get()
        userInput = tk.Label(root,text = x+"," + y, font=("arial",10,"bold"),bg="black", fg="white").place(x=580,y=720)
        
        
def currentStatus(locations):
    global remove1,remove2,remove3,remove4,remove5,remove6,remove7,remove8,remove9,remove10
    remove1 = []
    remove2 = []
    remove3 = []
    remove4 = []
    remove5 = []
    remove6 = []
    remove7 = []
    remove8 = []
    remove9 = []
    remove10 = []
    '''Live check up'''
    if locations == 1:
        base1_1 = tk.Checkbutton(my_canvas, text="Base")
        base1_1.place(x=20, y=460)
        base1_2 = tk.Checkbutton(my_canvas, text="Location 1")
        base1_2.place(x=80, y=460)
        base1_3 = tk.Checkbutton(my_canvas, text="Returned to base")
        base1_3.place(x=180, y=460)
        remove1.extend((base1_1,base1_2,base1_3))
    elif locations == 2:
        base2_1 = tk.Checkbutton(my_canvas, text="Base")
        base2_1.place(x=20, y=460)
        base2_2 = tk.Checkbutton(my_canvas, text="Location 1")
        base2_2.place(x=80, y=460)
        base2_3 = tk.Checkbutton(my_canvas, text="Location 2")
        base2_3.place(x=180, y=460)
        base2_4 = tk.Checkbutton(my_canvas, text="Returned to base")
        base2_4.place(x=280, y=460)
        remove2.extend((base2_1, base2_2, base2_3,base2_4))
    elif locations == 3:
        base3_1 = tk.Checkbutton(my_canvas, text="Base")
        base3_1.place(x=20, y=460)
        base3_2 = tk.Checkbutton(my_canvas, text="Location 1")
        base3_2.place(x=80, y=460)
        base3_3 = tk.Checkbutton(my_canvas, text="Location 2")
        base3_3.place(x=180, y=460)
        base3_4 = tk.Checkbutton(my_canvas, text="Location 3")
        base3_4.place(x=280, y=460)
        base3_5 = tk.Checkbutton(my_canvas, text="Returned to base")
        base3_5.place(x=380, y=460)
        remove3.extend((base3_1, base3_2, base3_3,base3_4,base3_5))
    elif locations == 4:
        base4_1 = tk.Checkbutton(my_canvas, text="Base")
        base4_1.place(x=20, y=460)
        base4_2 = tk.Checkbutton(my_canvas, text="Location 1")
        base4_2.place(x=80, y=460)
        base4_3 = tk.Checkbutton(my_canvas, text="Location 2")
        base4_3.place(x=180, y=460)
        base4_4 = tk.Checkbutton(my_canvas, text="Location 3")
        base4_4.place(x=280, y=460)
        base4_5 = tk.Checkbutton(my_canvas, text="Location 4")
        base4_5.place(x=380, y=460)
        base4_6 = tk.Checkbutton(my_canvas, text="Returned to base")
        base4_6.place(x=480, y=460)
        remove4.extend((base4_1, base4_2, base4_3, base4_4, base4_5,base4_6))
    elif locations == 5:
        base5_1 = tk.Checkbutton(my_canvas, text="Base")
        base5_1.place(x=20, y=460)
        base5_2 = tk.Checkbutton(my_canvas, text="Location 1")
        base5_2.place(x=80, y=460)
        base5_3 = tk.Checkbutton(my_canvas, text="Location 2")
        base5_3.place(x=180, y=460)
        base5_4 = tk.Checkbutton(my_canvas, text="Location 3")
        base5_4.place(x=280, y=460)
        base5_5 = tk.Checkbutton(my_canvas, text="Location 4")
        base5_5.place(x=380, y=460)
        base5_6 = tk.Checkbutton(my_canvas, text="Location 5")
        base5_6.place(x=480, y=460)
        base5_7 = tk.Checkbutton(my_canvas, text="Returned to base")
        base5_7.place(x=580, y=460)
        remove5.extend((base5_1, base5_2, base5_3, base5_4, base5_5, base5_6,base5_7))
    elif locations == 6:
        base6_1 = tk.Checkbutton(my_canvas, text="Base")
        base6_1.place(x=20, y=460)
        base6_2 = tk.Checkbutton(my_canvas, text="Location 1")
        base6_2.place(x=80, y=460)
        base6_3 = tk.Checkbutton(my_canvas, text="Location 2")
        base6_3.place(x=180, y=460)
        base6_4 = tk.Checkbutton(my_canvas, text="Location 3")
        base6_4.place(x=280, y=460)
        base6_5 = tk.Checkbutton(my_canvas, text="Location 4")
        base6_5.place(x=380, y=460)
        base6_6 = tk.Checkbutton(my_canvas, text="Location 5")
        base6_6.place(x=480, y=460)
        base6_7 = tk.Checkbutton(my_canvas, text="Location 6")
        base6_7.place(x=480, y=460)
        base6_8 = tk.Checkbutton(my_canvas, text="Returned to base")
        base6_8.place(x=20, y=490)
        remove6.extend((base6_1, base6_2, base6_3, base6_4, base6_5, base6_6, base6_7,base6_8))
    elif locations == 7:
        base7_1 = tk.Checkbutton(my_canvas, text="Base")
        base7_1.place(x=20, y=460)
        base7_2 = tk.Checkbutton(my_canvas, text="Location 1")
        base7_2.place(x=80, y=460)
        base7_3 = tk.Checkbutton(my_canvas, text="Location 2")
        base7_3.place(x=180, y=460)
        base7_4 = tk.Checkbutton(my_canvas, text="Location 3")
        base7_4.place(x=280, y=460)
        base7_5 = tk.Checkbutton(my_canvas, text="Location 4")
        base7_5.place(x=380, y=460)
        base7_6 = tk.Checkbutton(my_canvas, text="Location 5")
        base7_6.place(x=480, y=460)
        base7_7 = tk.Checkbutton(my_canvas, text="Location 6")
        base7_7.place(x=480, y=460)
        base7_8 = tk.Checkbutton(my_canvas, text="Location 7")
        base7_8.place(x=20, y=490)
        base7_9 = tk.Checkbutton(my_canvas, text="Returned to base")
        base7_9.place(x=110, y=490)
        remove7.extend((base7_1, base7_2, base7_3, base7_4, base7_5, base7_6, base7_7,base7_8,base7_9))
    elif locations == 8:
        base8_1 = tk.Checkbutton(my_canvas, text="Base")
        base8_1.place(x=20, y=460)
        base8_2 = tk.Checkbutton(my_canvas, text="Location 1")
        base8_2.place(x=80, y=460)
        base8_3 = tk.Checkbutton(my_canvas, text="Location 2")
        base8_3.place(x=180, y=460)
        base8_4 = tk.Checkbutton(my_canvas, text="Location 3")
        base8_4.place(x=280, y=460)
        base8_5 = tk.Checkbutton(my_canvas, text="Location 4")
        base8_5.place(x=380, y=460)
        base8_6 = tk.Checkbutton(my_canvas, text="Location 5")
        base8_6.place(x=480, y=460)
        base8_7 = tk.Checkbutton(my_canvas, text="Location 6")
        base8_7.place(x=480, y=460)
        base8_8 = tk.Checkbutton(my_canvas, text="Location 7")
        base8_8.place(x=20, y=490)
        base8_9 = tk.Checkbutton(my_canvas, text="Location 8")
        base8_9.place(x=110, y=490)
        base8_10 = tk.Checkbutton(my_canvas, text="Returned to base")
        base8_10.place(x=210, y=490)
        remove8.extend((base8_1, base8_2, base8_3, base8_4, base8_5, base8_6, base8_7, base8_8, base8_9,base8_10))
    elif locations == 9:
        base9_1 = tk.Checkbutton(my_canvas, text="Base")
        base9_1.place(x=20, y=460)
        base9_2 = tk.Checkbutton(my_canvas, text="Location 1")
        base9_2.place(x=80, y=460)
        base9_3 = tk.Checkbutton(my_canvas, text="Location 2")
        base9_3.place(x=180, y=460)
        base9_4 = tk.Checkbutton(my_canvas, text="Location 3")
        base9_4.place(x=280, y=460)
        base9_5 = tk.Checkbutton(my_canvas, text="Location 4")
        base9_5.place(x=380, y=460)
        base9_6 = tk.Checkbutton(my_canvas, text="Location 5")
        base9_6.place(x=480, y=460)
        base9_7 = tk.Checkbutton(my_canvas, text="Location 6")
        base9_7.place(x=480, y=460)
        base9_8 = tk.Checkbutton(my_canvas, text="Location 7")
        base9_8.place(x=20, y=490)
        base9_9 = tk.Checkbutton(my_canvas, text="Location 8")
        base9_9.place(x=110, y=490)
        base9_10 = tk.Checkbutton(my_canvas, text="Location 9")
        base9_10.place(x=210, y=490)
        base9_11 = tk.Checkbutton(my_canvas, text="Returned to base")
        base9_11.place(x=310, y=490)
        remove9.extend((base9_1, base9_2, base9_3, base9_4, base9_5, base9_6, base9_7, base9_8, base9_9,base9_10,base9_11))

    elif locations == 10:
        base10_1 = tk.Checkbutton(my_canvas, text="Base")
        base10_1.place(x=20, y=460)
        base10_2 = tk.Checkbutton(my_canvas, text="Location 1")
        base10_2.place(x=80, y=460)
        base10_3 = tk.Checkbutton(my_canvas, text="Location 2")
        base10_3.place(x=180, y=460)
        base10_4 = tk.Checkbutton(my_canvas, text="Location 3")
        base10_4.place(x=280, y=460)
        base10_5 = tk.Checkbutton(my_canvas, text="Location 4")
        base10_5.place(x=380, y=460)
        base10_6 = tk.Checkbutton(my_canvas, text="Location 5")
        base10_6.place(x=480, y=460)
        base10_7 = tk.Checkbutton(my_canvas, text="Location 6")
        base10_7.place(x=480, y=460)
        base10_8 = tk.Checkbutton(my_canvas, text="Location 7")
        base10_8.place(x=20, y=490)
        base10_9 = tk.Checkbutton(my_canvas, text="Location 8")
        base10_9.place(x=110, y=490)
        base10_10 = tk.Checkbutton(my_canvas, text="Location 9")
        base10_10.place(x=210, y=490)
        base10_11 = tk.Checkbutton(my_canvas, text="Location 10")
        base10_11.place(x=310, y=490)
        base10_12 = tk.Checkbutton(my_canvas, text="Returned to base")
        base10_12.place(x=410, y=490)
        remove9.extend((base10_1, base10_2, base10_3, base10_4, base10_5, base10_6, base10_7, base10_8, base10_9,base10_10,base10_11,base10_12))

'''Validating user input'''
def correct(input):
    if(input.isdigit()):
        return True
    elif input is "":
        return True
    else:
        return False
'''User Input text Entry'''
input1 = tk.IntVar()
user_input = tk.Entry(root,textvariable=input1, width =6)
user_input.place(x =1020,y=410)
def reset():
    for i in remove1:
        i.destroy()
    for i in remove2:
        i.destroy()
    for i in remove3:
        i.destroy()
    for i in remove4:
        i.destroy()
    for i in remove5:
        i.destroy()
    for i in remove6:
        i.destroy()
    for i in remove7:
        i.destroy()
    for i in remove8:
        i.destroy()
    for i in remove9:
        i.destroy()
    for i in remove10:
        i.destroy()
    for i in entry1Remove:
        i.destroy()
    for i in entry2Remove:
        i.destroy()
    for i in removeLabel:
        i.destroy()
    for i in range(locations):
        submit_btn.destroy()
        stats_label.destroy()
        for i in range(locations):
            oval_label = 'label' + str(i)
            location_label = 'label' + str(i)
            cur1_label = tk.Label(my_canvas, text="L" + str(i + 1), font=("arial", 6, "bold"), bg="black",
                                 fg="black")
            cur1_label.place(x=1440 - i * 70, y=70)
            oval_label = my_canvas.create_oval(1450 - i * 70, 110, 1430 - i * 70, 100, width=0, fill='black')
            my_canvas.create_rectangle(20, 450, 700,650 , width=0, fill='black')
        i = i - 1

def readFromFile():
    file = open("test.txt", "r")
    read = file.readline()
    Scores = tk.Label(root,text = read, font=("arial",10,"bold"),bg="black", fg="white").place(x=70,y=370)

'''readFromFile()'''
def readImage():
    photo = tk.PhotoImage(file ='Picture.png')
    photo.one =photo
    my_canvas.create_image(20,25,image=photo,anchor = tk.NW)

'''readImage()'''
'''Validating user input'''
reg = my_canvas.register(correct)
user_input.config(validate ="key",validatecommand =(reg,'%P'))
'''User locations go button'''
userButton = tk.Button(root,text="Submit",fg="Black",command= userInput).place(x=1065,y=410, width =40, height =20)
btn_reset = tk.Button(root,text="Reset",fg="Black", command = reset )
btn_reset.place(x=1120, y=410, width =40, height =20)
root.mainloop()
