library(nycflights13)
library(dplyr)

flights = flights %>%
  select(dep_time, arr_time, sched_dep_time, sched_arr_time)

# Convertir las variables de hora a formato fecha y hora
flights <- flights %>% 
  mutate(
  dep_time_dt = as.POSIXct(dep_time, format = "%H%M"),
  arr_time_dt = as.POSIXct(arr_time, format = "%H%M"),
  sched_dep_time_dt = as.POSIXct(sched_dep_time, format = "%H%M"),
  sched_arr_time_dt = as.POSIXct(sched_arr_time, format = "%H%M")
)

# Calcular el delay de la salida y la llegada
flights <- flights %>% 
  mutate(
  dep_delay = dep_time_dt - sched_dep_time_dt,
  arr_delay = arr_time_dt - sched_arr_time_dt
)

#Calcular delay total
flights <- flights %>% 
  mutate(
  delay_total = dep_delay + arr_delay
)

head(flights)

