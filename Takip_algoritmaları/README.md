# Video Takip Algoritmaları

Bu proje, çeşitli OpenCV takip algoritmalarını kullanarak video akışındaki nesneleri takip etmenizi sağlar. Kullanıcı, farklı takip algoritmalarından birini seçerek ilgi alanı (ROI) belirleyebilir ve seçilen algoritma ile takip işlemini gerçekleştirebilir.

## Özellikler

- **Çoklu Algoritma Seçeneği**: CSRT, KCF, MIL, MedianFlow, MOSSE ve Boosting gibi farklı takip algoritmaları desteklenmektedir.
- **Kullanıcı Dostu Arayüz**: Kullanıcıdan izlenecek alanı seçmesini isteyen ve seçilen alanı ekranda gösteren basit ve etkileşimli bir arayüz.
- **Gerçek Zamanlı Takip**: Seçilen nesne, video boyunca gerçek zamanlı olarak takip edilir.

## Kurulum

Projeyi kullanmak için aşağıdaki adımları izleyin:

1. Bu depoyu yerel makinenize klonlayın:
    ```bash
    git clone https://github.com/ahmetduman23/OpenCV_algorithms.git
    ```
2. Gerekli Python kütüphanelerini yükleyin:
    ```bash
    pip install -r requirements.txt
    ```
    `requirements.txt` dosyasında sadece OpenCV gereksinimi olacağı için şu içeriği ekleyin:
    ```
    opencv-python
    opencv-contrib-python
    ```

## Kullanım

1. Projeyi çalıştırmak için terminal üzerinden aşağıdaki komutu kullanın:
    ```bash
    python algoritmalar.py
    ```
2. Kullanmak istediğiniz takip algoritmasının adını girin: `csrt`, `kcf`, `mil`, `medianflow`, `mosse` veya `boosting`.
3. Takip edilecek nesneyi seçmek için ekrandaki kareyi kullanın.
4. Takip işlemi başlar ve nesnenin hareketi ekranda gösterilir.
5. Takibi sonlandırmak için `q` tuşuna basın.

## Desteklenen Takip Algoritmaları

- **CSRT**: Discriminative Correlation Filter Tracker with Channel and Spatial Reliability
- **KCF**: Kernelized Correlation Filters
- **MIL**: Multiple Instance Learning Tracker
- **MedianFlow**: Robust tracker based on median flow
- **MOSSE**: Minimum Output Sum of Squared Error
- **Boosting**: Ensemble of Weak Classifiers (similar to AdaBoost)

## Gereksinimler

- Python 3.x
- OpenCV (opencv-python ve opencv-contrib-python paketleri)

## Katkıda Bulunma

Katkılarınızı bekleriz! Herhangi bir öneri, hata bildirimi veya yeni özellik eklemek için lütfen bir [issue](https://github.com/ahmetduman23/OpenCV_algorithms/issues) oluşturun veya bir pull request gönderin.
