import string
import secrets
import qrcode
import uuid
import pyfiglet
import os
import time
import tkinter as tk
import datetime
import sys

CYAN = "\033[36m"
YELLOW = "\033[33m"
ORANGE = '\033[38;5;214m'
RESET = "\033[0m"

ascii_raw = pyfiglet.figlet_format('            TadicGenerator', font='slant')
RealTDC_text = CYAN + ascii_raw + RESET

def clr_shit():
     os.system('cls' if os.name == 'nt' else 'clear')

def password_generator():
        clr_shit()
        karakterler = string.ascii_letters + string.digits + "!@#$%&*"
        customsifre = input('Select length (Max 30) (only type numbers): ')
        try:
            customsifre_int = int(customsifre)
            if customsifre_int > 30 or customsifre_int <= 0:
                print('Invalid Length!')
                print(' ')
                input('press enter to go back')
                clr_shit()
            else:
                sifre = "".join(secrets.choice(karakterler) for _ in range(customsifre_int))
                print('Generating password...')
                print(' ')
                print(sifre)
                print(' ')
                input('Press ENTER to copy password and go back...')
                root = tk.Tk()
                root.withdraw() 
                root.clipboard_clear()
                root.clipboard_append(sifre)
                root.update() 
                root.destroy() 
               
                clr_shit()
                print("✔ Password copied to clipboard successfully!")
                time.sleep(1.5)
                clr_shit()
        except ValueError:
            print('Please enter a valid number!')
            input('press enter to go back')
            return

def qr_code_generator():
        clr_shit()
        veri = input("Enter text or URL: ")
        img = qrcode.make(veri)
        img.save("qr.png")
        print("QR code saved as qr.png")
        print("Saved to:", os.path.abspath("qr.png"))
        input('press enter to go back')
        return

def uuid_generator():
        clr_shit()
        generated_uuid = str(uuid.uuid4()) 
        print('Your UUID:')
        print(generated_uuid) 
        print(' ')
         
        try:
            with open("uuid.txt", "a", encoding="utf-8") as f:
                f.write(" " + "\n")
                f.write(f"Generated UUID ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}):\n")
                f.write(generated_uuid + "\n")
             
            print("Saved to: ", os.path.abspath("uuid.txt"))
        except Exception as e:
            print(f"Error saving file: {e}")
             
        print(' ')
        input('press enter to go back')
        return

def banner_generator():
       clr_shit()
       ascii_text = input("Text: ")
       print(pyfiglet.figlet_format(ascii_text, font='banner'))
       print(' ')
       input('press enter to go back')
       clr_shit()

def exit_program():
        sys.exit()

generators = {
      '1': password_generator,
      '2': qr_code_generator,
      '3': uuid_generator,
      '4': banner_generator,
      '5': exit_program
}

clr_shit()

while True:
      time.sleep(0.1)
      print(RealTDC_text)
      print(YELLOW + 'Hello! This is TadicGenerator by TADIC SERVICES. Simple generators. No ads. No nonsense. Select an option below:' + RESET)
      print(' ')
      print(ORANGE + '[1. Password Generator]                [2. QR Code Generator]' + RESET)
      print(ORANGE + '[3. UUID Generator]                    [4. ASCII Banner Generator]' + RESET)
      print('[5. EXIT]')
      print(' ')
      print(YELLOW + '--Made by Eymorty--' + RESET)
      print(YELLOW + ' itch.io: https://eymorty.itch.io' + RESET)
      print(YELLOW + ' Website: https://tadicservicesofficial.netlify.app or https://ishowdih.github.io' + RESET)
      print(YELLOW + ' Github:  https://github.com/ishowdih/' + RESET)
      print(' ')

      choice = input('Select a Generator: ')

      if choice in generators:
          generators[choice]()

      else:
            clr_shit()
            print('Well, either you typed it wrong or just didn\'t select something. Please enter a valid number.')
            input('press enter to go back')
            clr_shit()


