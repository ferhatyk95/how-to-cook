## Yemek Tarifleri Uygulaması

Bu basit Python programı, kullanıcıya çeşitli yemek tariflerini gösteren bir uygulamadır. Kullanıcı, program aracılığıyla belirli bir yemeğin tarifini görebilir.

### Kullanım

1. `tarif_goster(yemek)` fonksiyonu, belirli bir yemeğin tarifini gösterir. Kullanıcı, bu fonksiyona yemek adını parametre olarak vererek istediği yemeğin tarifine erişebilir.

2. Yemekler ve malzemeleri `yemekler` adlı bir sözlük içinde tanımlanmıştır. Her yemeğin malzemeleri bu sözlükte listelenmiştir.

### Örnek Kullanım

```python
onerilen_yemek = "pizza"
tarif_goster(onerilen_yemek)
Yukarıdaki örnekte, kullanıcıya "pizza" yemeğinin tarifi gösterilmektedir. tarif_goster fonksiyonu, belirtilen yemeğin malzemelerini ve adım adım yapılışını ekrana yazdırır.

Notlar
Bu program, sadece belirli yemekler için tanımlı olan tarifleri destekler. Eğer yeni yemekler eklenmek istenirse, yemekler sözlüğü güncellenmelidir.
Geliştirme
Programın geliştirilmesi için ek yemek tarifleri eklenebilir veya mevcut tariflerde değişiklik yapılabilir.
Kullanıcı arayüzü geliştirilerek, kullanıcıya menü seçenekleri sunulabilir.
Hata yönetimi geliştirilerek, kullanıcıya daha açıklayıcı hata mesajları gösterilebilir
