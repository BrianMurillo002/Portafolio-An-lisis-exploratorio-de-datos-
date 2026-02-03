# 💳 Análisis de churn e ingresos por suscripciones

## 🎯 Objetivo
Analizar el comportamiento de los usuarios según el tipo de plan contratado,
identificando la tasa de cancelación (churn), los ingresos generados y la
distribución de clientes por ciudad.

## 📊 Datos
Se utilizaron datos simulados de 200 clientes, generados directamente en R,
incluyendo información sobre:
- Ciudad
- Tipo de plan
- Fecha de registro
- Estado del cliente (activo / cancelado)
- Ingresos mensuales

## 🔍 Metodología
- Generación de datos con `tibble()`
- Limpieza y transformación de variables
- Cálculo de métricas de negocio (churn, ingresos)
- Análisis descriptivo y visualización con ggplot2

## 📈 Hallazgos clave
- La tasa de cancelación es cercana al 30%.
- El plan Estándar genera mayores ingresos totales.
- Bogotá concentra la mayor cantidad de usuarios y cancelaciones.
- Los ingresos muestran variaciones mensuales relevantes.

## ✅ Conclusión
Los resultados sugieren oportunidades de mejora en estrategias de retención,
especialmente en ciudades con mayor concentración de clientes, así como el
fortalecimiento de planes con mejor rendimiento económico.

## 📄 Archivos del análisis

- 📘 [Ver análisis en R Markdown](analisis_suscripciones.Rmd)
- 🌐 [Ver reporte en HTML](analisis_suscripciones.html)

