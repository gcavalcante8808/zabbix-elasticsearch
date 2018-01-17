Zabbix-ElasticSearch
--------------------

This repository have all neeeded tools to properly do a good monitoring of a elasticsearch cluster.

How it Works
------------


Install
-------

To install the required tools to start the monitoring of the elastic search, you should do the following:

1. Download the latest release of the scripts and descompact it to the location "/usr/local/share/zabbix/externalscripts";
2. Configure your zabbix-agentd to read additional configuration from the folder "/usr/local/etc/zabbix_agentd.conf.d/";
3. Download the latest userparameter configuration to a folder that your zabbix_agentd will read (we going to use /usr/local/etc/zabbix_agentd.conf.d/ in this example):

```
wget https://raw.githubusercontent.com/gcavalcante8808/zabbix-elasticsearch/master/userparams/es.userparams.conf -C /usr/local/etc/zabbix_agentd.conf.d/
```

4. Restart the agentd to apply the configurations:
5. Test the new userparameters support:

```
zabbix_agentd -p
```

At the end of the list, the keys and some errors (after all we didnt provide the required params) will be showed.

6. Import the template into your Zabbix Server;
7. Create a new Host with the following configurations:

 * HostName: HostName of the ZabbixAgent that have the userparams installed;
 * Agent Interface: Ip or Hostname of the ZabbixAgent that have the userparams installed;
 * Link the template "Template App Elastic Search" to the Host;
 * Define the user macro "${ES_URL}" value to your elasticsearch address in a valid url format. Eg http://myes:9200/.

Enjoy!
