# USOM-Malicious-Links

## Zararlı Bağlantılar Engelleme ve Takip Sistemi

USOM (Ulusal Siber Olaylara Müdahale Merkezi) tarafından yayınlanan zararlı bağlantılar listesi, phishing, C2C (Command and Control) gibi birçok zararlı faaliyet için kullanılmaktadır. USOM, bu bağlantıların tespiti halinde ISP'lerden (İnternet Servis Sağlayıcıları) engellenmesi yönünde çalışma yapmaktadır. Ancak, tüm ISP'lerde bu engelleme tam olarak uygulanamamaktadır. Bu nedenle, zararlı bağlantı listesinin proxy, firewall gibi ürünlere eklenerek ve SIEM üzerinden takip edilerek güvenliğin sağlanması faydalı olacaktır.

### Sorun Tanımı

USOM'un zararlı bağlantılar listesi çok büyümüştür ve şu anda 320,109 kayıt içermektedir. Bu listeye günlük yaklaşık 1,000 yeni kayıt eklenmektedir. Bu durum, firewall ve proxy gibi güvenlik ürünlerinin tüm listeyi engellemekte yetersiz kalmasına yol açmaktadır.

### Çözüm

Hem güvenlik ürünlerini yormamak hem de güvenliği sağlamak amacıyla, son eklenen zararlı bağlantıları IP ve domain olarak ayıran ve ürünlere dinamik olarak eklenebilecek şekilde .txt dosyalarında tutan bir repo oluşturulmuştur. Bu liste, her 30 dakikada bir kendini yenileyecek şekilde ayarlanmıştır.

### Kullanımı
https://github.com/ziyadnz/USOM-Malicious-Links linkindeki domain ve ip listelerini:
* [ipv4.txt](https://raw.githubusercontent.com/ziyadnz/USOM-Malicious-Links/main/ipv4.txt?token=GHSAT0AAAAAACRHHTTTCJAAZX5O6WAJDOICZTDR2XQ)  ve [domain.txt](https://raw.githubusercontent.com/ziyadnz/USOM-Malicious-Links/main/domain.txt?token=GHSAT0AAAAAACRHHTTSVTW7BYLWKFKU3Q7CZTDR6TA) olmak üzere iki linki güvenlik ürünlerinizde dinamik liste olarak tanımlayın. Bunlara kendi ortamınızı göz önüne alarak yenilemesi için bir zamanlayıcı belirleyin. Bu listeleri SIEM üzerinde takip ederek olası açıklıkları (güvenlik ürünlerinden geçen spam maili vb) tespit etmekte kullanabilirsiniz.

### Katkıda Bulunma

Katkıda bulunmak için, lütfen bir pull request gönderin veya bir issue açın.
