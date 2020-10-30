import webbrowser
import time
url = "https://www.youtube.com/watch?v=6n3pFFPSlW4"
i = 10
while i >= 0:
	print(i)
	if i == 0:
		webbrowser.open(url,new=1)
	i -= 1
	time.sleep(1)
