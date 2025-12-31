-- SQL para estruturação da tabela de usuários
create table users(
    id serial primary key,
    nome varchar(100) not null,
    email varchar(50) not null unique,
    senha varchar(255) not null,
    created_at timestamp default now()
)