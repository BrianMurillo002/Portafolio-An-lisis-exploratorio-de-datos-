# 🚲 Análisis del comportamiento de usuarios – Bicicletas compartidas

## 🎯 Objetivo
Analizar el comportamiento de uso entre usuarios ocasionales y miembros
anuales de un sistema de bicicletas compartidas, con el fin de identificar
oportunidades que ayuden a mejorar la conversión hacia planes de membresía.

## 📊 Datos
Se utilizaron 12 archivos correspondientes a un año completo de viajes (2025),
los cuales fueron consolidados en un único dataset.  
Durante la preparación de los datos se eliminaron:
- Valores nulos
- Duraciones negativas
- Viajes con duración superior a 24 horas (registros anómalos)

## 🔍 Metodología
- Limpieza y validación de datos en R
- Creación de variables temporales (día y mes)
- Análisis exploratorio de datos
- Visualización con ggplot2

## 📈 Hallazgos clave
- Los usuarios ocasionales presentan viajes de mayor duración promedio.
- El uso recreativo se concentra en fines de semana y meses de verano.
- Los miembros anuales muestran patrones más regulares y funcionales.

## ✅ Conclusión
La baja conversión de usuarios ocasionales no responde a falta de interés,
sino a un desajuste entre el modelo de membresía y su comportamiento de uso.
Se recomienda implementar planes flexibles de corta duración y promociones
estacionales para mejorar la conversión.

## 📄 Archivos del análisis

- 📘 [Ver reporte en Rmd](bicicletas_compartidas(caso estudio1).Rmd)
- 🌐 [Ver reporte en HTML](Bicicletas_compartidas.html)

