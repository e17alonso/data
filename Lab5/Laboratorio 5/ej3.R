obtener_signo_zodiacal <- function(fecha_nacimiento) {
  fechas_inicio <- c(321, 421, 521, 621, 722, 823, 923, 1023, 1122, 1222, 1231)
  signos <- c("Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo",
              "Libra", "Escorpio", "Sagitario", "Capricornio", "Acuario", "Piscis")
  
  fecha_numero <- as.numeric(format(fecha_nacimiento, "%m%d"))
  
  for (i in 1:length(fechas_inicio)) {
    if (fecha_numero <= fechas_inicio[i]) {
      return(signos[i])
    }
  }
  
  return("Capricornio")
}
fecha_nacimiento <- as.Date("2002-02-17")
signo <- obtener_signo_zodiacal(fecha_nacimiento)
cat("Tu signo zodiacal es:", signo, "\n")

