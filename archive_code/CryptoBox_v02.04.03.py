# __________/\\\\\\\\\________________________________________________________________________/\\\\\\\\\\\\\__________________________________
#  _______/\\\////////________________________________________________________________________\/\\\/////////\\\________________________________
#   _____/\\\/____________________________/\\\__/\\\___/\\\\\\\\\______/\\\____________________\/\\\_______\/\\\________________________________
#    ____/\\\______________/\\/\\\\\\\____\//\\\/\\\___/\\\/////\\\__/\\\\\\\\\\\_____/\\\\\____\/\\\\\\\\\\\\\\______/\\\\\_____/\\\____/\\\____
#     ___\/\\\_____________\/\\\/////\\\____\//\\\\\___\/\\\\\\\\\\__\////\\\////____/\\\///\\\__\/\\\/////////\\\___/\\\///\\\__\///\\\/\\\/_____
#      ___\//\\\____________\/\\\___\///______\//\\\____\/\\\//////______\/\\\_______/\\\__\//\\\_\/\\\_______\/\\\__/\\\__\//\\\___\///\\\/_______
#       ____\///\\\__________\/\\\__________/\\_/\\\_____\/\\\____________\/\\\_/\\__\//\\\__/\\\__\/\\\_______\/\\\_\//\\\__/\\\_____/\\\/\\\______
#        ______\////\\\\\\\\\_\/\\\_________\//\\\\/______\/\\\____________\//\\\\\____\///\\\\\/___\/\\\\\\\\\\\\\/___\///\\\\\/____/\\\/\///\\\____
#         _________\/////////__\///___________\////________\///______________\/////_______\/////_____\/////////////_______\/////_____\///____\///_____
#          ____________________________________________________________________________________________________________________________________________
#           ____/\\\\\_____/\\\____________________________________/\\\\\\______________________________________________________________________________
#            ___\/\\\\\\___\/\\\___________________________________\////\\\______________________________________________________________________________
#             ___\/\\\/\\\__\/\\\__/\\\___/\\\\\\\\____________________\/\\\______________________________________________________________________________
#              ___\/\\\//\\\_\/\\\_\///___/\\\////\\\_____/\\\\\\\\_____\/\\\______________________________________________________________________________
#               ___\/\\\\//\\\\/\\\__/\\\_\//\\\\\\\\\___/\\\/////\\\____\/\\\______________________________________________________________________________
#                ___\/\\\_\//\\\/\\\_\/\\\__\///////\\\__/\\\\\\\\\\\_____\/\\\______________________________________________________________________________
#                 ___\/\\\__\//\\\\\\_\/\\\__/\\_____\\\_\//\\///////______\/\\\______________________________________________________________________________
#                  ___\/\\\___\//\\\\\_\/\\\_\//\\\\\\\\___\//\\\\\\\\\\__/\\\\\\\\\___________________________________________________________________________
#                   ___\///_____\/////__\///___\////////_____\//////////__\/////////____________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________________________

#   Initial version was built in July 2016                                       #
#                                                                                #
#   Version Number Defination:                                                   #
#   v01.01.01 20170513                                                           #
#    -- -- --                                                                    #
#     |  |  |                                                                    #
#     |  |  +------     GUI Updates                                              #
#     |  +---------     Crypto Function Updates                                  #
#     +------------     Published Version (Major Change)                         #
#                                                                                #
# _______________________________________________________________________________#
#
#   DES operation works very well on v00.09.09.x 201610xx
#   v00.09.09 has been added new buttons:
#   01. TDES algorithm has been added !!! Works well !!!
#   02. AES  algorithm has been added !!! Works well !!!
#   03. Random number generator has been added !!! Works well !!!
#   04. Added a Exit button to quit program !!! Works well !!!
#   05. Added algo_tab (x6). SHA and RSA are not completed xxx - (RSA is not correct - 20161219)
#       RSA calculation is correct - 20170301
#   06. Adding the menu bar.............(No idea so far how to do so :( )
#   07. DES/TDES function is corrected !!!
#   08. Adding length counter after key and iv fileds..............(No idea :( )
#   09. Adding fileopen function for RSA key-file and data-file import
#   10. Adding Hash function and GUI...........all done except HMAC operation
#   11. Scrollbar has not been added due to lack of knowledge............
#   12. Incorrect key length error message is removed in DES/TDES - solved!!!
#   13. "Use output as the key" function is added!!!
#   14. Correct all fonts !!!
#   15. Digital clock and counter for 120PIN have been completed !!!
#   16. RSA datainput and dataoutput text box works well !!!
#   17. RSA calculation is fully solved !!!!!!! 20170301
#   18. David gave me a suggestion on using RSA.construct((n, e, d)) to import keys
#   19. RSA.construct() is being used correctly!!! 20170301
#   20. Code migration from Python2 to Python3 20230825 - v02.01.01
#   21. Correcting the functionalities in the Python3 code 20230919 - v02.01.02
#   22. Released final version - v02.02.00
#   23. Adding new files hasing - v02.03.xx - from 2024.10.25
#   24. Adding password generator - v02.04.01 - Done on 2025.05.28
#   25. Changing icon to a single file - v02.04.02 - Done on 2025.08.04         
#   26. Updated icon style - v02.04.04 - Done on 2025.09.04         
# ______________________________________________________________________________#

#   Python Execution Guidance                                                   #    
#                                                                               #
#   pip3 uninstall pycrypto     (if an old version was installed)               #
#   pip3 uninstall crypto       (if an old version was installed)               #
#   pip3 uninstall pycrypto     (if an old version was installed)               #
#   python.exe -m pip install --upgrade pip                                     #
#   pip3 install pycryptodome                                                   #
#   pip3 install pyOpenSSL                                                      #
# ______________________________________________________________________________#

from tkinter import *
from tkinter import messagebox, filedialog, messagebox, ttk
from tkinter import filedialog as fd  # imports the filedialog  box

#   Crypto import
from Crypto.Cipher import DES, DES3, AES, PKCS1_OAEP
from Crypto.Hash import SHA, SHA224, SHA256, SHA384, SHA512, MD4, MD5, HMAC
from Crypto.Hash import SHA3_224, SHA3_256, SHA3_384, SHA3_512
from Crypto.PublicKey import RSA
from Crypto.Util.asn1 import DerSequence
from binascii import a2b_base64
from OpenSSL import SSL
# from crcmod import predefined
from Crypto import Random
from datetime import date
#from pyasn1_modules import pem, rfc2459
#from pyasn1.codec.der import decoder

import os, operator
import codecs
import socket
import string
import select
import binascii
import time
import webbrowser
import hashlib
import secrets
import base64

# === Paste your Base64 encoded PNG string here ===
ICON_PNG_BASE64 = """
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cGUvUmVzb3VyY2VFdmVudCMiCiAgICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgICB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyIKICAgIHhtbG5zOkdJTVA9Imh0dHA6Ly93d3cuZ2ltcC5vcmcveG1wLyIKICAgIHhtbG5zOmlwdGNFeHQ9Imh0dHA6Ly9pcHRjLm9yZy9zdGQvSXB0YzR4bXBFeHQvMjAwOC0wMi0yOS8iCiAgICB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iCiAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgeG1wTU06RG9jdW1lbnRJRD0iZ2ltcDpkb2NpZDpnaW1wOmE4MzRhNmI1LWQyMDAtNGEzZC05NWZmLTI2ODlkNzIzOTlkMCIKICAgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDphNDczZjIyNy02MTAwLTQ3NTAtOGI4OC00NDUyMzkyOWQxOWMiCiAgIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDoxZTkwM2UyNy1jZmMwLTQ4NzAtYjE0Mi1mZTI4MjczMTQ3YTAiCiAgIGRjOkZvcm1hdD0iaW1hZ2UvcG5nIgogICBleGlmOkRhdGVUaW1lT3JpZ2luYWw9IjIwMjUtMDktMDNUMDY6Mzk6MTArMDA6MDAiCiAgIEdJTVA6QVBJPSIyLjAiCiAgIEdJTVA6UGxhdGZvcm09IldpbmRvd3MiCiAgIEdJTVA6VGltZVN0YW1wPSIxNzU2ODgxODY3NzE2MTExIgogICBHSU1QOlZlcnNpb249IjIuMTAuMzAiCiAgIGlwdGNFeHQ6RGlnaXRhbFNvdXJjZUZpbGVUeXBlPSJodHRwOi8vY3YuaXB0Yy5vcmcvbmV3c2NvZGVzL2RpZ2l0YWxzb3VyY2V0eXBlL2NvbXBvc2l0ZVdpdGhUcmFpbmVkQWxnb3JpdGhtaWNNZWRpYSIKICAgaXB0Y0V4dDpEaWdpdGFsU291cmNlVHlwZT0iaHR0cDovL2N2LmlwdGMub3JnL25ld3Njb2Rlcy9kaWdpdGFsc291cmNldHlwZS9jb21wb3NpdGVXaXRoVHJhaW5lZEFsZ29yaXRobWljTWVkaWEiCiAgIHBob3Rvc2hvcDpDcmVkaXQ9IkVkaXRlZCB3aXRoIEdvb2dsZSBBSSIKICAgcGhvdG9zaG9wOkRhdGVDcmVhdGVkPSIyMDI1LTA5LTAzVDA2OjM5OjEwKzAwOjAwIgogICB0aWZmOk9yaWVudGF0aW9uPSIxIgogICB4bXA6Q3JlYXRvclRvb2w9IkdJTVAgMi4xMCI+CiAgIDx4bXBNTTpIaXN0b3J5PgogICAgPHJkZjpTZXE+CiAgICAgPHJkZjpsaQogICAgICBzdEV2dDphY3Rpb249InNhdmVkIgogICAgICBzdEV2dDpjaGFuZ2VkPSIvIgogICAgICBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjllMmQxYTUwLTcyMWEtNDU1MC05Y2RkLTA2ZmM0ZDJiYTQ3OCIKICAgICAgc3RFdnQ6c29mdHdhcmVBZ2VudD0iR2ltcCAyLjEwIChXaW5kb3dzKSIKICAgICAgc3RFdnQ6d2hlbj0iMjAyNS0wOS0wM1QxNjo0MjoyNCIvPgogICAgIDxyZGY6bGkKICAgICAgc3RFdnQ6YWN0aW9uPSJzYXZlZCIKICAgICAgc3RFdnQ6Y2hhbmdlZD0iLyIKICAgICAgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDpkZmMxZjVmOC00NTIxLTQ5YzMtODA0YS03ODMzYzY4NThhMTkiCiAgICAgIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkdpbXAgMi4xMCAoV2luZG93cykiCiAgICAgIHN0RXZ0OndoZW49IjIwMjUtMDktMDNUMTY6NDQ6MjciLz4KICAgIDwvcmRmOlNlcT4KICAgPC94bXBNTTpIaXN0b3J5PgogIDwvcmRmOkRlc2NyaXB0aW9uPgogPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg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
"""

key_pub_filename = ''
key_pri_filename = ''
input_filename = ''
p120_butt_clicked = 0


def update_timeText():
    # Get the current time, note you can change the format as you wish
    current = time.strftime("%Y/%m/%d  %H:%M:%S")
    # Update the timeText Label box with the current time
    realtime.configure(text=current)
    # Call the update_timeText() function after 1 second
    root.after(100, update_timeText)


root = Tk()
CryB_ver = "02.04.03"
CryB_yr = "2025.08.04"
root.title('CryptoBox' + " (v" + CryB_ver +")" + " - " + CryB_yr + " - Nigel Zhai")
root.geometry("540x500+200+200")    #("560x480+0+0") for Linux; ("530+470+20+20") for Windows
root.minsize(540, 500)
root.maxsize(540, 500)
root.resizable(False, False)
algo_tab = ttk.Notebook(root)
frame_1_TDES = ttk.Frame(algo_tab)
frame_2_AES = ttk.Frame(algo_tab)
frame_3_1_RSA = ttk.Frame(algo_tab)
frame_3_2_RSA = ttk.Frame(algo_tab)
frame_3_3_RSA = ttk.Frame(algo_tab)
frame_4_HASH = ttk.Frame(algo_tab)
frame_5_XOR = ttk.Frame(algo_tab)
frame_6_RNG = ttk.Frame(algo_tab)
frame_6_PWD = ttk.Frame(algo_tab)
frame_7_120 = ttk.Frame(algo_tab)
frame_8_ABT = ttk.Frame(algo_tab)
algo_tab.add(frame_1_TDES, text='TDES\n')
algo_tab.add(frame_2_AES, text='AES\n')
algo_tab.add(frame_3_1_RSA, text='RSA\nGen.')
algo_tab.add(frame_3_2_RSA, text='RSA\nImport.')
algo_tab.add(frame_3_3_RSA, text='RSA\nCrypto.')
algo_tab.add(frame_4_HASH, text='HASH\n')
algo_tab.add(frame_5_XOR, text='XOR\n')
algo_tab.add(frame_6_RNG, text='RNG\n')
algo_tab.add(frame_6_PWD, text='PWD\nGen')
algo_tab.add(frame_7_120, text='120PINs\n')
algo_tab.add(frame_8_ABT, text='About\n...')
algo_tab.pack()
operation_SLC_DES = IntVar()
operation_SLC_TDES = IntVar()
operation_SLC_AES = IntVar()
operation_SLC_RSA = IntVar()
operation_SLC_HASH = IntVar()
operation_SLC_HASH_hmac = IntVar()

# Enc_Dec_SLC_DES = IntVar()
# Enc_Dec_SLC_TDES = IntVar()
# Enc_Dec_SLC_AES = IntVar()
MODE_SLC_TDES = IntVar()
MODE_SLC_AES = IntVar()
KEY_IMPORT_METHOD = IntVar()
HASH_SOURCE_IMPORT_METHOD = IntVar()

default_TDES_key = StringVar(frame_1_TDES, value = "0123456789ABCDEF123456789ABCDEF0")
default_AES_key  = StringVar(frame_2_AES,  value = "0123456789ABCDEF123456789ABCDEF0")
default_iv_8B    = StringVar(frame_1_TDES, value = "0000000000000000")
default_iv_16B   = StringVar(frame_2_AES,  value = "00000000000000000000000000000000")

global temp_d, temp_e, temp_n

# Create a timeText Label (a text box)
realtime = Label(root, text="", font=("Helvetica", 20))
realtime.pack(side=LEFT)
# Creat a Exit button
exit_button = Button(root, text="Exit", width=10, bg='#FF5C5C', command=root.quit)
exit_button.pack(side=RIGHT)
exit_button.place(x=438, y=465)

abt_msg = '''
The CryptoBox is a UL-TS cryptographic calculator developed internally.
It supports multiple algorithms include single DES, triple TDES, AES, RSA,
HASH, as well as exclusive OR operation, random number generator,and 
other non-cryptographic features.\n\n
Please contact the developer if you have any suggestion or feedback
on the current CryptoBox.\n\n
Thank you for using CryptoBox!
'''

pwd_gen_msg = '''
Pwassword Generator is a tool to generate random passwords with:
- Uppercase letters
- Lowercase letters
- Digits
- Special characters\n
'''

class MenuBar(Frame):
    def __init__(self):
        Frame.__int__(self)
        self.menubar = Menu(self)
        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(lable="About", menu=menu)
        menu.add_command(label="Copyright")




class CryptoBox(Tk):
    #   GUI interface definition
    print("\n\n=======================================")
    print(    "|--    Welcome to use CryptoBox     --|")
    print(    "|--                                 --|")
    print(    "|-- Author  : todearnigel@gmail.com --|")
    print(    "|-- Version :", CryB_ver, "             --|")
    print(    "|-- Date    :", CryB_yr, "           --|")
    print(    "=======================================\n\n")
    
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.set_window_icon() # Call the new function here

    def set_window_icon(self):
        try:
            # Decode the Base64 string to get the PNG image data
            # The base64 library is already imported
            icon_data = base64.b64decode(ICON_PNG_BASE64)
            # Create a PhotoImage from the decoded data
            # Use 'data=' parameter to pass the raw image data
            photo_image = PhotoImage(data=icon_data)
            # Set the window icon using the PhotoImage object
            self.iconphoto(True, photo_image)
        except Exception as e:
            # Handle potential errors during decoding or image creation
            print(f"Error setting window icon: {e}")


    #   Crypto function - DES
    def execution_TDES(self):
        #   algo & operation Judgment
        selection_EorD = operation_SLC_TDES.get()
        key_raw_xDES = self.key_textbox_TDES.get()
        key_len_check = (len(key_raw_xDES))/2
        #print 'key len                :', key_len_check
        '''
        if key_len_check != 8 or key_len_check != 16 or key_len_check != 24:
            self.output_textbox_TDES.delete(1.0, END)
            self.output_textbox_TDES.insert(1.0, "TDES Key length is not correct!")
        else:
            pass
        '''

        # python_2 grammar:
        # hkey_xDES = key_raw_xDES.replace(' ', '').decode('hex')
        hkey_xDES = bytes.fromhex(key_raw_xDES.replace(' ', ''))
        key_len = (len(key_raw_xDES))//2        
        # print("\nDES/TDES key           :", hkey_xDES.encode('hex'))
        print("\nDES/TDES key           :", key_raw_xDES)
        # print hkey_xDES.encode('hex')
        # print "\nhkey value",hkey_xDES
        # print hkey_xDES
        iv_raw_xDES = self.iv_textbox_TDES.get()
        # python_2 grammar:
        # hiv_xDES = iv_raw_xDES.replace(' ', '').decode('hex')
        hiv_xDES = bytes.fromhex(iv_raw_xDES.replace(' ', ''))
        
        # -2- print("initialization vector  :", hiv_xDES.encode('hex'))
        print("initialization vector  :", iv_raw_xDES)
        # print hiv_xDES.encode('hex')
        input_raw_xDES = self.input_textbox_TDES.get()
        
        # print des_inpD
        # python_2 grammar:
        # h_in_data_xDES = input_raw_xDES.replace(' ', '').decode('hex')
        h_in_data_xDES = bytes.fromhex(input_raw_xDES.replace(' ', ''))
        print("DES input data         :", input_raw_xDES)
        if key_len<9:
            print("DES/TDES key length    :", key_len, " | <Byte>")
        else:
            print("DES/TDES key length    :", key_len, "| <Bytes>")
        print("Encryption/Decryption  :", selection_EorD, " | <1:Encryption; 2:Decryption>")
        
        if selection_EorD == 0:
            self.output_textbox_TDES.delete(1.0, END)
            self.output_textbox_TDES.insert(1.0, "Operation is not correct")
        elif selection_EorD == 1 and key_len == 8:  # Enc operation
            #   'mode' Judgment - single DES does't need a mode selection
            #   ECB as a default mode
            mode = DES.MODE_ECB
            # obj = DES.new(hkey_xDES, mode, hiv_xDES)
            obj = DES.new(hkey_xDES, mode)
            #   Encryption !!
            output_raw_e = obj.encrypt(h_in_data_xDES)
            h_out_data_e = output_raw_e.hex().upper()
            print("DES output (Enc)       :", h_out_data_e)
            # print h_out_data_e
            # print output_raw_e
            self.output_textbox_TDES.delete(1.0, END)
            self.output_textbox_TDES.insert(1.0, h_out_data_e)
        elif selection_EorD == 2 and key_len == 8:  # Dec operation
            #   'mode' Judgment - single DES does't need a mode selection
            #   ECB as a default mode
            mode = DES.MODE_ECB
            # obj = DES.new(hkey_xDES, mode, hiv_xDES)
            obj = DES.new(hkey_xDES, mode)
            #   Decryption !!
            output_raw_d = obj.decrypt(h_in_data_xDES)
            h_out_data_d = output_raw_d.hex().upper()
            print("DES output (Dec)       :", h_out_data_d)
            # print h_out_data_d
            # print output_raw_d
            # return pt.encode('hex')
            self.output_textbox_TDES.delete(1.0, END)
            self.output_textbox_TDES.insert(1.0, h_out_data_d)

        elif key_len == 16 or key_len == 24:  # TDES algo
            mode_judge = MODE_SLC_TDES.get()
            if mode_judge == 1:
                mode = DES.MODE_ECB
            elif mode_judge == 2:
                mode = DES.MODE_CBC
            elif mode_judge == 3:
                mode = DES.MODE_CFB
            elif mode_judge == 4:
                mode = DES.MODE_OFB
            else:
                self.output_textbox_TDES.delete(1.0, END)
                self.output_textbox_TDES.insert(1.0, "Select a correct mode please.")
            # DES.MODE_ECB, DES.MODE_CBC, DES.MODE_OFB
            # mode = MODE_SLC_TDES.get()  
            print("TDES mode is           :", mode_judge, " | <1:ECB, 2:CBC, 3:CFB, 4:OFB>")
            #   'Enc/Dec' Judgment, and execute!!!
            if selection_EorD == 0:
                self.output_textbox_TDES.delete(1.0, END)
                self.output_textbox_TDES.insert(1.0, "Please select an operation")

            elif selection_EorD == 1 :  # Enc operation
                #   'mode' Judgment - single DES does't need a mode selection
                #   ECB as a default mode
                # mode = DES.MODE_ECB
                # obj = DES3.new(hkey_xDES, mode, hiv_xDES)
                
                #   ECB does not requires iv. Avoid iv in obj
                if mode_judge == 1:
                    obj = DES3.new(hkey_xDES, DES.MODE_ECB)
                else:
                    obj = DES3.new(hkey_xDES, mode, hiv_xDES)
                
                #   Encryption !! - TDES
                output_raw_e = obj.encrypt(h_in_data_xDES)
                # -2- h_out_data_e = output_raw_e.encode('hex').upper()
                str_out_data_e = output_raw_e.hex().upper()
                print("TDES output (Enc)      :", str_out_data_e)
                # print str_out_data_e
                # print output_raw_e
                self.output_textbox_TDES.delete(1.0, END)
                self.output_textbox_TDES.insert(1.0, str_out_data_e)

            elif selection_EorD == 2:  # Dec operation
                #   'mode' Judgment - single DES does't need a mode selection
                #   ECB as a default mode
                # mode = DES.MODE_ECB

                if mode_judge == 1:
                    obj = DES3.new(hkey_xDES, DES.MODE_ECB)
                else:
                    obj = DES3.new(hkey_xDES, mode, hiv_xDES)
                

                #   Decryption !! - TDES
                output_raw_d = obj.decrypt(h_in_data_xDES)
                h_out_data_d = output_raw_d.hex().upper()
                print("TDES output (Dec)     :", h_out_data_d)
                # print h_out_data_d
                # print output_raw_d
                # return pt.encode('hex')
                self.output_textbox_TDES.delete(1.0, END)
                self.output_textbox_TDES.insert(1.0, h_out_data_d)
            else:
                print("\nUnknow error. Please contact with Nigel through todearnigel@gmail.com")
        else:
            pass  # algo END
        # else: pass
        #   Crypto function - TDES

    #   Magic function - use output as a new xDES key
    def copy_key_value_TDES(self):
        key_temp_value_TDES = self.output_textbox_TDES.get(1.0, END)
        self.output_textbox_TDES.delete(1.0, END)
        self.key_textbox_TDES.delete(0, END)
        key_temp_value_TDES_no_0 = key_temp_value_TDES.replace("\r", '')
        print("key_temp_value_TDES_no_0", key_temp_value_TDES_no_0, key_temp_value_TDES_no_0)
        self.key_textbox_TDES.insert(0, key_temp_value_TDES)
        print("new key value:", key_temp_value_TDES)
        print("copy the TDES output value to key value...")


    #   Crypto function - AES
    def execution_AES(self):
        # print "AES Algo is under developing..."
        selection_aes_EorD = operation_SLC_AES.get()
        key_raw_AES = self.key_textbox_AES.get()
        key_aes_len = (len(key_raw_AES))//2
        
        key_len_check_aes = len(key_raw_AES)
        if key_len_check_aes != 32 or key_len_check_aes != 48 or key_len_check_aes != 64:
            self.output_textbox_AES.delete(1.0, END)
            self.output_textbox_AES.insert(1.0, "AES Key length or other parameter is not correct !")
        else:
            pass

        hkey_AES = bytes.fromhex(key_raw_AES.replace(' ', ''))
        print("\nAES key                :", key_raw_AES)
        iv_raw_AES = self.iv_textbox_AES.get()
        hiv_AES = bytes.fromhex(iv_raw_AES.replace(' ', ''))
        print("initialization vector  :", iv_raw_AES)

        input_raw_AES = self.input_textbox_AES.get()
        h_in_data_AES = bytes.fromhex(input_raw_AES.replace(' ', ''))
        input_len = (len(input_raw_AES))//2
        
        input_len_check = len(input_raw_AES)
        if input_len_check != 32 or input_len_check != 48 or input_len_check != 64:
            self.output_textbox_AES.delete(1.0, END)
            self.output_textbox_AES.insert(1.0, "Select a correct mode. Otherwise send this error to todearnigel@gmail.com")
        else:
            pass
        
        print("AES input data         :", h_in_data_AES.hex().upper())
        print("key_aes_len            :", key_aes_len, "| <Bytes>")
        print("Encryption/Decryption  :", selection_aes_EorD, " | <1:Encryption; 2:Decryption>")
        mode_judge = MODE_SLC_AES.get()
        if mode_judge == 1:
            mode = AES.MODE_ECB
        elif mode_judge == 2:
            mode = AES.MODE_CBC
        elif mode_judge == 3:
            mode = AES.MODE_CFB
        elif mode_judge == 4:
            mode = AES.MODE_OFB
        else:
            self.output_textbox_AES.delete(1.0, END)
            self.output_textbox_AES.insert(1.0, "Select a correct mode. Otherwise send this error to todearnigel@gmail.com")
        # mode = MODE_SLC_AES.get()  #   AES.MODE_ECB, AES.MODE_CBC, AES.MODE_OFB
        print("AES mode is            :", mode_judge, " | <1:ECB, 2:CBC, 3:CFB, 4:OFB>")
        
        
        #   'Enc/Dec' Judgment, and execute!!!
        if selection_aes_EorD == 0:
            self.output_textbox_AES.delete(1.0, END)
            self.output_textbox_AES.insert(1.0, "Please select an operation")
        

        #   Encryption !!
        elif selection_aes_EorD == 1 :  # AES Enc operation
            
            if mode_judge == 1:
                obj = AES.new(hkey_AES, mode)
            else:
                obj = AES.new(hkey_AES, mode, hiv_AES)

            output_aes_raw_e = obj.encrypt(h_in_data_AES)
            h_out_data_aes_e = output_aes_raw_e.hex().upper()
            print("AES output (Enc)       :", h_out_data_aes_e)
            self.output_textbox_AES.delete(1.0, END)
            self.output_textbox_AES.insert(1.0, h_out_data_aes_e)
        

        #   Decryption !!
        elif selection_aes_EorD == 2 :  # AES Dec operation

            if mode_judge == 1:
                obj = AES.new(hkey_AES, mode)
            else:
                obj = AES.new(hkey_AES, mode, hiv_AES)

            output_aes_raw_d = obj.decrypt(h_in_data_AES)
            h_out_data_aes_d = output_aes_raw_d.hex().upper()
            print("AES output (Dec)       :", h_out_data_aes_d)
            self.output_textbox_AES.delete(1.0, END)
            self.output_textbox_AES.insert(1.0, h_out_data_aes_d)
        else:
            pass

    #   Magic function - use output as a new AES key
    def copy_key_value_AES(self):
        key_temp_value_AES = self.output_textbox_AES.get(1.0, END)
        self.output_textbox_AES.delete(1.0, END)
        self.key_textbox_AES.delete(0, END)
        self.key_textbox_AES.insert(0, key_temp_value_AES)
        print("new key value          :", key_temp_value_AES)
        print("copy the TDES output value to key value...")


    #   Crypto function - RSA
    def RSA_key_pair_gen_func(self):
        #get RSA key length:

        #rsa_len = 1024
        #enable the following line on the published version:
        rsa_len = self.RSA_k_len_En.get()
        print('RSA private key length is:', rsa_len)
        #generate private RSA key: "key"
        key = RSA.generate(int(rsa_len), e=3)
        public  = key.publickey()
        print("========================================================|")
        print("--- pub & pri key check --------------------------------|")

        self.RSAgen_pri_key_tx.delete(1.0, END)
        self.RSAgen_pri_key_tx.insert(1.0, key.exportKey())
        self.RSAgen_pub_key_tx.delete(1.0, END)
        self.RSAgen_pub_key_tx.insert(1.0, public.exportKey())


        #   binascii.b2a_hex() is used for converting sth to hex string!!!!!
        # print("========================================================|")
        print("--- RSA Key Pair Generation ----- Start ----------------|")
        print("Key exponents:")
        print(hex(key.e).rstrip("L").lstrip("0x").upper())
        print("Private key:")
        print(hex(key.d).rstrip("L").lstrip("0x").upper())
        print("Public key:")
        print(hex(key.n).rstrip("L").lstrip("0x").upper())
        print("--- RSA Key Pair Generation ----- End ------------------|")
        print("\n")
        private_key = key.export_key()
        file_out = open("pri_key.pem", "wb")
        file_out.write(private_key)
        file_out.close()
        public_key = key.publickey().export_key()
        file_out = open("pub_key.pem", "wb")
        file_out.write(public_key)
        file_out.close()

        self.RSAgen_output_exp_tx.delete(1.0, END)
        self.RSAgen_output_exp_tx.insert(1.0, hex(key.e).rstrip("L").lstrip("0x").upper())
        self.RSAgen_output_pri_tx.delete(1.0, END)
        self.RSAgen_output_pri_tx.insert(1.0, hex(key.d).rstrip("L").lstrip("0x").upper())
        self.RSAgen_output_pub_tx.delete(1.0, END)
        self.RSAgen_output_pub_tx.insert(1.0, hex(key.n).rstrip("L").lstrip("0x").upper())

        self.rsa_key_exp_import_tx.delete(1.0, END)
        self.rsa_key_exp_import_tx.insert(1.0, hex(key.e).rstrip("L").lstrip("0x").upper())
        self.rsa_key_pri_import_tx.delete(1.0, END)
        self.rsa_key_pri_import_tx.insert(1.0, hex(key.d).rstrip("L").lstrip("0x").upper())
        self.rsa_key_pub_import_tx.delete(1.0, END)
        self.rsa_key_pub_import_tx.insert(1.0, hex(key.n).rstrip("L").lstrip("0x").upper())

        with open("rsa_e_imported.imp", "w") as RSA_e:
            RSA_e.write(hex(key.e))
        with open("rsa_d_imported.imp", "w") as RSA_d:
            RSA_d.write(hex(key.d))
        with open("rsa_n_imported.imp", "w") as RSA_n:
            RSA_n.write(hex(key.n))


    def rsa_key_import_func(self):

        import_flag = KEY_IMPORT_METHOD.get()

        if import_flag == 0:
            self.rsa_key_imported_done.delete(1.0, END)
            self.rsa_key_imported_done.insert(1.0, "Please select an  importing method!")
        
        # Import keys from *.imp files
        elif import_flag == 1:  
            with open('rsa_e_imported.imp', 'r') as RSA_e_temp:
                test_value_e = RSA_e_temp.read()
            with open('rsa_d_imported.imp', 'r') as RSA_d_temp:
                test_value_d = RSA_d_temp.read()
            with open('rsa_n_imported.imp', 'r') as RSA_n_temp:
                test_value_n = RSA_n_temp.read()

            print("========================================================|")
            print("--- RSA Keys are being imported from the *.imp files ---|")
            print("\ntest_value_e: (hex)")
            print(test_value_e)
            print("\ntest_value_d: (hex)")
            print(test_value_d)
            print("\ntest_value_n: (hex)")
            print(test_value_n)
            print("--- RSA Keys have been imported from the *.imp files ---|")
            print("\n")

            #convert hex string to long:
            key_n = int(test_value_n, 16)
            key_e = int(test_value_e, 16)
            key_d = int(test_value_d, 16)

            pri_const = RSA.construct((key_n, key_e, key_d))
            pub_const = RSA.construct((key_n, key_e))

            self.rsa_key_exp_import_tx.delete(1.0, END)
            self.rsa_key_exp_import_tx.insert(1.0, test_value_e.rstrip("L").lstrip("0x").upper())
            self.rsa_key_pri_import_tx.delete(1.0, END)
            self.rsa_key_pri_import_tx.insert(1.0, test_value_d.rstrip("L").lstrip("0x").upper())
            self.rsa_key_pub_import_tx.delete(1.0, END)
            self.rsa_key_pub_import_tx.insert(1.0, test_value_n.rstrip("L").lstrip("0x").upper())


            self.rsa_key_imported_done.delete(1.0, END)
            self.rsa_key_imported_done.insert(1.0, "Keys are imported!Go to RSA Crypto.!")

        # Import keys from 3 text boxes
        elif import_flag == 2:

            rsa_exp_import = self.rsa_key_exp_import_tx.get("1.0", END)    #"1.0", END
            rsa_pri_import = self.rsa_key_pri_import_tx.get("1.0", END)
            rsa_pub_import = self.rsa_key_pub_import_tx.get("1.0", END)

            if len(rsa_exp_import)==0 or len(rsa_pri_import)==0 or len(rsa_pub_import)==0:
                print("rsa_exp_import")
                print(rsa_exp_import)
                print("rsa_pri_import")
                print(rsa_pri_import)
                print("rsa_pub_import")
                print(rsa_pub_import)
            else:
                with open("rsa_e_imported.imp", "w") as RSA_e_imported:
                    RSA_e_imported.write(rsa_exp_import)
                with open("rsa_d_imported.imp", "w") as RSA_d_imported:
                    RSA_d_imported.write(rsa_pri_import)
                with open("rsa_n_imported.imp", "w") as RSA_n_imported:
                    RSA_n_imported.write(rsa_pub_import)
                with open('rsa_e_imported.imp', 'r') as RSA_e_temp:
                    test_value_e = RSA_e_temp.read()
                with open('rsa_d_imported.imp', 'r') as RSA_d_temp:
                    test_value_d = RSA_d_temp.read()
                with open('rsa_n_imported.imp', 'r') as RSA_n_temp:
                    test_value_n = RSA_n_temp.read()
                #   number will only be printed in decimal format!!
                print("========================================================|")
                print("--- RSA Keys are being imported from 3 text boxes ------|")
                print("\ntest_value_e: (hex)")
                print(test_value_e)
                print("\ntest_value_d: (hex)")
                print(test_value_d)
                print("\ntest_value_n: (hex)")
                print(test_value_n)
                print("--- RSA Keys have been imported from 3 text boxes ------|")
                # print("rsa_exp_import:\n", rsa_exp_import)
                print("\n\n")

                #convert hex string to long:
                key_n = int(test_value_n, 16)
                key_e = int(test_value_e, 16)
                key_d = int(test_value_d, 16)

                pri_const = RSA.construct((key_n, key_e, key_d))
                pub_const = RSA.construct((key_n, key_e))

                print("========================================================|")
                print("--- RSA key logs ---------------------------------------|")
                print("\nrsa_input_exp: (hex)")
                print(rsa_exp_import)
                print("\nrsa_input_pri: (hex)")
                print(rsa_pri_import)
                print("\nrsa_input_pub: (hex)")
                print(rsa_pub_import)
                print("--- RSA key logs ---------------------------------------|")
                print("\n")


                # print("\n#  6  -----------------------------------------------------------------------------")
                '''print "rsa_input_exp(hex)", hex(rsa_input_exp)
                print "rsa_input_pri(hex)", hex(rsa_input_pub)
                print "rsa_input_pub(hex)", hex(rsa_input_pub)'''

                self.rsa_key_exp_import_tx.delete(1.0, END)
                self.rsa_key_exp_import_tx.insert(1.0, test_value_e)
                self.rsa_key_pri_import_tx.delete(1.0, END)
                self.rsa_key_pri_import_tx.insert(1.0, test_value_d)
                self.rsa_key_pub_import_tx.delete(1.0, END)
                self.rsa_key_pub_import_tx.insert(1.0, test_value_n)
                self.rsa_key_imported_done.delete(1.0, END)
                self.rsa_key_imported_done.insert(1.0, "Keys are imported!Go to RSA Crypto.!")


    def execution_RSA_enc(self):
        rsa_exp_4enc = self.rsa_key_exp_import_tx.get("1.0", END)
        rsa_pri_4enc = self.rsa_key_pri_import_tx.get("1.0", END)
        rsa_pub_4enc = self.rsa_key_pub_import_tx.get("1.0", END)

        plaintext_input_raw = self.rsa_data_in.get("1.0", END)
        # plaintext_input = int(plaintext_input_raw, 16)
        plaintext_input = bytes.fromhex(plaintext_input_raw.replace(' ', ''))

        key_e_4enc = int(rsa_exp_4enc, 16)
        key_d_4enc = int(rsa_pri_4enc, 16)
        key_n_4enc = int(rsa_pub_4enc, 16)

        pub_const = RSA.construct((key_n_4enc, key_e_4enc, key_d_4enc))

        # test py3 new feature:
        pub = RSA.import_key(open("pub_key.pem").read())
        pub_rsa = PKCS1_OAEP.new(pub)

        # py v2:
        # ciphertext_output = pub_const.encrypt(plaintext_input, 32)[0]
        ciphertext = pub_rsa.encrypt(plaintext_input)
        ciphertext_output = ciphertext.hex().upper()
        print("Ciphertext data:")
        print(ciphertext_output)
        print("\n")
        # print("ciphertext_output:", binascii.hexlify(ciphertext_output))

        self.rsa_data_out.delete(1.0, END)
        self.rsa_data_out.insert(1.0, ciphertext_output) # to be fixed

    def execution_RSA_dec(self):
        rsa_exp_4dec = self.rsa_key_exp_import_tx.get("1.0", END)
        rsa_pri_4dec = self.rsa_key_pri_import_tx.get("1.0", END)
        rsa_pub_4dec = self.rsa_key_pub_import_tx.get("1.0", END)

        ciphertext_input_raw = self.rsa_data_in.get("1.0", END)
        # py2 ver:
        # ciphertext_input = int(ciphertext_input_raw, 16)
        ciphertext_input = bytes.fromhex(ciphertext_input_raw.replace(' ', ''))

        key_e_4dec = int(rsa_exp_4dec, 16)
        key_d_4dec = int(rsa_pri_4dec, 16)
        key_n_4dec = int(rsa_pub_4dec, 16)

        pri_const = RSA.construct((key_n_4dec, key_e_4dec, key_d_4dec))

        pri = RSA.import_key(open("pri_key.pem").read())
        pri_rsa = PKCS1_OAEP.new(pri)

        # py v2:
        # plaintext_output = pri_const.decrypt(ciphertext_input)
        plaintext = pri_rsa.decrypt(ciphertext_input)
        plaintext_output = plaintext.hex().upper()
        print("Plaintext data:")
        print( plaintext_output)
        print("\n")

        self.rsa_data_out.delete(1.0, END)
        self.rsa_data_out.insert(1.0, plaintext_output)

    #   HASH/HMAC function - SHA, SHA224, SHA256, SHA384, SHA512, MD4, MD5, HMAC ??
    def execution_HASH(self):
        hash_algo_selector = operation_SLC_HASH.get()
        hash_algo_selector_hmac = operation_SLC_HASH_hmac.get()
        #   When HASH_SOURCE_IMPORT_METHOD is '0' -> hash source button is not pressed.
        #   When HASH_SOURCE_IMPORT_METHOD is '1' -> hash a hex data.
        #   When HASH_SOURCE_IMPORT_METHOD is '2' -> hash a file
        hash_source_flag = HASH_SOURCE_IMPORT_METHOD.get()
        
        if hash_source_flag == 0:
            self.hash_output_text.delete(1.0, END)
            self.hash_output_text.insert(1.0, "Please select an hash Source via the buttons above!")
            print("[debug] hash_source_flag:", hash_source_flag)
        
        #   HASH operations
        #   to verify the results, go https://emn178.github.io/online-tools/sha256.html
        elif hash_source_flag == 1 and hash_algo_selector_hmac ==0:
            if hash_algo_selector == 0:
                self.hash_output_text.delete(1.0, END)
                self.hash_output_text.insert(1.0, "Please select a hash alogrithm")
                pass
            elif hash_algo_selector == 1:
                hash_algo = SHA
            elif hash_algo_selector ==2:
                hash_algo = MD4
            elif hash_algo_selector ==3:
                hash_algo = MD5
            elif hash_algo_selector ==5:
                hash_algo = SHA224
            elif hash_algo_selector ==6:
                hash_algo = SHA256
            elif hash_algo_selector ==7:
                hash_algo = SHA384
            elif hash_algo_selector ==8:
                hash_algo = SHA512
            elif hash_algo_selector ==9:
                hash_algo = SHA3_224
            elif hash_algo_selector ==10:
                hash_algo = SHA3_256
            elif hash_algo_selector ==11:
                hash_algo = SHA3_384
            elif hash_algo_selector ==12:
                hash_algo = SHA3_512
            else:
                pass
            hash_input_data = self.hash_input_entry.get()
            if len(hash_input_data)==0:
                self.hash_output_text.delete(1.0, END)
                self.hash_output_text.insert(1.0, "Please enter a input data")
            else:
                print("HASH input data (hex):")
                print(hash_input_data)
                h_hash_data = bytes.fromhex(hash_input_data.replace(' ', ''))

                if  hash_algo_selector == 1 or hash_algo_selector == 2 or \
                    hash_algo_selector == 3 or hash_algo_selector == 5 or \
                    hash_algo_selector == 6 or hash_algo_selector == 7 or \
                    hash_algo_selector == 8 or hash_algo_selector == 9 or \
                    hash_algo_selector == 10 or hash_algo_selector == 11 or \
                    hash_algo_selector == 12:
                    obj = hash_algo.new()
                    obj.update(h_hash_data)
                    ret = obj.digest()
                    h_output_hash = ret.hex()
                    self.hash_output_text.delete(1.0, END)
                    self.hash_output_text.insert(1.0, h_output_hash)
                    print("Hashed value (hex):")
                    print(h_output_hash, "\n")
                else:
                    pass

        #   HMAC operation
        #   to verify the results, go https://www.liavaag.org/English/SHA-Generator/HMAC/
        elif hash_source_flag == 1 and hash_algo_selector_hmac == 1:
            hmac_key = self.hash_hmac_key_entry.get()
            h_hmac_key = bytes.fromhex(hmac_key.replace(' ', ''))
            hmac_data = self.hash_input_entry.get()
            print("HMAC key (hex):")
            print(hmac_key)
            print("HMAC input data (hex):")
            print(hmac_data)

            h_hmac_data = bytes.fromhex(hmac_data.replace(' ', ''))
            if hash_algo_selector == 0:
                self.hash_output_text.delete(1.0, END)
                self.hash_output_text.insert(1.0, "Please select a hash alogrithm")
            elif hash_algo_selector == 1:
                hash_algo = SHA
            elif hash_algo_selector ==2:
                hash_algo = MD4
            elif hash_algo_selector ==3:
                hash_algo = MD5
            elif hash_algo_selector ==5:
                hash_algo = SHA224
            elif hash_algo_selector ==6:
                hash_algo = SHA256
            elif hash_algo_selector ==7:
                hash_algo = SHA384
            elif hash_algo_selector ==8:
                hash_algo = SHA512
            elif hash_algo_selector ==9:
                hash_algo = SHA3_224
            elif hash_algo_selector ==10:
                hash_algo = SHA3_256
            elif hash_algo_selector ==11:
                hash_algo = SHA3_384
            elif hash_algo_selector ==12:
                hash_algo = SHA3_512
            else:
                pass
            hash_input_data = self.hash_input_entry.get()
            if len(hash_input_data)==0:
                self.hash_output_text.delete(1.0, END)
                self.hash_output_text.insert(1.0, "Please enter a input data")
            else:    
                obj_hmac = HMAC.new(h_hmac_key, h_hmac_data, hash_algo)
                self.hash_output_text.delete(1.0, END)
                self.hash_output_text.insert(1.0, obj_hmac.digest().hex().upper())
                print("Hashed value:")
                print(obj_hmac.digest().hex().upper(), "\n")

        elif hash_source_flag == 2:
            to_be_hashed_file = fd.askopenfilename()
            self.file_path_output_text.delete(1.0, END)
            self.file_path_output_text.insert(1.0, to_be_hashed_file)
            with open(to_be_hashed_file,"rb") as hash_object:
                hash_obj = hash_object.read() # read file as bytes
                
                if hash_algo_selector == 1:
                    readable_hash = hashlib.sha1(hash_obj).hexdigest();
                elif hash_algo_selector ==3:
                    readable_hash = hashlib.md5(hash_obj).hexdigest();
                elif hash_algo_selector ==5:
                    readable_hash = hashlib.sha224(hash_obj).hexdigest();
                elif hash_algo_selector ==6:
                    readable_hash = hashlib.sha256(hash_obj).hexdigest();
                elif hash_algo_selector ==7:
                    readable_hash = hashlib.sha384(hash_obj).hexdigest();
                elif hash_algo_selector ==8:
                    readable_hash = hashlib.sha512(hash_obj).hexdigest();
                elif hash_algo_selector ==9:
                    readable_hash = hashlib.sha3_224(hash_obj).hexdigest();
                elif hash_algo_selector ==10:
                    readable_hash = hashlib.sha3_256(hash_obj).hexdigest();
                elif hash_algo_selector ==11:
                    readable_hash = hashlib.sha3_2384(hash_obj).hexdigest();
                elif hash_algo_selector ==12:
                    readable_hash = hashlib.sha3_512(hash_obj).hexdigest();
                elif hash_algo_selector ==2:
                    self.hash_output_text.delete(1.0, END)
                    self.hash_output_text.insert(1.0, "Sorry. Hashing a file by MD4 is not support!")
                    pass
                else:
                    pass
                self.hash_output_text.delete(1.0, END)
                self.hash_output_text.insert(1.0, readable_hash)
                print("Hashed file name:")
                print(to_be_hashed_file)

                print("Hashed value:")
                print(readable_hash.upper(), "\n")
                
                # if hash_algo_selector ==2:
                #     self.hash_output_text.delete(1.0, END)
                #     self.hash_output_text.insert(1.0, "Sorry. Hashing a file by MD4 is not support!")
                # print(readable_hash)


    #   Crypto function - XOR
    def execution_XOR(self):
        data_A = self.xor_inputA_value.get()
        data_B = self.xor_inputB_value.get()
        '''
        Description: Performs an exclusive or (XOR) operation
        Arguments:
        hstr1: A hex encoded string containing data to xor
        hstr2: A hex encoded string containing more data to xor
        Returns:
        A strong containing the xor'ed value as hex string
        '''
        if len(data_A) != len(data_B):
            self.xor_result_value.delete(1.0, END)
            self.xor_result_value.insert(1.0, "Input A and Input B must be equal!")
        hstr1 = bytes.fromhex(data_A.replace(' ', ''))
        hstr2 = bytes.fromhex(data_B.replace(' ', ''))
        hstr1_test = hstr1.hex().upper()
        hstr2_test = hstr2.hex().upper()
        # out_str = ''
        xor_output = bytes(a ^ b for (a, b) in zip(hstr1, hstr2))
        print("xor_output:")
        print(xor_output.hex().upper())
        self.xor_result_value.delete(1.0, END)
        self.xor_result_value.insert(1.0, xor_output.hex().upper())



    #   Crypto function - RND
    #   RNG function - gerate a 8 bytes random number
    def rng_gen_8B(self):
        rndfile = Random.new()
        rnd = rndfile.read(8)
        h_rnd = rnd.hex()
        self.rng_8B_textbox.delete(1.0, END)
        self.rng_8B_textbox.insert(1.0, h_rnd)
        print(h_rnd)

    def rng_gen_32B(self):
        rndfile = Random.new()
        rnd = rndfile.read(32)
        h_rnd = rnd.hex()
        self.rng_32B_textbox.delete(1.0, END)
        self.rng_32B_textbox.insert(1.0, h_rnd)
        print(h_rnd)

    def rng_gen_88B(self):
        rndfile = Random.new()
        rnd = rndfile.read(88)
        h_rnd = rnd.hex()
        self.rng_88B_textbox.delete(1.0, END)
        self.rng_88B_textbox.insert(1.0, h_rnd)
        print(h_rnd)
    '''
    def close_CryptoBox(self):
        global root
        root.destroy()
    '''

    def pwd_gen_8dig(self):
        # Generates a random password including uppercase, lowercase, numbers, and symbols.
        # Args:
            # length: The desired length of the password (default is 12).
        # Returns:
            # A string representing the generated password.
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(8))
        self.pwd_8dig_textbox.delete(1.0, END)
        self.pwd_8dig_textbox.insert(1.0, password)
        print(password)
    
    def pwd_gen_16dig(self):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(16))
        self.pwd_16dig_textbox.delete(1.0, END)
        self.pwd_16dig_textbox.insert(1.0, password)
        print(password)

    def p120_start(self):
        # 1. get the current time!
        log_time_temp = time.strftime("%Y/%m/%d  %H:%M:%S")
        realtime.configure(text=log_time_temp)
        # 2. write it into the text box
        self.start_tm.delete(1.0, END)
        self.last_tm.delete(1.0, END)
        self.start_tm.insert(1.0, log_time_temp)
        self.last_tm.insert(1.0, "***Entry started at: " + log_time_temp + "\n")
        global p120_butt_clicked
        p120_butt_clicked = 0

    def p120_go(self):
        global p120_butt_clicked
        p120_butt_clicked += 1
        # 1. get the current time to log_time_temp:
        log_time_temp = time.strftime("%Y/%m/%d  %H:%M:%S")
        realtime.configure(text=log_time_temp)
        print("current time:", log_time_temp)
        # 2. write time to text box
        if 0<p120_butt_clicked<10:
            filled_text = "#00" + str(p120_butt_clicked) + " PIN entered at: " + str(log_time_temp)
        elif 10<=p120_butt_clicked<100:
            filled_text = "#0" + str(p120_butt_clicked) + " PIN entered at: " + str(log_time_temp)
        else:
            filled_text = "#" + str(p120_butt_clicked) + " PIN entered at: " + str(log_time_temp)
        print("filled_text", filled_text)
        self.last_tm.insert(0.0, filled_text + "\n")

    def p120_end(self):
        # 1. get the current time to log_time_temp:
        log_time_temp = time.strftime("%Y/%m/%d  %H:%M:%S")
        realtime.configure(text=log_time_temp)
        print("end time:", log_time_temp)
        # 2. write time to text box
        self.last_tm.insert(0.0, "**The last entry at: " + log_time_temp + "\n")
        self.last_tm.insert(0.0, "--------- Online PIN entry test ---------\n--------- Elapsed timetable log ---------\n")
        # 3. write whole log to the log file
        log_120pin = self.last_tm.get("1.0", END)
        with open("Online PIN_120_per_hour_test.txt", "w") as log_write:
            log_write.write(log_120pin)
        global p120_butt_clicked
        p120_butt_clicked = 0

    def contact_developer(self):
        messagebox.showinfo("Developer info", "todearnigel@gmail.com\n\nThank you for your feedback!")
        
        #webbrowser.open_new(r"fill-a-web-address-start-with-http://")

    def input_file():
        global input_filename
        input_filename = askopenfilename(defaultextension='.txt')
        if input_filename == '':
            input_filename = None
        else:
            root.title('Key FileName:' + os.path.basename(input_filename))
            textPad.delete(1.0, END)
            f = open(input_filename, 'r')
            textPad.insert(1.0, f.read())
            f.close()

    #=========================================================================================================
    #   Create Frame/Label/Text/...etc
    def __init__(self, *args, **kwargs):

        #   1.1 TDES - Encryption or Decryption Selection Frame
        self.operation_bar_TDES = LabelFrame(frame_1_TDES, text="Enc/Dec", font=("Helvetica", 12, "bold"), padx=5, pady=5, bd=4)
        self.operation_bar_TDES.grid(row=0, column=1, padx=5, sticky=W)
        self.Enc_label_TDES = Radiobutton(self.operation_bar_TDES, text="Enc ", indicatoron=0, value=1, width=10, variable=operation_SLC_TDES)
        self.Enc_label_TDES.grid(row=1, column=1, padx=5, pady=5)
        self.Dec_label_TDES = Radiobutton(self.operation_bar_TDES, text="Dec ", indicatoron=0, value=2, width=10, variable=operation_SLC_TDES)
        self.Dec_label_TDES.grid(row=2, column=1, padx=5, pady=5)
        #   1.2 Modes Selection Frame
        self.Mode_bar_TDES = LabelFrame(frame_1_TDES, text="Modes", font=("Helvetica", 12, "bold"), padx=5, pady=5, bd=4)
        self.Mode_bar_TDES.grid(row=0, column=2, rowspan=2, sticky=W)
        self.mode_ECB_TDES = Radiobutton(self.Mode_bar_TDES, text="ECB ", indicatoron=0, value=1, width=10, variable=MODE_SLC_TDES)
        self.mode_ECB_TDES.grid(row=1, column=2, padx=5, pady=5)
        self.mode_CBC_TDES = Radiobutton(self.Mode_bar_TDES, text="CBC ", indicatoron=0, value=2, width=10, variable=MODE_SLC_TDES)
        self.mode_CBC_TDES.grid(row=2, column=2, padx=5, pady=5)
        self.mode_CFB_TDES = Radiobutton(self.Mode_bar_TDES, text="CFB ", indicatoron=0, value=3, width=10, variable=MODE_SLC_TDES)
        self.mode_CFB_TDES.grid(row=1, column=3, padx=5, pady=5)
        self.mode_OFB_TDES = Radiobutton(self.Mode_bar_TDES, text="OFB ", indicatoron=0, value=4, width=10, variable=MODE_SLC_TDES)
        self.mode_OFB_TDES.grid(row=2, column=3, padx=5, pady=5)
        
        #   1.4 Key Entry Textbox
        self.key_label_TDES = Label(frame_1_TDES, text="Key value")
        self.key_label_TDES.grid(row=5, column=0, sticky=E)
        self.key_textbox_TDES = Entry(frame_1_TDES, textvariable = default_TDES_key, font = "Courier 9", width=64)
        self.key_textbox_TDES.grid(row=5, column=1, columnspan=4, padx=5, pady=5, sticky=W)
        #   RULER !
        self.ruler = Label(frame_1_TDES, text="|----8 Bytes---||----8 Bytes---||----8 Bytes---|", font="Courier 9",width=48)
        self.ruler.grid(row=6, column=1, columnspan=4, padx=6, sticky=W)
        #   1.5 IV Entry Textbox
        self.iv_label_TDES = Label(frame_1_TDES, text="IV")
        self.iv_label_TDES.grid(row=7, column=0, sticky=E)
        self.iv_textbox_TDES = Entry(frame_1_TDES, textvariable = default_iv_8B, font = "Courier 9", width=64)
        self.iv_textbox_TDES.grid(row=7, column=1, columnspan=4, padx=5, pady=5, sticky=W)
        #   1.6 Input  Data Entry Textbox
        self.input_label_TDES = Label(frame_1_TDES, text="Input")
        self.input_label_TDES.grid(row=8, column=0, sticky=E)
        self.input_textbox_TDES = Entry(frame_1_TDES, font = "Courier 9", width=64)
        self.input_textbox_TDES.grid(row=8, column=1, columnspan=4, padx=5, pady=5, sticky=W)
        #   RULER !
        self.ruler = Label(frame_1_TDES, text="|----8 Bytes---||----8 Bytes---||----8 Bytes---||----8 Bytes---|", font="Courier 9",width=64)
        self.ruler.grid(row=9, column=1, columnspan=4, padx=6, sticky=W)
        #   1.7 Output Data Entry Textbox
        self.output_label_TDES = Label(frame_1_TDES, text="Output")
        self.output_label_TDES.grid(row=10, column=0, sticky=E)
        self.output_textbox_TDES = Text(frame_1_TDES, font = "Courier 9", height=8, width=64)
        self.output_textbox_TDES.grid(row=10, column=1, columnspan=4, padx=5, pady=5, sticky=W)

        #   1.8 Go Button and Exit Button
        self.go_button_TDES = Button(frame_1_TDES, text="Use output\nas the key", width=10, command=self.copy_key_value_TDES)
        self.go_button_TDES.grid(row=11, column=1, padx=5, pady=5, sticky=W)
        self.go_button_TDES = Button(frame_1_TDES, text="Go!", width=10, bg='#D1FFBD', command=self.execution_TDES)
        self.go_button_TDES.grid(row=11, column=4, padx=5, pady=5, sticky=E)

        #   2.1 AES - Encryption or Decryption Selection Frame
        self.EncOrDec_bar_AES = LabelFrame(frame_2_AES, text="Enc/Dec", font=("Helvetica", 12, "bold"), padx=5, pady=5, bd=4)
        self.EncOrDec_bar_AES.grid(row=0, column=1, padx=5, sticky=W)
        self.Enc_label_AES = Radiobutton(self.EncOrDec_bar_AES, text="Enc ", indicatoron=0, value=1, width=10, variable=operation_SLC_AES)
        self.Enc_label_AES.grid(row=1, column=1, padx=5, pady=5)
        self.Dec_label_AES = Radiobutton(self.EncOrDec_bar_AES, text="Dec ", indicatoron=0, value=2, width=10, variable=operation_SLC_AES)
        self.Dec_label_AES.grid(row=2, column=1, padx=5, pady=5)
        #   2.2 Modes Selection Frame
        self.Mode_bar_AES = LabelFrame(frame_2_AES, text="Modes", font=("Helvetica", 12, "bold"), padx=5, pady=5, bd=4)
        self.Mode_bar_AES.grid(row=0, column=2, rowspan=2, sticky=W)
        self.mode_ECB_AES = Radiobutton(self.Mode_bar_AES, text="ECB ", indicatoron=0, value=1, width=10, variable=MODE_SLC_AES)
        self.mode_ECB_AES.grid(row=1, column=2, padx=5, pady=5)
        self.mode_CBC_AES = Radiobutton(self.Mode_bar_AES, text="CBC ", indicatoron=0, value=2, width=10, variable=MODE_SLC_AES)
        self.mode_CBC_AES.grid(row=2, column=2, padx=5, pady=5)
        self.mode_CFB_AES = Radiobutton(self.Mode_bar_AES, text="CFB ", indicatoron=0, value=3, width=10, variable=MODE_SLC_AES)
        self.mode_CFB_AES.grid(row = 1, column=3, padx=5, pady=5)
        self.mode_OFB_AES = Radiobutton(self.Mode_bar_AES, text="OFB ", indicatoron=0, value=4, width=10, variable=MODE_SLC_AES)
        self.mode_OFB_AES.grid(row=2, column=3, padx=5, pady=5)
        #   2.3 Key Entry Textbox
        self.key_label_AES = Label(frame_2_AES, text="Key value")
        self.key_label_AES.grid(row=5, column=0, sticky=E)
        self.key_textbox_AES = Entry(frame_2_AES, textvariable = default_AES_key,font = "Courier 9", width=64)
        self.key_textbox_AES.grid(row=5, column=1, columnspan=4, padx=5, pady=5, sticky=W)
        #   RULER !
        self.ruler = Label(frame_2_AES, text="|----8 Bytes---||----8 Bytes---||----8 Bytes---||----8 Bytes---|", font="Courier 9", width=64)
        self.ruler.grid(row=6, column=1, columnspan=4, padx=6, sticky=W)
        #   2.4 IV Entry Textbox
        self.iv_label_AES = Label(frame_2_AES, text="IV")
        self.iv_label_AES.grid(row=7, column=0, sticky=E)
        self.iv_textbox_AES = Entry(frame_2_AES, textvariable = default_iv_16B, font = "Courier 9", width=64)
        self.iv_textbox_AES.grid(row=7, column=1, columnspan=4, padx=5, pady=5, sticky=W)
        #   2.5 Input  Data Entry Textbox
        self.input_label_AES = Label(frame_2_AES, text="Input")
        self.input_label_AES.grid(row=8, column=0, sticky=E)
        self.input_textbox_AES = Entry(frame_2_AES, font = "Courier 9", width=64)
        self.input_textbox_AES.grid(row=8, column=1, columnspan=4, padx=5, pady=5, sticky=W)
        #   RULER !
        self.ruler = Label(frame_2_AES, text="|----8 Bytes---||----8 Bytes---||----8 Bytes---||----8 Bytes---|", font="Courier 9", width=64)
        self.ruler.grid(row=9, column=1, columnspan=4, padx=6, sticky=W)
        #   Scroll of the input text box
        # self.input_scroll = Scrollbar(self.input_textbox)
        # self.input_scroll.config(yscrollcommand = self.input_scroll.set)
        # self.input_scroll.config(command = self.input_scroll.yview)
        # self.input_scroll.pack(side = RIGHT, fill = Y)
        #   2.6 Output Data Entry Textbox
        self.output_label_AES = Label(frame_2_AES, text="Output")
        self.output_label_AES.grid(row=10, column=0, sticky=E)
        self.output_textbox_AES = Text(frame_2_AES, font = "Courier 9", height=8, width=64)
        self.output_textbox_AES.grid(row=10, column=1, columnspan=4, padx=5, pady=5, sticky=W)
        #   Scroll of the output text box
        # self.input_scroll = Scrollbar(self.input_textbox)
        # self.input_scroll.config(yscrollcommand = self.input_scroll.set)
        # self.input_scroll.config(command = self.input_scroll.yview)
        # self.input_scroll.pack(side = RIGHT, fill = Y)
        #   2.7 Go Button and Exit Button
        self.go_button_AES = Button(frame_2_AES, text="Use output\nas the key", width=10,
                                       command=self.copy_key_value_AES)
        self.go_button_AES.grid(row=11, column=1, padx=5, pady=5, sticky=W)
        self.go_button_AES = Button(frame_2_AES, text="Go!", width=10, bg='#D1FFBD', command=self.execution_AES)
        self.go_button_AES.grid(row=11, column=4, padx=5, pady=5, sticky=E)

        #   3_1   RSA Gen.

        #   3_1.1 RSA Key Gen
        self.Key_Gen = LabelFrame(frame_3_1_RSA, text=" RSA Key Pair Generation (PEM) ", font=("Helvetica", 12, "bold"), padx=5, pady=5)
        self.Key_Gen.grid(row=1, column=2, rowspan=4, sticky=W)
        self.RSAgen_pri_key_lb = Label(self.Key_Gen, text="Private\n(.pem)\n(d)")
        self.RSAgen_pri_key_lb.grid(row=2, column=1, padx=5, pady=5, sticky=W+N)
        self.RSAgen_pri_key_tx = Text(self.Key_Gen, font = "Courier 9", height=4, width=64)
        self.RSAgen_pri_key_tx.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        self.RSAgen_pub_key_lb = Label(self.Key_Gen, text="Public \n(.pem)\n(n)")
        self.RSAgen_pub_key_lb.grid(row=3, column=1, padx=5, pady=5, sticky=W+N)
        self.RSAgen_pub_key_tx = Text(self.Key_Gen, font = "Courier 9", height=4, width=64)
        self.RSAgen_pub_key_tx.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        self.RSAgen_output_exp_lb = Label(self.Key_Gen, text="exp.\n(hex)")
        self.RSAgen_output_exp_lb.grid(row=4, column=1, padx=5, pady=5, sticky=W+N)
        self.RSAgen_output_exp_tx = Text(self.Key_Gen, font = "Courier 9", height=1, width=64)
        self.RSAgen_output_exp_tx.grid(row=4, column=2, padx=5, pady=5, sticky=W)
        self.RSAgen_output_pri_lb = Label(self.Key_Gen, text="Private\n(hex)\n(d)")
        self.RSAgen_output_pri_lb.grid(row=5, column=1, padx=5, pady=5, sticky=W+N)
        self.RSAgen_output_pri_tx = Text(self.Key_Gen, font = "Courier 9", height=4, width=64)
        self.RSAgen_output_pri_tx.grid(row=5, column=2, padx=5, pady=5, sticky=W)
        self.RSAgen_output_pub_lb = Label(self.Key_Gen, text="Public \n(hex)\n(n)")
        self.RSAgen_output_pub_lb.grid(row=6, column=1, padx=5, pady=5, sticky=W+N)
        self.RSAgen_output_pub_tx = Text(self.Key_Gen, font = "Courier 9", height=4, width=64)
        self.RSAgen_output_pub_tx.grid(row=6, column=2, padx=5, pady=5, sticky=W)

        self.RSA_key_pair_gen_bot = Button(self.Key_Gen, text="Gen RSA key pair", width=17, bg='#D1FFBD', command=self.RSA_key_pair_gen_func)
        self.RSA_key_pair_gen_bot.grid(row=7, column=2, padx=5, pady=5, sticky=N+E)

        self.RSA_k_len_lb = Label(self.Key_Gen, text="key len")
        self.RSA_k_len_lb.grid(row=7, column=1, padx=5, pady=5, sticky=N+W)
        self.RSA_k_len_En = Entry(self.Key_Gen, width=5)
        self.RSA_k_len_En.grid(row=7, column=2, padx=5, pady=5, sticky=N+W)

        #   3_1.4 output file - enciphered/plaintext binary data

        #   3_2     RSA key Import # with Dave's great help
        self.rsa_key_import = LabelFrame(frame_3_2_RSA, text = " Import your RSA key pair ",
                                            font=("Helvetica", 12, "bold"), padx=5, pady=5)
        self.rsa_key_import.grid(row=1, column=2, rowspan=4, sticky=W)

        self.rsa_import_meth_1 = Radiobutton(self.rsa_key_import, text="Import keys from .imp files",
                                                indicator=0, value=1, width=22, variable=KEY_IMPORT_METHOD)
        self.rsa_import_meth_1.grid(row=2, column=2, padx=5, pady=1, sticky = W)
        self.rsa_import_meth_2 = Radiobutton(self.rsa_key_import, text="Import keys to the 3 boxes ",
                                                indicator=0, value=2, width=22, variable=KEY_IMPORT_METHOD)
        self.rsa_import_meth_2.grid(row=3, column=2, padx=5, pady=1, sticky = W)

        self.rsa_key_exp_import_lb = Label(self.rsa_key_import, text="exp.   ")
        self.rsa_key_exp_import_lb.grid(row=4, column=1, padx=5, pady=5, sticky =W+N)
        self.rsa_key_exp_import_tx = Text(self.rsa_key_import, font = "Courier 9", height=1, width=64)
        self.rsa_key_exp_import_tx.grid(row=4, column=2, padx=5, pady=5, sticky=W)
        self.rsa_key_pri_import_lb = Label(self.rsa_key_import, text="Private\n(d)")
        self.rsa_key_pri_import_lb.grid(row=5, column=1, padx=5, pady=5, sticky =W+N)
        self.rsa_key_pri_import_tx = Text(self.rsa_key_import, font = "Courier 9", height=6, width=64)
        self.rsa_key_pri_import_tx.grid(row=5, column=2, padx=5, pady=5, sticky=W)
        self.rsa_key_pub_import_lb = Label(self.rsa_key_import, text="Public \n(n)")
        self.rsa_key_pub_import_lb.grid(row=6, column=1, padx=5, pady=5, sticky =W+N)
        self.rsa_key_pub_import_tx = Text(self.rsa_key_import, font = "Courier 9", height=6, width=64)
        self.rsa_key_pub_import_tx.grid(row=6, column=2, padx=5, pady=5, sticky=W)

        self.rsa_key_imported_done = Text(self.rsa_key_import, font="Courier 9", height=2, width=18)
        self.rsa_key_imported_done.grid(row=7, column=2, padx=5, pady=5, sticky=N + W)

        self.rsa_key_pub_import_bot = Button(self.rsa_key_import, text="Import your RSA key pair",
                                                width=20, bg='#D1FFBD', command=self.rsa_key_import_func)
        self.rsa_key_pub_import_bot.grid(row=7, column=2, padx=5, pady=5, sticky=N+E)


        #   3_3     RSA Crypto.
        #   3_3.1 Operation selection
        '''
        self.EncOrDec_bar_RSA = LabelFrame(frame_3_3_RSA, text="Operation", padx=10, pady=10)
        self.EncOrDec_bar_RSA.grid(row=1, column=1, rowspan=4, sticky=W+N)
        self.Enc_label_RSA = Radiobutton(self.EncOrDec_bar_RSA, text="Enc", indicatoron=0, value=1, width=10,
                                            variable=operation_SLC_RSA)
        self.Enc_label_RSA.grid(row=2, column=1, padx=5, pady=5)
        self.Dec_label_RSA = Radiobutton(self.EncOrDec_bar_RSA, text="Dec", indicatoron=0, value=2, width=10,
                                            variable=operation_SLC_RSA)
        self.Dec_label_RSA.grid(row=3, column=1, padx=5, pady=5)
        '''

        #   3_3.2 input file - plaintext/enciphered binary data
        self.rsa_data_work = LabelFrame(frame_3_3_RSA, text=" RSA Calculator ",
                                     font=("Helvetica", 12, "bold"), padx=5, pady=5)
        self.rsa_data_work.grid(row=1, column=2, rowspan=4, sticky=W)

        self.rsa_data_in_lb = Label(self.rsa_data_work, text="Input")
        self.rsa_data_in_lb.grid(row=2, column=1, padx=5, pady=5, sticky=W+N)
        self.rsa_data_in = Text(self.rsa_data_work, font = "Courier 9", height=8, width=64)
        self.rsa_data_in.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        self.rsa_data_out_lb = Label(self.rsa_data_work, text="Output")
        self.rsa_data_out_lb.grid(row=3, column=1, padx=5, pady=5, sticky=W+N)
        self.rsa_data_out = Text(self.rsa_data_work, font = "Courier 9", height=8, width=64)
        self.rsa_data_out.grid(row=3, column=2, padx=5, pady=5, sticky=W)


        #   3_3.1 RSA Enc/Dec
        self.key_pub_butt_RSA = Button(self.rsa_data_work, text="Encrypt Input data", width=17, bg='#D1FFBD', command=self.execution_RSA_enc)
        self.key_pub_butt_RSA.grid(row=4, column=2, padx=5, pady=5, sticky=N+E)
        self.key_pri_butt_RSA = Button(self.rsa_data_work, text="Decrypt Input data", width=17, bg='#D1FFBD', command=self.execution_RSA_dec)
        self.key_pri_butt_RSA.grid(row=5, column=2, padx=5, pady=5, sticky=N+E)

        self.rsa_note = Label(self.rsa_data_work,
                                      text="\nNote:\nPrivate key, Public key, and exp. must be\npre-imported under 'RSA import.' tag",
                                      font=("Helvetica", 8))
        self.rsa_note.config(justify=LEFT)
        self.rsa_note.grid(row=4, column=2, rowspan=3, padx=5, sticky=W+N)

        #   4.1 Hash - (SHA, SHA224, SHA256, SHA384, SHA512, MD4, MD5, HMAC??)
        self.HASH_frame = LabelFrame(frame_4_HASH, text=" Algorithms ", font=("Helvetica", 12, "bold"), padx=5, pady=5, bd=4)
        self.HASH_frame.grid(row=1, column=1, rowspan=4, columnspan=3, padx=5, sticky=W)
        #   4.1.1 algorithm selection buttons
        self.hash_SHA_1 = Radiobutton(self.HASH_frame, text="SHA", indicator=0, value=1, width=8, variable=operation_SLC_HASH)
        self.hash_SHA_1.grid(row=2, column=1, padx=5, pady=5)
        self.hash_MD4 = Radiobutton(self.HASH_frame, text="MD4", indicator=0, value=2, width=8, variable=operation_SLC_HASH)
        self.hash_MD4.grid(row=2, column=2, padx=5, pady=5)
        self.hash_MD5 = Radiobutton(self.HASH_frame, text="MD5", indicator=0, value=3, width=8, variable=operation_SLC_HASH)
        self.hash_MD5.grid(row=2, column=3, padx=5, pady=5)
        
        self.hash_SHA2_224 = Radiobutton(self.HASH_frame, text="SHA224", indicator=0, value=5, width=8, variable=operation_SLC_HASH)
        self.hash_SHA2_224.grid(row=3, column=1, padx=5, pady=5)
        self.hash_SHA2_256 = Radiobutton(self.HASH_frame, text="SHA256", indicator=0, value=6, width=8, variable=operation_SLC_HASH)
        self.hash_SHA2_256.grid(row=3, column=2, padx=5, pady=5)
        self.hash_SHA2_384 = Radiobutton(self.HASH_frame, text="SHA384", indicator=0, value=7, width=8, variable=operation_SLC_HASH)
        self.hash_SHA2_384.grid(row=3, column=3, padx=5, pady=5)
        self.hash_SHA2_512 = Radiobutton(self.HASH_frame, text="SHA512", indicator=0, value=8, width=8, variable=operation_SLC_HASH)
        self.hash_SHA2_512.grid(row=4, column=1, padx=5, pady=5)
        self.hash_SHA3_224 = Radiobutton(self.HASH_frame, text="SHA3_224", indicator=0, value=9, width=8, variable=operation_SLC_HASH)
        self.hash_SHA3_224.grid(row=4, column=2, padx=5, pady=5)
        self.hash_SHA3_256 = Radiobutton(self.HASH_frame, text="SHA3_256", indicator=0, value=10, width=8, variable=operation_SLC_HASH)
        self.hash_SHA3_256.grid(row=4, column=3, padx=5, pady=5)
        self.hash_SHA3_384 = Radiobutton(self.HASH_frame, text="SHA3_384", indicator=0, value=11, width=8, variable=operation_SLC_HASH)
        self.hash_SHA3_384.grid(row=5, column=1, padx=5, pady=5)
        self.hash_SHA3_512 = Radiobutton(self.HASH_frame, text="SHA3_512", indicator=0, value=12, width=8, variable=operation_SLC_HASH)
        self.hash_SHA3_512.grid(row=5, column=2, padx=5, pady=5)
        self.hash_HMAC = Checkbutton(self.HASH_frame, text="HMAC", width=5, variable=operation_SLC_HASH_hmac)
        self.hash_HMAC.grid(row=5, column=3, padx=5, pady=5)
        
        #   4.2 Source - (Hex data, or file)
        self.Source_frame = LabelFrame(frame_4_HASH, text=" Source ", font=("Helvetica", 12, "bold"), padx=5, pady=5, bd=4)
        self.Source_frame.grid(row=1, column=4, rowspan=4, padx=15, sticky=NW)
        
        #   4.2.1 adding "Source" - new row is 6
        # self.hash_source_label = Label(frame_4_HASH, text="Source")
        # self.hash_source_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
        
        self.hash_source_data = Radiobutton(self.Source_frame, text="Hash a HEX data", indicator=0, value=1, width=15, variable=HASH_SOURCE_IMPORT_METHOD)
        self.hash_source_data.grid(row=2, column=4, padx=5, pady=5, sticky = NE)
        self.hash_source_file = Radiobutton(self.Source_frame, text="Hash a file", indicator=0, value=2, width=15, variable=HASH_SOURCE_IMPORT_METHOD)
        self.hash_source_file.grid(row=3, column=4, padx=5, pady=5, sticky = NE)
        
        # self.hash_source_file_import = Button(self.Source_frame, text = "Import your file!", width=12, bg='#D1FFBD', command=self.hash_fileimport_func)
        # self.hash_source_file_import.grid(row=4, column=4, padx=3, pady=8, sticky = NW)
        
        #   4.x adding "File path" - new row is 7
        self.file_path_label = Label(frame_4_HASH, text="File path")
        self.file_path_label.grid(row=7, column=0, sticky=E)
        self.file_path_output_text = Text(frame_4_HASH, font = "Courier 9", height=2, width=64)
        self.file_path_output_text.grid(row=7, column=1, columnspan=4, padx=5, pady=5, sticky=W)
        
        #   4.2 HMAC key input - was row 6. changed to 8
        self.hash_hmac_key_label = Label(frame_4_HASH, text="HMAC key")
        self.hash_hmac_key_label.grid(row=8, column=0, sticky=E)
        self.hash_hmac_key_entry = Entry(frame_4_HASH, font = "Courier 9", width=64)
        self.hash_hmac_key_entry.grid(row=8, column=1, columnspan=4, padx=5, pady=5, sticky=W)

        #   RULER ! - was row 7. changed to 9
        self.ruler = Label(frame_4_HASH, text="|----8 Bytes---||----8 Bytes---||----8 Bytes---||----8 Bytes---|", font="Courier 9", width=64)
        self.ruler.grid(row=9, column=1, columnspan=4, padx=6, sticky=W)

        #   4.3 Data Input - was row 8. changed to 10
        self.hash_input_label = Label(frame_4_HASH, text="HEX data")
        self.hash_input_label.grid(row=10, column=0, sticky=E)
        self.hash_input_entry = Entry(frame_4_HASH, font = "Courier 9", width=64)
        # self.hash_input_entry = Text(frame_4_HASH, font = "Courier 9", height=2, width=64)
        self.hash_input_entry.grid(row=10, column=1, columnspan=4, padx=5, pady=5, sticky=W)
        #   4.4 Data Output - was row 9. changed to 11
        self.hash_output_label = Label(frame_4_HASH, text="Hash\nResult")
        self.hash_output_label.grid(row=11, column=0, sticky=E)
        self.hash_output_text = Text(frame_4_HASH, font = "Courier 9", height=4, width=64)
        self.hash_output_text.grid(row=11, column=1, columnspan=4, padx=5, pady=5, sticky=W)
        #   4.4 Go button - was row 10. changed to 12
        self.go_button_hash = Button(frame_4_HASH, text="Go!", width=10, bg='#D1FFBD', command=self.execution_HASH)
        self.go_button_hash.grid(row=12, column=4, padx=5, pady=5, sticky=E)

        #   5   XOR
        self.XOR_frame = LabelFrame(frame_5_XOR, text=" XOR ", font=("Helvetica", 12, "bold"), padx=5, pady=5)
        self.XOR_frame.grid(row=1, column=1, rowspan=4, columnspan=4, sticky=NS)
        #   5.1 data A & B & result labels
        self.xor_inputA_label = Label(self.XOR_frame, text="Input A")
        self.xor_inputA_label.grid(row=2, column=1, padx=5, sticky=W)
        self.xor_inputB_label = Label(self.XOR_frame, text="Input B")
        self.xor_inputB_label.grid(row=4, column=1, padx=5, sticky=W)
        self.xor_result_label = Label(self.XOR_frame, text="Output")
        self.xor_result_label.grid(row=5, column=1, padx=5, sticky=W)

        #   RULER !
        self.ruler = Label(self.XOR_frame, text="|----8 Bytes---||----8 Bytes---||----8 Bytes---||----8 Bytes---|", font="Courier 9", width=64)
        self.ruler.grid(row=3, column=2, padx=6, sticky=W)

        #   5.2 data A & B Entry widgets
        self.xor_inputA_value = Entry(self.XOR_frame, font = "Courier 9", width=64)
        self.xor_inputA_value.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky=W)
        self.xor_inputB_value = Entry(self.XOR_frame, font = "Courier 9", width=64)
        self.xor_inputB_value.grid(row=4, column=2, columnspan=2, padx=5, pady=5, sticky=W)
        self.xor_result_value = Text(self.XOR_frame, font = "Courier 9", height=8, width=64)
        self.xor_result_value.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky=W)
        #   5.3 button GO!
        self.go_button_XOR = Button(frame_5_XOR, text="Go!", width=10, bg='#D1FFBD', command=self.execution_XOR)
        self.go_button_XOR.grid(row=9, column=4, padx=5, pady=5, sticky=E)

        #   6   Random number generator button
        self.rng_bar_bar = LabelFrame(frame_6_RNG, text=" Random number generator ", font=("Helvetica", 12, "bold"), padx=5, pady=5)
        self.rng_bar_bar.grid(row=1, column=1, rowspan=4)
        self.rng_butt_8B = Button(self.rng_bar_bar, text="Generate 8-byte rng", command=self.rng_gen_8B)
        self.rng_butt_8B.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.rng_8B_textbox = Text(self.rng_bar_bar, font = "Courier 9", height=1, width=64)
        self.rng_8B_textbox.grid(row=5, column=1, padx=5, pady=5, sticky=N+W)

        self.rng_butt_32B = Button(self.rng_bar_bar, text="Generate 32-byte rng", command=self.rng_gen_32B)
        self.rng_butt_32B.grid(row=6, column=1, padx=5, pady=5, sticky=W)
        self.rng_32B_textbox = Text(self.rng_bar_bar, font = "Courier 9", height=4, width=64)
        self.rng_32B_textbox.grid(row=7, column=1, padx=5, pady=5, sticky=N+W)

        self.rng_butt_88B = Button(self.rng_bar_bar, text="Generate 88-byte rng", command=self.rng_gen_88B)
        self.rng_butt_88B.grid(row=8, column=1, padx=5, pady=5, sticky=W)
        self.rng_88B_textbox = Text(self.rng_bar_bar, font = "Courier 9", height=4, width=64)
        self.rng_88B_textbox.grid(row=9, column=1, padx=5, pady=5, sticky=N+W)

        #   6.1 PWD gen
        self.pwd_bar = LabelFrame(frame_6_PWD, text=" Password generator ", font=("Helvetica", 12, "bold"), padx=5, pady=5)
        self.pwd_bar.grid(row=1, column=1, rowspan=4)
        self.pwd_8dig_butt = Button(self.pwd_bar, text="Generate 8-digit password", command=self.pwd_gen_8dig)
        self.pwd_8dig_butt.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.pwd_8dig_textbox = Text(self.pwd_bar, font = "Courier 9", height=2, width=64)
        self.pwd_8dig_textbox.grid(row=5, column=1, padx=5, pady=5, sticky=N+W)

        self.pwd_16dig_butt = Button(self.pwd_bar, text="Generate 16-digit password", command=self.pwd_gen_16dig)
        self.pwd_16dig_butt.grid(row=6, column=1, padx=5, pady=5, sticky=W)
        self.pwd_16dig_textbox = Text(self.pwd_bar, font = "Courier 9", height=2, width=64)
        self.pwd_16dig_textbox.grid(row=7, column=1, padx=5, pady=5, sticky=N+W)

        self.PWD_gen_note = Label(self.pwd_bar, justify=LEFT, anchor=W, text=pwd_gen_msg)
        self.PWD_gen_note.grid(row=8, column=0, columnspan=2, sticky='new', padx=5, pady=5)

        #   7   120 PINs
        self.pin_120_bar = LabelFrame(frame_7_120, text=" Elapsed time of 120 online PIN entry test ", font=("Helvetica", 12, "bold"), padx=5, pady=5)
        self.pin_120_bar.grid(row=1, column=1, columnspan=4)

        self.start_lb = Label(self.pin_120_bar, text="PIN entry started at:")
        self.start_lb.grid(row=1, column=1, sticky=E, padx=5, pady=5)
        self.start_tm = Text(self.pin_120_bar, font=("Courier", 9), height=1, width=42)
        self.start_tm.grid(row=1, column=2, sticky=W, padx=5, pady=5)

        self.last_lb = Label(self.pin_120_bar, text="Last PIN entered at:")
        self.last_lb.grid(row=2, column=1, sticky=E, padx=5, pady=5)
        self.last_tm = Text(self.pin_120_bar, font=("Courier", 9), height=15, width=42)
        self.last_tm.grid(row=2, column=2, sticky=W, padx=5, pady=5)

        self.pin_entry_start_bt = Button(self.pin_120_bar, text="Start!", width=10, command=self.p120_start)
        self.pin_entry_start_bt.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky=W)

        self.pin_entry_going_bt = Button(self.pin_120_bar, text="Go!", width=10, command=self.p120_go)
        self.pin_entry_going_bt.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky=E)

        self.pin_entry_end_bt = Button(self.pin_120_bar, text="Terminate!", width=10, command=self.p120_end)
        self.pin_entry_end_bt.grid(row=4, column=2, columnspan=2, padx=5, pady=5, sticky=E)

        #   8   About CryptoBox
        self.abt_bar = LabelFrame(frame_8_ABT, text=" About CryptoBox ", font=("Helvetica", 16, "bold"))
        self.abt_bar.grid(row=1, column=1)

        self.CB_about_label = Label(self.abt_bar, justify=LEFT, anchor=N, text=abt_msg)
        self.CB_about_label.grid(row=2, column=2, columnspan=2, sticky='new', padx=5, pady=5)

        self.developer = Button(self.abt_bar, text="Contact me!", width=15, command=self.contact_developer)
        self.developer.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

def quit():
    global root
    root.quit()

update_timeText()
app = CryptoBox()
root.iconbitmap('logo.ico')
root.mainloop()