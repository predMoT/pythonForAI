# Özellik Ölçekleme (Feature Scaling)

Özellik ölçekleme, makine öğrenmesi ve veri madenciliği süreçlerinde verilerin uygun bir ölçeğe getirilmesi işlemidir. Farklı ölçeklerdeki değişkenlerin makine öğrenmesi modellerini yanıltmasını önlemek amacıyla yapılır.

---

##  Neden Özellik Ölçekleme Yapılır?

- Özellikler farklı aralıklarda olabilir (örneğin bir değişken 0-1 arasında iken diğeri 0-1000 arasında olabilir).
- Bu durum özellikle mesafeye dayalı algoritmalarda (K-NN, K-Means, SVM vb.) modellerin performansını olumsuz etkiler.
- Modelin daha doğru tahminler yapması ve daha hızlı öğrenmesi sağlanır.
- Bazı modeller (örneğin Decision Tree, Random Forest) ölçeklemeye duyarsızken bazıları (örneğin Logistic Regression, SVM) oldukça duyarlıdır.

---

##  Ölçeklemeden Etkilenen Algoritmalar

Özellik ölçekleme aşağıdaki algoritmalar için oldukça önemlidir:

- K-En Yakın Komşu (K-NN)
- Destek Vektör Makineleri (SVM)
- K-Ortalamalar Kümeleme (K-Means)
- Lojistik Regresyon
- Lineer Regresyon
- Yapay Sinir Ağları (Neural Networks)
- PCA (Principal Component Analysis)

Ölçeklemeden çok etkilenmeyen algoritmalar:

- Karar Ağaçları (Decision Trees)
- Rastgele Ormanlar (Random Forest)
- Gradient Boosting algoritmaları

---

##  Özellik Ölçekleme Yöntemleri

### 1. Min-Max Normalizasyonu

Verileri 0 ile 1 arasına (veya belirli başka bir aralığa) dönüştürür.

**Formül:**
X_scaled = (X - X_min) / (X_max - X_min)


**Python Örneği:**
```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

---

### 2. Standartlaştırma (Z-Score Normalizasyonu)

**Formül:**
X_scaled = (X - μ) / σ

**Python Örneği:**
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

---

### 3. MaxAbs Scaling
Verileri -1 ile 1 arasında ölçeklendirir. Özellikle sparse (seyrek) matrisler için uygundur çünkü 0 değerlerini değiştirmez.

**Python Örneği:**
from sklearn.preprocessing import MaxAbsScaler

scaler = MaxAbsScaler()
X_scaled = scaler.fit_transform(X)

---

### 4. Robust Scaler
Aykırı değerlere karşı dayanıklıdır. Medyan ve çeyrekler arası aralığı (IQR) kullanır.

**Python Örneği:**
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)

---

### Hangi Durumda Hangi Ölçekleme Yöntemi Kullanılır?
| Ölçekleme Yöntemi | Uygun Olduğu Durumlar                          |
| ----------------- | ---------------------------------------------- |
| MinMaxScaler      | Özellikler belirli bir aralıktaysa             |
| StandardScaler    | Veriler normal dağılıma yakınsa                |
| RobustScaler      | Aykırı değerlerin yoğun olduğu veri setlerinde |
| MaxAbsScaler      | Seyrek (sparse) veri yapısında                 |

---

### Sonuç
Özellik ölçekleme, makine öğrenmesi projelerinde genellikle göz ardı edilen ancak model performansı üzerinde büyük etkisi olan bir adımdır. Doğru ölçekleme yöntemi seçilerek modelin hem doğruluğu hem de eğitim süresi iyileştirilebilir. Her zaman veri setinin yapısına göre en uygun yöntemi belirleyerek ilerleyin.
