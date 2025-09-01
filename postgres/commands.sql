CREATE SCHEMA dev;
CREATE SCHEMA prod;

CREATE EXTENSION postgis;

CREATE USER nifi WITH PASSWORD 'passwordpasswordpassword';
CREATE USER weather_app WITH PASSWORD 'passwordpasswordpassword';

CREATE TABLE dev.zones
(id VARCHAR(255) PRIMARY KEY,
name VARCHAR(255),
state VARCHAR(2),
type VARCHAR(255));

CREATE TABLE dev.geometries (
id VARCHAR(255) REFERENCES dev.zones (id),
geom GEOMETRY
);

CREATE TABLE dev.forecasts
(id VARCHAR(255) REFERENCES dev.zones (id),
period INT,
name TEXT,
forecast TEXT,
updated TIMESTAMP,
CONSTRAINT unique_forecasts UNIQUE (id, period)
);

CREATE INDEX geometries_idx ON dev.geometries USING GIST (geom);

GRANT CONNECT ON DATABASE weather TO nifi;
GRANT ALL PRIVILEGES ON DATABASE weather TO nifi;
GRANT USAGE ON SCHEMA dev TO nifi;
GRANT ALL PRIVILEGES ON SCHEMA dev TO nifi;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA dev TO nifi;
GRANT CONNECT ON DATABASE weather TO weather_app;
GRANT USAGE ON SCHEMA dev TO weather_app;
GRANT SELECT ON ALL TABLES IN SCHEMA dev TO weather_app;
