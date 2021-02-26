import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

closing_ch=0
#Set the timer here
t=0.5

#For first (right) cell 
GPIO.setup(2,GPIO.OUT)  #1
GPIO.setup(3,GPIO.OUT)  #2
GPIO.setup(17,GPIO.OUT)  #3
GPIO.setup(27,GPIO.OUT)  #4
GPIO.setup(22,GPIO.OUT)  #5
GPIO.setup(10,GPIO.OUT)  #6

#for second (right) cell
GPIO.setup(9,GPIO.OUT)  #1
GPIO.setup(5,GPIO.OUT)  #2
GPIO.setup(6,GPIO.OUT)  #3
GPIO.setup(13,GPIO.OUT)  #4
GPIO.setup(19,GPIO.OUT)  #5
GPIO.setup(26,GPIO.OUT)  #6

#play-pause
GPIO.setup(18,GPIO.IN)

def print_braille_right(arr):
    GPIO.output(2,arr[0])
    GPIO.output(3,arr[1])
    GPIO.output(17,arr[2])
    GPIO.output(27,arr[3])
    GPIO.output(22,arr[4])
    GPIO.output(10,arr[5])
    #time.sleep(t)
    
def print_braille_left(arr):
    GPIO.output(9,arr[0])
    GPIO.output(5,arr[1])
    GPIO.output(6,arr[2])
    GPIO.output(13,arr[3])
    GPIO.output(19,arr[4])
    GPIO.output(26,arr[5])
    #time.sleep(t)    

br_script={ 'a':[1,0,0,0,0,0], 'b':[1,1,0,0,0,0], 'c':[1,0,0,1,0,0], 'd':[1,0,0,1,1,0], 'e':[1,0,0,0,1,0],
'f':[1,1,0,1,0,0], 'g':[1,1,0,1,1,0], 'h':[1,1,0,0,1,0], 'i':[0,1,0,1,0,0], 'j':[0,1,0,1,1,0],
'k':[1,0,1,0,0,0], 'l':[1,1,1,0,0,0], 'm':[1,0,1,1,0,0], 'n':[1,0,1,1,1,0], 'o':[1,0,1,0,1,0], 
'p':[1,1,1,1,0,0], 'q':[1,1,1,1,1,0], 'r':[1,1,1,0,1,0], 's':[0,1,1,1,0,0], 't':[0,1,1,1,1,0], 
'u':[1,0,1,0,0,1], 'v':[1,1,1,0,0,1], 'w':[0,1,0,1,1,1], 'x':[1,0,1,1,0,1], 'y':[1,0,1,1,1,1], 
'z':[1,0,1,0,1,1], '1':[1,0,0,0,0,0], '2':[1,1,0,0,0,0], '3':[1,0,0,1,0,0], '4':[1,0,0,1,1,0], '5':[1,0,0,0,1,0],
'6':[1,1,0,1,0,0], '7':[1,1,0,1,1,0], '8':[1,1,0,0,1,0], '9':[0,1,0,1,0,0], '0':[0,1,0,1,1,0], ' ':[0,0,0,0,0,0], '.':[0,1,0,1,0,1] }

book_name='book red'
#book_name='book green'
#book_name='book blue'


ch_file_name=book_name+'_ch.txt'

f=open(ch_file_name,'r')
ch_num=f.read()
ch_num=int(ch_num)
f.close()

f=open('ab.txt')
text=f.read()

#new_words=[]
full_text=text.split(' ')

full_text_len=len(full_text)

#print(text)
#print(w_len)


  
for i in range(ch_num,full_text_len):
    len_ch=len(full_text[i])
    text_word=full_text[i]
    while(GPIO.input(18)==1):
        for j in range(len_ch):
            #print_braille_left(br_script[text[i]])
            print(text_word[j])
            #print_braille_right(br_script[text[i+1]])
            if j!=len_ch-1:
                print(text_word[j+1])
            else:
                continue
            time.sleep(t)        
        
        os.system('espeak '+full_text[i]+' 2>/dev/null')
    
closing_ch=i        

f=open(ch_file_name,'w+')
f.write(str(closing_ch))
f.close()

