library(readxl)
library(writexl)
library(dplyr)

modificar <-  function(archives){
  data = read_excel(archives)
  data = select(data, COD_VIAJE, CLIENTE, UBICACION, CANTIDAD, PILOTO, Q, CREDITO, UNIDAD)
  mes = substr(archives, 3, 4)
  ano = substr(archives, 6, 9)
  data$Fecha = paste0(mes, "-", ano)
  return(data)
}
ruta = 'Lab1'
lista = list.files(pattern = "\\.xlsx", full.names = TRUE)
print(lista)
listadf=lapply(lista, modificar)
tabla = bind_rows(listadf)
print(tabla)
write_xlsx(tabla, "tabla.csv")