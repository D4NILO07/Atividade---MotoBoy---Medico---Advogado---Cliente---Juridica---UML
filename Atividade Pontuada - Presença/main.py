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

# Atualização dos endereços
endereco_medico = Endereco("Rua das Palmeiras", "88", "Apartamento 404", "20250-400", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO.nome)
endereco_motoboy = Endereco("Rua do Comércio", "900", "Sala 501", "20010-000", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO.nome)
endereco_advogado = Endereco("Rua das Nações", "1100", "Andar 4", "22222-000", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO.nome)
endereco_cliente = Endereco("Avenida Paulista", "1234", "Cobertura", "01310-100", "São Paulo", UnidadeFederativa.SAO_PAULO.nome)
endereco_juridica = Endereco("Rua BEIA", "300", "Bloco C", "40711-600", "Salvador", UnidadeFederativa.BAHIA.nome)

# Atualização das instâncias
medico = Medico("Rafael Silva", "71 98888-9999", "rafael.silva@medico.com", endereco_medico, "12345678901", "987654321", "12/06/1985", Sexo.MASCULINO, "4567891234567", Setor.ENGENHARIA, 3200.00, "56789")

motoboy = Motoboy("Juliana Santos", "11 99999-2222", "juliana.santos@entrega.com", endereco_motoboy, "10987654321", "123456789", "22/03/1989", Sexo.FEMININO, "404040", Setor.OPERACOES, 1900.00, "5678901234")

advogado = Advogado("Lucas Pereira", "61 98888-5555", "lucas.pereira@advocacia.com", endereco_advogado, "23456789012", "876543210", "30/08/1980", Sexo.MASCULINO, "987654", Setor.JURIDICO, 5000.00, "DF654321")

cliente = Cliente("Mariana Costa", "21 98888-7777", "mariana.costa@cliente.com", endereco_cliente, "10987654321", "123456789", "05/09/1991", Sexo.FEMININO, "AT202309004")

juridica = Juridica("Global Tech LTDA", "21 99999-5555", "contato@globaltech.com", endereco_juridica, "12.345.678/0001-91", "87654321")

print(medico)
print("\n")
print(cliente)
print("\n")
print(motoboy)
print("\n")
print(advogado)
print("\n")
print(juridica)
