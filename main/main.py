print ("Bem-vindo ao gerador de nomes de bandas!")
import random

perguntas = [
  "Qual é a sua cor favorita?",
  "Qual é o seu animal favorito?",
  "Qual é a sua estação do ano preferida?",
  "Se você pudesse viajar no tempo, para qual época iria?",
  "Qual é o seu filme favorito de todos os tempos?",
  "Se você tivesse um superpoder, qual seria?",
  "Qual é o seu hobby favorito?",
  "Se você pudesse jantar com qualquer pessoa, viva ou morta, quem seria?",
  "Qual é a sua comida favorita?",
  "Qual é o seu lugar favorito na cidade?",
  "Se você fosse um personagem de livro, quem seria?",
  "Qual é a sua banda ou artista musical favorito(a)?",
  "Se você pudesse aprender a tocar qualquer instrumento, qual seria?",
  "Se você fosse um tipo de clima, qual seria?",
  "Qual é o seu livro favorito?",
  "Se você pudesse ter um encontro com um personagem fictício, quem seria?",
  "Qual é a sua série de TV favorita?",
  "Qual é o seu esporte favorito?",
  "Se você pudesse ser um explorador, para onde iria?",
  "Qual é o seu sabor de sorvete favorito?",
  "Se você fosse um herói de quadrinhos, qual seria seu nome?",
  "Qual é o seu número da sorte?",
  "Se você tivesse uma nave espacial, para onde viajaria primeiro?",
  "Qual é a sua palavra favorita?",
  "Se você pudesse ser um animal por um dia, qual seria?",
  "Qual é a sua bebida favorita?",
  "Se você pudesse ter uma casa em qualquer lugar do mundo, onde seria?",
  "Qual é o seu jogo de tabuleiro favorito?",
  "Se você pudesse ter um talento especial, qual seria?",
  "Qual é o seu instrumento musical favorito?",
  "Se você pudesse viver em qualquer era histórica, qual seria?",
  "Qual é o seu doce favorito?",
  "Se você pudesse visitar qualquer país, qual seria?",
  "Qual é o seu estilo de dança favorito?",
  "Se você fosse um personagem de desenho animado, quem seria?",
  "Qual é o seu programa de TV dos anos 90 favorito?",
  "Se você pudesse ter um carro de qualquer cor, qual seria?",
  "Qual é o seu tipo de música favorito?",
  "Se você fosse um tipo de flor, qual seria?",
  "Qual é a sua atividade ao ar livre favorita?",
  "Se você pudesse ser um profissional em qualquer esporte, qual seria?",
  "Qual é o seu jogo de videogame favorito?",
  "Se você pudesse ter um animal de estimação exótico, qual seria?",
  "Qual é o seu prato de comida internacional favorito?",
  "Se você fosse um elemento da natureza, qual seria?",
  "Qual é o seu objeto de decoração favorito em casa?",
  "Se você pudesse ser um personagem de filme de terror, quem seria?",
  "Qual é o seu dia da semana favorito?",
  "Se você pudesse ter um superpoder de ficção científica, qual seria?",
  "Qual é o seu estilo de moda favorito?",
  "Se você fosse um tipo de nuvem, qual seria?",
  "Qual é o seu programa de culinária favorito?",
  "Se você pudesse ter uma profissão diferente, qual seria?",
  "Qual é a sua estação de rádio favorita?",
  "Se você fosse um tipo de árvore, qual seria?",
  "Qual é o seu feriado favorito?",
  "Se você pudesse ter uma casa na praia ou nas montanhas, qual escolheria?",
  "Qual é o seu destino de viagem dos sonhos?",
  "Se você pudesse ter um superpoder de teletransporte, para onde iria agora?",
  "Qual é o seu prato de comida caseira favorito?",
  "Se você fosse um tipo de rocha ou cristal, qual seria?",
  "Qual é o seu programa de festa temática favorito?",
  "Se você fosse um personagem de conto de fadas, quem seria?",
  "Qual é o seu programa de TV de culinária favorito?",
  "Se você fosse um instrumento musical, qual seria?",
  "Qual é a sua estação de rádio online favorita?",
  "Se você pudesse ter um animal de estimação mitológico, qual seria?",
  "Qual é a sua comida de rua favorita?",
  "Se você fosse um elemento do universo, qual seria?",
  "Qual é o seu estilo de decoração favorito?",
  "Se você pudesse ser um personagem de ficção científica, quem seria?",
  "Qual é o seu dia festivo preferido?",
  "Se você fosse uma bebida, qual seria?",
  "Qual é o seu prato gourmet favorito?",
  "Se você pudesse ser um fenômeno natural, qual seria?",
  "Qual é o seu evento esportivo favorito?",
  "Se você fosse um personagem histórico, quem seria?",
  "Qual é a sua série de TV de suspense favorita?",
  "Se você pudesse ter um animal de estimação fantástico, qual seria?",
  "Qual é a sua comida rápida favorita?",
  "Se você fosse um elemento químico, qual seria?",
  "Qual é o seu programa de TV de comédia favorito?",
  "Se você pudesse ter um talento artístico, qual seria?",
  "Qual é a sua estação de rádio de música clássica favorita?",
  "Se você fosse um ser mágico, qual seria?",
  "Qual é o seu tipo de comida asiática favorito?",
  "Se você fosse um fenômeno meteorológico, qual seria?",
  "Qual é o seu esporte olímpico favorito?",
  "Se você fosse uma figura mítica, quem seria?",
  "Qual é o seu programa de TV de fantasia favorito?",
  "Se você pudesse ter uma profissão criativa, qual seria?",
  "Qual é a sua estação de rádio local favorita?",
  "Se você fosse um ser mágico, qual seria?",
  "Qual é o seu prato vegetariano favorito?",
  "Se você pudesse ser um elemento natural, qual seria?",
  "Qual é o seu evento esportivo ao ar livre favorito?",
  "Se você fosse um personagem mitológico, quem seria?",
  "Qual é o seu tipo de comida mexicana favorito?",
  "Se você pudesse ser um elemento do cosmos, qual seria?",
  "Qual é o seu programa de TV de fantasia favorito?"
]

def escolher(n):
  #retorna N perguntas aleatórias da lista
  return random.sample(perguntas, n)

def fazerPerguntas(perguntas):
  # Faz as perguntas ao usuário
  respostas = []
  for i, pergunta in enumerate(perguntas, start=1):
      resposta = input(f"Pergunta {i}: {pergunta} ")
      respostas.append(resposta)  # Adiciona a resposta à lista
  return respostas

while True:
  # Escolhe aleatoriamente as perguntas
  perguntasAleatórias = escolher(2)
  respostas = fazerPerguntas(perguntasAleatórias)
  # Exibe o nome da banda com as respostas
  print("O nome da sua banda pode ser " + " ".join(respostas))
  resposta = input("Gostaria de tentar novamente? Digite 'sim' ou 'não':")
  if resposta.lower() == "não":
      print("Obrigado por usar o gerador de nomes de bandas!")
      break