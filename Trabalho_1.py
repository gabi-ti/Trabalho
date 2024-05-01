# A. Mensagen de boas-vindas
print('Bem-vinda a Loja da Gabriela Lopes')

# B. Inserido o valor do produto e a quantidade de produtos comprada
valor_prod = float (input('Digite o valor do produto:'))
quantidade_prod = int (input('Digite a quantidade do produto:'))

# C. Abaixo iremos aplicar os descontos conforme a promoção da loja.

# D. O total do valor sem desconto

total_sem_desconto = valor_prod * quantidade_prod


# E. Aplicando os descontos.

if (total_sem_desconto <2500):
  desconto = 0
elif (total_sem_desconto >= 2500 and total_sem_desconto < 6000):
  desconto = 0.04
  print ('Parabéns! Você ganhou 4% de desconto')
elif (total_sem_desconto >= 6000 and total_sem_desconto < 10000):
  desconto = 0.07
  print ('Parabéns! Você ganhou 7% de desconto')
else:
  desconto = 0.11
  print ('Parabéns! Você ganhou 11% de desconto')    

  valor_desc = total_sem_desconto * desconto
  valor_total_com_desc = total_sem_desconto - valor_desc
 
# F. Neste prgrama, apresento minha loja, onde de acordo com o total de compras feitas pelo cliente
# aplicamos 3 opções de descontos.

# G. Feito na linha 2


print('Valor total sem desconto: R$ {:.2f}'. format(total_sem_desconto))
print('Valor total com desconto: R$ {:.2f}'. format(valor_total_com_desc))

