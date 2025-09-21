# Weather Map Application

This repository contains code for building a simple weather forecast map for the mid-Atlantic region of the United States. This project involves an Extract, Transform, and Load (ETL) process with Apache NiFi, PostgreSQL/PostGIS, and the National Weather Service (NWS) API. The maps and forecasts are displayed using Streamlit with Folium, FastAPI, and Nginx. All these tools and processes are containerized with Docker.

## Technologies Used
- Docker
- Apache NiFi
- PostgreSQL/PostGIS
- Streamlit with Folium
- Python
- FastAPI
- Nginx

## Getting Started
### Prerequisites
- Docker

### Installation
1. Clone this repository to your local machine.
```sh
git clone
```

2. Navigate to the project directory.
```sh
cd weather-app
```

3. Start the Docker containers.
```
docker compose up -d
```

4. Enter into the PostGIS container.
```
docker exec -it postgis_container_prod bash
```

5. Run the following commands in psql. Changes the passwords in the commands.sql as necessary.
```
psql -U admin -c "CREATE DATABASE weather;"
```
```
psql -U admin -d weather
```
```
\i commands.sql
```

6. Login into Apache NiFi and import the NiFi flow that is stored in the nifi folder.

7. Change the parameters in the weatherFlow parameter context as necessary - especially if you changed the passwords in the  commands.sql file. Start all processors. 

8. View the map at http://localhost:8080.

### Configuration
1. The NWS API does not require an API key, but does require an email address in the header. Change the email parameter in the weatherFlow paramter context.

2. Set up your credentials in .env and commands.sql.
```
URL_DATABASE=postgresql://weather_app:passwordpasswordpassword@postgis_container_prod:5432/weather
POSTGRES_USER=admin
POSTGRES_PASSWORD=passwordpassword
SINGLE_USER_CREDENTIALS_USERNAME=admin
SINGLE_USER_CREDENTIALS_PASSWORD=passwordpasswordpassword
API_KEY=mysecretkey
```

## Output
<img width="752" height="525" alt="output" src="https://github.com/theapphiker/weather-app/blob/main/output.png/">
