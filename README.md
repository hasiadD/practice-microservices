# Практика: проєкти до звіту

## Завдання 3 — веб-додаток (web/)
Відкрийте web/index.html у браузері (потрібен інтернет). Оберіть фото, зробіть скриншот.

## Завдання 4 — мікросервіси
1. Встановіть Docker Desktop.
2. У цій папці: `docker compose up --build`
3. Перевірте: http://localhost:8080/products — скриншот.
   Замовлення (PowerShell):
   Invoke-RestMethod -Method Post -Uri http://localhost:8080/orders -ContentType "application/json" -Body '{"product_id":1}'
4. Хмара (Google Cloud Run), для кожного сервісу окремо:
   gcloud run deploy product-service --source ./product-service --region europe-central2 --allow-unauthenticated
   gcloud run deploy order-service --source ./order-service --region europe-central2 --allow-unauthenticated --set-env-vars PRODUCT_URL=<URL product-service>
   gcloud run deploy gateway --source ./gateway --region europe-central2 --allow-unauthenticated --set-env-vars PRODUCT_URL=<URL product-service>,ORDER_URL=<URL order-service>
   Порт: Cloud Run сам передає змінну PORT, код її читає.

## Завдання 5 — Flutter (mobile/)
1. Встановіть Flutter SDK і Android Studio (емулятор).
2. `flutter create shop_app` ; `cd shop_app` ; `flutter pub add http`
3. Замініть shop_app/lib/main.dart файлом mobile/lib/main.dart
4. Вкажіть baseUrl (емулятор + docker compose: http://10.0.2.2:8080; хмара: URL gateway).
5. `flutter run` — скриншот.
