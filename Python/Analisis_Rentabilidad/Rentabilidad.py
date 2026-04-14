import pandas as pd

# Datos de productos y costos
datos_rentabilidad = {
    'Producto': ['Seguro de Vida', 'Tarjeta Joven', 'Crédito Micro', 'Seguro Vehicular', 'Cuenta Ahorro'],
    'Precio_Venta': [120000, 45000, 350000, 280000, 15000],
    'Costo_Variable': [45000, 38000, 210000, 245000, 2000]
}

df_margen = pd.DataFrame(datos_rentabilidad)
df_margen['Margen_Contribucion_Unitario'] = df_margen['Precio_Venta'] - df_margen['Costo_Variable']
df_margen

df_margen['%_Margen'] = (df_margen['Margen_Contribucion_Unitario'] / df_margen['Precio_Venta'] * 100)
df_margen['%_Margen'] = df_margen['%_Margen'].round(2)
df_margen

Producto	        Precio_Venta	Costo_Variable	Margen_Contribucion_Unitario	%_Margen
0	Seguro de Vida	  120000	        45000	               75000	              62.50
1	Tarjeta Joven	     45000	        38000	                7000	              15.56
2	Crédito Micro	    350000	       210000	              140000	              40.00
3	Seguro Vehicular  280000         245000	               35000	              12.50
4	Cuenta Ahorro	     15000	         2000	               13000	              86.67


df_Eficiencia = df_margen[df_margen['%_Margen'] > 25].copy()
df_Eficiencia

Producto	        Precio_Venta	Costo_Variable	Margen_Contribucion_Unitario	%_Margen
0	Seguro de Vida	  120000	        45000	                75000	                62.50
2	Crédito Micro	    350000	       210000	               140000	                40.00
4	Cuenta Ahorro	     15000	         2000	                13000	                86.67

# Aplicando la recomendación para la Tarjeta Joven
# Bajamos el costo variable de 38.000 a 30.000
df_margen.loc[df_margen['Producto'] == 'Tarjeta Joven', 'Costo_Variable'] = 30000

# Recalculamos
df_margen['Nuevo_Margen_Unitario'] = df_margen['Precio_Venta'] - df_margen['Costo_Variable']
df_margen['Nuevo_%_Margen'] = (df_margen['Nuevo_Margen_Unitario'] / df_margen['Pre
# Recalculamoscio_Venta']) * 100

print(df_margen[df_margen['Producto'] == 'Tarjeta Joven'])

        Producto  Precio_Venta  Costo_Variable  Margen_Contribucion_Unitario  \
1  Tarjeta Joven         45000           30000                          7000   

   %_Margen  Nuevo_Margen_Unitario  Nuevo_%_Margen  
1     15.56                  15000       33.333333  
