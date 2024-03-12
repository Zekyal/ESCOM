create table categoria(
	idcategoria serial not null primary key,
	nombreCategoria varchar(50) not null,
	descripcionCategoria varchar(100) not null
);

create table producto(
	idProducto serial not null primary key,
	nombreProducto varchar(50) not null,
	descripcionProducto varchar(100) not null,
	precio money not null,
	existencia int not null,
	idcategoria int not null,
	foreign key(idcategoria) references categoria (idcategoria) on delete cascade on update cascade 
);

INSERT INTO categoria (nombrecategoria,descripcioncategoria) VALUES
	 ('deportes','todo de deportes');
INSERT INTO categoria (nombrecategoria,descripcioncategoria) VALUES
	 ('tecnologia','celualares varotos'),
	 ('computacion','computacion'),
	 ('muebleria','muebles trancazo'),
	 ('instrumentos musicales','guitarras, pianos, etc.'),
	 ('musica','todo de musica'),
	 ('farmacia','todo sobre medicamentos'),
	 ('armas','resorteras y chinanpinas'),
	 ('joyeria','joyas interesantes'),
	 ('papeleria','lapices y libretas variados'),
	 ('ropa','ropa de moda'),
	 ('ferreteria','todo de tuberias'),
	 ('limpieza','limpieza');
	 
INSERT INTO producto (nombreproducto,descripcionproducto,existencia,idcategoria,precio) VALUES
	 ('balon','Balon para pruebas',30,3,550.0);
INSERT INTO producto (nombreproducto,descripcionproducto,existencia,idcategoria,precio) VALUES
	 ('laptop dy','laptop hp al reves',10,1,5000.0),
	 ('teclado sin RGB','teclado sencillo',100,1,100.0),
	 ('teclado con RGB','teclado para juegos',100,1,1000.0),
	 ('maestro sucio','jabon para trastes',1000,2,20.0),
	 ('paroxetina','pastilla de la felicidad',100,10,75.0),
	 ('clonazepam','gotita de la felicidad',40,10,200.0),
	 ('silla no gamer','silla sin luces led',20,4,1500.0),
	 ('silla gamer','silla de muebles trancaso con luces led',30,4,4000.0),
	 ('resortera simple','resortera sencilla',23,11,20.0),
	 ('resortera tactica','resortera militar patentada por la UNAM',10,11,1000.0);
	 
--ALTER SEQUENCE producto_idProducto_seq RESTART WITH 12;
--ALTER SEQUENCE categoria_idcategoria_seq RESTART WITH 14;