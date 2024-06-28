CREATE_DB = "CREATE DATABASE IF NOT EXISTS sharpsell"
CREATE_TABLE = "CREATE TABLE IF NOT EXISTS orders ( p_id integer, price integer, datetime timestamp default current_timestamp)"

CREATE_USER = 'CREATE USER postgres WITH option CREATEDB, PASSWORD "postgres"'
