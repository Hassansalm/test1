from flet import *

def create_appbar():
    return AppBar(
        title=Text("routers",size=18,weight='bold',color="#34759b"),
        bgcolor="#524F4F",
        center_title=True,
        leading=Icon(Icons.HOME ,color='white'),
        actions=[
            IconButton(Icons.NOTIFICATIONS,icon_color='white'),
            IconButton(Icons.ACCOUNT_CIRCLE,icon_color="white")
        ]
    )
