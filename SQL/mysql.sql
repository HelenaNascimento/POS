/*CREATE TABLE FUNCIONARIO(
    "ID_FUNC" INTEGER,
    "NOME VARCHAR(50)" NOT NULL,
    "SOBRENOME VARCHAR(50)" NOT NULL,
    "ANO_NASCIMENTO" DATE,
	PRIMARY KEY ("ID_FUNC" AUTOINCREMENT)
);

CREATE TABLE LOJA (
    "ID_LOJA" INTEGER,
    "ENDERECO_LOJA" VARCHAR(80) NOT NULL,
    "CIDADE" VARCHAR (30) DEFAULT 'Fortaleza',
    "REGIAO" VARCHAR(20) CHECK (REGIAO IN ('NORDESTE', 'SUL' )),
    "ESTADO" CHAR (2) NOT NULL,
    "PAIS" VARCHAR(20) NOT NULL,
	PRIMARY KEY ("ID_LOJA" AUTOINCREMENT)
);

CREATE TABLE TIPO_VENDAS(
    ID_TIP_VENDAS INTEGER,
    NOME_TIPO VARCHAR (30),
	PRIMARY KEY ("ID_TIP_VENDAS" AUTOINCREMENT)
);

CREATE TABLE EVENTO(
    "ID_EVENTO" INTEGER,
    "DATA_EVENTO" DATE,
    "SEMANA_EVENTO" INTEGER,
    "MES_EVENTO" INTEGER,
    "ANO_EVENTO" INTEGER,
	PRIMARY KEY ("ID_EVENTO" AUTOINCREMENT)
);


CREATE TABLE PRODUTO(
    "ID_PRODUTO" INTEGER,
    "NOME_PRODUTO" VARCHAR(40) NOT NULL,
    "TIPO_PRODUTO" VARCHAR(30) NOT NULL,
	PRIMARY KEY ("ID_PRODUTO" AUTOINCREMENT)
);

CREATE TABLE FATO(
    "ID_FATO" INTEGER,
    "ID_PRODUTO" INTEGER NOT NULL,
    "ID_EVENTO" INTEGER NOT NULL,
    "ID_LOJA" INTEGER NOT NULL,
    "ID_FUNCIONARIO" INTEGER NOT NULL,
    "ID_TIPO_VENDAS" INTEGER NOT NULL,
    "PRECO" NUMERIC (8,2) NOT NULL,
    "QUANTIDADE" DECIMAL(8,2) NOT NULL,
    FOREIGN KEY ("ID_PRODUTO") REFERENCES "PRODUTO"("ID_PRODUTO"),
    FOREIGN KEY ("ID_EVENTO") REFERENCES "EVENTO"("ID_EVENTO"),
    FOREIGN KEY ("ID_LOJA") REFERENCES "LOJA"("ID_LOJA"),
    FOREIGN KEY ("ID_FUNCIONARIO") REFERENCES "FUNCIONARIO"("ID_FUNCIONARIO"),
    FOREIGN KEY ("ID_TIPO_VENDAS") REFERENCES "TIPO_VENDAS"("ID_TIPO_VENDAS"),
	PRIMARY KEY ("ID_FATO" AUTOINCREMENT)
);


INSERT INTO "Produto" (nome_produto, tipo_produto) 
VALUES 
('Smartphone X', 'Eletrônicos'),
('Notebook Pro', 'Eletrônicos'),
('Fones de Ouvido Plus', 'Acessórios'),
('Smartwatch 2', 'Vestíveis'),
('Tablet 8', 'Eletrônicos'),
('Câmera Z', 'Fotografia'),
('Caixa de Som Loud', 'Áudio'),
('Drone Fly', 'Gadgets'),
('Monitor 4K', 'Monitores'),
('Teclado Swift', 'Periféricos');


update produto
set cores = 'Amarelo'
where tipo_produto = 'Acessórios';

update produto
set cores = 'Verde'
where tipo_produto = 'Fotografia';

update produto
set cores = 'Azul'
where tipo_produto = 'Áudio';

update produto
set cores = 'Branco'
where tipo_produto = 'Monitores';

INSERT INTO "FUNCIONARIO" (NOME, SOBRENOME, ANO_NASCIMENTO) VALUES 
('Maria', 'Santos', '1977-04-05'),
('José', 'Oliveira', '1981-06-09'),
('Ana', 'Pereira', '1985-03-05'),
('Antônio', 'Costa', '1995-01-01'),
('Francisca', 'Dias', '1972-02-04');

*/
