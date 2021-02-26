import os

f=open('a.txt')
text=f.read()

new_words=[]
w=text.split(' ')

w_len=len(w)

#print(text)
#print(w)

for i in range(w_len):
	os.system('espeak '+w[i]+' 2>/dev/null')
	
