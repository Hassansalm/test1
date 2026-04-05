from flet import *
from scripts.appbar import create_appbar
from scripts.singlecard import create_image
from scripts.card import create_cards
from scripts.virtcard import create_vcard

def main(page:Page):
    page.title="Routers"
    page.window.top=1
    page.window.left=960
    page.window.width=350
    page.window.height=950
    page.bgcolor="#2c2c2c"
    page.vertical_alignment=MainAxisAlignment.CENTER
    page.horizontal_alignment=CrossAxisAlignment.CENTER
    page.scroll=ScrollMode.AUTO

    page.appbar =create_appbar()



    page.add(
        create_image(),
        Text("TYPE OF ROUTERS",size=24,color="#34759b",weight="bold"),
        create_cards(),
        create_vcard()
    )

    page.update()

app(target=main)
