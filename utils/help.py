from utils import messages

def basic_help():
    print(
        f"""
{messages.title} clear              Clears your screen.
{messages.title} modules            shows available modules.
{messages.title} info               information.
        """)


def modules_show():
    print(
        f"""
{messages.title} 1            Stars the Token generator.
{messages.title} 2               No handlings currently.
        """)