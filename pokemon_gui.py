from guizero import App, Text, TextBox, PushButton, Picture
from pokebase import pokemon
from requests import get
from PIL import Image
from io import BytesIO

def fetch_pokemon():
    name = input_box.value
    try:
        poke = pokemon(name)
        pic = get(poke.sprites.front_default).content
        height.value = "Height " + str(poke.height) + "ft"
        weight.value = "Weight " + str(poke.weight) + "lbs"
        image = Image.open(BytesIO(pic))
        image.save('poke.gif')
        icon.value = 'poke.gif'
        response.value=""
    except:
        response.value="Pokemon not found"
        height.value = ""
        weight.value = "" 
    

    
app = App(title='Pokemon Fetcher', width=300, height=300)
input_box = TextBox(app, text='Name')
icon = Picture(app, image="poke.gif")
height = Text(app, text="Height")
weight= Text(app, text="Weight")
submit = PushButton(app, command=fetch_pokemon, text='Submit')
response = Text(app, text="")

app.display()


