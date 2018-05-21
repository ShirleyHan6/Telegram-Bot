import telepot
import time
from Project_helping_lib_A import welcome_keyboard, project_keyboard,project_add,\
     confirm_add_info_E,confirm_add_info_C,confirm_add_info_R,\
     add_to_database_E,add_to_database_C,add_to_database_R,\
     confirm_info,Count_E_students,Count_C_students,Count_R_students,\
     Browse_datails_E,Browse_datails_C,Browse_datails_R,\
     delete_info_from_E_first,delete_info_from_E_second ,delete_info_from_C_first,delete_info_from_C_second,delete_info_from_R_first,delete_info_from_R_second,\
     news_keyboard, ask_if_news
from Project_helping_lib_C import menu, newstypeFT, newstypeURL, form, projectype, nextfiveras, nextfiveard
from Project_helping_lib_B import electronics, software, hardware, ProjectExample
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telepot import DelegatorBot
from telepot.delegate import pave_event_space, per_chat_id, create_open
import csv
project =['Electronic devices','Computer software','Robots']		

class ProjectBot(telepot.helper.ChatHandler):
    
    def __init__(self, *args, **kwargs):
        super(ProjectBot, self).__init__(include_callback_query=True, *args, **kwargs)
        
        self.ID = 0
        #--These variables control the flow of adding info--
        self.step  = 0
        self.E_step = 0
        self.C_step = 0
        self.R_step = 0
        #--This variable records the last message
        self.lastmsg = ''
        #--These boolean variables controls the condition--
        self.Add_info = False
        self.Add_info_E = False
        self.Add_info_C = False
        self.Add_info_R = False
        self.Browse_info = False
        self.Browse_info_E = False
        self.Browse_info_C = False
        self.Browse_info_R = False
        self.Delete_info_E = False
        self.Delete_info_C = False
        self.Delete_info_R = False
        self.News = False
        #--These variables help to store the user's info--
        self.name  = ''
        self.school = ''
        self.year = ''
        self.sex = ''
        self.contact = ''
        self.email = ''
        self.idea= ''
        self.info = []
        #--These variables help to count the numbers of students in database--
        self.E_num = 0
        self.C_num = 0
        self.R_num = 0
        #--Theses variables help to delete the info--
        self.name_deleted =''
        self.rows_after_deleted = []
        
        
    
    def on_chat_message(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        #--------Check status, this condition satisfies neither add info nor browse news--------
        if self.Add_info == False and self.News == False:
            if content_type == 'text':
                if (msg['text'].startswith('/')):
                    command = msg['text'][1:].lower()
                    if (command == 'start'):
                        bot.sendMessage(chat_id, 'I am a project-helping bot.\nYou can get inspirations and find your best teammates with me!',reply_markup = welcome_keyboard())
                        #----Initialize all boolean variables when back in main menu----
                        self.Add_info = False
                        self.Add_info_E = False
                        self.Add_info_C = False
                        self.Add_info_R = False
                    if (command == 'restart'):
                        bot.sendMessage(chat_id, 'Welcome back to the main menu\nYou can get inspirations and find your best teammates here!',reply_markup = welcome_keyboard())
                        #----Initialize all boolean variables when back in main menu----
                        self.Add_info = False
                        self.Add_info_E = False
                        self.Add_info_C = False
                        self.Add_info_R = False
                        
                elif msg['text'] == 'Got idea! Find teammates! / Do not have an idea, but want to join a project！':
                    #--If the user wants to do projects, let him or her choose category of projects--
                    self.lastmsg = msg['text']
                    bot.sendMessage(chat_id, 'Hey, what kind of projects do you want to do?',reply_markup = project_keyboard())


                elif msg['text'] == 'Do not have an idea yet. Looking forward to getting inspired!':
                    #--If the user does not want to do project, ask if he or she wants news and project examples--
                    self.lastmsg = msg['text']
                    bot.sendMessage(chat_id,'Okay, do you want to browse some latest technology news?',reply_markup = ask_if_news())

                elif msg['text'] == 'Sure' and self.lastmsg == 'Do not have an idea yet. Looking forward to getting inspired!':
                    #--User has chosen to browse nows, browse news status become 'True'--
                    confirm_news = ReplyKeyboardMarkup(keyboard =
                    [
                    [KeyboardButton(text = 'Ok')]
                    ])
                    bot.sendMessage(chat_id,'News and project examples are here for you.',reply_markup = confirm_news)
                    self.News = True

                elif msg['text'] == 'No thanks' and self.lastmsg == 'Do not have an idea yet. Looking forward to getting inspired!':
                    #--User does not want news, back to main menu--
                    keyboard_back_to_main = ReplyKeyboardMarkup(keyboard =
                    [
                    [KeyboardButton(text = '/restart')]
                
                    ])

                    bot.sendMessage(chat_id,'Ok, you may go back to the main menu now.', reply_markup = keyboard_back_to_main)
                    


                    
                elif self.lastmsg == 'Got idea! Find teammates! / Do not have an idea, but want to join a project！' and msg['text'] == 'Electronic devices':
                    #--User chooses to do project and choose 'Electronic devices'--
                    self.lastmsg = msg['text']
                    bot.sendMessage(chat_id,'Do you want to store your info into my database?',reply_markup = project_add())
                elif self.lastmsg == 'Electronic devices':
                    if msg['text'] == 'Yes,I would like to add my info.':
                        #--The user wants to add info to database, add info status becomes 'True'--
                        self.Add_info_E = True 
                        bot.sendMessage(chat_id,'Confirm to add your info?',reply_markup = confirm_add_info_E())
                    elif msg['text'] == 'Not now, I would like to see the database first, thanks.':
                        #--The user wants to check the database--
                        self.lastmsg = msg['text']
                        want_to_check_data_E = keyboard_name = InlineKeyboardMarkup(inline_keyboard=[
                                   [InlineKeyboardButton(text='Ok, sure', callback_data='browseE')],
                                   [InlineKeyboardButton(text='No, thanks', callback_data='No_browse')]
                               ]) 
                        bot.sendMessage(chat_id, 'Would you like to browse some info of students who want to make some electronic devices?',reply_markup = want_to_check_data_E)
                    elif msg['text'] == 'I would like to delete my info from the database.':
                        #--The user wants to delete his or her info from database--
                        self.lastmsg = msg['text']
                        self.Delete_info_E = True
                        bot.sendMessage(chat_id,'Ok, your name please.')
                        
                elif self.Delete_info_E == True:
                    #--Confirm to delete the info from database--
                    confirm_to_delete_data = keyboard_name = InlineKeyboardMarkup(inline_keyboard=[
                                   [InlineKeyboardButton(text='Confirm', callback_data='DeleteE')],
                                   [InlineKeyboardButton(text='Let me think about it.', callback_data='No_delete')]
                               ])
                    self.name_deleted = msg['text']
                    bot.sendMessage(chat_id,'Confirm to delete your info from the database?',reply_markup = confirm_to_delete_data)
                    
                        
                elif self.Browse_info_E == True:
                    #----The user has chosen to browse the 'Electronic devices' database----
                    if msg['text'] == 'Ok':
                        self.lastmsg = msg['text']
                        self.E_num = Count_E_students()
                        confirm_to_check_data_E = keyboard_name = InlineKeyboardMarkup(inline_keyboard=[
                                   [InlineKeyboardButton(text='Details', callback_data='browseE_datails')],
                                   
                               ])
                        bot.sendMessage(chat_id, 'There are ' + str(self.E_num) + ' students who want to do Electronic devices projects',reply_markup = confirm_to_check_data_E)
                    elif self.lastmsg == 'Ok':
                        keyboard_back_to_main = ReplyKeyboardMarkup(keyboard =
                            [
                            [KeyboardButton(text = '/restart')]
                        
                            ])
                        #----Some wishes and back to main menu----
                        if msg['text'] == 'Contact them':
                            bot.sendMessage(chat_id,'Go ahead! Best wishes for your project!')
                            self.Browse_info_E = False
                            bot.sendMessage(chat_id,'You may go back to the main menu now.', reply_markup = keyboard_back_to_main)
                        if msg['text'] == 'Not now, thanks':
                            bot.sendMessage(chat_id, 'No problem, you may go back to the main menu now.',reply_markup = keyboard_back_to_main)
                            self.Browse_info_E = False
                            bot.sendMessage(chat_id, 'Hope you can check my database regularly.I believe you can find teammates here！')
                    else:
                        bot.sendMessage(chat_id,'Please press the \'Ok\'.')


                    
                elif self.lastmsg == 'Got idea! Find teammates! / Do not have an idea, but want to join a project！' and msg['text'] == 'Computer software':
                    #--User chooses to do project and choose 'Computer software'--
                    self.lastmsg = msg['text']
                    bot.sendMessage(chat_id,'Do you want to store your info into my database?',reply_markup = project_add())
                elif self.lastmsg == 'Computer software': 
                    if msg['text'] == 'Yes,I would like to add my info.':
                        #--The user wants to add info to database, add info status becomes 'True'--
                        self.Add_info_C = True
                        bot.sendMessage(chat_id,'Confirm to add your info?',reply_markup = confirm_add_info_C())
                    elif msg['text'] == 'Not now, I would like to see the database first, thanks.':
                        #--The user wants to check the database--
                        self.lastmsg = msg['text']
                        want_to_check_data_C = keyboard_name = InlineKeyboardMarkup(inline_keyboard=[
                                   [InlineKeyboardButton(text='Ok，sure', callback_data='browseC')],
                                   [InlineKeyboardButton(text='No, thanks', callback_data='No_browse')]
                               ]) 
                        bot.sendMessage(chat_id, 'Would you like to browse some info of students who want to do Computer software projects ?',reply_markup = want_to_check_data_C)
                    elif msg['text'] == 'I would like to delete my info from the database.':
                        #--The user wants to delete his or her info from database--
                        self.lastmsg = msg['text']
                        self.Delete_info_C = True
                        bot.sendMessage(chat_id,'Ok, your name please')
                        
                elif self.Delete_info_C == True:
                    #--Confirm to delete the info from database--
                    confirm_to_delete_data = keyboard_name = InlineKeyboardMarkup(inline_keyboard=[
                                   [InlineKeyboardButton(text='Confirm', callback_data='DeleteC')],
                                   [InlineKeyboardButton(text='Let me think about it.', callback_data='No_delete')]
                               ])
                    self.name_deleted = msg['text']
                    bot.sendMessage(chat_id,'Confirm to delete your info from the database?',reply_markup = confirm_to_delete_data)
                        
                        
                elif self.Browse_info_C == True:
                    #----The user has chosen to browse the 'Computer software' database----
                    if msg['text'] == 'Ok':
                        self.lastmsg = msg['text']
                        self.C_num = Count_C_students()
                        confirm_to_check_data_C = keyboard_name = InlineKeyboardMarkup(inline_keyboard=[
                                   [InlineKeyboardButton(text='Details', callback_data='browseC_datails')],
                                   
                               ])
                        bot.sendMessage(chat_id, 'There are ' + str(self.C_num) + ' students who want to do Computer software projects',reply_markup = confirm_to_check_data_C)
                    elif self.lastmsg == 'Ok':
                        keyboard_back_to_main = ReplyKeyboardMarkup(keyboard =
                            [
                            [KeyboardButton(text = '/restart')]
                        
                            ])
                        #----Some wishes and back to main menu----
                        if msg['text'] == 'Contact them':
                            bot.sendMessage(chat_id,'Go ahead! Best wishes for your project!')
                            self.Browse_info_C = False
                            bot.sendMessage(chat_id,'You may go back to the main menu now.', reply_markup = keyboard_back_to_main)
                        if msg['text'] == 'Not now, thanks':
                            bot.sendMessage(chat_id, 'No problem, you may go back to the main menu now.',reply_markup = keyboard_back_to_main)
                            self.Browse_info_C = False
                            bot.sendMessage(chat_id, 'Hope you can check my database regularly.I believe you can find teammates here.')
                    else:
                        bot.sendMessage(chat_id,'Please press the \'Ok\'.')



                    
                elif self.lastmsg == 'Got idea! Find teammates! / Do not have an idea, but want to join a project！' and msg['text'] == 'Robots':
                    #--User chooses to do project and choose 'Robots'--
                    self.lastmsg = msg['text']
                    bot.sendMessage(chat_id,'Do you want to store your info into my database?',reply_markup = project_add())
                elif self.lastmsg == 'Robots':
                    #--The user wants to add info to database, add info status becomes 'True'--
                    if msg['text'] == 'Yes, I would like to add my info.':
                        self.Add_info_R = True
                        bot.sendMessage(chat_id,'Confirm to add your info?',reply_markup = confirm_add_info_R())
                    elif msg['text'] == 'Not now, I would like to see the database first, thanks.':
                        #--The user wants to check the database--
                        self.lastmsg = msg['text']
                        want_to_check_data_R = keyboard_name = InlineKeyboardMarkup(inline_keyboard=[
                                   [InlineKeyboardButton(text='Ok，sure', callback_data='browseR')],
                                   [InlineKeyboardButton(text='No,thanks', callback_data='No_browse')]
                               ]) 
                        bot.sendMessage(chat_id, 'Would you like to browse some info of students who want to bulid robots?',reply_markup = want_to_check_data_R)
                    elif msg['text'] == 'I would like to delete my info from the database.':
                        #--The user wants to delete his or her info from database--
                        self.lastmsg = msg['text']
                        self.Delete_info_R = True
                        bot.sendMessage(chat_id,'Ok, your name please')
                        
                elif self.Delete_info_R == True:
                    #--Confirm to delete the info from database--
                    confirm_to_delete_data = keyboard_name = InlineKeyboardMarkup(inline_keyboard=[
                                   [InlineKeyboardButton(text='Confirm', callback_data='DeleteR')],
                                   [InlineKeyboardButton(text='Let me think about it.', callback_data='No_delete')]
                               ])
                    self.name_deleted = msg['text']
                    bot.sendMessage(chat_id,'Confirm to delete your info from the database?',reply_markup = confirm_to_delete_data)
                    
                elif self.Browse_info_R == True:
                    #----The user has chosen to browse the 'Robots' database----
                    if msg['text'] == 'Ok':
                        self.lastmsg = msg['text']
                        self.R_num = Count_R_students()
                        confirm_to_check_data_R = keyboard_name = InlineKeyboardMarkup(inline_keyboard=[
                                   [InlineKeyboardButton(text='Details', callback_data='browseR_datails')],
                                   
                               ])
                        bot.sendMessage(chat_id, 'There are ' + str(self.R_num) + ' students who want to do build robots',reply_markup = confirm_to_check_data_R)
                    elif self.lastmsg == 'Ok':
                        keyboard_back_to_main = ReplyKeyboardMarkup(keyboard =
                            [
                            [KeyboardButton(text = '/restart')]
                        
                            ])
                        #----Some wishes and back to main menu----
                        if msg['text'] == 'Contact them':
                            bot.sendMessage(chat_id,'Go ahead! Best wishes for your project!')
                            self.Browse_info_R = False
                            bot.sendMessage(chat_id,'You may go back to the main menu now.', reply_markup = keyboard_back_to_main)
                        if msg['text'] == 'Not now, thanks':
                            
                            bot.sendMessage(chat_id, 'No problem, you may go back to the main menu now.',reply_markup = keyboard_back_to_main)
                            self.Browse_info_R = False
                            bot.sendMessage(chat_id, 'Hope you can check my database regularly.I believe you can find teammates here.') 
                    else:
                        bot.sendMessage(chat_id,'Please press the \'Ok\'.')

                
        elif self.Add_info == True and self.News == False:
            #----If the Add_info becomes True, do these steps----
            def Enter_the_info_E(chat_id,self,msg,step):
                #----This function helps the user to enter the info to the 'Electronic devices' database----
                if step == 0:
                    keyboard_name = InlineKeyboardMarkup(inline_keyboard=[
                                   [InlineKeyboardButton(text='Answer question', callback_data='nameE')],
                               ])       
                    bot.sendMessage(chat_id,'Press the \'Answer question\' button and give me your reply',reply_markup = keyboard_name)
                if step == 1:
                    self.info = []
                    self.name = msg['text']
                    self.info.append(self.name)
                    keyboard_school = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='schoolE')],
                           ])
                    bot.sendMessage(chat_id,'Press the \'Answer question\' button and give me your reply\nNote: If you would like to change the answer for the last question,do not press the  \'Answer question\'button. Just answer it again\nIf you confrim your reply, then you can press',reply_markup = keyboard_school)
                if step == 2:
                    self.info = [self.name]
                    print(self.info)
                    self.school = msg['text']
                    self.info.append(self.school)
                    keyboard_year = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='yearE')],
                           ])
                    bot.sendMessage(chat_id, 'Press the inline keyboard and answer the next question',reply_markup = keyboard_year)

                if step == 3:
                    self.info = [self.name,self.school]
                    print(self.info)
                    self.year = msg['text']
                    self.info.append(self.year)
                    keyboard_sex = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='sexE')],
                           ])
                    bot.sendMessage(chat_id, 'Press the \'Answer question\' button and give me your reply\nNote: If you would like to change the answer for the last question,do not press the  \'Answer question\'button. Just answer it again\nIf you confrim your reply, then you can press',reply_markup = keyboard_sex)

                if step == 4:
                    self.info = [self.name,self.school,self.year]
                    print(self.info)
                    self.sex = msg['text']
                    self.info.append(self.sex)
                    keyboard_contact = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='contactE')],
                           ])
                    bot.sendMessage(chat_id, 'Press the \'Answer question\' button and give me your reply\nNote: If you would like to change the answer for the last question,do not press the \'Answer question\' button. Just answer it again\nIf you confrim your reply, then you can press',reply_markup = keyboard_contact)

                if step == 5:
                    self.info = [self.name,self.school,self.year,self.sex]
                    print(self.info)
                    self.contact = msg['text']
                    self.info.append(self.contact)
                    keyboard_idea = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='emailE')],
                           ])
                    
                    bot.sendMessage(chat_id, 'Press the \'Anwer question\' button and give me your reply\nNote: If you would like to change the answer for the last question,do not press the \'Answer question\' button. Just answer it again\nIf you confrim your reply, then you can press',reply_markup = keyboard_idea)

                if step == 6:
                    self.info = [self.name,self.school,self.year,self.sex,self.contact]
                    print(self.info)
                    self.email = msg['text']
                    self.info.append(self.email)
                    keyboard_finish = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='ideaE')],
                           ])
                    bot.sendMessage(chat_id, 'Press the \'Anwer question\' button and give me your reply\nNote: If you would like to change the answer for the last question,do not press the \'Answer question\' button. Just answer it again\nIf you confrim your reply, then you can press',reply_markup = keyboard_finish)

                if step == 7:
                    self.info = [self.name,self.school,self.year,self.sex,self.contact,self.email]
                    print(self.info)
                    self.idea = msg['text']
                    self.info.append(self.idea)
                    keyboard_finish = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Finish', callback_data='finishE')],
                           ])
                    bot.sendMessage(chat_id, 'We have collected all the info needed',reply_markup = keyboard_finish)
                    
                if step == 8:
                    #----This step means that the adding is over----
                    print(self.info)
                    print(self.Add_info_E)
                    print(self.Add_info_C)
                    print(self.Add_info_R)
                    if msg['text'] != 'Confirm info': 
                        bot.sendMessage(chat_id, 'Category: Electronic Devices')
                        bot.sendMessage(chat_id,'Name:   ' + self.name + '\nSchool:  ' + self.school + '\nYear:  ' + self.year + '\nSex:   ' + self.sex.upper() + '\nContact No.:  ' + self.contact + '\nE-mail:  ' + self.email + '\nIdea:  ' + self.idea)
                        bot.sendMessage(chat_id, 'Confirm your info?',reply_markup = confirm_info())

                if step == 9:
                    #----This step is to make sure one user can only add one set of info in to this database----
                    #----Assign the Add_info and Add_info_E back to False----
                    self.Add_info = False
                    self.Add_info_E = False
                    keyboard_back_to_main = ReplyKeyboardMarkup(keyboard =
                    [
                    [KeyboardButton(text = '/restart')]
            
                    ])
                    bot.sendMessage(chat_id, 'You have successfully uploaded your info to the Electronic devices database, You may go back to the main menu now.',reply_markup = keyboard_back_to_main)
                    
            def Enter_the_info_C(chat_id,self,msg,step):
                #----This function helps the user to enter the info to the 'Computer software' database----
                if step == 0:
                    keyboard_name = InlineKeyboardMarkup(inline_keyboard=[
                                   [InlineKeyboardButton(text='Answer question', callback_data='nameC')],
                               ])       
                    bot.sendMessage(chat_id,'Press the \'Anwer question\' button and give me your reply',reply_markup = keyboard_name)
                if step == 1:
                    self.info = []
                    self.name = msg['text']
                    self.info.append(self.name)
                    keyboard_school = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='schoolC')],
                           ])
                    bot.sendMessage(chat_id,'Press the \'Anwer question\' button and give me your reply\nNote: If you would like to change the answer for the last question,do not press the \'Answer question\' button. Just answer it again\nIf you confrim your reply, then you can press',reply_markup = keyboard_school)
                if step == 2:
                    self.info = [self.name]
                    self.school = msg['text']
                    self.info.append(self.school)
                    keyboard_year = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='yearC')],
                           ])
                    bot.sendMessage(chat_id, 'Press the \'Anwer question\' button and give me your reply\nNote: If you would like to change the answer for the last question,do not press the \'Answer question\' button. Just answer it again\nIf you confrim your reply, then you can press',reply_markup = keyboard_year)

                if step == 3:
                    self.info = [self.name,self.school]
                    self.year = msg['text']
                    self.info.append(self.year)
                    keyboard_sex = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='sexC')],
                           ])
                    bot.sendMessage(chat_id, 'Press the \'Anwer question\' button and give me your reply\nNote: If you would like to change the answer for the last question,do not press the \'Answer question\' button. Just answer it again\nIf you confrim your reply, then you can press',reply_markup = keyboard_sex)

                if step == 4:
                    self.info = [self.name,self.school,self.year]
                    self.sex = msg['text']
                    self.info.append(self.sex)
                    keyboard_contact = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='contactC')],
                           ])
                    bot.sendMessage(chat_id, 'Press the \'Anwer question\' button and give me your reply\nNote: If you would like to change the answer for the last question,do not press the \'Answer question\' button. Just answer it again\nIf you confrim your reply, then you can press',reply_markup = keyboard_contact)

                if step == 5:
                    self.info = [self.name,self.school,self.year,self.sex]
                    self.contact = msg['text']
                    self.info.append(self.contact)
                    keyboard_idea = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='emailC')],
                           ])
                    
                    bot.sendMessage(chat_id, 'Press the \'Anwer question\' button and give me your reply\nNote: If you would like to change the answer for the last question,do not press the \'Answer question\'button. Just answer it again\nIf you confrim your reply, then you can press',reply_markup = keyboard_idea)

                if step == 6:
                    self.info = [self.name,self.school,self.year,self.sex,self.contact]
                    self.email = msg['text']
                    self.info.append(self.email)
                    keyboard_finish = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='ideaC')],
                           ])
                    bot.sendMessage(chat_id, 'Press the \'Anwer question\' button and give me your reply\nNote: If you would like to change the answer for the last question,do not press the  \'Answer question\'button. Just answer it again\nIf you confrim your reply, then you can press',reply_markup = keyboard_finish)

                if step == 7:
                    self.info = [self.name,self.school,self.year,self.sex,self.contact,self.email]
                    self.idea = msg['text']
                    self.info.append(self.idea)
                    keyboard_finish = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Finish', callback_data='finishC')],
                           ])
                    bot.sendMessage(chat_id, 'We have collected all the info needed',reply_markup = keyboard_finish)
                    
                if step == 8:
                    #----This step means that the adding is over----
                    print(self.info)
                    print(self.Add_info_E)
                    print(self.Add_info_C)
                    print(self.Add_info_R)
                    if msg['text'] != 'Confirm info': 
                        bot.sendMessage(chat_id, 'Categroy: Computer software')
                        bot.sendMessage(chat_id,'Name:   ' + self.name + '\nSchool:  ' + self.school + '\nYear:  ' + self.year + '\nSex:   ' + self.sex.upper() + '\nContact No.:  ' + self.contact + '\nE-mail:  ' + self.email + '\nIdea:  ' + self.idea)
                        bot.sendMessage(chat_id, 'Confirm your info?',reply_markup = confirm_info())
                    
                if step == 9:
                    #----This step is to make sure one user can only add one set of info in to this database----
                    #----Assign the Add_info and Add_info_C back to False----
                    self.Add_info = False
                    self.Add_info_C = False
                    keyboard_back_to_main = ReplyKeyboardMarkup(keyboard =
                    [
                    [KeyboardButton(text = '/restart')]
            
                    ])
                    bot.sendMessage(chat_id, 'You have successfully uploaded your info to the Computer software database, you may go back to the main menu now',reply_markup = keyboard_back_to_main)
                    
            def Enter_the_info_R(chat_id,self,msg,step):
                #----This function helps the user to enter the info to the 'Robots' database----
                if step == 0:
                    keyboard_name = InlineKeyboardMarkup(inline_keyboard=[
                                   [InlineKeyboardButton(text='Answer question', callback_data='nameR')],
                               ])       
                    bot.sendMessage(chat_id,'Press the \'Anwer question\' and give me your corresponding reply',reply_markup = keyboard_name)
                if step == 1:
                    self.info = []
                    self.name = msg['text']
                    print(self.info)
                    print(self.name)
                    self.info.append(self.name)
                    keyboard_school = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='schoolR')],
                           ])
                    bot.sendMessage(chat_id,'Press the \'Anwer question\' and give me your reply\nNote: If you would like to change the answer for the last question,do not press the  \'Answer question\'button. Just answer it again\nIf you confrim your reply, then you can press',reply_markup = keyboard_school)
                if step == 2:
                    self.info = [self.name]
                    self.school = msg['text']
                    print(self.info)
                    print(self.school)
                    self.info.append(self.school)
                    keyboard_year = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='yearR')],
                           ])
                    bot.sendMessage(chat_id, 'Press the \'Anwer question\' and give me your reply\nNote: If you would like to change the answer for the last question,do not press the  \'Answer question\'button. Just answer it again\nIf you confrim your reply, then you can press',reply_markup = keyboard_year)

                if step == 3:
                    self.info = [self.name,self.school]
                    self.year = msg['text']
                    print(self.info)
                    print(self.year)
                    self.info.append(self.year)
                    keyboard_sex = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='sexR')],
                           ])
                    bot.sendMessage(chat_id, 'Press the \'Anwer question\' and give me your reply\nNote: If you would like to change the answer for the last question,do not press the  \'Answer question\'button. Just answer it again\nIf you confrim your reply, then you can press',reply_markup = keyboard_sex)

                if step == 4:
                    self.info = [self.name,self.school,self.year]
                    self.sex = msg['text']
                    print(self.info)
                    print(self.sex)
                    self.info.append(self.sex)
                    keyboard_contact = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='contactR')],
                           ])
                    bot.sendMessage(chat_id, 'Press the inline keyboard and answer the next question',reply_markup = keyboard_contact)

                if step == 5:
                    self.info = [self.name,self.school,self.year,self.sex]
                    self.contact = msg['text']
                    print(self.info)
                    print(self.contact)
                    self.info.append(self.contact)
                    keyboard_idea = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='emailR')],
                           ])
                    
                    bot.sendMessage(chat_id, 'Press the \'Anwer question\' and give me your reply\nNote: If you would like to change the answer for the last question,do not press the \'Answer question\' button. Just answer it again\nIf you confrim your reply, then you can press',reply_markup = keyboard_idea)

                if step == 6:
                    self.info = [self.name,self.school,self.year,self.sex,self.contact]
                    self.email = msg['text']
                    print(self.info)
                    print(self.email)
                    self.info.append(self.email)
                    keyboard_finish = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Answer question', callback_data='ideaR')],
                           ])
                    bot.sendMessage(chat_id, 'Press the \'Anwer question\' and give me your reply\nNote: If you would like to change the answer for the last question,do not press the \'Answer question\' button. Just answer it again\nIf you confrim your reply, then you can press',reply_markup = keyboard_finish)

                if step == 7:
                    self.info = [self.name,self.school,self.year,self.sex,self.contact,self.email]
                    self.idea = msg['text']
                    print(self.info)
                    print(self.idea)
                    self.info.append(self.idea)
                    keyboard_finish = InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text='Confirm all the information and finish', callback_data='finishR')],
                           ])
                    bot.sendMessage(chat_id, 'We have collected all the info needed',reply_markup = keyboard_finish)
                    
                if step == 8:
                    #----This step means that the adding is over----
                    print(self.info)
                    print(self.Add_info_E)
                    print(self.Add_info_C)
                    print(self.Add_info_R)
                    if msg['text'] != 'Confirm info':
                        bot.sendMessage(chat_id, 'Category: Robots')
                        bot.sendMessage(chat_id,'Name:   ' + self.name + '\nSchool:  ' + self.school + '\nYear:  ' + self.year + '\nSex:   ' + self.sex.upper() + '\nContact No.:  ' + self.contact + '\nE-mail:  ' + self.email + '\nIdea:  ' + self.idea)
                        bot.sendMessage(chat_id, 'Confirm your info?',reply_markup = confirm_info())

                if step == 9:
                    #----This step is to make sure one user can only add one set of info in to this database----
                    #----Assign the Add_info and Add_info_R back to False----
                    self.Add_info = False
                    self.Add_info_R = False
                    keyboard_back_to_main = ReplyKeyboardMarkup(keyboard =
                    [
                    [KeyboardButton(text = '/restart')]
            
                    ])
                    bot.sendMessage(chat_id, 'You have uploaded your info to the \n Robots\' database, you may go back to the main menu now.',reply_markup = keyboard_back_to_main)
                
            
                    
            if self.Add_info_E == True:
                Enter_the_info_E(chat_id,self,msg,self.E_step)
    

            elif self.Add_info_C == True:
                Enter_the_info_C(chat_id,self,msg,self.C_step)
                

            elif self.Add_info_R == True:
                Enter_the_info_R(chat_id,self,msg,self.R_step)
                
                
            
            
            if msg['text'] == 'Confirm info':                
                #----Confirm add the info to databases----
                if self.Add_info_E == True:
                    add_to_database_E(self.info)
                    self.E_step = 9
                    self.Add_info_E = False
                
                elif self.Add_info_C == True:
                    add_to_database_C(self.info)
                    self.C_step = 9
                    self.Add_info_C = False

                elif self.Add_info_R == True:
                    add_to_database_R(self.info)
                    self.R_step = 9
                    self.Add_info_R = False

                bot.sendMessage(chat_id,'Thank you, your info has been successfully stored.\n You can now look through our database for info of other students or wait for others to contact you')
                
                keyboard_back_to_main = ReplyKeyboardMarkup(keyboard =
                [

                [KeyboardButton(text = '/restart')]
            
                ])
                bot.sendMessage(chat_id,'Send restart command to back to main menu',reply_markup = keyboard_back_to_main)
                    
                self.Add_info = False

        elif self.News == True:
            def want_news_and_project_example(self,msg):
                if content_type == 'text':
                    # ----Check different situations and give corresponding respond----
                    if msg['text'] == 'News Feeds':
                        bot.sendMessage(chat_id,'Please select the format of the news:',reply_markup = form())
                            
                    elif msg['text'] == 'Title&Date&Full Text':
                        bot.sendMessage(chat_id,'Which kind of example do you want to look through?:',reply_markup = newstypeFT())

                    elif msg['text'] == 'Title&URL':
                        bot.sendMessage(chat_id,'Which kind of example do you want to look through?',reply_markup = newstypeURL())

                    elif msg['text'] == 'back':
                        bot.sendMessage(chat_id,'Which kind of example do you want to look through?',reply_markup = newstypeFT())

                    elif msg['text'] == 'return':
                        bot.sendMessage(chat_id,'Which kind of example do you want to look through?',reply_markup = newstypeURL())
                            
                    elif msg['text'] == 'Project Examples':
                        bot.sendMessage(chat_id,'Which kind of example do you want to look through?',reply_markup = projectype())

                    # ----Push the examles one at a time----
                    elif msg['text'] == 'Arduino':
                        self.begin = 2
                        self.stop = 7
                        for n in range(self.begin,self.stop):
                            bot.sendMessage(chat_id,ProjectExample(n,'Arduino'),reply_markup = nextfiveard())

                    elif msg['text'] == 'RaspberryPi':
                        self.begin = 2
                        self.stop = 7
                        for n in range(self.begin,self.stop):
                            bot.sendMessage(chat_id,ProjectExample(n,'RaspberryPi'),reply_markup = nextfiveras())

                    # ----Achieve the aim of reading five more examples----
                    elif msg['text'] == 'Please give me five more Arduino examples.':
                        self.begin += 5
                        self.stop += 5
                        try:
                            for n in range(self.begin,self.stop):
                                bot.sendMessage(chat_id,ProjectExample(n,'Arduino'),reply_markup = nextfiveard())
                        except Exception as IndexError:
                            bot.sendMessage(chat_id,'You have looked through all the examples. Returning to the project-type-choosing menu now.',reply_markup = projectype())
                                    
                    elif msg['text'] == 'Please load five more RaspberryPi examples for me.':
                        self.begin += 5
                        self.stop += 5
                        try:
                            for n in range(self.begin,self.stop):
                                bot.sendMessage(chat_id,ProjectExample(n,'RaspberryPi'),reply_markup = nextfiveras())
                        except Exception as IndexError:
                            bot.sendMessage(chat_id,'You have looked through all the examples. Returning to the project-type-choosing menu now.',reply_markup = projectype())
                                    
                    # ----Achieve the aim of returning to former menus----
                    elif msg['text'] == 'You have looked through all the examples. Return to project-type-choosing menu now.':
                        bot.sendMessage(chat_id,'Which kind of example do you want to look through?',reply_markup = projectype())

                    elif msg['text'] == 'Back to main menu.':
                        keyboard_back_to_main = ReplyKeyboardMarkup(keyboard =
                        [
                        [KeyboardButton(text = '/restart')]
                    
                        ])
                        
                        bot.sendMessage(chat_id,'Press /restart and back to main.',reply_markup = keyboard_back_to_main)
                        self.News = False
                    # ----When the text is not matched, do the following----
                    else:
                        bot.sendMessage(chat_id,"Hello, you can find the best technology news and project examples here!", reply_markup = menu())
        

            want_news_and_project_example(self,msg)            
     
    def on_callback_query(self,msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
       
        bot.answerCallbackQuery(query_id, text='Got it, just a second')
        keyboard_give_greeting = ReplyKeyboardMarkup(keyboard =
            [
            [KeyboardButton(text = 'Hello!')]
            
            ])
        if (query_data == 'Confirm add info to E'):
            #---The useer has choesn to add info to 'Electronic devices'---
            bot.sendMessage(from_id,'Hello, give me a greeting and I\'ll ask you some questions',reply_markup = keyboard_give_greeting)
            self.Add_info = True
            self.Add_info_E = True
            
        elif (query_data == 'Confirm add info to C'):
            #---The useer has choesn to add info to 'Computer software'---
            bot.sendMessage(from_id,'Hello, give me a greeting and I\'ll ask you some questions',reply_markup = keyboard_give_greeting)
            self.Add_info = True
            self.Add_info_C = True

        elif (query_data == 'Confirm add info to R'):
            #---The useer has choesn to add info to 'Robots'---
            bot.sendMessage(from_id,'Hello, give me a greeting and I\'ll ask you some questions',reply_markup = keyboard_give_greeting)
            self.Add_info = True
            self.Add_info_R = True
            
        elif (query_data == 'Cancel add info'):
            #---Cancel the info adding---
            keyboard_back_to_main = ReplyKeyboardMarkup(keyboard =
                [
                [KeyboardButton(text = '/restart')]
            
                ])
            self.Add_info = False
            bot.sendMessage(from_id,'Emmmmmm, you may go back to the main menu.', reply_markup = keyboard_back_to_main)

        elif (query_data == 'browseE'):
            #---The user want to browse 'Electronic devices' database---
            self.Browse_info_E = True
            keyboard_reply_confirm_browse = ReplyKeyboardMarkup(keyboard =
            [
            [KeyboardButton(text = 'Ok')]
            
            ])
            bot.sendMessage(from_id, 'Here is the \'Electronic devices\' project database.Press \'Ok\' to continue',reply_markup = keyboard_reply_confirm_browse)

        elif (query_data == 'browseC'):
            #---The user want to browse 'Computer software' database---
            self.Browse_info_C = True
            keyboard_reply_confirm_browse = ReplyKeyboardMarkup(keyboard =
            [
            [KeyboardButton(text = 'Ok')]
            
            ])
            bot.sendMessage(from_id, 'Here is the \'Computer softwares\' project database.Press \'Ok\' to continue',reply_markup = keyboard_reply_confirm_browse)

        elif (query_data == 'browseR'):
            #---The user want to browse 'Robots' database---
            self.Browse_info_R = True
            keyboard_reply_confirm_browse = ReplyKeyboardMarkup(keyboard =
            [
            [KeyboardButton(text = 'Ok')]
            
            ])
            bot.sendMessage(from_id, 'You have access to the Robots project database.Press \'Ok\' to continue',reply_markup = keyboard_reply_confirm_browse)

        elif (query_data == 'browseE_datails'):
            #---The user want to check details of 'Electronic devices' database---
            Browse_datails_E(from_id,self.E_num)

        elif (query_data == 'browseC_datails'):
            #---The user want to check details of 'Computer software' database---
            Browse_datails_C(from_id,self.C_num)

        elif (query_data == 'browseR_datails'):
            #---The user want to check details of 'Robots' database---
            Browse_datails_R(from_id,self.R_num)                      
        
        #----These query_data is to control the flow of adding info to 'Electronic devices' database----
        elif (query_data == 'nameE'):
            self.E_step =  1
            bot.sendMessage(from_id,'Hey, what\'s your name?')
            
        elif (query_data == 'schoolE'):
            self.E_step =  2
            bot.sendMessage(from_id,'Hey, ' + self.name +', which school are you from?')

        elif (query_data == 'yearE'):
            self.E_step =  3
            bot.sendMessage(from_id, 'You are in year...?')

        elif (query_data == 'sexE'):
            self.E_step = 4
            bot.sendMessage(from_id, 'May I have your gender please?')

        elif (query_data == 'contactE'):
            self.E_step = 5
            bot.sendMessage(from_id,'Hey, can you give me your telephone number')

        elif (query_data == 'emailE'):
            self.E_step = 6
            bot.sendMessage(from_id,'Your e-mail?\n(Both NTU e-mail and personal e-mail are ok)')

        elif (query_data == 'ideaE'):
            self.E_step  = 7
            bot.sendMessage(from_id,'Talk about your idea, in one message please.\nIf you do not have idea yet, please write \'none\'.')

        elif (query_data == 'finishE'):
            self.E_step = 8
            keyboard_finsih_all_and_ok = ReplyKeyboardMarkup(keyboard =
            [
            [KeyboardButton(text = 'Ok,thank you!')]
            
            ])
            bot.sendMessage(from_id,'Well, done!\n Say okay and proceed to the confirmation.',reply_markup = keyboard_finsih_all_and_ok)

        #----These query_data is to control the flow of adding info to 'Computer software' database----
        elif (query_data == 'nameC'):
            self.C_step =  1
            bot.sendMessage(from_id,'Hey, what\'s your name?')
            
        elif (query_data == 'schoolC'):
            self.C_step =  2
            bot.sendMessage(from_id,'Hey, ' + self.name +', which school are you from?')

        elif (query_data == 'yearC'):
            self.C_step =  3
            bot.sendMessage(from_id, 'You are in year...?')

        elif (query_data == 'sexC'):
            self.C_step = 4
            bot.sendMessage(from_id, 'May I have your gender please?')

        elif (query_data == 'contactC'):
            self.C_step = 5
            bot.sendMessage(from_id,'Hey, can you give me your telephone number')

        elif (query_data == 'emailC'):
            self.C_step = 6
            bot.sendMessage(from_id,'Your e-mail address?\n(Both NTU and personal e-mail are ok)')

        elif (query_data == 'ideaC'):
            self.C_step  = 7
            bot.sendMessage(from_id,'Talk about your idea, in one message please.\nIf you do not have an idea yet, please enter \'none\'.')

        elif (query_data == 'finishC'):
            self.C_step = 8
            keyboard_finsih_all_and_ok = ReplyKeyboardMarkup(keyboard =
            [
            [KeyboardButton(text = 'Ok,thank you!')]
            
            ])
            bot.sendMessage(from_id,'Well, done!\n Say okay and proceed to the confirmation.',reply_markup = keyboard_finsih_all_and_ok)

        #----These query_data is to control the flow of adding info to 'Robots' database----
        elif (query_data == 'nameR'):
            self.R_step =  1
            bot.sendMessage(from_id,'Hey, what\'s your name?')
            
        elif (query_data == 'schoolR'):
            self.R_step =  2
            bot.sendMessage(from_id,'Hey, ' + self.name +', which school are you from?')
            
        elif (query_data == 'yearR'):
            self.R_step =  3
            bot.sendMessage(from_id, 'You are in year...?')

        elif (query_data == 'sexR'):
            self.R_step = 4
            bot.sendMessage(from_id, 'May I have your gender please?')

        elif (query_data == 'contactR'):
            self.R_step = 5
            bot.sendMessage(from_id,'Hey, can you give me your telephone number')

        elif (query_data == 'emailR'):
            self.R_step = 6
            bot.sendMessage(from_id,'Your e-mail address?\n(Both NTU E-mail and personal E-mail are ok)')

        elif (query_data == 'ideaR'):
            self.R_step  = 7
            bot.sendMessage(from_id,'Talk about your idea, in one message please.\nIf you do not have an idea yet, please enter \'none\'.')

        elif (query_data == 'finishR'):
            self.R_step = 8
            keyboard_finsih_all_and_ok = ReplyKeyboardMarkup(keyboard =
            [
            [KeyboardButton(text = 'Ok,thank you!')]
            
            ])
            bot.sendMessage(from_id,'Well, done!\n Say okay and proceed to the confirmation.',reply_markup = keyboard_finsih_all_and_ok)

        #----The user wants to delete info from 'Electronic devices' database----
        elif(query_data == 'DeleteE'):
            delete_info_from_E_first(self.name_deleted)
            self.rows_after_deleted = delete_info_from_E_first(self.name_deleted)
            print(self.rows_after_deleted)
            delete_info_from_E_second(self.rows_after_deleted)
            self.Delete_info_E = False
            self.E_step = 0
            keyboard_back_to_main = ReplyKeyboardMarkup(keyboard =
            [
            [KeyboardButton(text = '/restart')]
        
            ])
            bot.sendMessage(from_id,'Ok, done, you may go back to the main menu now.',reply_markup = keyboard_back_to_main)

        #----The user wants to delete info from 'Electronic devices' database----    
        elif(query_data == 'DeleteC'):
            delete_info_from_C_first(self.name_deleted)
            self.rows_after_deleted = delete_info_from_C_first(self.name_deleted)
            print(self.rows_after_deleted)
            delete_info_from_C_second(self.rows_after_deleted)
            self.Delete_info_C = False
            self.C_step = 0
            keyboard_back_to_main = ReplyKeyboardMarkup(keyboard =
            [
            [KeyboardButton(text = '/restart')]
        
            ])
            bot.sendMessage(from_id,'Ok, done, you may go back to the main menu now.',reply_markup = keyboard_back_to_main)
            
        #----The user wants to delete info from 'Electronic devices' database----
        elif(query_data == 'DeleteR'):
            delete_info_from_R_first(self.name_deleted)
            self.rows_after_deleted = delete_info_from_R_first(self.name_deleted)
            print(self.rows_after_deleted)
            delete_info_from_R_second(self.rows_after_deleted)
            self.Delete_info_R = False
            self.R_step = 0
            keyboard_back_to_main = ReplyKeyboardMarkup(keyboard =
            [
            [KeyboardButton(text = '/restart')]
        
            ])
            bot.sendMessage(from_id,'Ok, done, you may go back to the main menu now.',reply_markup = keyboard_back_to_main)


        #----The user does not want to delete info now----            
        elif(query_data == 'No_delete'):
            keyboard_back_to_main = ReplyKeyboardMarkup(keyboard =
            [
            [KeyboardButton(text = '/restart')]
        
            ])
            self.Delete_info_E = False
            self.Delete_info_C = False
            self.Delete_info_R = False
            bot.sendMessage(from_id,'You may go back to the main menu now.', reply_markup = keyboard_back_to_main)
            
        #---=Push different kinds of news---
        elif (query_data == 'Software News FT'):
            #--Push news one piece at a time--
            for n in range(0,5):
                bot.sendMessage(from_id,text = software(n,1))
            keyboard_back_to_main_or_back = ReplyKeyboardMarkup(keyboard =
            [
            [KeyboardButton(text = 'back')],
            [KeyboardButton(text = 'News & Project examples main')],
            ])
            bot.sendMessage(from_id,text = 'Type "back" to return to last menu',reply_markup = keyboard_back_to_main_or_back)
            
        elif (query_data == 'Electronics News FT'):
            #--Push news one piece at a time--
            for n in range(0,5):
                bot.sendMessage(from_id,text = electronics(n,1))
            keyboard_back_to_main_or_back = ReplyKeyboardMarkup(keyboard =
            [
            [KeyboardButton(text = 'back')],
            [KeyboardButton(text = 'News & Project examples main')],
            ])
            bot.sendMessage(from_id,text = 'Type "back" to return to last menu',reply_markup = keyboard_back_to_main_or_back)
        
        elif (query_data == 'Hardware News FT'):
            #--Push news one piece at a time--
            for n in range(0,5):
                bot.sendMessage(from_id,text = hardware(n,1))
            keyboard_back_to_main_or_back = ReplyKeyboardMarkup(keyboard =
            [
            [KeyboardButton(text = 'back')],
            [KeyboardButton(text = 'News & Project examples main')],
            ])
            bot.sendMessage(from_id,text = 'Type "back" to return to last menu',reply_markup = keyboard_back_to_main_or_back)
            
        elif (query_data == 'Software News URL'):
            #--Push news one piece at a time--
            for n in range(0,5):
                bot.sendMessage(from_id,text = software(n,0))
            keyboard_back_to_main_or_return = ReplyKeyboardMarkup(keyboard =
            [
            [KeyboardButton(text = 'return')],
            [KeyboardButton(text = 'News & Project examples main')],
            ])
            bot.sendMessage(from_id,text = 'Type "return" to return to last menu',reply_markup = keyboard_back_to_main_or_return)
            
        elif (query_data == 'Electronics News URL'):
            #--Push news one piece at a time--
            for n in range(0,5):
                bot.sendMessage(from_id,text = electronics(n,0))
            keyboard_back_to_main_or_return = ReplyKeyboardMarkup(keyboard =
                        [
                        [KeyboardButton(text = 'return')],
                        [KeyboardButton(text = 'News & Project examples main')],
                        ])
            bot.sendMessage(from_id,text = 'Type "return" to return to last menu',reply_markup = keyboard_back_to_main_or_return)
            
            
        elif (query_data == 'Hardware News URL'):
            #--Push news one piece at a time--
            for n in range(0,5):
                bot.sendMessage(from_id,text = hardware(n,0))
            keyboard_back_to_main_or_return = ReplyKeyboardMarkup(keyboard =
            [
            [KeyboardButton(text = 'return')],
            [KeyboardButton(text = 'News & Project examples main')],
            ])
            bot.sendMessage(from_id,text = 'Type "return" to return to last menu',reply_markup = keyboard_back_to_main_or_return)
            
    
TOKEN = '326542063:AAFTqDm9Mw281pPictZRnXa6fUAyUfmZ8Zc'
bot = DelegatorBot(TOKEN, [
    pave_event_space()
    (per_chat_id(), create_open, ProjectBot, timeout=1000)
])
MessageLoop(bot).run_as_thread()
print('Project bot at your service...')
while True:
    time.sleep(10)
