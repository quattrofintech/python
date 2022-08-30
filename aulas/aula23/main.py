from classe import Editora
from classe import Livro


editora = Editora()
editora.razaoSocial = "Safaria"
editora.email = "contato@safaria.com.br"
editora.telefone = '11236987456'
editora.listarEditora()


livro = Livro("O titulo", "Pt-br")
livro.editora = editora
livro.listarLivro()