# Poomsae Öğretici Video Oynatıcı

Poomsae Öğretici Video Oynatıcı, taekwondo poomsae'leri öğretmek için kullanılan bir video oynatıcı uygulamasıdır. Uygulama, videolar arasında gezinebilmenizi, video oynatma hızını ayarlayabilmenizi, notlar alabilmenizi ve karanlık mod ile aydınlık mod arasında geçiş yapabilmenizi sağlar.

## Özellikler

- **Video Oynatma**: Videoları sırayla oynatır ve ilerlemeyi gösterir.
- **Not Alma**: Videoları izlerken notlar alabilir ve kaydedebilirsiniz.
- **Aydınlık ve Karanlık Mod**: Temayı aydınlık veya karanlık mod olarak değiştirebilirsiniz.
- **İlerleme Çubuğu**: İlerlemenizi yüzdelik olarak gösteren bir ilerleme çubuğu.
- **Oynatma Hızı**: Videonun oynatma hızını ayarlayabilirsiniz.
- **Tam Ekran**: Videoları tam ekran modunda izleyebilirsiniz.
- **Kemer Renkleri**: Videoların zorluk seviyelerine göre kemer renkleriyle gösterimi.

## Gereksinimler

- Python 3.x
- Aşağıdaki Python kütüphaneleri:
  - `tkinter`
  - `pillow`
  - `opencv-python`

## Kurulum

1. Bu projeyi klonlayın veya indirin.
    ```sh
    git clone <repo-url>
    cd <repo-folder>
    ```

2. Gerekli Python kütüphanelerini yükleyin. Bu kütüphaneleri yüklemek için `pip` kullanabilirsiniz:
    ```sh
    pip install tkinter pillow opencv-python
    ```

3. Proje dosyalarını bu linkten indirip (https://github.com/sercanbahadiir/POOMSAE_OGRETICI_VIDEO_OYNATICI/tree/main/POOMSAE_OGRETICI_VIDEO_OYNATICI) aşağıdaki gibi düzenleyin. Gerekli dosya ve dizinlerin doğru konumda olduğundan emin olun:
    ```
    proje_dizini/
    ├── icons/
    │   ├── reset.png
    │   ├── back.png
    │   ├── play.png
    │   ├── pause.png
    │   ├── next.png
    │   └── fullscreen.png
    ├── videos/
    │   ├── part_1.mp4
    │   ├── part_2.mp4
    │   └── ...
    ├── notes.txt
    ├── main.py
    ```

4. `icons` dizininde gerekli ikon dosyalarının ve `videos` dizininde oynatılacak video dosyalarının bulunduğundan emin olun. `notes.txt` dosyası notlarınızı saklamak için kullanılacaktır.

## Kullanım

Uygulamayı çalıştırmak için aşağıdaki adımları izleyin:

1. Uygulamayı başlatmak için ana Python dosyasını çalıştırın:
    ```sh
    python main.py
    ```

2. Uygulama açıldıktan sonra videoları izlemeye başlayabilir, notlar alabilir ve temayı değiştirebilirsiniz.

### Uygulama Kullanımı

- **Video Oynatma Kontrolleri**: 
  - `⏪`: Önceki videoya geçiş yapar.
  - `⏸/▶`: Videoyu duraklatır veya oynatır.
  - `⏩`: Sonraki videoya geçiş yapar.
  - `🔄`: Videoyu baştan başlatır.
  - `⚙ Oynatma Hızı`: Videonun oynatma hızını seçmenizi sağlar.
  - `🔲`: Tam ekran moduna geçiş yapar.

- **Not Alma**: Sağ tarafta yer alan not alanına istediğiniz notları yazabilirsiniz. Uygulama kapatıldığında notlar `notes.txt` dosyasına kaydedilir.

- **Tema Değiştirme**: Sağ alt köşedeki `☀🌙` butonuna tıklayarak aydınlık ve karanlık mod arasında geçiş yapabilirsiniz.
