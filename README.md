
# Automação de processos em Python 

Essa é uma automação que faz os seguintes passos:
- Abre o Google Chrome;
- Entra no site `www.google.com`;
- Faz a pesquisa `"Cases de agentes de IA"`;
- Extrai os 25 primeiros resultados, adicionando os links e os respectivos títulos em uma planilha Excel.

# Bibliotecas utilizadas 

## Undetected Chrome Driver 
Essa biblioteca foi utilizada para abrir o aplicativo do Google Chrome sem a verificação de bots feita pelo próprio Google. Sem ela, o Google conseguiria ser aberto, mas após realizar a pesquisa, o navegador barraria por conta do número de solicitações. Logo, usar essa biblioteca foi essencial para ultrapassar essa barreira.

## Selenium
Essa biblioteca é a base da automação. Ela localiza a barra de pesquisa utilizando o `XPATH`, clica e digita o tema da pesquisa, e logo em seguida aperta o `ENTER`. Após a pesquisa, ela localiza o `XPATH` padrão dos sites e os numera. Tudo isso estando em um loop, ela clica no primeiro que aparece, entra no site, extrai URL e título (duas funções nativas do Selenium), salva os dados na planilha Excel e sai do site. Ela repete essa ação, só que agora para o segundo site, o terceiro, e assim por diante. 

Quando chega ao fim da página, a biblioteca reconhece que chegou ao fim, e assim localiza o `XPATH` da barra de páginas e clica para ir para a segunda página, e depois para a terceira, e assim por diante. Em uma nova página, ela realiza o mesmo loop citado acima. ELa realiza todo esse processo até a automação chegar no número de dados solicitado.

## Openpyxl
Essa biblioteca faz a conexão com a planilha Excel, onde os dados serão armazenados. Todas as vezes que a automação consegue extrair os dados, essa biblioteca é acionada, assim ela faz a conexão e joga os dados dentro da planilha. Ao final do processo, quando a automação estiver atingido o número máximo de daods, a biblioteca salva todas as alterações da pĺanilha
