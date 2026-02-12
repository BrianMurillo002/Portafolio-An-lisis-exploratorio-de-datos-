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

## Insight Claves

La categoría Accesorios concentra la mayor participación en ingresos del semestre, lo que indica una alta demanda y potencial para estrategias de cross-selling.
Se observa un crecimiento progresivo desde febrero hasta mayo, alcanzando el pico en mayo, lo que sugiere un posible comportamiento estacional o efecto acumulativo de ventas.
El cliente 311 concentra el mayor volumen de ingresos, lo que lo convierte en un cliente de alto valor (High Value Customer).
La ciudad de Bogotá presenta los mayores ingresos en el semestre

## Estrategias sugeridas
Diseñar campañas focalizadas para categorías con menor participación, utilizando promociones o bundles con la categoría líder.
Realizar planes durante el mes de febrero para dar aumento en los ingresos de ese mes
Brindar incentivos o promociones a los clientes que alcanzan los primeros 3 puestos del top en los ingresos por compras para la empresa, esto con la finalidad de premiar a esos clientes y de incentivar a los otros clientes a comprar mas en los productos de la empresa.
