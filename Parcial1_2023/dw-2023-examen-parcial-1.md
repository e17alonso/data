dw-2023-parcial-1
================
Tepi
9/11/2023

# Examen parcial

Indicaciones generales:

- Usted tiene el período de la clase para resolver el examen parcial.

- La entrega del parcial, al igual que las tareas, es por medio de su
  cuenta de github, pegando el link en el portal de MiU.

- Pueden hacer uso del material del curso e internet (stackoverflow,
  etc.). Sin embargo, si encontramos algún indicio de copia, se anulará
  el exámen para los estudiantes involucrados. Por lo tanto, aconsejamos
  no compartir las agregaciones que generen.

## Sección 0: Preguntas de temas vistos en clase (20pts)

- Responda las siguientes preguntas de temas que fueron tocados en
  clase.

1.  ¿Qué es una ufunc y por qué debemos de utilizarlas cuando
    programamos trabajando datos? R= Es una función vectorial que se
    aplica a cada elemento de un vector y se recomienda utilizarlas
    porque son mas eficientes.

2.  Es una técnica en programación numérica que amplía los objetos que
    son de menor dimensión para que sean compatibles con los de mayor
    dimensión. Describa cuál es la técnica y de un breve ejemplo en R.
    R= Broadcasting. Por ejemplo, si tenemos dos objetos de diferente
    dimension y los queremos sumar se puede hacer mediante el operador
    +, esto hace que la dimension del objeto menor se amplie para ser
    compatible con el objeto de mayor dimension.

3.  ¿Qué es el axioma de elegibilidad y por qué es útil al momento de
    hacer análisis de datos? R= Consiste en que un conjunto de datos
    debe ser representativo de la población de la cual se desea
    estudiar. Lo que significaaque las características de los datos
    deben ser similares a las características de la población. Esto es
    muy útil ya que garantiza que los datos sean válidos

4.  Cuál es la relación entre la granularidad y la agregación de datos?
    Mencione un breve ejemplo. Luego, exploque cuál es la granularidad o
    agregación requerida para poder generar un reporte como el
    siguiente:

| Pais | Usuarios |
|------|----------|
| US   | 1,934    |
| UK   | 2,133    |
| DE   | 1,234    |
| FR   | 4,332    |
| ROW  | 943      |

## Sección I: Preguntas teóricas. (50pts)

- Existen 10 preguntas directas en este Rmarkdown, de las cuales usted
  deberá responder 5. Las 5 a responder estarán determinadas por un
  muestreo aleatorio basado en su número de carné.

- Ingrese su número de carné en `set.seed()` y corra el chunk de R para
  determinar cuáles preguntas debe responder.

``` r
set.seed("20210421") 
v<- 1:10
preguntas <-sort(sample(v, size = 5, replace = FALSE ))

paste0("Mis preguntas a resolver son: ",paste0(preguntas,collapse = ", "))
```

    ## [1] "Mis preguntas a resolver son: 1, 3, 6, 9, 10"

### Listado de preguntas teóricas

1.  Para las siguientes sentencias de `base R`, liste su contraparte de
    `dplyr`:

    - `str()` - glimpse()
    - `df[,c("a","b")]` - select()
    - `names(df)[4] <- "new_name"` donde la posición 4 corresponde a la
      variable `old_name` - rename()
    - `df[df$variable == "valor",]` - filter()

2.  Al momento de filtrar en SQL, ¿cuál keyword cumple las mismas
    funciones que el keyword `OR` para filtrar uno o más elementos una
    misma columna?

3.  ¿Por qué en R utilizamos funciones de la familia apply
    (lapply,vapply) en lugar de utilizar ciclos? R= Para aplicar una
    misma función a todos los elementos dentro de una lista. Se utiliza
    en vez de los ciclos ya que son menos eficientes, además que lapply
    tiene más flexibilidad en cuanto a las funciones que se pueden
    aplicar.

4.  ¿Cuál es la diferencia entre utilizar `==` y `=` en R?

5.  ¿Cuál es la forma correcta de cargar un archivo de texto donde el
    delimitador es `:`?

6.  ¿Qué es un vector y en qué se diferencia en una lista en R? R= Los
    elementos del vector deben ser de un mismo tipo, mientras que los
    elementos de una lista en R pueden ser de diferente tipo

7.  ¿Qué pasa si quiero agregar una nueva categoría a un factor que no
    se encuentra en los niveles existentes?

8.  Si en un dataframe, a una variable de tipo `factor` le agrego un
    nuevo elemento que *no se encuentra en los niveles existentes*,
    ¿cuál sería el resultado esperado y por qué?

    - El nuevo elemento
    - `NA`

9.  En SQL, ¿para qué utilizamos el keyword `HAVING`? R= HAVING se
    utiliza en sql para filtrar acorde a ciertas condiciones, pero a
    diferencia de WHERE, esta aplica grupos en su totalidad.

10. Si quiero obtener como resultado las filas de la tabla A que no se
    encuentran en la tabla B, ¿cómo debería de completar la siguiente
    sentencia de SQL?

    - SELECT \* FROM A \_\_\_\_\_\_\_ B ON A.KEY = B.KEY WHERE
      \_\_\_\_\_\_\_\_\_\_ = \_\_\_\_\_\_\_\_\_\_

r= \* SELECT \* FROM A LEFT JOIN B ON A.KEY = B.KEY WHERE B.KEY IS NULL

Extra: ¿Cuántos posibles exámenes de 5 preguntas se pueden realizar
utilizando como banco las diez acá presentadas? (responder con código de
R.)

## Sección II Preguntas prácticas. (30pts)

- Conteste las siguientes preguntas utilizando sus conocimientos de R.
  Adjunte el código que utilizó para llegar a sus conclusiones en un
  chunk del markdown.

A. De los clientes que están en más de un país,¿cuál cree que es el más
rentable y por qué?

B. Estrategia de negocio ha decidido que ya no operará en aquellos
territorios cuyas pérdidas sean “considerables”. Bajo su criterio,
¿cuáles son estos territorios y por qué ya no debemos operar ahí?

### I. Preguntas teóricas

## A

``` r
###resuelva acá

library(dplyr)
```

    ## 
    ## Attaching package: 'dplyr'

    ## The following objects are masked from 'package:stats':
    ## 
    ##     filter, lag

    ## The following objects are masked from 'package:base':
    ## 
    ##     intersect, setdiff, setequal, union

``` r
parcial_anonimo <- readRDS("C:/Users/Alonso/Downloads/Parcial1_2023/parcial_anonimo.rds")
parcial_anonimo %>%
  select(Cliente, Venta, Pais) %>%
  group_by(Cliente) %>%
  summarise(n=n_distinct(Pais), Ventas=sum(Venta)) %>%
  filter(n>1) %>%
  arrange(desc(Ventas))
```

    ## # A tibble: 7 × 3
    ##   Cliente      n Ventas
    ##   <chr>    <int>  <dbl>
    ## 1 a17a7558     2 19818.
    ## 2 ff122c3f     2 15359.
    ## 3 c53868a0     2 13813.
    ## 4 044118d4     2  9436.
    ## 5 f676043b     2  3635.
    ## 6 f2aab44e     2   400.
    ## 7 bf1e94e9     2     0

``` r
#El cliente que es más rentable que se encuentre en diferentes paaíses es a17a7558 porque es el que mayor ingresos genera a través de las ventas
```

## B

``` r
###resuelva acá
library(dplyr)
```

    ## 
    ## Attaching package: 'dplyr'

    ## The following objects are masked from 'package:stats':
    ## 
    ##     filter, lag

    ## The following objects are masked from 'package:base':
    ## 
    ##     intersect, setdiff, setequal, union

``` r
parcial_anonimo %>%
  filter(Venta<0) %>%
  group_by(Territorio) %>%
  summarise(n=sum(Venta)) %>%
  arrange((n))
```

    ## # A tibble: 79 × 2
    ##    Territorio       n
    ##    <chr>        <dbl>
    ##  1 f7dfc635   -14985.
    ##  2 77192d63    -5641.
    ##  3 72520ba2    -3761.
    ##  4 69c1b705    -3370.
    ##  5 1d407777    -3300.
    ##  6 bc8e06ed    -3269.
    ##  7 2e812869    -3056.
    ##  8 67e9cc18    -2721.
    ##  9 8f79b7f8    -1858.
    ## 10 a0d39798    -1779.
    ## # ℹ 69 more rows

``` r
#Debemos deshacernos de los territorios con perdidas 
```
