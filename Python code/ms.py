import serial
import time
import telebot
from telebot import apihelper
import config
bot = telebot.TeleBot(config.token)

ser = serial.Serial('', 9600, timeout=1) #copy the serial port of the arduino into the ''
time.sleep(2)

mtr = {'A': '12', 'B': '2111', 'C': '2121' , 'D': '211', 'E': '1', 'F': '1121', 'G': '221', 'H': '1111', 'I': '11',
'J': '1222', 'K': '212', 'L' : '1211', 'M': '22', 'N': '21', 'O': '222', 'P': '1221', 'Q': '2212', 'R': '121',
'S': '111', 'T': '2', 'U': '112', 'V': '1112', 'W': '122', 'X': '2112', 'Y': '2122', 'Z': '2211', '1': '12222',
'2': '11222', '3': '11122', '4': '11112', '5': '11111', '6': '21111', '7': '22111', '8': '22211', '9': '22221', '0': '22222'}

@bot.message_handler(content_types=["text"])



def startHandler(message):
    string = message.text
    print("got text")
    string = string.upper()
    file = string.split()
    print (file)

    ser.write(b'0')
    for i in range(len(file)):
        wor = file[i]
        word = wor + 'Э'
        print (word)
        for i in range(len(word)):
            if word[i] == 'Э':
                ser.write(b'3')
            else:
                letter = word[i]
                code = mtr.get(letter)
                for i in range(len(code)):
                    s = code[i]
                    if s == '1':
                        time.sleep(0.11)
                        print (s)
                        ser.write(b'1')
                        print("sent")


                    if s == '2':
                        time.sleep(0.11)
                        print (s)
                        ser.write(b'2')
                        print("sent")

if __name__ == '__main__':
   bot.polling(none_stop=True)
