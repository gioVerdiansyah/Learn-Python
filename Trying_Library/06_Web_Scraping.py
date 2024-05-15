# Web Scraping
# Library web scraping adalah jenis library untuk membantu pengguna mengumpulkan data dari halaman web. Proses ini disebut sebagai “web scraping” atau “web crawling”.

from urllib.request import urlopen
import bs4

# Mengambil konten halaman
url = "https://python.org/"
page = urlopen(url)
html = page.read().decode('utf-8')

# Object BeautifulSoup
soup = bs4.BeautifulSoup(html, "html.parser")

# Mencetak title halaman
print(soup.title)

si = html.find("<title>") + len("<title>")
ei = html.find("</title>")

print(html[si:ei])