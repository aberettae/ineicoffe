PROYECTO INEICOFFE
==================
Proyecto para el curso de python/django ENEI

Configurar el proyecto para desarrollo
---------------------------------------

1. Crear archivo local
    
    cd icoffe/icoffe/settings/
    cp example_enviroment.py local.py
    
2. Descargar los archivos assets y media

    http://goo.gl/8jT3fk
    


data de prueba Fixture
----------------

1. Crear fixture

    dumpdata ambientes recursoshumanos productos ventas contactenos reservas -o ../fixture/data-demo.json
    
2. importar fixture

    ../fixture/data-demo.json
