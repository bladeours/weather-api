# weather-api

## dokumentacja kodu

### pakiet controller

zawiera klasę Controller która odpowiada za wystawienie endpointów

### pakiet flask

zawiera flask config

### pakiet models

zawiera model Weather

### pakiet service

zawiera klasę Service która odpowiada za wysyłanie zapytań do OpenWeatherMap oraz open-meteo. Używam dwóch ponieważ OpenWeatherMap nie ma darmowych danych historycznych. Klasa zawiera również metodę do zapisywania danych do pliku w formacie CSV.

## dokumentacja użytkownika

wystarczy uruchomić aplikacje poprzez `python3 run.py`, aplikacja domyślnie odpala się na porcie 8080.

## endpointy

### /current

zwraca pogodę w tym momencie w danym mieście.

parametry:

- city - miasto, w którym chcemy poznać pogodę

`curl http://localhost:8080/current?city=<city_name>`

przykładowa odpowiedź:

```json
{
   "city":"Berlin",
   "cloudiness":0,
   "date":"29-06-2023",
   "feels_like":22.09,
   "humidity":69,
   "temperature":22.03,
   "wind_speed":2.24
}
```

### /historical

zwraca pogodę w danym mieście w konkretnym dniu z przeszłości.

parametry:

- city - miasto, w którym chcemy poznać pogodę
- date - data w formacie `yyyy-mm-dd` z której chcemy poznać pogodę

`curl http://localhost:8080/historical?city=<city_name>&date=<yyyy-mm-dd>`

przykładowa odpowiedź:

```json
{
   "city":"Berlin",
   "cloudiness":0,
   "date":"29-06-2023",
   "feels_like":22.09,
   "humidity":69,
   "temperature":22.03,
   "wind_speed":2.24
}
```

### /chart/rain

zwraca nam wykres opadów z okresu który podamy

parametry:

- city - miasto, w którym chcemy poznać pogodę
- start_date - data startowa w formacie `yyyy-mm-dd`
- end_date - data końcowa w formacie `yyyy-mm-dd`

`curl http://localhost:8080/chart/rain?city=<city_name>&start_date=yyyy-mm-dd>&end_date=<yyyy-mm-dd>`

przykładowa odpowiedź:

![rain](rain.png)

### /chart/temp

zwraca nam wykres temperatury z okresu który podamy

parametry:

- city - miasto, w którym chcemy poznać pogodę
- start_date - data startowa w formacie `yyyy-mm-dd`
- end_date - data końcowa w formacie `yyyy-mm-dd`

`curl http://localhost:8080/chart/temp?city=<city_name>&start_date=yyyy-mm-dd>&end_date=<yyyy-mm-dd>`

przykładowa odpowiedź:

![temp](temp.png)