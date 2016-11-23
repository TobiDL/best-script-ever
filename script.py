import webbrowser, BeautifulSoup ,requests

print('Enter your programming related question:')
question = raw_input()

res = requests.get('https://www.google.ca/search?q=' + question+" stack+overflow")

res.raise_for_status()

soup = BeautifulSoup.BeautifulSoup(res.text)

text = str(soup).split()

link = ""

for x in text:
    if "stackoverflow" in x:
        link = x[13:].split("\"")[0]
        break

if link != "":
    webbrowser.open(link)
else:
    print("Sorry, but no answer was found for your question")
