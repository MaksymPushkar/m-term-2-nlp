# Dataset Card — ProZorro Tender Text Classification

## Назва проєкту
Класифікація текстів публічних закупівель ProZorro за тематикою.

## Задача
Тип задачі: A — Text Classification.

Вхід:
текст тендера (title + description + items).

Вихід:
один з класів:
- construction
- medicine
- it
- other

## Джерело даних
Офіційний Public API системи OpenProcurement (ProZorro):
https://public.api.openprocurement.org/api/2.5/tenders

Документація:
https://prozorro-api-docs.readthedocs.io/

## Обсяг
800 документів (тендерів).
4 класи.

## Мова / домен
Мова: переважно українська (частково mixed UA/EN).
Домен: державні закупівлі, технічні та юридичні тексти.

## Очищення даних
- об’єднання кількох полів тендера в один текст
- нормалізація пробілів
- уніфікація апострофів
- маскування:
  - <URL>
  - <EMAIL>
  - <PHONE>
  - <DATE>
  - <MONEY>
  - <NUM>

## Ризики даних
- можливий дисбаланс класів
- шум у вигляді технічних специфікацій
- дублікати однакових закупівель
- змішана мова (UA + EN терміни)
- слабка rule-based розмітка

## План для Lab 2
- ручна перевірка частини розмітки
- балансування класів
- розширення правил нормалізації
- побудова baseline моделі (TF-IDF + Logistic Regression)
