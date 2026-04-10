-- GestaAdvance: Enterprise Resource Planning
CREATE TABLE funcionarios (
    id_fun SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(50)
);

CREATE TABLE inventario (
    id_prod SERIAL PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    preco_compra DECIMAL(10,2),
    preco_venda DECIMAL(10,2),
    qtd_atual INT DEFAULT 0
);

CREATE TABLE movimentacoes (
    id_mov SERIAL PRIMARY KEY,
    id_prod INT REFERENCES inventario(id_prod),
    tipo_mov VARCHAR(10), -- 'ENTRADA' ou 'SAIDA'
    quantidade INT,
    data_mov TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
