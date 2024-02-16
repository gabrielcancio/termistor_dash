# Termistor Dash
Dashboard para feia em Django para vizualizar dados de temperatura de sistema de medição usando termistor NTC enviados via MQTT.

## Instruções de instalação
1. Necessário instalar o django
2. Necessário instalar paho-mqtt: `pip install paho-mqtt`
3. Necessário Iniciar as migrations: `python manage.py migrate`

## Instruções para execução
1. Inciar consumer para o tópico EQ1/temp: `python manage.py init_mqtt_consumer`
2. Iniciar consumer para o tópico EQ1/temp1: `python manage.py init_mqtt_consumer_1`
3. Iniciar app Django: `python manage.py runserver`