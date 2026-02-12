# 🛒 Análisis de Ventas E-Commerce  
**BigQuery (SQL) + Looker Studio**

## 📌 Descripción del Proyecto

Este proyecto simula el análisis comercial de una empresa de e-commerce durante el primer semestre del año.  

Se desarrolló un modelo de datos en BigQuery a partir de tres tablas principales:

- `customers`
- `products`
- `orders`

Posteriormente, se creó una tabla analítica consolidada mediante JOIN para facilitar el cálculo de métricas y la construcción de un dashboard ejecutivo en Looker Studio.

---

## 🧱 Modelado de Datos

Se realizó la unión de tablas utilizando:

- `customer_id`
- `product_id`

Se construyó una tabla analítica con las siguientes variables clave:

- order_id  
- order_date  
- city  
- category  
- price  
- quantity  
- total_venta (quantity * price)

Ejemplo de métrica principal:

```sql
SUM(o.quantity * p.price) AS total_venta
