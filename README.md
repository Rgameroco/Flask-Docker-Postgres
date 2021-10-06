### 2 

Para este proyecto prefiero usar una bd relacional. Si fuera una bd muy grande donde mis consultas fueran a demorar mucho, consideraria NOSQL. Aunque al ser un bd chica si podria usar una no sql ya que no necesito tener integridad de los datos. En realidad las dos opciones son validas para este caso.

CREATE TABLE jokes(
    id serial primary key,
    jokes VARCHAR(256) NOT NULL,
    create_at TIMESTAMP NOT NULL,
    active BOOLEAN NOT NULL DEFAULT TRUE
);

db.createCollection(jokes, {
    id: <number>,
    jokes:<string>,
    create_at:<string>,
    active:<boolean>
})

### 3

#### 3.1 Ejecutar
Para ejecutar el proyecto usar docker-compose.
    docker-compose up -d --build
    docker-compose up
Psdata: Si estas en Linux y no tienes docker agregado a un grupo usar SUDO.

### 3.2 Doc

#### Contrato GET

http://172.19.0.3:5000/jokes$value={}

#### Contrato Post

http://172.19.0.3:5000/jokes$value={}

#### Contrato Patch

http://172.19.0.3:5000/jokes$id={}$joke={}

#### Contrato Delete

http://172.19.0.3:5000/jokes$id={}