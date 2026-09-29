
SELECT 
	tb_usuarios.id_usuario, tb_usuarios.nome,
	tb_alugados.data_aluguel, tb_alugados.data_devolucao, tb_alugados.valor,
	tb_livros.id_livro, tb_livros.titulo
FROM 
	tb_livros
join tb_itens_alugados
	on tb_livros.id_livro = tb_itens_alugados.id_livro
join tb_alugados
	on tb_itens_alugados.id_aluguel = tb_alugados.id_aluguel
join tb_usuarios
	on tb_usuarios.id_usuario = tb_alugados.id_usuario;