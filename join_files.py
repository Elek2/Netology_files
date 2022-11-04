import requests


def get_example_files():
	url1 = 'https://raw.githubusercontent.com/netology-code/py-homework-basic-files/master/2.4.files/sorted/1.txt'
	url2 = 'https://raw.githubusercontent.com/netology-code/py-homework-basic-files/master/2.4.files/sorted/2.txt'
	url3 = 'https://raw.githubusercontent.com/netology-code/py-homework-basic-files/master/2.4.files/sorted/3.txt'
	urls = [url1, url2, url3]

	new_files_names = ['Text1.txt', 'Text2.txt', 'Text3.txt']

	for url, new_files_name in zip(urls, new_files_names):
		response = requests.get(url)
		text = response.content

		with open(new_files_name, 'wb') as f:
			f.write(text)

get_example_files()


def join_files():
	files_names = ['Text1.txt', 'Text2.txt', 'Text3.txt']
	all_files = []
	for file in files_names:
		with open(file, encoding='utf-8') as f:
			# text = f.readlines()
			text = [i.rstrip('\n') for i in f.readlines()]
			file_info = [file, text, len(text)]
		all_files.append(file_info)
	print(*all_files, sep='\n')

	with open('Result_text.txt', 'w', encoding="utf-8") as res:
		for i in sorted(all_files, key=lambda x: x[2]):
			res.write(i[0])
			res.write('\n')
			res.write(str(i[2]))
			res.write('\n')
			res.write('\n'.join(i[1]))
			res.write('\n')

join_files()
