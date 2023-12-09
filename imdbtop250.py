#!/usr/bin/env python3
import subprocess, sys, os
import time

try:
    import requests
    from pyfiglet import Figlet
    from bs4 import BeautifulSoup

except ImportError:
    print("Gerekli modüller indiriliyor...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "BeautifulSoup", "BeautifulSoup4", "pyfiglet"])



r = requests
url = "https://www.imdb.com/chart/top/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = r.get(url, headers=headers)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")


def listele():
    ad = []
    rating = []
    for i in soup.find_all("h3",{"class","ipc-title__text"}):
        ad.append(i.text)
    for i in soup.find_all("span",{"class","ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"}):
        rating.append(i.text[0:3])
    for ad, rating in zip(ad,rating):
        print("")
        print("Başlık",ad)
        print("Rating",rating +"\n")
        print("------------------------")

    while True:
        input("Ana Menü İçin Herhangi Bir Tuşa Basın...")
        break
def rating():
    a = float(input("Rating'i giriniz:"))
    global basliklar
    global ratingler

    basliklar = soup.find_all("h3",{"class","ipc-title__text"})
    ratingler = soup.find_all("span",{"class","ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"})

    for baslik, rating in zip(basliklar, ratingler):
        baslik = baslik.text
        rating = rating.text[0:3]

        baslik = baslik.strip()
        baslik = baslik.replace("\n", "")

        rating = rating.strip()
        rating = rating.replace("\n", "")

        if (float(rating) > a):
            print("")
            print("Film ismi: {} \n Filmin Ratingi : {}".format(baslik, rating))
            print("")
            print("-----------------------")
    while True:
        input("Ana Menü İçin Herhangi Bir Tuşa Basın...")
        break
def main():
    while True:
        f = Figlet(font='slant')
        print(f.renderText("IMDB TOP 250"))
        print("-----------------------------------")
        print("Yapmak İstediğiniz İşlemi Seçin")
        print("1 - IMDB TOP 250 Sırala")
        print("2 - Reytinge Göre Sırala")
        print("Çıkmak İçin: 'q'")
        try:
            secim = input("")
        except:
            print("Lütfen Geçerli Bir Değer Girin")
        if secim == "q":
            print("İyi Günler Dilerim...")
            time.sleep(2)
            break
            quit()
        if secim == "1":
            listele()
        if secim == "2":
            rating()
        else:
            print("Lütfen Geçerli Bir Değer Girin")
        


main()