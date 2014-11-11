# __     ____   __
# \ \   / /\ \ / /
#  \ \ / /  \ V / 
#   \ V /    | |  
#    \_/     |_|  
#                 

What is vy? 
It is an attempt of mine(Tau a.k.a Iury) to implement a vim-like editor in python.
I feel as i'm close to this goal since i have been using vy for all kind of tasks 
that i used vim in the past.

Why would one implement a vim-like in python? 
Well, python is such a powerful language, i used vim for years when i noticed vimscript wasn't
really cool and i couldn't use vim python plugin api in the way i would like.

Does vy mimic vim?
No, it is slightly similar, it has a standard mode, an insert mode and
some of the key-commands perform similar operations in vy and vim.

Vy supports an interesting feature, it is the capacity of talking to external processes
It is all thanks to untwisted although it could be done with any other library that supports a reactor
with a update function. The main idea behind to talking to external processes is the concept of e-scripts.

E-scripts are an interesting way of programming repeatitive tasks. The first time i had contact
with this abstraction was with one of my university teachers. It is worth reading about. He has
implemented eev that is a set of emacs keys to perform cool tasks as well as send stuff to external
processes. Consequently it turns easy the task of creating e-scripts to automatize repetitive tasks.

You can read more about e-scripts and eev in.

http://angg.twu.net/eev-intros/

The person who implemented eev implements e-scripts in a nice way, you can go
through some of the examples and learn a bit of how implementing e-scripts.

#  __  __  ___  ____  _____   ______   ______ _____ _____ __  __ 
# |  \/  |/ _ \|  _ \| ____| / ___\ \ / / ___|_   _| ____|  \/  |
# | |\/| | | | | | | |  _|   \___ \\ V /\___ \ | | |  _| | |\/| |
# | |  | | |_| | |_| | |___   ___) || |  ___) || | | |___| |  | |
# |_|  |_|\___/|____/|_____| |____/ |_| |____/ |_| |_____|_|  |_|
#                                                                


Vy is similar to vim in the sense that it has a mode system. 
There are some keys that change the way of how vy understands the pressing
of keys. Vy permits an infinite set of modes.

The best way to understand modes is through a simple example.

Press Escape -> STANDARD MODE -> Press i -> INSERT MODE

It basically is: When you press Escape it gets in STANDARD MODE
from this mode, if you press i then it gets in INSERT MODE.

The INSERT MODE tells vy that whatever key you press it should echo
over the text area. So, whenever you are in INSERT MODE if you type
a printable key it will echo over the text area.

The best way to understand that is through a simple test.

1) Run vy.
2) Press Escape
3) Press i
4) Press any key that corresponds to a printable character.

You will notice the characters echoing over the text area that has focus. It is not a lot of fun but it is a start. 

After you get bored of telling vy to print characters over the text area you can try going
back to the STANDARD MODE. 

How could you do so? Well, when you press Escape
in insert mode it tells vy to go to STANDARD MODE.

So, in a simpler manner you have.

Press Escape -> Press i -> INSERT MODE -> Press Escape -> STANDARD MODE

Try it out !


Now, you are done to play with what you have written over INSERT MODE.
The first thing you will learn is how to move the cursor. Since everything in vy
depends on you moving the cursor around.

The keys h, j, k, l in STANDARD MODE tells vy to move the cursor around.

After you got used to these keys you can start reading the session of the STANDARD MODE.
You will be able to execute all basic operations after reading this session. Things like
copying text, pasting, inserting line, searching stuff etc.


#  ____ _____  _    _   _ ____    _    ____  ____    __  __  ___  ____  _____ 
# / ___|_   _|/ \  | \ | |  _ \  / \  |  _ \|  _ \  |  \/  |/ _ \|  _ \| ____|
# \___ \ | | / _ \ |  \| | | | |/ _ \ | |_) | | | | | |\/| | | | | | | |  _|  
#  ___) || |/ ___ \| |\  | |_| / ___ \|  _ <| |_| | | |  | | |_| | |_| | |___ 
# |____/ |_/_/   \_\_| \_|____/_/   \_\_| \_\____/  |_|  |_|\___/|____/|_____|
#                                                                             


#   ____            _             _           _ 
#  / ___|___  _ __ | |_ _ __ ___ | |       __| |
# | |   / _ \| '_ \| __| '__/ _ \| |_____ / _` |
# | |__| (_) | | | | |_| | | (_) | |_____| (_| |
#  \____\___/|_| |_|\__|_|  \___/|_|      \__,_|
#                                               

# Control-d

It opens a file selection window to pick up a file to edit.

Whenever you press Control-d over a text area it will open a file selection window
then after picking up a file it will load the content over the text area.


#  _____ ___  
# |  ___( _ ) 
# | |_  / _ \ 
# |  _|| (_) |
# |_|   \___/ 
#             

It opens a file selection window to pick up a file, after you have picked up a file
it will load the contents of the file in a new tab.


#  _____ _____ 
# |  ___|___  |
# | |_     / / 
# |  _|   / /  
# |_|    /_/   
#              

It creates a new tab area. 


#   ____            _             _           
#  / ___|___  _ __ | |_ _ __ ___ | |      ___ 
# | |   / _ \| '_ \| __| '__/ _ \| |_____/ __|
# | |__| (_) | | | | |_| | | (_) | |_____\__ \
#  \____\___/|_| |_|\__|_|  \___/|_|     |___/
#                                             

It saves the contents in the opened file.

#  ____  _     _  __ _            
# / ___|| |__ (_)/ _| |_      ___ 
# \___ \| '_ \| | |_| __|____/ __|
#  ___) | | | | |  _| ||_____\__ \
# |____/|_| |_|_|_|  \__|    |___/
#                                 


It opens a file selection window to save the text area contents with
in a given path. 

#  _  __                ____  
# | |/ /___ _   _      |  _ \ 
# | ' // _ \ | | |_____| | | |
# | . \  __/ |_| |_____| |_| |
# |_|\_\___|\__, |     |____/ 
#           |___/             

It clears all text in the text area.

#   ____            _             _       _____                          
#  / ___|___  _ __ | |_ _ __ ___ | |     | ____|___  ___ __ _ _ __   ___ 
# | |   / _ \| '_ \| __| '__/ _ \| |_____|  _| / __|/ __/ _` | '_ \ / _ \
# | |__| (_) | | | | |_| | | (_) | |_____| |___\__ \ (_| (_| | |_) |  __/
#  \____\___/|_| |_|\__|_|  \___/|_|     |_____|___/\___\__,_| .__/ \___|
#                                                            |_|         

It saves the content of the text area then quits.

#  ____  _     _  __ _        _____                          
# / ___|| |__ (_)/ _| |_     | ____|___  ___ __ _ _ __   ___ 
# \___ \| '_ \| | |_| __|____|  _| / __|/ __/ _` | '_ \ / _ \
#  ___) | | | | |  _| ||_____| |___\__ \ (_| (_| | |_) |  __/
# |____/|_| |_|_|_|  \__|    |_____|___/\___\__,_| .__/ \___|
#                                                |_|         

It quits.

#  _____ _  _   
# |  ___| || |  
# | |_  | || |_ 
# |  _| |__   _|
# |_|      |_|  
#               

It adds a horizontal area.

#  _____ ____  
# |  ___| ___| 
# | |_  |___ \ 
# |  _|  ___) |
# |_|   |____/ 
#              

It adds a vertical area.

#  _____ __   
# |  ___/ /_  
# | |_ | '_ \ 
# |  _|| (_) |
# |_|   \___/ 
#             


It removes the area with focus.

#  _____           _ 
# | ____|_ __   __| |
# |  _| | '_ \ / _` |
# | |___| | | | (_| |
# |_____|_| |_|\__,_|
#                    

It removes the selected tab.


#   __ 
#  / _|
# | |_ 
# |  _|
# |_|  
#      

It adds selection to the cursor line position.


#        
#   __ _ 
#  / _` |
# | (_| |
#  \__, |
#  |___/ 
#       

It removes selection from a char over the cursor. 

#       
# __  __
# \ \/ /
#  >  < 
# /_/\_\
#       

It deletes a line from the cursor position.

#      
#  ____
# |_  /
#  / / 
# /___|
#      

It deletes a character over the cursor position.

#        
#   ___  
#  / _ \ 
# | (_) |
#  \___/ 
#        

It puts the cursor over the start of the line. 

#        
#  _ __  
# | '_ \ 
# | |_) |
# | .__/ 
# |_|    
#

It puts the cursor over the end of the line. 

#  _ 
# / |
# | |
# | |
# |_|
#    

It puts the cursor in the start of the file.


#  ____  
# |___ \ 
#   __) |
#  / __/ 
# |_____|
#        

It puts the cursor in the end of the file.


#        
#  _   _ 
# | | | |
# | |_| |
#  \__, |
#  |___/ 

It copies selected text to the clipboard.


#        
#  _   _ 
# | | | |
# | |_| |
#  \__,_|
#        

It cuts selected text and append it to the clipboard.



#       
#  _ __ 
# | '__|
# | |   
# |_|   
#       

It pastes text from the clipboard one line down the cursor position.

#       
#   ___ 
#  / _ \
# |  __/
#  \___|
#       

It pastes text from the clipboard one line up the cursor position.

#  _   
# | |_ 
# | __|
# | |_ 
#  \__|
#      

It pastes text from the clipboard on the cursor positon.


#        
#  _ __  
# | '_ \ 
# | | | |
# |_| |_|
#        

It inserts one line up the cursor position then goes to INSERT MODE.

#            
#  _ __ ___  
# | '_ ` _ \ 
# | | | | | |
# |_| |_| |_|
#            


It inserts one line down the cursor position then goes to INSERT MODE.

#    
#    
#    
#  _ 
# ( )
# |/ 


It does undo on the text area.

#    
#    
#    
#  _ 
# (_)
#    

It does redo on the text area.



#    
#  _ 
# (_)
#  _ 
# ( )
# |/ 

It pops a insert area where you can type vy python command.

#  __ 
# | _|
# | | 
# | | 
# | | 
# |__|

It selects a word that is on the cursor.


#  _____ _  _   
# |  ___| || |  
# | |_  | || |_ 
# |  _| |__   _|
# |_|      |_|  
#               

It adds another text area vertically.

#  _____ ____  
# |  ___| ___| 
# | |_  |___ \ 
# |  _|  ___) |
# |_|   |____/ 
#              

It adds another text area horizontally.


#  _____ __   
# |  ___/ /_  
# | |_ | '_ \ 
# |  _|| (_) |
# |_|   \___/ 
#             

It removes the text area that has focus.

#  _____ _____ 
# |  ___|___ / 
# | |_    |_ \ 
# |  _|  ___) |
# |_|   |____/ 
#              

It pops an insert area where you can type line.col
then press enter it would jump to the specified line and col
in the text area that has focus.

It accepts just the line too. As in
Press F3 -> Pops the window -> Insert 3 -> Cursor goes to line 3.








