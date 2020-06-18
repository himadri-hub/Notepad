from tkinter import*
from tkinter import ttk, font

from tkinter.filedialog import askopenfile #to open any file
from tkinter.filedialog import asksaveasfile  # to save any file
import tkinter.messagebox
from tkinter import messagebox
from datetime import datetime


root= Tk()
root.title("Notepad")

root.geometry("1370x600")
root.configure(background= "black")

photo = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\notepad.PNG")
root.iconphoto(False, photo)


#------------------------------------------------------------Frames--------------------------------------------------------------------------
menubar = Menu()


status_frame = Frame(root, bd=1, relief=RAISED)
status_frame.pack(side=TOP, fill=X)
##
text_frame = Frame(root, bd= 10, relief= RIDGE)
text_frame.pack(side= TOP)
##
###--------------------------------------Importing icons----------------------------------------------
##
###--------------------------------------Importing  File icons----------------------------------------------
##
new_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\new.PNG")
new_icon_resize = new_icon.subsample(4, 4)

open_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\open.PNG")
open_icon_resize = open_icon.subsample(10,10)

save_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\save.PNG")
save_icon_resize = save_icon.subsample(10, 10)

exit_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\exit.PNG")
exit_icon_resize = exit_icon.subsample(4, 4)
#-----------------------------------------------------Function for File menu--------------------------------------------------------------------
def to_make_new():
    txt_display.delete("1.0", END)
    
def to_open():
    
    path = askopenfile(mode ='r')
    if path is not None: 
        content = path.read()
        txt_display.delete("1.0", END)
        txt_display.insert(END, content)
        
##    with open("file.txt") as file:
##        txt_display.delete("1.0", END)
##        txt_display.insert(END, file.read())
        
def to_save():
    file_content= txt_display.get("1.0", END)
    print(file_content)
    path = asksaveasfile(mode = 'w', defaultextension ='.txt')
    path.write(file_content)
    
def to_exit():
    iExit= tkinter.messagebox.askyesno("Notepad", "Please confirm if you wish to exit")
    if iExit > 0:
        root.destroy()  


filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", image = new_icon_resize, compound= LEFT, accelerator = 'Ctrl+N',command = to_make_new)
filemenu.add_command(label="Open", image = open_icon_resize, compound= LEFT, accelerator = 'Ctrl+O', command=to_open)
filemenu.add_command(label="Save", image= save_icon_resize, compound= LEFT, accelerator = 'Ctrl+S', command= to_save)
filemenu.add_command(label="Exit", image= exit_icon_resize, compound= LEFT,command=to_exit)

menubar.add_cascade(label="File", menu=filemenu)



#--------------------------------------------------Edit Function------------------------------------------------------------------------
def to_undo():
    txt_display.event_generate("<<Undo>>")
    
def to_cut():    
    txt_display.event_generate("<<Cut>>")
    
def to_copy():
    txt_display.event_generate("<<Copy>>")
    
def to_paste():
    txt_display.event_generate("<<Paste>>")
    
def to_delete():
    txt_display.delete("1.0", END)

def to_find():

    find_word= StringVar()
    
    def find_me():
        
        #remove tag 'found' from index 1 to END 
        txt_display.tag_remove('found', '1.0', END)  # To remove previosely serached word
          
        #returns to widget currently in focus 
        word = find_word.get()  
        if word: 
            index = '1.0'
            while 1: 
                #searches for desried string from index 1 
                index = txt_display.search(word, index, nocase=1, stopindex=END)  
                if not index:
                    break
                  
                #last index sum of current index and 
                #length of text 
                lastidx = '%s+%dc' % (index, len(word))  
                  
                #overwrite 'Found' at idx 
                txt_display.tag_add('found', index, lastidx)  
                index = lastidx 
              
            #mark located string as red 
            txt_display.tag_config('found', foreground='red', background= "yellow")
    
    find_dailogue= Toplevel()
    find_dailogue.title("Find")

    lblsearch= Label(find_dailogue, font=("arial", 14, "bold"), text= "find: ", bd=7)
    lblsearch.grid(row=0, column=0, sticky=W)


    txtsearch= Entry(find_dailogue, textvariable=find_word, justify= RIGHT)
    txtsearch.grid(row=0, column=1)

    btnfind= Button(find_dailogue, font= ("arial", 14, "bold"), text= "Find", command= find_me)
    btnfind.grid(row=0, column=2)

    find_dailogue.mainloop()

def to_replace():
    find_word = StringVar()
    replace_word = StringVar()

    def find_me():
        txt_display.tag_remove('found', '1.0', END)  # To remove previosely serached word
          
        #returns to widget currently in focus 
        word = find_word.get()  
        if word: 
            index = '1.0'
            while 1: 
                #searches for desried string from index 1 
                index = txt_display.search(word, index, nocase=1, stopindex=END)  
                if not index:
                    break
                  
                #last index sum of current index and 
                #length of text 
                lastidx = '%s+%dc' % (index, len(word))  
                  
                #overwrite 'Found' at idx 
                txt_display.tag_add('found', index, lastidx)  
                index = lastidx 
              
            #mark located string as red 
            txt_display.tag_config('found', foreground='red', background= "yellow")
    def replace_me():
        word_find = find_word.get()
        word_replace = replace_word.get()
        
        notepad_content= txt_display.get(1.0, END)
        
        new_content_notepad= notepad_content.replace(word_find, word_replace)

        txt_display.delete("1.0", "end")   #Deletes previous data
        txt_display.insert(END, new_content_notepad)

        


    find_dailogue= Toplevel()
    find_dailogue.title("Find")
    

    lblsearch= Label(find_dailogue, font=("arial", 10, "bold"), text= "find word: ", bd=7)
    lblsearch.grid(row=0, column=0, sticky=W)

    lblreplace= Label(find_dailogue, font=("arial", 10, "bold"), text= "Replace with: ", bd=7)
    lblreplace.grid(row=1, column=0, sticky=W)


    txtsearch= Entry(find_dailogue, textvariable=find_word, justify= RIGHT)
    txtsearch.grid(row=0, column=1)

    btnfind= Button(find_dailogue, font= ("arial", 10, "bold"), text= "Find", command= find_me)
    btnfind.grid(row=2, column=0)

    txtreplace= Entry(find_dailogue, textvariable=replace_word, justify= RIGHT)
    txtreplace.grid(row=1, column=1)
        
    btnreplace= Button(find_dailogue, font= ("arial", 10, "bold"), text= "Replace", command= replace_me)
    btnreplace.grid(row=2, column=1)
#--------------------------------------Importing edit icons----------------------------------------------
undo_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\undo.PNG")
undo_icon_resize = undo_icon.subsample(4, 4)

cut_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\cut.PNG")
cut_icon_resize = cut_icon.subsample(10, 10)

copy_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\copy.PNG")
copy_icon_resize = copy_icon.subsample(10, 10)

paste_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\paste.PNG")
paste_icon_resize = paste_icon.subsample(10, 10)


delete_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\delete.PNG")
delete_icon_resize = delete_icon.subsample(10, 10)

find_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\find.PNG")
find_icon_resize = find_icon.subsample(10, 10)

replace_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\replace.PNG")
replace_icon_resize = replace_icon.subsample(8, 8)

editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label="Undo", image = undo_icon_resize, compound= LEFT, accelerator = 'Ctrl+Z',command=to_undo)
editmenu.add_command(label="Cut", image = cut_icon_resize, compound= LEFT, accelerator = 'Ctrl+X',command=to_cut)
editmenu.add_command(label="Copy", image= copy_icon_resize, compound= LEFT, accelerator = 'Ctrl+C',command=to_copy)
editmenu.add_command(label="Paste", image = paste_icon_resize, compound= LEFT, accelerator = 'Ctrl+V',command=to_paste)
editmenu.add_command(label="Delete", image= delete_icon_resize, compound= LEFT,command=to_delete)
editmenu.add_command(label="Find", image = find_icon_resize, compound= LEFT, accelerator = 'Ctrl+F',command=to_find)
editmenu.add_command(label="Replace", image= replace_icon_resize, compound= LEFT,command=to_replace)

menubar.add_cascade(label="Edit", menu=editmenu)

#--------------------------------------Importing view icons----------------------------------------------


zoom_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\zoom.PNG")
zoom_icon_resize = zoom_icon.subsample(8, 8)

viewmenu = Menu(menubar, tearoff=0)

viewmenu.add_command(label="Zoom", image = zoom_icon_resize, compound= LEFT)
menubar.add_cascade(label="View", menu=viewmenu)
###--------------------------------------------New Frame for Style------------------------------------------------------------------------------------------------------
##
###----------------------------------------------------function fr style----------------------------------------------------------------------


def to_bold():
    combo_box_textsize_var = combo_box_textsize.get()
    text_original_property= font.Font(font= txt_display["font"])
    print(text_original_property.actual())
    if (text_original_property.actual()["weight"]== "normal"):
        txt_display.configure(font=("Times New Roman", combo_box_textsize_var, "bold"))
    else:
        txt_display.configure(font=("Times New Roman", 12, "normal"))
        
   # print(text_original_property)
def to_italics():
    combo_box_textsize_var = combo_box_textsize.get()
    text_original_property= font.Font(font= txt_display["font"])
    if (text_original_property.actual()["slant"]== "roman"):
        txt_display.configure(font=("Times New Roman", combo_box_textsize_var, "italic"))
    else:
        txt_display.configure(font=("Times New Roman", 12, "normal"))
def to_underlined():
    combo_box_textsize_var = combo_box_textsize.get()
    text_original_property= font.Font(font= txt_display["font"])
    print(text_original_property.actual())
    if (text_original_property.actual()["underline"]== 0):
        txt_display.configure(font=("Times New Roman", combo_box_textsize_var, "underline"))
    else:
        txt_display.configure(font=("Times New Roman", 12, "normal"))
def text_family(self):
    combo_box_textsize_var = combo_box_textsize.get()
    combo_box_textname_var = combo_box_textname.get()
    txt_display.configure(font=(combo_box_textname_var, combo_box_textsize_var))
def text_size(self):
    print("For size")
    combo_box_textsize_var = combo_box_textsize.get()
    print(combo_box_textsize_var)
    txt_display.configure(font=("Times New Roman", combo_box_textsize_var))
    
def to_rytalign():
    file_content= txt_display.get("1.0", END)
    txt_display.delete("1.0", END)
    txt_display.tag_configure("right", justify='right')
    txt_display.insert("1.0", file_content)
    txt_display.tag_add("right", "1.0", "end")

def to_leftalign():
    file_content= txt_display.get("1.0", END)
    txt_display.delete("1.0", END)
    txt_display.tag_configure("left", justify='left')
    txt_display.insert("1.0", file_content)
    txt_display.tag_add("left", "1.0", "end")
    
def to_centeralign():
    file_content= txt_display.get("1.0", END)
    txt_display.delete("1.0", END)
    txt_display.tag_configure("center", justify='center')
    txt_display.insert("1.0", file_content)
    txt_display.tag_add("center", "1.0", "end")
    
def background_color(self):
    text_color= combo_box_bg.get()
    txt_display.configure(bg= text_color)
        
def foreground_color(self):
    textfg_color = combo_box_fg.get()
    txt_display.configure(fg= textfg_color)

#--------------------------------------Importing writing style icons----------------------------------------------



bold_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\bold.PNG")
bold_icon_resize = bold_icon.subsample(15, 15)

italics_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\italics.PNG")
italics_icon_resize = italics_icon.subsample(14, 14)

underlined_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\underlined.PNG")
underlined_icon_resize = underlined_icon.subsample(15, 15)

text_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\text.PNG")
text_icon_resize = text_icon.subsample(15, 15)


rightalign_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\right align.PNG")
rightalign_icon_resize = rightalign_icon.subsample(15, 15)

leftalign_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\left alignment.PNG")
leftalign_icon_resize = leftalign_icon.subsample(15, 15)

centeralign_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\center align.PNG")
centeralign_icon_resize = centeralign_icon.subsample(15, 15)

bgcolor_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\background colour.PNG")
bgcolor_icon_resize = bgcolor_icon.subsample(15, 15)

fgcolor_icon = PhotoImage(file = r"F:\udemy_python\tkinter\note_pad\icons\foreground color.PNG")
fgcolor_icon_resize = fgcolor_icon.subsample(10, 10)

#-------------------------------------------------btns for style-------------------------------------------------------------

btnbold= Button(status_frame, font= ("arial", 10, "bold"), image = bold_icon_resize, command= to_bold)
btnbold.grid(row=0, column=2)

btnitalics= Button(status_frame, font= ("arial", 10, "bold"), image = italics_icon_resize,  command= to_italics)
btnitalics.grid(row=0, column=3)

btnunderlined= Button(status_frame, font= ("arial", 10, "bold"), image = underlined_icon_resize, command= to_underlined)
btnunderlined.grid(row=0, column=4)

btnryt_align= Button(status_frame, font= ("arial", 10, "bold"), image = rightalign_icon_resize,  command= to_rytalign)
btnryt_align.grid(row=0, column=5)

btnleft_align= Button(status_frame, font= ("arial", 10, "bold"), image = leftalign_icon_resize, command= to_leftalign)
btnleft_align.grid(row=0, column=6)

btncentr_align= Button(status_frame, font= ("arial", 10, "bold"), image = centeralign_icon_resize,  command= to_centeralign)
btncentr_align.grid(row=0, column=7)

##btnbg_color= Button(status_frame, font= ("arial", 10, "bold"), image = bgcolor_icon_resize, command= to_bgcolor)
##btnbg_color.grid(row=0, column=8)
##
##btnfg_color= Button(status_frame, font= ("arial", 10, "bold"), image = fgcolor_icon_resize, command= to_fgcolor)
##btnfg_color.grid(row=0, column=9)


#-------------------------------------------------------------------------combo box------------------------------------------------------------------------

combo_box_textname = StringVar()
all_font_name= font.families()

Combo_Text_name_list= ttk.Combobox(status_frame, textvariable= combo_box_textname, state= "readonly", font= ("arial", 10, "bold"), width= 10)
Combo_Text_name_list["value"]= all_font_name
Combo_Text_name_list.current(0)
Combo_Text_name_list.grid(row=0, column=0)
Combo_Text_name_list.bind("<<ComboboxSelected>>", text_family)


combo_box_textsize = StringVar()
all_font_size= tuple(range(5, 80, 5)) # font size from 8  to 72

combo_box_textsize_list= ttk.Combobox(status_frame, textvariable= combo_box_textsize, state= "readonly", font= ("arial", 10, "bold"), width= 4)
combo_box_textsize_list["value"]= all_font_size
combo_box_textsize_list.current(1)
combo_box_textsize_list.grid(row=0, column=1)
combo_box_textsize_list.bind("<<ComboboxSelected>>", text_size)

combo_box_bg = StringVar()
bg_colour= ("Select background colour", "Black", "Red", "Green", "Grey", "Light Blue", "Light Green", "White")

Combo_bg_colour= ttk.Combobox(status_frame, textvariable= combo_box_bg, state= "readonly", font= ("arial", 10, "bold"), width= 25)
Combo_bg_colour["value"]= bg_colour
Combo_bg_colour.current(0)
Combo_bg_colour.grid(row=0, column=8)
Combo_bg_colour.bind("<<ComboboxSelected>>", background_color)


combo_box_fg = StringVar()
fg_colour= ("Select Forground colour","Black", "Red", "Green", "Grey", "Light Blue", "Light Green", "White")

combo_fg_colour= ttk.Combobox(status_frame, textvariable= combo_box_fg, state= "readonly", font= ("arial", 10, "bold"), width= 25)
combo_fg_colour["value"]= fg_colour
combo_fg_colour.current(0)
combo_fg_colour.grid(row=0, column=9)
combo_fg_colour.bind("<<ComboboxSelected>>", foreground_color)
###-------------------------------------------------Text Editor---------------------------------------------------------------------
##
txt_display= Text(text_frame, width=168, height= 39,  wrap= WORD, undo= True)
txt_display.grid(row=0, column=0)


scrollbar = Scrollbar(text_frame)
scrollbar.grid(row=0, column=0, sticky=N+S+E)
txt_display.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command = txt_display.yview )


#---------------------------------------------------------------------------------------------------------------------------------------


root.config(menu=menubar)

root.mainloop()
