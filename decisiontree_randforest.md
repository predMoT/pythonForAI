# Karar Ağaçları (Decision Tree) ve Rastgele Orman (Random Forest) Algoritmaları

## 1. Karar Ağaçları (Decision Tree)

Karar ağaçları, veri kümesi üzerinde **"eğer-böyleyse"** kuralları oluşturarak sınıflandırma veya regresyon yapan gözetimli öğrenme algoritmalarıdır.

- **Yapısı:** Her düğüm (node) bir özelliği (feature) test eder, dallar karar sonuçlarına göre ayrılır ve yaprak düğümler nihai sınıfı veya regresyon değerini gösterir.

### Avantajları:
- Kolay anlaşılır ve görselleştirilebilir.
- Kategorik ve sayısal verilerle çalışabilir.
- Feature Engineering'e çok ihtiyaç duymaz.

### Dezavantajları:
- Aşırı öğrenmeye (overfitting) meyillidir.
- Küçük veri değişikliklerinden fazla etkilenebilir (kararsız yapı).
- Karmaşık veri setlerinde doğruluk oranı düşebilir.

---

## 2. Rastgele Orman (Random Forest)

Random Forest, çok sayıda karar ağacının birleşiminden oluşan bir **ensemble** (topluluk) yöntemidir. Her ağaç farklı bir veri alt kümesi ve özellik kombinasyonuyla eğitilir. Nihai sonuç, ağaçların oylamasıyla belirlenir.

### Avantajları:
- Overfitting riskini azaltır.
- Genellikle karar ağaçlarından daha yüksek doğruluk sağlar.
- Gürültülü verilere karşı daha dayanıklıdır.

### Dezavantajları:
- Yorumlaması zordur.
- Eğitimi ve tahmini daha yavaştır.
- Kaynak tüketimi yüksektir.

---

## Karşılaştırma Tablosu

| Özellik                    | Decision Tree                  | Random Forest                         |
|----------------------------|--------------------------------|---------------------------------------|
| Yorumlanabilirlik          | Yüksek                         | Düşük                                 |
| Aşırı Öğrenme              | Yüksek eğilimli                | Daha az eğilimli                      |
| Doğruluk                   | Orta                           | Genelde daha yüksek                   |
| Hesaplama Maliyeti         | Düşük                          | Orta-Yüksek                           |
| Dayanıklılık               | Düşük (gürültüye duyarlı)      | Yüksek (ensemble avantajı)            |

---

## Örnek Python Kodları

```python
# Decision Tree Örneği
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
