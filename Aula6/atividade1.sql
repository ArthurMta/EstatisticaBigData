SELECT
tb_pedidos.codigo_cliente , tb_clientes.nome , tb_pedidos.codigo_pedido , tb_pedidos.data_pedido , tb_produtos.produto , tb_produtos.preco
from
	tb_clientes
    join tb_pedidos
		on tb_clientes.codigo_cliente = tb_pedidos.codigo_cliente
	join tb_itens
		on tb_pedidos.codigo_pedido = tb_itens.codigo_pedido
	join tb_produtos
		on tb_itens.codigo_produto = tb_produtos.codigo_produto;
        