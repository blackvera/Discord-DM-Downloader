# Warning: This code has been obfuscated for privacy and protection purposes, but it is fully functional.

import os #line:1
import sys #line:2
import re #line:3
import datetime #line:4
def check_and_import (O0OOO000OOO0O0OOO ,pip_name =None ,color =None ):#line:6
    try :#line:7
        return __import__ (O0OOO000OOO0O0OOO )#line:8
    except ImportError :#line:9
        pip_name =pip_name or O0OOO000OOO0O0OOO #line:10
        color =color or '\033[91m'#line:11
        print (f"{color}The library '{pip_name}' is not installed. Install it with: pip install {pip_name}\033[0m")#line:12
        sys .exit (1 )#line:13
colorama =check_and_import ('colorama',color ='\033[95m')#line:15
from colorama import Fore ,Style #line:16
colorama .init ()#line:17
requests =check_and_import ('requests',color ='\033[96m')#line:18
COLORS ={"magenta":Fore .MAGENTA ,"cyan":Fore .CYAN ,"blue":Fore .BLUE ,"yellow":Fore .YELLOW ,"green":Fore .GREEN ,"red":Fore .RED ,"white":Fore .WHITE ,"reset":Style .RESET_ALL }#line:29
def colorize (O0OOOO0000OO0000O ):#line:31
    def OO00O000000OO00OO (OOOOOO00000000000 ):#line:32
        O00O0O0000O0OOO0O =OOOOOO00000000000 .group (1 )#line:33
        return COLORS .get (O00O0O0000O0OOO0O ,"")#line:34
    return re .sub (r"\{(.*?)\}",OO00O000000OO00OO ,O0OOOO0000OO0000O )+COLORS ["reset"]#line:35
os .system ('cls'if os .name =='nt'else 'clear')#line:37
print (colorize ("{white}┌─────────────────────────────────────────────┐{reset}\n" "{white}│{magenta}           DISCORD DM DOWNLOADER             {white}│{reset}\n" "{white}│{cyan}   by Nypher and Vera for Blackout Project   {white}│{reset}\n" "{white}│                                             │{reset}\n" "{white}│{blue}        https://linktr.ee/blackoutproj       {white}│{reset}\n" "{white}└─────────────────────────────────────────────┘{reset}"))#line:45
print ()#line:46
def get_messages (O00O0O00000OO0OOO ,OOO000OO0OO000O0O ):#line:48
    O000OOOO0000OO00O =f'https://discord.com/api/v10/channels/{O00O0O00000OO0OOO}/messages'#line:49
    O000O0OO0O0OO0000 ={'limit':100 }#line:50
    try :#line:51
        O0OO0O00OO00000OO =requests .get (O000OOOO0000OO00O ,headers =OOO000OO0OO000O0O ,params =O000O0OO0O0OO0000 )#line:52
        if O0OO0O00OO00000OO .status_code ==200 :#line:53
            return O0OO0O00OO00000OO .json ()#line:54
        else :#line:55
            print (f'Error: {O0OO0O00OO00000OO.status_code} - {O0OO0O00OO00000OO.text}')#line:56
            return None #line:57
    except Exception as O0O00O0OO00O00O0O :#line:58
        print (f"Error during request: {O0O00O0OO00O00O0O}")#line:59
        return None #line:60
def get_all_messages (OO0O000OOO000OOOO ,OOOOOOO00000OOOOO ):#line:62
    OO0OOOO00O00OOO00 =f'https://discord.com/api/v10/channels/{OO0O000OOO000OOOO}/messages'#line:63
    OO0OO0O00O0OOO00O =[]#line:64
    O0OO0OO00000O0O00 ={'limit':100 }#line:65
    O00000OOO00O0O0O0 =None #line:66
    while True :#line:67
        if O00000OOO00O0O0O0 :#line:68
            O0OO0OO00000O0O00 ['before']=O00000OOO00O0O0O0 #line:69
        try :#line:70
            O00OOOOOOO00OOO00 =requests .get (OO0OOOO00O00OOO00 ,headers =OOOOOOO00000OOOOO ,params =O0OO0OO00000O0O00 )#line:71
            if O00OOOOOOO00OOO00 .status_code ==200 :#line:72
                OO000O00OOO000OO0 =O00OOOOOOO00OOO00 .json ()#line:73
                if not OO000O00OOO000OO0 :#line:74
                    break #line:75
                OO0OO0O00O0OOO00O .extend (OO000O00OOO000OO0 )#line:76
                O00000OOO00O0O0O0 =OO000O00OOO000OO0 [-1 ]['id']#line:77
                if len (OO000O00OOO000OO0 )<100 :#line:78
                    break #line:79
            else :#line:80
                print (f'Error: {O00OOOOOOO00OOO00.status_code} - {O00OOOOOOO00OOO00.text}')#line:81
                break #line:82
        except Exception as O00OOO00OOOOOO000 :#line:83
            print (f"Error during request: {O00OOO00OOOOOO000}")#line:84
            break #line:85
    return OO0OO0O00O0OOO00O #line:86
while True :#line:88
    TOKEN =input (colorize ('{cyan}Enter your Discord token: {reset}')).strip ()#line:89
    if not TOKEN :#line:90
        print (colorize ('{red}Invalid token. Exiting.{reset}'))#line:91
        sys .exit (1 )#line:92
    CHANNEL_ID =input (colorize ('{cyan}Enter the DM channel ID: {reset}')).strip ()#line:93
    if not CHANNEL_ID :#line:94
        print (colorize ('{red}Invalid channel ID. Exiting.{reset}'))#line:95
        sys .exit (1 )#line:96
    headers ={'Authorization':TOKEN ,'User-Agent':'Mozilla/5.0'}#line:101
    messages =get_all_messages (CHANNEL_ID ,headers )#line:103
    if messages :#line:105
        messages =list (reversed (messages ))#line:106
        chunk_size =100 #line:107
        total =len (messages )#line:108
        num_files =(total +chunk_size -1 )//chunk_size #line:109
        folder_name =input (colorize ('{cyan}Enter the folder name to save the files: {reset}')).strip ()#line:110
        print ()#line:111
        if not folder_name :#line:112
            print (colorize ('{red}Invalid folder name. Exiting.{reset}'))#line:113
            sys .exit (1 )#line:114
        base_dir =os .path .dirname (os .path .abspath (__file__ ))#line:115
        save_dir =os .path .join (base_dir ,folder_name )#line:116
        os .makedirs (save_dir ,exist_ok =True )#line:117
        for i in range (num_files ):#line:118
            start =i *chunk_size #line:119
            end =min (start +chunk_size ,total )#line:120
            filename =f"dm_message{i+1}.txt"#line:121
            filepath =os .path .join (save_dir ,filename )#line:122
            with open (filepath ,'w',encoding ='utf-8')as f :#line:123
                for msg in messages [start :end ]:#line:124
                    author =msg .get ('author',{}).get ('username','Unknown')#line:125
                    content =msg .get ('content','')#line:126
                    f .write (f"{author}: {content}\n\n")#line:127
            print (colorize (f"{{green}}Messages saved to {filepath} ({{reset}}{{cyan}}{start+1}-{end}{{reset}}{{green}}){{reset}}"))#line:128
        print ()#line:129
        print (colorize ("{white}┌─────────────────────────────────────────────┐{reset}\n" "{white}│{green}         OPERATION COMPLETED!                 {white}│{reset}\n" "{white}│{cyan}   Your messages have been saved.            {white}│{reset}\n" "{white}└─────────────────────────────────────────────┘{reset}"))#line:135
    else :#line:136
        print ()#line:137
        print (colorize ("{white}┌─────────────────────────────────────────────┐{reset}\n" "{white}│{red}        NO MESSAGES RETRIEVED!                {white}│{reset}\n" "{white}│{yellow}   Check your token or channel ID.           {white}│{reset}\n" "{white}└─────────────────────────────────────────────┘{reset}"))#line:143
    choice =input (colorize ("\n{cyan}Do you want to perform another download? (y/n): {reset}")).strip ().lower ()#line:144
    if choice !='y':#line:145
        print (colorize ("{cyan}Goodbye!{reset}"))#line:146
        sys .exit (0 )#line:147
