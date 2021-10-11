print ('please enter the current tempertaure.')
Tem= int(input(''))
if temp > 90:
	print('Wear Shorts')
elif temp > 70:
	print('short sleeves are fine')
elif temp > 50:
	print('wear a jacket')
elif temp > 32:
	print('wear a heavy coat')
else: 
	print('stay inside')
