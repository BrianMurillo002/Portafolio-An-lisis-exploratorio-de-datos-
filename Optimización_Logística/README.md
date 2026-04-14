# 🚚 Optimización Logística y Análisis de Cumplimiento (SLA)

## 📌 Contexto del Proyecto
En este caso de estudio, analicé la eficiencia operativa de una red de distribución regional (Cali, Yumbo y Jamundí). El enfoque principal fue medir el impacto financiero de los retrasos en las entregas mediante el cálculo automático de penalizaciones por incumplimiento de tiempos estimados (SLA).

## 🛠️ Herramientas Utilizadas
* **Lenguaje:** Python (Pandas).
* **Lógica Aplicada:** Funciones condicionales para el cálculo de multas escalonadas (20% y 50% del flete).
* **Visualización:** Power BI con integración de mapas georreferenciados.

## 📊 Hallazgos Críticos (KPIs)
A través del análisis de datos se identificaron los siguientes puntos:

* **Ingreso Neto Total:** $184.000 generados en la jornada.
* **Acumulado de Retrasos:** 115 minutos de desviación total en la operación.
* **Ruta de Mayor Impacto:** **Yumbo-Industrial** es la más rentable ($40.000 neto), pero presenta el mayor retraso acumulado (50 min adicionales), lo que pone en riesgo la fidelización del cliente industrial.
* **Eficiencia Geográfica:** Las rutas hacia el sur (Cali-Sur y Jamundí) presentan el mejor cumplimiento de tiempos, manteniendo el 100% de los ingresos sin penalizaciones.

## 🚀 Propuestas de Mejora
1. **Reestructuración de Rutas Críticas:** Evaluar horarios de salida escalonados para las rutas de Yumbo y Cali-Oeste para mitigar el impacto del tráfico.
2. **Ajuste de Promesa de Entrega:** Sincronizar los tiempos estimados con la realidad operativa para evitar el pago de multas innecesarias.

## 🖼️ Dashboard Logístico
![Dashboard Logístico y Mapas](image_8bd5f5.png)
