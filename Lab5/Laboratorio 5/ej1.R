library(lubridate)
library(chron)
fecha_eclipse<- as.POSIXct("2017-08-21 18:26:40")
synodic_month <- days(29)+hours(12)+minutes(44)+seconds(3)
saros <- 223
tiempo <- 223*synodic_month

# Fecha del siguiente eclipse solar
fecha_eclipse_siguiente <- fecha_eclipse + tiempo

print(fecha_eclipse_siguiente)