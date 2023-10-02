# Cargar el paquete lubridate
library(lubridate)
library(dplyr)
# Leer el dataset
data <- read_xlsx("data.xlsx")

# Convertir los datos
data$`Fecha Final` <- as.Date(data$`Fecha Final`, format = "%d-%m-%Y")
data %>%
  filter(Call==1) %>%
  mutate(mes = month(`Fecha Final`)) %>%
  group_by(mes, Cod) %>%
  count() %>%
  arrange(n, desc(n))
#Diciembre es el mes con mayor cantidad de llamadas

data %>%
  mutate(dia = wday(`Fecha Final`)) %>%
  group_by(dia) %>%
  count() %>%
  arrange(n, desc(n))
# El día 4 es el día más ocupado de la semana

data %>%
  mutate(mes = month(`Fecha Final`)) %>%
  group_by(mes) %>%
  count() %>%
  arrange(n, desc(n))
#Diciembre es el mes más ocupado

#Existe una concentración de llamadas más altas en Diciembre

data %>%
  filter(Call==1) %>%
  mutate(duracion = (`Hora Final`)-(`Hora Creación`))%>%
  summarise(proemdio_duracion=mean(duracion))
#La duración promedio de la llamada es de 873.47 segundos
data %>%
  filter(Call==1) %>%
  mutate(duracion = (`Hora Final`)-(`Hora Creación`))%>%
  mutate(duracion_llamada_minutos = case_when(
    duracion < 300 ~ "Menos de 5 minutos",
    duracion >= 300 & duracion < 600 ~ "Entre 5 y 10 minutos",
    duracion >= 600 & duracion < 900 ~ "Entre 10 y 15 minutos",
    duracion >= 900 ~ "Más de 15 minutos"
  )) %>%
  count(duracion_llamada_minutos)
