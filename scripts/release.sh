#!/bin/bash

CONTAINER_NAME=dockerzabbix_agentd_1

for i in $(ls *.py); do 
    pyinstaller -F $i;
    rm *.spec 
done

for i in $(ls dist/); do
    docker cp dist/$i ${CONTAINER_NAME}:/usr/local/share/zabbix/external_scripts/
done
