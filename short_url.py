import pyshorteners

try:
	while True:
		link = input(">>>")

		if link == 'q':
			print("Good luck!")
			break

		print('\n')

		shortener = pyshorteners.Shortener()
		url = shortener.tinyurl.short(link)

		print(f"Your link: {url}")
		print("[*] Type 'q' to quit.")

except KeyboardInterrupt:
	print("Good luck!")

