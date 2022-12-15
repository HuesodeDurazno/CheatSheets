# Pytest

Correr todos los comandos 
    pytest

Ver detalles 
    pytest -v

Metodos utiles en clases
    setup
        se ejecuta una vez por cada single test
    
    teardown
        despues una vez para cada single test
    setup_class(cls)
        una vez antes de los test que contiene la clase 
    teardown_class(cls)
        una vez despues **

multiples parametros para un solo assert
    @pytest.mark.parametrize('value',[list_values])

modo debbuger
    --pdb
ver recoleccion de test
    --collect-only
parar al primer error
    -x
