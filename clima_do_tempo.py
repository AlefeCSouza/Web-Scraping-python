#fazer a requisição ao endereço da internet e conteudo da pagina 
import requests

#responsavel para processar e extrair dados da estrutura HTML e converter em python
from bs4 import BeautifulSoup

# URL da previsão do tempo
url = "https://www.tempo.com/sao-paulo.htm"

# Faz a requisição
resposta = requests.get(url)
#caso a pagina não carregue retornara o erro 
resposta.raise_for_status()  

# Parsear o HTML
soup = BeautifulSoup(resposta.text, 'html.parser')

# Encontrar o elemento que contém a temperatura
# OBS: Isso depende da estrutura do site e precisa ser ajustado
temperatura = soup.find('span', class_='dato-temperatura changeUnitT')
descricao = soup.find('span', class_='descripcion').get_text(strip=True)

# Mostrar os resultados
print(f"Temperatura atual: {temperatura.get_text(strip=True)}")
print(f"Descrição: {descricao}") 
