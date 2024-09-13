from os import system
from models.Motoboy import Motoboy
from models.Medico import Medico
from models.Advogado import Advogado
from models.Endereco import Endereco
from models.Sexo import Sexo
from models.Setor import Setor
from models.UnidadeFederativa import UnidadeFederativa
from models.Cliente import Cliente
from models.Juridica import Juridica
system("cls||clear")

endereco_medico = Endereco("Rua das Flores", "250", "Sala 3", "30150-300", "Belo Horizonte", UnidadeFederativa.MINAS_GERAIS.nome)
endereco_motoboy = Endereco("Avenida Brasil", "200", "Casa 4", "22290-000", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO.nome)
endereco_advogado = Endereco("Rua Pedro II", "150", "Cobertura", "40100-000", "Salvador", UnidadeFederativa.BAHIA.nome)
endereco_cliente = Endereco("Rua Augusta", "500", "Loja 12", "01413-000", "São Paulo", UnidadeFederativa.SAO_PAULO.nome)
endereco_juridica = Endereco("Avenida Goiás", "900", "Andar 2", "74000-000", "Goiânia", UnidadeFederativa.GOIAS.nome)

medico = Medico("Juliana Santos", "31 91234-5678", "juliana.santos@medico.com", endereco_medico, "12345678922", "765432123", "05/06/1980", Sexo.FEMININO, "CRM12345", Setor.SAUDE, 3500.00, "123456")

motoboy = Motoboy("Rafael Lima", "21 92345-6789", "rafael.lima@entregas.com", endereco_motoboy, "98765432222", "654321987", "11/02/1995", Sexo.MASCULINO, "CNPJ654321", Setor.LOGISTICA, 2200.00, "456789")

advogado = Advogado("Mariana Oliveira", "71 93456-7890", "mariana.oliveira@advocacia.com", endereco_advogado, "09876543211", "876543210", "18/09/1978", Sexo.FEMININO, "OAB87654", Setor.JURIDICO, 5000.00, "DF654321")

cliente = Cliente("Pedro Almeida", "11 99876-5432", "pedro.almeida@cliente.com", endereco_cliente, "56473829100", "987654321", "25/12/1990", Sexo.MASCULINO, "CLI987654")

juridica = Juridica("Tech Solutions LTDA", "62 99345-6789", "contato@techsolutions.com", endereco_juridica, "99.876.543/0001-10", "54321876")

print(medico)
print("\n")
print(cliente)
print("\n")
print(motoboy)
print("\n")
print(advogado)
print("\n")
print(juridica)
