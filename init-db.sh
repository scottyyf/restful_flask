#!/usr/bin/bash

init_db(){
    flask db init
    flask db migrate -m "init_db"
    flask db upgrade
}

init_db