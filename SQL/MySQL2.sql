/*

INSERT INTO Produto (nome_produto, tipo_produto) VALUES 
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

SELECT * FROM PRODUTO;

use dbvendas;

alter table produto modify column cores varchar(20);

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

INSERT INTO Funcionario (nome, sobrenome, data_nascimento) VALUES 
('João', 'Silva', '1985-03-05'),
('Maria', 'Santos', '1977-04-05'),
('José', 'Oliveira', '1981-06-09'),
('Ana', 'Pereira', '1985-03-05'),
('Antônio', 'Costa', '1995-01-01'),
('Francisca', 'Dias', '1972-02-04');

select * from funcionario

INSERT INTO Tipo_Vendas (nome_tipo) VALUES 
('Venda Direta'),
('Venda Online'),
('Venda por Telefone'),
('Venda por Representante'),
('Venda em Loja'),
('Venda por Catálogo'),
('Venda Corporativa'),
('Venda por Atacado'),
('Venda por Consignação'),
('Venda por Assinatura');

select * from tipo_vendas


INSERT INTO Evento (data_evento, semana_evento, mes_evento, ano_evento) VALUES 
('2023-01-01', 1, 1, 2023),
('2023-01-08', 2, 1, 2023),
('2023-01-15', 3, 1, 2023),
('2023-01-22', 4, 1, 2023),
('2023-01-29', 5, 1, 2023),
('2023-02-05', 6, 2, 2023),
('2023-02-12', 7, 2, 2023),
('2023-02-19', 8, 2, 2023),
('2023-02-26', 9, 2, 2023),
('2023-03-05', 10, 3, 2023);

select * from tipo_vendas

INSERT INTO Loja (endereco_loja, cidade, regiao, estado, pais) VALUES 
('Rua das Flores, 123', 'São Paulo', 'SUL', 'SP', 'Brasil'),
('Avenida Brasil, 456', 'Rio de Janeiro', 'SUL', 'RJ', 'Brasil'),
('Praça da Sé, 789', 'Salvador', 'Nordeste', 'BA', 'Brasil'),
('Rua XV de Novembro, 101', 'Fortaleza', 'Nordeste', 'CE', 'Brasil'),
('Avenida Paulista, 202', 'Belo Horizonte', 'Sul', 'MG', 'Brasil'),
('Rua das Palmeiras, 303', 'Brasília', 'Sul', 'DF', 'Brasil'),
('Avenida das Nações, 404', 'Curitiba', 'Sul', 'PR', 'Brasil'),
('Rua Grande, 505', 'Manaus', 'Nordeste', 'AM', 'Brasil'),
('Avenida Goiás, 606', 'Goiânia', 'Sul', 'GO', 'Brasil'),
('Rua Osvaldo Cruz, 707', 'Recife', 'Nordeste', 'PE', 'Brasil');

Select * from Loja


INSERT INTO Fato (id_produto, id_evento, id_loja, id_tipo_vendas, id_funcionario, preco, quantidade) VALUES 
(1, 1, 11, 1, 1, 999.99, 5),
(2, 2, 12, 2, 2, 1299.99, 3),
(3, 3, 13, 3, 3, 199.99, 10),
(4, 4, 14, 4, 4, 299.99, 4),
(5, 5, 15, 5, 5, 499.99, 6),
(6, 6, 16, 6, 6, 599.99, 7),
(7, 7, 17, 7, 3, 699.99, 8),
(8, 8, 18, 8, 4, 799.99, 9),
(9, 9, 19, 9, 5, 899.99, 10),
(10, 10, 20, 10, 6, 999.99, 11);



*/
