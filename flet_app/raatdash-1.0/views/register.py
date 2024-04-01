import flet as ft
from password_strength import PasswordPolicy

policy = PasswordPolicy.from_names(
    length = 13,  # need min. 2 non-letter characters (digits, specials, anything)
)

def Register(router):

    def validate(e):
        page = e.page
        if all([Username.value, Email.value, Pass.value, PassConfirm.value]):
            if policy.test(Pass.value) != []:
                Submit.disabled = True
                Pass.error_text = "Password must be >12 characters."
                page.update()
            else:
                Pass.error_text = ""
                page.update()
                if Pass.value != PassConfirm.value:
                    Submit.disabled = True
                    PassConfirm.error_text = "Passwords do not match."
                    page.update()
                else:
                    PassConfirm.error_text=""
                    Submit.disabled = False
                    page.update()
        else:
            Submit.disabled = True
            page.update()
    
    def submitform(e):
        page = e.page
        page.clean()
        page.add(ft.Text(value="Success!"))
        page.update()
    
    def loginclick(e):
        page = e.page
        page.go('/login')

    
    WelcomeHeader = ft.Text("Registration", size=30)
    Username = ft.TextField(label="Username", width = 400, bgcolor="white")
    Email = ft.TextField(label = "Email", width = 400, bgcolor="white")
    Pass = ft.TextField(label = "Password", password=True, can_reveal_password=True, width = 400, bgcolor="white")
    PassConfirm = ft.TextField(label = "Confirm password", password = True, can_reveal_password=True, width = 400, bgcolor="white")
    Submit = ft.IconButton(icon="arrow_forward", icon_size=40, disabled=True)
    GoBack = ft.TextButton(text="Go back to login.", on_click=loginclick)

    Username.on_change = validate
    Email.on_change = validate
    Pass.on_change = validate
    PassConfirm.on_change = validate
    Submit.on_click = submitform

    content = ft.Container(
            content=
                ft.Column(
                    controls = [WelcomeHeader, Email, Username, Pass, PassConfirm, ft.Container(content = Submit, alignment= ft.alignment.center_right), 
                                ft.Container(content = GoBack, alignment=ft.alignment.center_left)],
                    alignment = ft.alignment.center
            ),
            padding = 40,
            bgcolor = "white",
            border_radius = 5,
            
        )
    return content
