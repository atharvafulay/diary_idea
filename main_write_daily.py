''' 
---------1--------------------------------------------------------------------------------
        1) Let the user write notes, and save notes quickly.
I think this is pretty easy. 
Just have the user enter something. That's all. Save. Then, after the user is done, 
we have to put a timestamp on it (preferably at the top, or if we can create a subject 
/ separate part of the note for just that - maybe a tuple)
---------2--------------------------------------------------------------------------------
        2) Have "back" option for every page.
Just have a back page that just reloads what 
was on the previous page.
---------3--------------------------------------------------------------------------------
        3) Let user access previous notes with ease. Also, have total count of all notes.
This is hard? When they first enter the program, they should have to choose between
'going through old ones', or 'writing a new one'. Then, once they are done, they come 
back to that same page. If they want to leave the app/program, have them enter 'QUIT'. 
---------4--------------------------------------------------------------------------------
        4) Possibly cluster notes by time period.
Yea, idk how to do this. At least not yet. Maybe, have the program look at the dates 
and then just manually look in the past day, day - week, week - month, month - 3 months, 
3 - 6 months, 6month - 1 year, 1year +. 
---------5--------------------------------------------------------------------------------
        5) Prompt questions (above) for user to answer.
Under the 'writing a new one', have an option for prompted questions, in which case, 
they get questions. If not, they can just write. I guess give them the option to not
have the program request it each time.
---------6--------------------------------------------------------------------------------
        6) Have access to time/clock/whatever so user can have a notification at certain 
        times to get prompted to answer questions of just write [Reminder feature]
python.now, use the dates, etc. Look at 1). They should not put in the time. 
It should use (manually, by the program) the python function, android, whatever.
---------7--------------------------------------------------------------------------------
        7) Search feature? Filter feature by date? I guess? 
They can search, but we look for keywords. parse/slice the search and look for that in 
other entries. then, give them the option to choose one, (also show what the text is 
[maybe like 25 chars on each side], and when it was written). open that file. back key 
will get them back to prev. page(s). If they want something specific, have them put 
quotes, create a more intensive search that way.
---------8--------------------------------------------------------------------------------
        8) Save/sync with Google Drive?
no clue
---------9--------------------------------------------------------------------------------
LATER IDEAS: 
Some incentive(s)/badge(s) to keep writing daily, keep the streak going, etc.
Let users favorite/pin notes
Anniversaries for notes - like the first note, fiftth, hundredth note, favorites/pins etc.
'''

# ----------------------------------------------------------------------------------------
from datetime import datetime
import random
import math
import os

# Create a file just for the saved notes: Saved_Notes.
if not os.path.exists('Saved_Notes'):
    os.makedirs('Saved_Notes')

# This function gives us the date and time for the notes. There are 2 main variables. time_now, used returned to wherever called from, and get_date_time, which is for the file naming system as of now.
def get_date_time(): 
    date_time =  datetime.now()

    month = date_time.month
    month = str(month)

    day = date_time.day
    day = str(day)

    year = date_time.year
    year = str(year)
    
    hour = date_time.hour
    am_pm = hour/12
    hour = hour%12
    hour = str(hour)

    num_minute = date_time.minute
    minute = str(num_minute)
    if num_minute < 10: # Makes it more consistent with the numbers
        minute = "0"+minute

    if am_pm == 0: # setup an am/pm system
        get_date_time.date_for_saving = hour + "_" + minute + "_AM_" + month + "-" + day + "-" + year  
        time_now = hour+":"+minute+" AM, "+month+"/"+day+"/"+year
    else:
        get_date_time.date_for_saving = hour + "_" + minute + "_PM_" + month + "-" + day + "-" + year  
        time_now = hour+":"+minute+" PM, "+month+"/"+day+"/"+year
    return time_now

# This function makes the questions. Not really much use now, but might expand on this later.
def question_maker(question_num): 
    questions_prompt = question_bank(question_num)
    return questions_prompt

# This is the question bank. Has all the questions and should be pretty easy to add more questions. It will have some tinkering when we want to add more categories, I believe.
def question_bank(n):
    if n == 1: # general question
        general_question = ["How was your day? Why do you feel that way? What happened?\n","How are you doing? Why do you feel that way? What happened?\n","Hope you're well! What all happened today? Why do you feel that way?\n","How has your day been? Why do you feel that way? What happened?\n","How is your day going? Why do you feel that way? What happened?\n"]
        r_num = random.randint(0,len(general_question)-1)
        return general_question[r_num]
    elif n == 2: # positive, good things
        pos_question = ["What was the most positive event that happened today? Why do you feel that way? What happened?\n","What was the best experience of the day? Why do you feel that way? What happened?\n","What couldn't have gone better today? Why do you feel that way? What happened?\n","What went exactly according to plan? Why do you feel that way? What happened?\n","What is something awesome that happened today? Why do you feel that way? What happened?\n"]
        r_num = random.randint(0,len(pos_question)-1)
        return pos_question[r_num]
    elif n == 3: # bad experiences, things to improve on
        improve_question = ["What didn't go according to plan? Why do you feel that way? What happened?\n","If anything, what went wrong today? Why do you feel that way? What happened?\n","What could have gone better today? Why do you feel that way? What happened?\n","What went poorly today? Why do you feel that way? What happened?\n","What is something you need to improve on? Why do you feel that way? What happened?\n"]
        r_num = random.randint(0,len(improve_question)-1)
        return improve_question[r_num]
    elif n == 4: # something along the best moment of the day
        memorable_question = ["What is a memory that is sticking to your mind? Why do you feel that way? What happened?\n","Which of today's events or experiences was most memorable? Why do you feel that way? What happened?\n","What can't you get out of your head right now? Why do you feel that way? What happened?\n","What unforgettable event or experience happened today? Why do you feel that way? What happened?\n","What is something unique that happened today? Why do you feel that way? What happened?\n"]
        r_num = random.randint(0,len(memorable_question)-1)
        return memorable_question[r_num]
    elif n == 5: # other, things to vent about, emotions to pour out?
        other_question = ["Is there anything else you want to add?\n","Any other comments, things to vent about, emotions to pour out?\n","Any other experiences events you weren't able to write yet?\n","Thinking or pondering about anything else?\n","Anything you didn't get to cover yet?\n"]
        r_num = random.randint(0,len(other_question)-1)
        return other_question[r_num]
    else: return
# ----------------------------------------------------------------------------------------
def new_option():
    y_n = raw_input("Do you want a guided (prompts will appear) note? Select 'yes' or 'no'. If you select 'no', you will be able to freewrite. Type 'exit' to exit the program. Anything other than 'yes', 'no', or 'exit' will send you back to the home page.\n")
    # PROMPTED
    if ('y' or 'yes' or 'YES') in y_n:
        new_note = range(1,11)
        new_note = range(1,11)
        # FOR LOOP is assigns questions and prompts for their answer (one after) in the form of a list
        for i in range(1,6):
            # this is the question.
            new_note[2*i-2] = question_maker(i)
            # this is their answer            
            new_note[2*i-1] = raw_input(new_note[2*i-2])
        new_note.append(get_date_time()) # adds the timestamp to the note.
        time_stamp = new_note[10]
        # PRINT LINE + FOR LOOP: this prints the TIME STAMP + new_note for the user to see.
        print "------------------------------------------------------\nHERE'S THE NOTE YOU JUST CREATED:\n\n\n"+new_note[10]
        for i in range(1,6):
            new_note[i].strip()
            print new_note[(2*i)-2], new_note[(2*i)-1],"\n"
    
        # This is automatically saving whatever the user wrote. It saves the question as well as the answers. 
        get_date_time()
        file_name = "Saved_Notes/"+get_date_time.date_for_saving + ".txt"
        NOTE = open(file_name, "w")
        time_stamp = new_note[10]
        NOTE.write(time_stamp)
        for j in range(1,6): # Saves the file as a text, converting from a list
            NOTE.write(new_note[(2*j)-2] + new_note[(2*j)-1] + "\n")
        NOTE.close()
        print "\nThis note has been saved."        
        home_page()

    # FREE WRITE
    elif('n' or 'no' or 'NO') in y_n:
        new_note = raw_input("Let's write a new note! You can start writing below! You can finish your note by pressing ENTER:\n\n")
        new_note = new_note.strip()
        new_note = get_date_time()+"\n"+new_note # Get the note, strip it of the all the extra spaces, etc. Give it a timestamp. Then, show the user what they just wrote. Maybe have an edit feature, cause right now they can't.
        print "------------------------------------------------------\nHERE'S THE NOTE YOU JUST CREATED:\n\n\n"+new_note
    
        # This is automatically saving whatever the user wrote.
        get_date_time()
        file_name = "Saved_Notes/"+get_date_time.date_for_saving + ".txt"
        NOTE = open(file_name, "w") 
        NOTE.write(new_note)
        NOTE.close()
        
        print "\nThis note has been saved."        
        home_page()
    
    elif('exit') in y_n:
        print "Invalid entry or Program exit command."
        exit()
        
    else:
        print "Invalid entry - returning to home page."
        home_page()
        
def old_option():
        # this prints whichever notes are previously saved in the Saved_Notes folder (see line 55)
        print "Here are some recent notes you\'ve written.\n"
        old_notes = os.listdir("Saved_Notes")

        file_num = -1 # file_num will be our reference number for their old file
        view_want = "no_file" # view_want will be the file name(i.e. '9_18_PM_2-13-2016.txt')
        range_num_notes = len(old_notes)-1 # range_num_notes will be the length of the Saved_Notes - 1 so we can refer to it below
        # FOR LOOP: this prints all the previous notes (up to 30)
        i = 0
        for text in old_notes: # range(0,range_num_notes):
            print text
            i = i+1
            if i >= 30:
                break
            

        # prompts user for which file. For now, they will just type 9_18_PM_2-13-2016.txt
        view_want = raw_input("Type or copy/paste exactly which file you want to look at.\n")

        # FOR LOOP: Searches for the file name from Saved_Notes
        for i in range(0,range_num_notes):
            if view_want in old_notes[i]:
                file_num = i
                break
        if file_num == -1:
            print "Incorrect file name. Please type or copy/paste exactly which file you want to look at."
            old_option()

        # After finding file_num, we use that to print the file that the user is looking for.
        if view_want in old_notes[file_num]:
            old_view = ("Saved_Notes/"+view_want)
            view = open(old_view,'r')
            for line in view:
                print line
        back_or_home = raw_input("Type 'back' to go back to the search file names. Type 'exit' to exit the program. If you type anything else, you will directed to the home page.\n")
        back_or_home = back_or_home.lower()
        if "back" in back_or_home:
            old_option()
        elif "exit" in back_or_home:
            exit()
        else:
            home_page()

def home_page():    
    # opening page/homescreen
    new_or_old = raw_input("Hey there! Would you like to look at 'old' notes or write a 'new' one? Type 'exit' to exit.\n\n")
    new_or_old = new_or_old.lower()
    # NEW
    if 'new' in new_or_old:
        new_option()
        # after they select new, ask if they want a prompted note
    # OLD
    elif 'old' in new_or_old:
        old_option()
    else:
        print "Invalid entry or Program exit command."
        exit()

home_page()