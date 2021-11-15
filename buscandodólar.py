from bs4 import BeautifulSoup
import requests
import pyautogui
import email.message
import smtplib
import time
import pyperclip






URLDOLARGOOGLE = 'https://www.google.com/search?q=d%C3%B3lar&rlz=1C1SQJL_pt-BRBR811BR811&oq=D%C3%93LAR&aqs=chrome.0.69i59j35i39j0i433i512l6j0i131i433i512j0i512.2545j0j7&sourceid=chrome&ie=UTF-8'

cabeçalho = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

site = requests.get(URLDOLARGOOGLE, headers=cabeçalho)

soup = BeautifulSoup(site.content, 'html.parser')

dolar = float(soup.find('span', class_= "DFlfde SwHCTb").get_text().strip().replace(',',''))/100

print(f'\nA cotação do dólar hoje és de {dolar} Dólares')

#print(soup.prettify())

URLALIBABA = 'https://portuguese.alibaba.com/product-detail/hot-selling-portable-charger-outdoor-5000mah-solar-power-bank-with-led-emergency-lights-mobile-power-supply-for-all-cell-phones-60817375464.html?spm=a2700.galleryofferlist.normal_offer.d_title.120c49f0EtrO5k'

CABEÇALHO = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

SITE = requests.get(URLALIBABA, headers=CABEÇALHO)

SOUP = BeautifulSoup(SITE.content, 'html.parser')

FORNECEDOR = float(int(SOUP.find('span', class_= "pre-inquiry-price").get_text().strip().replace(',','')[0:3])/100 - 0.20)

print(f'\nO preço do Enguia hoje és de {FORNECEDOR} Dólares')


icms_comer = 1
icms = 118/100
entrega = 0.51
lucro = 150/100
preço_de_conversão = dolar * FORNECEDOR
print(f'\nO preço convertido do Enguia para com o fornecedor és de {preço_de_conversão:.2f} Reais')

def preço_enguia_e_lucro():
  
  preço_com_imp = ((FORNECEDOR * icms) + entrega) + preço_de_conversão
  print(f'\nO preço de custo do produto (já incluindo o ICMS, a correção monetária, entrega e apenas faltando o preço de custo do frete do fornecedor) és de {preço_com_imp:,.2f} Reais')
  preço_de_venda = float(preço_com_imp * lucro)
  print(f'\nO preço de venda do produto és de {float(preço_com_imp * lucro):,.2f} Reais')
  print(f'\n{preço_de_venda - preço_com_imp:.2f} Reais de lucro por produto')
  
preço_enguia_e_lucro()


