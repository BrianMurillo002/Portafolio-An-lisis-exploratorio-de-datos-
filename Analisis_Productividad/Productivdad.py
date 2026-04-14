import pandas as pd

# Datos de producción (Turno de 8 horas)
datos_productividad = {
    'Operario': ['Carlos Ruiz', 'Ana Maria', 'Juan Pablo', 'Diana Luz', 'Luis Fer'],
    'Piezas_Producidas': [380, 450, 320, 410, 280],
    'Horas_Trabajadas': [8, 8, 8, 8, 8]
}

df_prod = pd.DataFrame(datos_productividad)

Operario	    Piezas_Producidas	Horas_Trabajadas
0	Carlos Ruiz	        380	            8
1	Ana Maria	          450	            8
2	Juan Pablo	        320	            8
3	Diana Luz	          410	            8
4	Luis Fer	          280	            8

df_prod['Productividad'] = df_prod['Piezas_Producidas'] / df_prod['Horas_Trabajadas']
df_prod

	Operario	    Piezas_Producidas	Horas_Trabajadas	Productividad
0	Carlos Ruiz	        380	              8	              47.50
1	Ana Maria	          450	              8	              56.25
2	Juan Pablo	        320	              8	              40.00
3	Diana Luz	          410	              8	              51.25
4	Luis Fer	          280      	        8	              35.00

df_prod['Cumplimiento'] = df_prod.apply(lambda x: 'Cumple' if x['Productividad'] > 50 else 'No cumple' , axis=1)
df_prod

	Operario	    Piezas_Producidas	Horas_Trabajadas	Productividad	Cumplimiento
0	Carlos Ruiz	        380	             8	              47.50	     No cumple
1	Ana Maria	          450	             8	              56.25	        Cumple
2	Juan Pablo	        320	             8	              40.00	     No cumple
3	Diana Luz	          410	             8	              51.25	        Cumple
4	Luis Fer	          280	             8	              35.00	     No cumple

Costo_por_hora = 15000
df_prod['Costo_por_Pieza'] = Costo_por_hora / df_prod['Productividad']
df_prod['Costo_por_Pieza'] = df_prod['Costo_por_Pieza'].round(2)
df_prod

Operario	      Piezas_Producidas	Horas_Trabajadas	Productividad	Costo_por_Pieza
0	Carlos Ruiz	        380	             8	              47.50	        315.79
1	Ana Maria	          450	             8	              56.25	        266.67
2	Juan Pablo	        320	             8	              40.00	        375.00
3	Diana Luz	          410	             8	              51.25	        292.68
4	Luis Fer	          280	             8	              35.00	        428.57

