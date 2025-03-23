# Görev Yönetimi Botu

Bot görev ekleme, silme, tamamlama ve tüm görevleri gösterme özelliklerini içerir.

## Yönetimsel Özellikler

Görev sadece yönetici tarafından (.env dosyası içinde id'si olan) izin verilen
kullanıcılar tarafından tanımlanabilir. Görevler sadece tanımlayan kişiler tarafından
tamamlanmış olarak işaretlenebilir. Kullanıcıların isim değişikliği yapma ihtimallerine karşı tüm bu özellikler kullanıcı kimlik numaraları (id) ile denetlenir.

## Bağımlılıklar
-discord.py
-dotenv (ortam değişkenlerini .env dosyası içinden yönetmek için)

## Test Etme Şekli
Testler teker teker çalıştırılmalı. Toplu olarak paralel biçimde çalıştıkları için çakışmaya sebebiyet veriyorlar. Dört görev için ana dizinde terminale aşağıdaki komutlar yazılarak çalıştırılabilir.

'''
python -m unittest tests/test_add_task.py
'''

'''
python -m unittest tests/test_delete_task.py
'''

'''
python -m unittest tests/test_complete_task.py
'''

''sh
python -m unittest tests/test_show_task.py
''
