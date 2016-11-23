import webbrowser, BeautifulSoup ,requests

print('Enter your programming related question:')
question = raw_input()

res = requests.get('https://www.google.ca/search?q=' + question+' site:stackoverflow.com')

res.raise_for_status()

soup = BeautifulSoup.BeautifulSoup(res.text, "html.parser")

text = str(soup).split()

link = ""

for x in text:
    if "http://stackoverflow.com/questions" in x and not 'webcache' in x:
        link = x[13:].split("&")[0]
        print(link)
        break


if link != "":
    webbrowser.open(link)
    pass
else:
    print("Sorry, but no answer was found for your question")
