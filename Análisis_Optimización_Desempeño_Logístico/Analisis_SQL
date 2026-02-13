## Análisis de Datos en SQL
--- 

📌 Objetivo
Realizar la limpieza, transformación y análisis de los datos logísticos para calcular métricas clave de desempeño operativo e impacto financiero.

1. Cálculo de KPIs principales

Total de envíos

SELECT COUNT(*) AS total_envios
FROM shipments;
📉 % de retrasos
SELECT
  COUNTIF(delivery_status = 'Late') / COUNT(*) AS porcentaje_retrasos
FROM shipments;


📊 Desempeño por ciudad

SELECT
  c.city,
  COUNT(*) AS total_envios,
  COUNTIF(s.delivery_status = 'Late') AS retrasos,
  COUNTIF(s.delivery_status = 'Late') / COUNT(*) AS porcentaje_retrasos
FROM shipments s
JOIN customers c
ON s.customer_id = c.customer_id
GROUP BY c.city
ORDER BY porcentaje_retrasos DESC;


🚚 Desempeño por conductor

SELECT
  d.driver_name,
  COUNT(*) AS total_envios,
  COUNTIF(delivery_status = 'On Time') / COUNT(*) AS porcentaje_cumplimiento
FROM shipments s
JOIN drivers d
ON s.driver_id = d.driver_id
GROUP BY d.driver_name
ORDER BY porcentaje_cumplimiento ASC;


💰 Impacto financiero de retrasos
SELECT
  delivery_status,
  SUM(shipment_value) AS ingresos_totales
FROM shipments
GROUP BY delivery_status;


🔎 Análisis temporal
SELECT
  DATE_TRUNC(shipment_date, MONTH) AS mes,
  COUNT(*) AS total_envios,
  COUNTIF(delivery_status = 'Late') / COUNT(*) AS porcentaje_retrasos
FROM shipments
GROUP BY mes
ORDER BY mes;
