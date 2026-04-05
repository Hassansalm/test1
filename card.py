from flet import *

def create_cards():
    items =[
        {"image":"assets/prodict/ac1200.jpeg"},
        {"image":"assets/prodict/ax10.jpeg"},
        {"image":"assets/prodict/ax12.jpeg"},
        {"image":"assets/prodict/ax55.jpeg"},
        {"image":"assets/prodict/mac1200.jpeg"},
        {"image":"assets/prodict/mac1900.jpeg"},
        {"image":"assets/prodict/decos7.jpeg"},
        {"image":"assets/prodict/huaweir.jpeg"},
        {"image":"assets/prodict/be6500.jpeg"},
        {"image":"assets/prodict/decom4.jpeg"}
    ]
    card_list=[]

    for item in items:
        card = Container(
            width=90,padding=0,bgcolor='white',
            border_radius=6,shadow=BoxShadow(blur_radius=3),

            content= Container(
                content=Image(
                    src=item["image"],
                    width=90,height=56,
                ),
                alignment=Alignment.CENTER,
                border=Border.all(2,"#000000"),
                border_radius=6
            )
        )
        card_list.append(card)
    raw_cont =Container(
        content=Row(
            card_list,
            spacing=8,
            alignment=MainAxisAlignment.START,
            scroll=ScrollMode.AUTO,
            height=80
            
        ),
        padding=20
    )
    return (raw_cont)    
