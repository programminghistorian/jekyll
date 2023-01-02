# Los paquetes que utilizaremos

library(rvest)
library(stringr)
library(readr)

# Creamos una carpeta para guardar los discurso
dir.create("discursos")

# Extracción discurso Gabriel Boric ----

## 1. Guardar el código html en un objeto
html_boric <- read_html("https://prensa.presidencia.cl/discurso.aspx?id=188237")

## 2. Extraer el texto de la sección de la página que nos interesa y editar su formato
discurso_boric <- html_boric |> 
  html_element("#main_ltContenido") |> 
  html_text2() |> 
  str_replace_all("\n\n", "\n") 

## 3. Guardar el archivo dentro de la carpeta "discursos"
write_lines(discurso_boric, "discursos/cl_2022_boric_asuncion-cargo.txt")


# Extracción discurso Sebastián Piñera ----

## 1. Guardar el código html en un objeto
url_pinera <- "https://prensa.presidencia.cl/discurso.aspx?id=71722"

## 2. Extraer el texto de la sección de la página que nos interesa y editar su formato
discurso_pinera <- read_html(url_pinera) |> 
  html_element("#main_ltContenido") |> 
  html_text2() |> 
  str_replace_all("\n\n", "\n") 

## 3. Guardar el archivo dentro de la carpeta "discursos"

write_lines(discurso_pinera, "discursos/cl_2018_pinera_asuncion-cargo.txt")
