from flet import *

def create_vcard():
    items= [
        {"image":"assets/prodict/ax10.jpeg","name":"tplink ax10","rating":4,"type":"wifi6"},
        {"image":"assets/prodict/ac1200.jpeg","name":"tplink ac1200","rating":3,"type":"wifi5"},
        {"image":"assets/prodict/ax12.jpeg","name":"tplink ax12","rating":4,"type":"wifi6"},
        {"image":"assets/prodict/ax55.jpeg","name":"tplink ax55","rating":5,"type":"wifi6"},
        {"image":"assets/prodict/be6500.jpeg","name":"tplink be6500","rating":6,"type":"wifi7"},
        {"image":"assets/prodict/c50.jpeg","name":"tplink c50","rating":3,"type":"wifi4"},
        {"image":"assets/prodict/decom4.jpeg","name":"tplink deco m4 ","rating":4,"type":"wifi5"},
        {"image":"assets/prodict/decos7.jpeg","name":"tplink seco s7","rating":5,"type":"wifi5"},
        {"image":"assets/prodict/huaweir.jpeg","name":"huawei","rating":4,"type":"wifi5"},
        {"image":"assets/prodict/mac1200.jpeg","name":" mercusys ac1200","rating":3,"type":"wifi5"},
        {"image":"assets/prodict/mac1300.jpeg","name":" mercusys ac1300","rating":3,"type":"wifi5"},
        {"image":"assets/prodict/mac1900.jpeg","name":"mercusys ac1900","rating":4,"type":"wifi5"},
    ]
    card_list = []

    for item in items:
        stars = Row(
            [Icon(Icons.STAR,color=Colors.YELLOW,size=16) for _ in range(item["rating"])],
            spacing=2
        )

        card =Container(
            padding=5,margin=5,bgcolor="brown",border_radius=8,
            shadow=BoxShadow(blur_radius=4),

            content =Row([                
                Column([
                    Text(f"Name:{item["name"]}",color='white',weight='bold',size=14),
                    Text(f"type:{item["type"]}",color='green',weight='bold',size=14),
                    
                    Row([Text("Rate: ",color="white"),stars])
                ],
                alignment=MainAxisAlignment.START,
                horizontal_alignment=CrossAxisAlignment.START,
                spacing=4,expand=True

                ),
                Container(
                    content=Image(src=item["image"],width=120,height=80),
                    alignment=Alignment.CENTER
                )
            ],
            spacing=10,vertical_alignment=CrossAxisAlignment.CENTER
            )
        )
        card_list.append(card)
    colmn =Container(
        content=Column(
            card_list,

            spacing=10,
            horizontal_alignment=CrossAxisAlignment.CENTER       
                                
        ),
        padding=5
    ) 
    return colmn
