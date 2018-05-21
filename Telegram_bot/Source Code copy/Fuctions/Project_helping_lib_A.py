import telepot
import time
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import csv
bot = telepot.Bot('326542063:AAFTqDm9Mw281pPictZRnXa6fUAyUfmZ8Zc')
def welcome_keyboard():
    tmp = ReplyKeyboardMarkup(keyboard =
    [
    [KeyboardButton(text ='Got idea! Find teammates! / Do not have an idea, but want to join a project！' )],

    [KeyboardButton(text = 'Do not have an idea yet. Looking forward to getting inspired!')]

    ])
    return tmp
def project_keyboard():
    tmp = ReplyKeyboardMarkup(keyboard =
    [
    [KeyboardButton(text = 'Electronic devices')],

    [KeyboardButton(text = 'Computer software')],
    
    [KeyboardButton(text = 'Robots')]

    ])
    return tmp
def news_keyboard():
    tmp = ReplyKeyboardMarkup(keyboard =
    [
    [KeyboardButton(text = 'hahahahahahah')],

    [KeyboardButton(text = 'lalalalallalal')],
    
    [KeyboardButton(text = 'emmmmmmmmmmmmm')],
    
    [KeyboardButton(text = '......')]
    
    ])
    return tmp
def project_add():
    tmp = ReplyKeyboardMarkup(keyboard =
    [
    [KeyboardButton(text = 'Yes,I would like to add my info.')],

    [KeyboardButton(text = 'Not now, I would like to see the database first, thanks.')],

    [KeyboardButton(text = 'I would like to delete my info from the database.')]
    
    ])
    return tmp
def confirm_add_info_E():
    tmp = InlineKeyboardMarkup(inline_keyboard =
    [
    [InlineKeyboardButton(text = 'Confirm',callback_data= 'Confirm add info to E')],

    [InlineKeyboardButton(text = 'Cancel',callback_data= 'Cancel add info')]
    
    ])
    return tmp
def confirm_add_info_C():
    tmp = InlineKeyboardMarkup(inline_keyboard =
    [
    [InlineKeyboardButton(text = 'Confirm',callback_data= 'Confirm add info to C')],

    [InlineKeyboardButton(text = 'Cancel',callback_data= 'Cancel add info')]
    
    ])
    return tmp
def confirm_add_info_R():
    tmp = InlineKeyboardMarkup(inline_keyboard =
    [
    [InlineKeyboardButton(text = 'Confirm',callback_data= 'Confirm add info to R')],

    [InlineKeyboardButton(text = 'Cancel',callback_data= 'Cancel add info')]
    
    ])
    return tmp
def confirm_info():
    tmp = ReplyKeyboardMarkup(keyboard =
    [
        
    [KeyboardButton(text = 'Confirm info')],

    [KeyboardButton(text = 'Emmmmm....')]
    
    ])
    return tmp
def Count_E_students():
    with open('Electronic.csv',newline = '') as file:
        file_read = csv.reader(file, delimiter = ',')
        count = 0
        for row in file_read:
            if row != []:
                if row[0] != 'Name':
                    count += 1
                else:
                    pass
            else: pass
    return count
def Count_C_students():
    with open('Computer Software.csv',newline = '') as file:
        file_read = csv.reader(file, delimiter = ',')
        count = 0
        for row in file_read:
            if row != []:
                if row[0] != 'Name':
                    count += 1
                else:
                    pass
            else: pass
    return count
def Count_R_students():
    with open('Robots.csv',newline = '') as file:
        file_read = csv.reader(file, delimiter = ',')
        count = 0
        for row in file_read:
            if row != []:
                if row[0] != 'Name':
                    count += 1
                else:
                    pass
            else: pass
    return count
def Browse_datails_E(ID,num):
    with open('Electronic.csv',newline = '') as file:
        file_read = csv.reader(file,delimiter = ',')
        if num == 0:
            bot.sendMessage(ID,'We haven\'t got any info yet. you can be the first one!')
        else:
            for row in file_read:
                if row != []:
                    if row[0] != 'Name':
                        try:
                            bot.sendMessage(ID,'Name: ' + row[0] + '\nSchool: ' + row[1] + '\nYear: ' + row[2] + '\nSex: ' + row[3] + '\nContact: ' + row[4] + '\nE-mail: ' + row[5] + '\nIdea: ' + row[6])
                        except Exception as IndexError:
                            bot.sendMessage(ID,'This user\'s info has not been completed')
                            pass
                        
                    else:
                        pass
                else:
                    pass
                
        answer = ReplyKeyboardMarkup(keyboard =
        [
        [KeyboardButton(text = 'Contact them')],

        [KeyboardButton(text = 'Not now, thanks')]
        
        ])
        
        bot.sendMessage(ID,'That\'s all, do you want to join them?\nGet their info and contact them.',reply_markup = answer)
        
def Browse_datails_C(ID,num):
    with open('Computer Software.csv',newline = '') as file:
        file_read = csv.reader(file,delimiter = ',')
        if num == 0:
            bot.sendMessage(ID,'We haven\'t got any info yet. You can be the first one!')
        else:
            for row in file_read:
                if row != []:
                    if row[0] != 'Name':
                        try:
                            bot.sendMessage(ID,'Name: ' + row[0] + '\nSchool: ' + row[1] + '\nYear: ' + row[2] + '\nSex: ' + row[3] + '\nContact: ' + row[4] + '\nE-mail: ' + row[5] + '\nIdea: ' + row[6])
                        except Exception as IndexError:
                            bot.sendMessage(ID,'This user\'s info has not been completed')
                            pass
                    else:
                        pass
                else:
                    pass
                
        answer = ReplyKeyboardMarkup(keyboard =
        [
        [KeyboardButton(text = 'Contact them')],

        [KeyboardButton(text = 'Not now, thanks')]
        
        ])
        
        bot.sendMessage(ID,'That\'s all, do you want to join them?\nGet their info and contact them.',reply_markup = answer)
        
def Browse_datails_R(ID,num):
    with open('Robots.csv',newline = '') as file:
        file_read = csv.reader(file,delimiter = ',')
        if num == 0:
            bot.sendMessage(ID,'We haven\'t got any info yet. You can be the first one!')
        else:
            for row in file_read:
                if row != []:
                    if row[0] != 'Name':
                        try:
                            bot.sendMessage(ID,'Name: ' + row[0] + '\nSchool: ' + row[1] + '\nYear: ' + row[2] + '\nSex: ' + row[3] + '\nContact: ' + row[4] + '\nE-mail: ' + row[5] + '\nIdea: ' + row[6])
                        except Exception as IndexError:
                            bot.sendMessage(ID,'This user\'s info has not been completed')
                            pass
                    else:
                        pass
                else:
                    pass
        answer = ReplyKeyboardMarkup(keyboard =
        [
        [KeyboardButton(text = 'Contact them')],

        [KeyboardButton(text = 'Not now, thanks')]
        
        ])
        bot.sendMessage(ID,'That\'s all, do you want to join them?\nGet their info and contact them.',reply_markup = answer)
                
def ask_if_news():
    tmp = ReplyKeyboardMarkup(keyboard =
    [
    [KeyboardButton(text = 'Sure')],

    [KeyboardButton(text = 'No thanks')]
    
    ])
    return tmp
def add_to_database_E(info):
    with open("Electronic.csv",'a',newline = '') as target_file:
        file_app = csv.writer(target_file)
        file_app.writerow(info)

def add_to_database_C(info):
    with open("Computer Software.csv",'a',newline = '') as target_file:
        file_app = csv.writer(target_file)
        file_app.writerow(info)

def add_to_database_R(info):
    with open("Robots.csv",'a',newline = '') as target_file:
        file_app = csv.writer(target_file)
        file_app.writerow(info)
        
def delete_info_from_E_first(deletename):
    with open('Electronic.csv', 'r', newline = '') as get_file:
        check = []
        rows = []
        file_read = csv.reader(get_file,delimiter = ',')
        for row in file_read:
            print(row)
            if row != []:
                if row[0] != 'Name' and row[0] != deletename:
                    check.append(row[0])
                    rows.append(row)
                else:
                    pass
            else:
                pass
        print(check)
        print(rows)
        return rows

def delete_info_from_E_second(rows):
    with open ('Electronic.csv','w', newline = '') as output_file:
        file_write = csv.writer(output_file) 
        file_write.writerows(rows)
        
def delete_info_from_C_first(deletename):
    with open('Computer Software.csv', 'r', newline = '') as get_file:
        check = []
        rows = []
        file_read = csv.reader(get_file,delimiter = ',')
        for row in file_read:
            print(row)
            if row != []:
                if row[0] != 'Name' and row[0] != deletename:
                    check.append(row[0])
                    rows.append(row)
                else:
                    pass
            else:
                pass
        print(check)
        print(rows)
        return rows

def delete_info_from_C_second(rows):
    with open ('Computer Software.csv','w', newline = '') as output_file:
        file_write = csv.writer(output_file) 
        file_write.writerows(rows)

def delete_info_from_R_first(deletename):
    with open('Robots.csv', 'r', newline = '') as get_file:
        check = []
        rows = []
        file_read = csv.reader(get_file,delimiter = ',')
        for row in file_read:
            print(row)
            if row != []:
                if row[0] != 'Name' and row[0] != deletename:
                    check.append(row[0])
                    rows.append(row)
                else:
                    pass
            else:
                pass
        print(check)
        print(rows)
        return rows

def delete_info_from_R_second(rows):
    with open ('Robots.csv','w', newline = '') as output_file:
        file_write = csv.writer(output_file) 
        file_write.writerows(rows)

    

    
    

        
        
