

def pay_view(payment):
    global user
    user = 10
    global server
    server = 0

    if payment == 200:
        if user < payment:
            print("not Enough Mony")
        else:
            user = user - payment
            server = server + payment
            return "yes"




pay = pay_view(200)
if pay:
    print("Payment successfull")
else:
    print("failed")


print("user:", user)
print("server: ", server)