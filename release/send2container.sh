#!/bin/bash

CONTAINER_NAME=dockerzabbix_agentd_1

for i in $(ls ../scripts/*.py); do 
    pyinstaller -F ../scripts/$i;
    rm *.spec 
done

for i in $(ls dist/); do
    docker cp dist/$i ${CONTAINER_NAME}:/usr/local/share/zabbix/external_scripts/
done
