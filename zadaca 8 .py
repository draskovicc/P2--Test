import re

regex_email = r"^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$"
regex_eduid = r"^[a-zA-Z]+\.[a-zA-Z]+\d*@sum\.ba$"

email = input("unesi e-mail:")
eduid = input("unesi eduid:")

if re.match(regex_email, email):
    print("E- mail je ipravan.")
else:
    print("E- mail nije ispravan.")


if re.match(regex_eduid, eduid):
    print("eduId je ispravan.")
else:
    print("eduId nije ispravan.")
