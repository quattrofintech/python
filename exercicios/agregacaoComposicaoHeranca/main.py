from classe import PessoaJuridica,PessoaFisica, Endereco

endPJ = Endereco(123, 'Rua ABC', 78, 'Bairro', 'Cidade', 'ES', '1236549877')

pj = PessoaJuridica(1, 'Pessoa ASD', '19/02/1992', endPJ, '12365487/0001-98', "ME")
pj.cadastrarContato('email: email@contato.com')
pj.cadastrarContato('celular: 21998456231')
pj.cadastrarContato('telefone: 2126978456')
pj.cadastrarContato('site: www.asdasdasd.com.br')
pj.listarPessoaJuridica()


endPF = Endereco(987, 'Rua Endereço', 11, 'Bairro', 'Cidade', 'ES', '98745632')
pf = PessoaFisica(159, 'Pessoa Fisica', '12/12/2002', endPF, '123987159-98', 'Masculino')
pf.cadastrarContato('celular: 21954165487')
pf.cadastrarContato('email: pessoafisica@contato.com')
pf.listarPessoaFisica()