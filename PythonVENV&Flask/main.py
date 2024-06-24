from flask import Flask
import random

app = Flask(__name__)

facts_list = [
    "Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
    "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
    "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir."
]

resim_list = [
    "https://st2.depositphotos.com/26270350/44699/i/450/depositphotos_446997772-stock-photo-stones-gray-isolated-stacked-variety.jpg",
    "https://media.istockphoto.com/id/1313037809/tr/foto%C4%9Fraf/gri-arka-plan-%C3%BCzerinde-izole-edilmi%C5%9F-bo%C5%9F-bir-a4-boyutlu-ka%C4%9F%C4%B1t-tutan-el.jpg?s=612x612&w=0&k=20&c=Yagp32DNd181sjSZ857lI01lHlBIdfAqerLw4VB-mDs=",
    "https://www.parti365.com/makas-celiksoz-nisan-makasi-horsehead-marka-p12-4374-36-B.jpg"
]

@app.route("/")
def hello_world():
    return '''
        <h1>MERHABA! Bu sayfada, teknolojik bağımlılıklar hakkında birkaç ilginç gerçeği öğrenebilirsiniz!</h1>
        <a href="/rastgele_gercek">Rastgele bir gerçeği görüntüle!</a><br>
        <a href="/rasgele_resim">Rastgele bir resmi görüntüle!</a>
    '''

@app.route("/rastgele_gercek")
def random_facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/rasgele_resim")
def random_image():
    image_url = random.choice(resim_list)
    return f'<img src="{image_url}" alt="Rastgele Resim">'


app.run(debug=True)
