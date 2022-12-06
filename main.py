print("Hey Users! I am CONVERTO, your Currency Converter.")
print("List of currency we convert")
print("1. Indian Rupees")
print("2. American Dollar")
print("3. Euros")
print("4. Dirham")
print("5. Kuwaiti Dinar")
print("6. Pound")
print("7. Japanese Yen")
print("8. Pakistani Rupee")
print("9. Nepalese Rupee")
print("10. Swedish Krona")
a=eval(input("Enter the amount which you want convert:\n"))
print("NOTE:- Please enter the name of currency from the list given above.")
print("NOTE:- Please make sure that you enter the first letter of each word capital.")
b=input("Enter the name of currency from which you want to convert:\n" )
c=input("Enter the name of currency to which you want to convert:\n")

if b=="American Dollar" and c=="Euros":
# 1 us dollar equal to 0.96 euros
    print(0.96*a, "EUR")
elif b=="Euros" and c=="American Dollar":
    print(a/0.96, "USD")
elif b=="American Dollar" and c=="Indian Rupees":
# 1 dollar equal to 81.67 ruppes
    print(a*81.67, "INR")
elif b=="Indian Rupees" and c=="American Dollar":
    print(a/81.67, "USD")
elif b=="Euros" and c=="Indian Rupees":
# 1 euros equal to 85.06 rupees
    print(a*85.06, "INR")
elif b=="Indian Rupees" and c=="Euros":
    print(a/85.06,"EUR")
elif b=="Dirham" and c=="Indian Rupees":
# 1 dirham equal to 22.24 rupees
    print(a*22.24,"INR")
elif b=="Indian Rupees" and c=="Dirham":
    print(a/22.24,"AED")
elif b=="Dirham" and c=="Euros":
# 1 dirham equal to 0.26 euros
    print(a*0.26,"EUR")
elif b=="Euros" and c=="Dirham":
    print(a/0.26,"AED")
elif b=="American Dollar" and c=="Dirham":
# 1 Dollar is equal to 3.67 Dollar
    print(a*3.67,"AED")
elif b=="Dirham" and c=="American Dollar":
    print(a/3.67,"USD")
elif b=="Kuwaiti Dinar" and c=="American Dollar":
# 1 kuwaiti dinar equal to 3.25 dollar
    print(a*3.25,"USD")
elif b=="American Dollar" and c=="Kuwaiti Dinar":
    print(a/3.25,"KWS")
elif b=="Euros" and c=="Kuwaiti Dinar":
# 1 euros equal to 0.32 kwd
    print(a*0.32,"KWD")
elif b=="Kuwaiti Dinar" and c=="Euros":
    print(a/0.32,"EUR")
elif b=="kuwaiti Dinar" and c=="Indian Rupees":
# 1 kuwaiti dinar equal to 265.58 rs
    print(a*265.58,"INR")
elif b=="Indian Rupees" and c=="Kuwaiti Dinar":
    print(a/265.58,"KWD")
elif b=="Dirham" and c=="Kuwaiti Dinar":
# 1 dirham equal to 0.084 kwd
    print(a*0.084,"KWD")
elif b=="Kuwaiti Dinar" and c=="Dirham":
    print(a/0.084,"AED")
elif b=="Pound" and c=="American Dollar":
# 1 pound equal to 1.21 dollar
    print(a*1.21,"USD")
elif b=="American Dollar" and c=="Pound":
    print(a/1.21,"GBP")
elif b=="Pound" and c=="Euros":
# 1 pound equal to 1.16 euros
    print(a*1.16,"EUR")
elif b=="Euros" and c=="Pound":
    print(a/1.16,"GBP")
elif b=="Pound" and c=="Indian Rupees":
# 1 rs equal 98.75 pound
    print(a*98.75,"INR")
elif b=="Indian Rupees" and c=="Pound":
    print(a/98.75,"GBP")
elif b=="Pound" and c=="Dirham":
# 1 pound equal to 4.44 dirham
    print(a*4.44,"AED")
elif b=="Dirham" and c=="Pound":
    print(a/4.44,"GBP")
elif b=="Pound" and c=="Kuwaiti Dinar":
# 1 pound equal to 0.37 kwd
    print(a*0.37,"KWD")
elif b=="Kuwaiti Dinar" and c=="Pound":
    print(a/0.37,"GBP")
elif b=="Japanese yen" and c=="American Dollar":
# 1 Japanese yen equal to 0.0072 dollar
    print(a*0.0072,"USD")
elif b=="American Dollar" and c=="Japanese Yen":
    print(a/0.0072,"JPY")
elif b=="Japanese Yen" and c=="Euros":
    # 1 Japanese yen equla to 0.0069 euros
    print(a*0.0069,"EUR")
elif b == "Euros" and c == "Japanese Yen":
    print(a/0.0069,"JPY")
elif b=="Japanese Yen" and c=="Indian Rupees":
# 1 Japanese yen equal to 0.59 rs
    print(a*0.59,"INR")
elif b=="Indian Rupees" and c=="Japanese Yen":
    print(a/0.59,"JPY")
elif b=="Japanese Yen" and c=="Dirham":
# 1 Japanese yen equal to 0.026 dirham
    print(a*0.026,"AED")
elif b=="Dirham" and c=="Japanese Yen":
    print(a/0.026,"JPY")
elif b=="Japanese Yen" and c=="Kuwaiti Dinar":
# 1 Japanese yen equal to 0.0022 kuwaiti Dinar
    print(a*0.0022,"KWD")
elif b=="Kuwaiti Dinar" and c=="Japanese Yen":
    print(a/0.0022,"JPY")
elif b=="Japanese Yen" and c=="Pound":
# 1 Japanese yen equal to 0.0059 pound
    print(a*0.0059,"GBP")
elif b=="Pound" and c=="Japanese Yen":
    print(a/0.00590,"JPY")
elif b=="American Dollar" and c=="Pakistani Rupee":
# 1 dollar equal to 223.50 pak rupee
    print(a*223.50,"PKR")
elif b=="Pakistani Rupee" and c=="American Dollar":
    print(a/223.50,"USD")
elif b=="Euros" and c=="Pakistani Rupee":
# 1 euro to pak rupees equal to 232.76
    print(a*232.76,"PKR")
elif b=="Pakistani Rupee" and c=="Euros":
    print(a/232.76,"EUR")
elif b=="Indian Rupees" and c=="Pakistani Rupee":
    # 1 Dirham equal to 60.85 pkr
    print(a*60.85,"PKR")
elif b=="Pakistani Rupee" and c=="Dirham":
    print(a/60.85,"AED")
elif b=="Kuwaiti Dinar" and c=="Pakistani Rupee":
# 1 kwd =728.03 pkr
    print(a*728.03,"PKR")
elif b=="Pakistani Rupee" and c=="kuwaiti Dinar":
    print(a/728.03,"KWD")
elif b=="Pound" and c=="Pakistani Rupee":
# 1 pound =270.23 pkr
    print(a*270.23,"PKR")
elif b=="Pakistani Rupee" and c=="Pound":
    print(a/270.23,"GBP")
elif b=="Japanese Yen" and c=="Pakistani Rupee":
# 1 japanese yen = 1.61 pkr
    print(a*1.61,"PKR")
elif b=="Pakistani Rupee" and c=="Japanese Yen":
    print(a/1.61,"JPY")
elif b=="American Dollar" and c=="Nepalese Rupee":
# 1 dollar = 130.55 npr
     print(a*130.55,"NPR")
elif b=="Nepalese Rupee" and c=="American Dollar":
    print(a/130.55,"USD")
elif b=="Euros" and c=="Nepalese Rupee":
#  1 euro =232.76 NPR
    print(a*232.76,"NPR")
elif b=="Nepalese Rupee" and c=="Euros":
    print(a/232.76,"EUR")
elif b=="Indian Rupees" and c=="Nepalese Rupee":
# 1 rupees = 1.60 npr
    print(a*1.60,"NPR")
elif b=="Nepalese Rupee" and c=="Indian Rupees":
    print(a/1.60,"INR")
elif b=="Dirham" and c=="Nepalese Rupee":
# 1 dirham = 35.54 npr
    print(a*35.54,"NPR")
elif b=="Nepalese Rupee" and c=="Dirham":
    print(a/35.54,"AED")
elif b=="Kuwaiti Dinar" and c=="Nepalese Rupee":
# 1 kwd = 425.26 npr
    print(a*425.26,"NPR")
elif b=="Nepalese Rupee" and c=="Kuwaiti Dinar":
    print(a/425.26,"KWD")
elif b=="Pound" and c=="Nepalese Rupee":
# 1 pound = 157.85 npr
    print(a*157.85,"NPR")
elif b=="Nepalese Rupee" and c=="Pound":
    print(a/157.85, "GBP")
elif b=="Japanese Yen" and c=="Nepalese Rupee":
# 1 japanese yen =0.94 npr
    print(a*0.94,"NPR")
elif b=="Nepalese Rupee" and c=="Japanese Yen":
    print(a/0.94,"JPY")
elif b=="Pakistani Rupee" and c=="Nepalese Rupee":
# 1 pkr =0.58 npr
    print(a*0.58,"NPR")
elif b=="Nepalese Rupee" and c=="Pakistani Rupee":
    print(a/0.58,"PKR")
elif b=="American Dollar" and c=="Swedish Krona":
# 1 dollar = 10.43 swedish krona
    print(a*10.43, "SEK")
elif b=="Swedish Krona" and c=="American Dollar":
    print(a/10.43,"USD")
elif b=="Euros" and c=="Swedish Krona":
# 1 euro = 10.85 Swedish krona
    print(a*10.85, "SEK")
elif b=="Swedish krona" and c=="Euros":
    print(a/10.85, "GBP")
elif b=="Indian Rupees" and c=="Swedish Krona":
# 1 inr = 0.13 Swedish krona
    print(a*0.13, "SEK")
elif b=="Swedish Krona" and c=="Indian Rupees":
    print(a/0.13, "INR")
elif b=="Dirham" and c=="Swedish Krona":
#  1 dirham = 2.84 Swedish krona
    print(a*2.84, "SEK")
elif b=="Swedish Krona" and c=="Dirham":
    print(a/2.84, "AED")
elif b=="Kuwaiti Dinar" and c=="Swedish Krona":
# 1 kwd = 33.99 Swedish krona
    print(a*33.99,"SEK")
elif b=="Swedish Krona" and c=="Kuwaiti Dinar":
    print(a/33.99, "KWD")
elif b=="Pound" and c=="Swedish Krona":
# 1 pound =12.62 Swedish krona
    print(a*12.62, "SEK")
elif b=="Swedish Krona" and c=="Pound":
    print(a/12.62, "GBP")
elif b=="Japanese Yen" and c=="Swedish Krona":
# 1 japanese yen =0.075 Swedish krona
    print(a*0.075, "SEK")
elif b=="Swedish Krona" and c=="Japanese Yen":
    print(a/0.075, "JPY")
elif b=="Pakistani Rupee" and c=="Swedish Krona":
# 1 pak rupee =0.047 Swedish krona
    print(a*0.047, "SEK")
elif b=="Swedish Krona" and c=="Pakistani Rupee":
    print(a/0.047, "PKR")
elif b=="Nepalese Rupee" and c=="Swedish Krona":
# 1 npr = 0.080 Swedish krona
    print(a*0.080,"SEK")
elif b=="Swedish Krona" and c=="Nepalese Rupee":
    print(a/0.080, "NPR")
else:
    print("Invalid statement")
