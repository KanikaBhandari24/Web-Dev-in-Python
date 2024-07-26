from bs4 import BeautifulSoup
import requests
import smtplib

mail="email dalo"
Pass="app password dalo"

url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
#live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

response=requests.get(url, headers=header)
soup=BeautifulSoup(response.content, "html.parser")
#print(soup.prettify())

price=soup.find(class_="a-offscreen").get_text()
pricec=price.split("$")[1]
pricef=float(pricec)
print(pricef)

#email sending
title=soup.find(id="productTitle").get_text().strip()
print(title)

buy=100
if pricef < buy:
    msg1=f"{title} is on sale for {price}!"

    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        result=connect.login(mail, password=Pass)
        connect.sendmail(
            from_addr=mail,
            to_addrs=mail,
            msg=f"Subject: Amazon Price Alert!\n\n{msg1}\n{url}".encode("utf-8")
        )
