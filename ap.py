from newsapi import NewsApiClient
import pycountry

newsapi = NewsApiClient(api_key='Your API Key')

input_country = input("Country: ")
input_countries = [f'{input_country.strip()}']
countries = {}

for country in pycountry.countries:
    countries[country.name] = country.alpha_2

codes = [countries.get(country.title(), 'Unknown code')
         for country in input_countries]

option = input(
    "Which category are you interested in?\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Science\n6.Technology\n\nEnter here: ")

top_headlines = newsapi.get_top_headlines(

    category=f'{option.lower()}', language='en', country=f'{codes[0].lower()}')

Headlines = top_headlines['articles']

if Headlines:
    for articles in Headlines:
        b = articles['title'][::-1].index("-")
        if "news" in (articles['title'][-b + 1:]).lower():
            print(
                f"{articles['title'][-b + 1:]}: {articles['title'][:-b - 2]}.")
        else:
            print(
                f"{articles['title'][-b + 1:]} News: {articles['title'][:-b - 2]}.")
else:
    print(
        f"Sorry no articles found for {input_country}, Something Wrong!!!")
option = input("Do you want to search again[Yes/No]?")
if option.lower() == 'yes':
    continue
else:
    exit()

canvas = tk.Tk()
canvas.geometry("900x600")
canvas.title("News App")

button = tk.Button(canvas, font = 24, text = "Reload", command = getNews)
button.pack(pady = 20)

label = tk.Label(canvas, font = 18, justify = "left")
label.pack(pady = 20)

getNews()

canvas.mainloop()