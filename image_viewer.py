from tkinter import*
import glob

#define the root
root=Tk()
root.title="image viewer"

#getting list of images in the folder
images=glob.glob("images\*.png")

#current image index
index = 0

#display first image
img=images[0]
image=PhotoImage(file=img)
label=Label(root,image=image)
label.grid(row=0,column=0,columnspan=3)

#define commands
def for_ward():
    global index
    global image
    global label

    # increment the image index
    index += 1

    # check if the image index is within the bounds of the list of images
    if index < len(images):
        # display the next image
        backward.config(state=ACTIVE)
        img = images[index]
        image = PhotoImage(file=img)
        label.grid_forget()
        label = Label(root,image=image)
        label.grid(row=0,column=0,columnspan=3)
    else:
        # disable the next button
        forward.config(state=DISABLED)

def back_ward():
    global index
    global image
    global label

    # decrement the image index
    index -= 1

    # check if the image index is within the bounds of the list of images
    if index >= 0:
        # display the previous image
        forward.config(state=ACTIVE)
        img = images[index]
        image = PhotoImage(file=img)
        label.grid_forget()
        label = Label(root,image=image)
        label.grid(row=0,column=0,columnspan=3)
    else:
        # disable the back button
        backward.config(state=DISABLED)

#define buttons
forward=Button(root,text=">>",command=for_ward)
Exit=Button(root,text="Exit",command=root.quit)
backward=Button(root,text="<<",command=back_ward,state=DISABLED)

#display Buttons
forward.grid(row=1,column=2)
Exit.grid(row=1,column=1)
backward.grid(row=1,column=0)

#run root
root.mainloop()