import random
import string
import os

PASSWORD_MIN_LENGTH = 6
PASSWORD_MAX_LENGTH = 30
settings = {
    'lower' : True,
    'upper' : True,
    'symbol' : True,
    'number' : True,
    'space' : False,
    'length' : 8 
}

def clear_screen():
    os.system('cls')

def get_password_length_user(defult,min_length_pass = PASSWORD_MIN_LENGTH ,max_length_pass= PASSWORD_MAX_LENGTH):
    while True:
        password_length_new = input(f'Defult value password = {defult}. '
        ' Enter your desired length(enter = defult):')
        if password_length_new == '':
            return defult
        if password_length_new.isdigit():
            len_pass = int(password_length_new)
            if min_length_pass <= len_pass <= max_length_pass : 
                return int(password_length_new)
            print(f'Your input is not valid . enter a number in range {min_length_pass}' 
            'fand {max_length_pass}).')
                             
        else:
            print('Your input is not valid . plz try again.')  

def get_setting_from_users(settings):
    for option, defult in settings.items():
        if option !='length':
            settings[option]=get_user_yes_no(option,defult)           
        else:
            settings[option] = get_password_length_user(defult)

def ask_change_setting(settings):
    while True:
        print(f'Defult setting is{settings}')
        user_response= input('Do you want to change settings (y:yes, n:no, enter:yes) ? ')
        if user_response in ['n','y','']:
            if user_response in ['y','']:
                print('_'*31 , 'CHANGE SETTING' ,'_'*31, sep='*')
                print()
                get_setting_from_users(settings)
            break
        else:
            print()
            print('Your input is not valid . plz try again.')
            print()
   
def get_user_yes_no(option,defult):
    while True:
        user_input = input(f'Include {option} ? Defult value is {defult}.(y:Yes , n:No) : ') 
        if user_input == '':
            return defult
    
        if  user_input in ['y','n'] :   
            return user_input == 'y'
        
        print('Your input is not valid . plz try again.')

def password_generator(settings):
    password_len = settings['length']
    final_pass = ''
    choeices = list(filter(lambda x:settings[x], ['lower','upper','number','symbol','space']))
    # settings(x) == True , x=['lower','upper','number','symbol','space']
    for i in range(password_len):
        final_pass += generator_random_char (choeices)
    return final_pass
     
def generator_random_char (choeices):
    choeice = random.choice(choeices)
    if choeice == 'upper':
        return random.choice(string.ascii_uppercase)
    elif choeice == 'lower':
        return random.choice(string.ascii_lowercase)
    elif choeice == 'symbol':
        return random.choice("""!"#$%^&'@*()+-/[\]_=|?<>:;{}~`.,""")
    elif choeice == 'space':
        return ' '
    elif choeice == 'number':
        return random.choice('0123456789')

def repeat_generation(settings):
    while True:
        print('_'*78)
        print(f'Generated Password:  {password_generator(settings)}')
        print('')
        if check_repeat_another_generate() == False:
            break      

def check_repeat_another_generate():
    while True:
        user_request = input('Regenerate(y:yes, n:no, enter:yes) ? ')
        if user_request in ['n','y','']:
            if user_request == 'n':
                return False
            return True
            
        else:
            print('Invalid input.choose from(y:yes, n:no, enter:yes): ')
            print('Try again')

def run():
    clear_screen()
    print('_'*20, 'Welcome to genrator passwoed program','_'*20)
    print()
    ask_change_setting(settings)
    repeat_generation(settings) 
    print()
    print('Thank you for choosing us :) ')

run()