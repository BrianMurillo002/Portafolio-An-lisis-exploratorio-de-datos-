# 🏭 Análisis de Confiabilidad y Disponibilidad de Planta

Este proyecto se enfoca en el análisis de paradas de máquina para optimizar el mantenimiento industrial. A través de un proceso de **ETL (Extracción, Transformación y Carga)**, se limpiaron datos de planta para identificar cuellos de botella y sobrecostos operativos.

## 🛠️ Desafío de Limpieza de Datos
Se gestionaron inconsistencias críticas en el dataset original:
* **Estandarización numérica:** Conversión de formatos decimales (comas a puntos) y limpieza de símbolos de moneda ($).
* **Tratamiento de Nulos:** Imputación de valores faltantes mediante la mediana para no sesgar el análisis.
* **Tipado de Datos:** Conversión de objetos de texto a flotantes para cálculos estadísticos.

## 🔍 Hallazgos Principales (Insights)
Tras el análisis de **51.50 horas totales de parada** y un gasto de **$12,000** en reparaciones, se identificó:

1. **Cuellos de Botella:** La **Extrusora_A** (21.9h) y la **Inyectora_1** (22.1h) concentran el 85% del tiempo de inactividad de la planta.
2. **Impacto Financiero:** La **Extrusora_A** no solo es la que más falla, sino la más costosa, con un **promedio de costo/hora de $350.50**, duplicando a las demás máquinas.
3. **Análisis por Turno:** El turno de la **Tarde** presenta la mayor acumulación de costos por hora, sugiriendo la necesidad de revisar los protocolos de mantenimiento en ese horario.

## 📊 Visualización
Se desarrolló un dashboard ejecutivo con los siguientes KPIs:
* **MTTR (Mean Time To Repair)** indirecto mediante la suma de horas parada.
* **Costo Total de Reparación** segmentado por activo.
* **Dispersión de Horas vs. Costo** para identificar anomalías de mantenimiento.

## 🛠️ Herramientas Utilizadas
* **Python:** Pandas, NumPy.
* **Visualización:** Looker Studio / Power BI.
