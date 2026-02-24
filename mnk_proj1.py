#Primeiro projeto de fundamentos da programação- MNK

#2.1.1:
def eh_tabuleiro(tab):
    """
    Função que define se o argumento apresentado é um tabuleiro.
    Determina o número máximo e mínimo de linhas e colunas.

    >>> eh_tabuleiro(((1,0,0,1),(-1,1,0,1),(-1,0,0,-1)))
    True

    {tuple} --> {bool}
    """
    if not type(tab) == tuple or len(tab) == 0:
        return False

    for i in tab:
        if type(i) != tuple:
            return False

    for m in range(len(tab)):
        for n in range(len(tab[m])):
            if len(tab[m]) != len(tab[0]) or not type(tab[m][n]) == int\
                or tab[m][n] not in (-1, 0, 1):
                return False
            
    # determinar se a função tem o número de linhas e de colunas correto
    m, n = len(tab), len(tab[0])

    if not 2 <= m <= 100 or not 2 <= n <= 100:
        return False

    return True

#2.1.2:
def eh_posicao(pos):
    """
    Função que valida uma posição no tabuleiro.
    Tem que estar entre 0 e 10000 porque o máximo de linhas e colunas é 100.

    >>> eh_posicao(9)
    True

    {int} --> {bool}
    """
    if not type(pos) == int or not 0 < pos <= 10000:
        return False
    
    return True

#2.1.3:
def obtem_dimensao(tab):
    """
    Função que determina o número de linhas e colunas.
    O número de colunas é o comprimento do tuplo de índice 0.
    O número de linhas é o número de tuplos dentro do tuplo inicial.

    >>> obtem_dimensao(((1,0,0,1),(-1,1,0,1),(-1,0,0,-1)))
    (3, 4)

    {tuple} --> {tuple}
    """
    linhas, colunas = 0, len(tab[0])

    for idx in tab:
        linhas += 1

    return (linhas, colunas)

#Função auxiliar 1
def transforma_tuplo(tab):
    """
    Função que torna um tuplo de tuplos num único tuplo.
    Cria um novo tuplo com os valores dos tuplos fornecidos.

    >>> transforma_tuplo((1,0,0,1),(-1,1,0,1),(-1,0,0,-1))
    (1,0,0,1,-1,1,0,1,-1,0,0,-1)

    {tuple} --> {tuple}
    """
    tuplo = ()

    for m in range(len(tab)):
        for n in range(len(tab[m])):           
            tuplo = tuplo + (tab[m][n],)
    
    return tuplo


#2.1.4:
def obtem_valor(tab, pos):
    """
    Função que devolve o valor de uma posição do tabuleiro.
    Utiliza a função auxiliar transforma_tuplo(tab).
    Como as posições no tabuleiro correspondem a +1 das posições do tuplo,\
    subtrai-se 1.

    >>>obtem_valor(((1,0,0,1),(-1,1,0,1),(-1,0,0,-1)), 1)
    1

    {tuple, int} --> {int}
    """
    return transforma_tuplo(tab)[pos-1]

#2.1.5:
def obtem_coluna(tab, pos):
    """
    Função que devolve a coluna onde está contida a posição fornecida.
    Utiliza a função auxiliar obtem_dimensao(tab).

    >>>obtem_coluna(((1,0,0,1),(-1,1,0,1),(-1,0,0,-1)), 2)
    (2, 6, 10)

    {tuple, int} --> {tuple}
    """
    m, n = obtem_dimensao(tab)
    coluna = (pos - 1) % n
    res = tuple(linha * n + coluna + 1 for linha in range(m))

    return res

#2.1.6:
def obtem_linha(tab, pos):
    """
    Função que devolve a linha do tabuleiro onde está inserida a posição\
    escolhida.
    Determina a posição inicial da linha e soma o seu comprimento.

    >>>obtem_linha(((1,0,0,1),(-1,1,0,1),(-1,0,0,-1)), 3)
    (1, 2, 3, 4)

    {tuple, int} --> {tuple}
    """
    #determina o tuplo(linha) onde está pos
    pos_linha = (pos - 1) // len(tab[0])
    #determina a posição do 1º elemento desse tuplo
    inicio_linha = pos_linha * len(tab[0]) + 1

    return tuple(range(inicio_linha, inicio_linha + len(tab[0])))

#Função auxiliar 2
def coordenada_elem(tab, pos):
    """
    Função que determina as coordenadas de uma posição.
    Recebe o número de linhas e colunas do tabuleiro e encontra a coordenada\
    a que pertence pos, somando às linhas e às colunas 1.

    >>> coordenada_elem(((1,0,0,1),(-1,1,0,1),(-1,0,0,-1)), 3)
    (1,3)

    {tuple, int} --> {tuple}
    """
    m, n = len(tab), len(tab[0])
    linha = (pos - 1) // n
    coluna = (pos - 1) % n

    return linha + 1, coluna + 1

#Função auxiliar 3:
def diagonais(tab, pos):
    """
    Função que devolve a diagonal de uma posição.
    Utiliza a função auxiliar coordenada_elem(tab, pos).
    Utilizada na função obtem_diagonais(tab, pos).
    Percorre o tuplo linha a linha e coluna a coluna.
    
    >>> tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1))
    >>> antidiagonais(tab, 6)
    (1, 6, 11)

    {tuple, int} --> {tuple}
    """
    linha, coluna = coordenada_elem(tab, pos)
    linha -= 1
    coluna -= 1
    diagonais = []
    x1, y1 = linha, coluna
    x2, y2 = linha + 1, coluna + 1

    while x1 >= 0 and y1 >= 0:
        diagonais += [x1 * len(tab[0]) + y1 + 1]
        x1 -= 1
        y1 -= 1

    while x2 < len(tab) and y2 < len(tab[0]):
        diagonais += [x2 * len(tab[0]) + y2 + 1]
        x2 += 1
        y2 += 1

    return tuple(sorted(diagonais))

#Função auxiliar 4:
def antidiagonais(tab, pos):
    """
    Função que devolve a antidiagonal de uma posição.
    Utiliza a função auxiliar coordenada_elem(tab, pos).
    Utilizada na função obtem_diagonais(tab, pos).
    Percorre o tuplo linha e linha e coluna a coluna.
    
    >>> tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1))
    >>> antidiagonais(tab, 6)
    (9, 6, 3)

    {tuple, int} --> {tuple}
    """
    linha, coluna = coordenada_elem(tab, pos)
    linha -= 1
    coluna -= 1
    antidiagonais = []
    x3, y3 = linha, coluna
    x4, y4 = linha + 1, coluna - 1

    while x3 >= 0 and y3 < len(tab[0]):
        antidiagonais += [x3 * len(tab[0]) + y3 + 1]
        x3 -= 1
        y3 += 1

    while x4 < len(tab) and y4 >= 0:
        antidiagonais += [x4 * len(tab[0]) + y4 + 1]
        x4 += 1
        y4 -= 1

    return tuple(sorted(antidiagonais, reverse=True))

#2.1.7:
def obtem_diagonais(tab ,pos):
    """
    Função que devolve os tuplos correspondentes à diagonal (descendente da
    esquerda para a direita ) e antidiagonal (ascendente da esquerda para a \
    direita).
    Utiliza as funções auxiliares diagonais(tab, pos) e antidiagonais(tab, pos).

    >>> tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1))
    >>> obtem_diagonais(tab, 6)
    ((1, 6, 11), (9, 6, 3))

    {tuple, int} --> {tuple}
    """
    diagonal = diagonais(tab, pos)
    antidiagonal = antidiagonais(tab, pos)

    return (diagonal, antidiagonal)

#2.1.8
def tabuleiro_para_str(tab):
    """
    Representação externa do tabuleiro.
    'X' representa 1, '+' representa 0 e 'O' representa o -1. Utilizar append \
    para adicionar esses valores a uma lista vazia adicionando '---' entre eles. 
    Depois de cada linha, exceto na última, acrescentar uma linha de "|", com o\
    número de "|" igual ao tamanho da 1ª linha.  

    >>>tabuleiro_para_str((1, 0, 0), (-1, 1, 0), (-1,0,0))
    'X---+---+\n|   |   |\nO---X---+\n|   |   |\nO---+---+'

    {tuple} --> {string}
    """
    linhas = []

    for i, linha in enumerate(tab):
        linhas.append('---'.join(['X' if x == 1 else 'O' if x == -1 else '+' \
                                  for x in linha]))

        if i < len(tab) - 1:
            linhas.append('|   ' * (len(linha) - 1) + '|')
        
    return '\n'.join(linhas)

#2.2.1:
def eh_posicao_valida(tab, pos):
    """
    Função que determina se uma determinada posição pertence ao tabuleiro.
    Utiliza a função eh_tabuleiro(tab) para validar o argumento
    Utiliza a função auxiliar transforma_tuplo(tab), comparando a posição dos \
    elementos do tuplo com pos.

    >>>eh_posicao_valida(((1,0,0,1),(-1,1,0,1),(-1,0,0,-1)), 9)
    True

    {tuple, int} --> {bool}
    """
    if not type(pos) == int or not eh_tabuleiro(tab):
        raise ValueError("eh_posicao_valida: argumentos invalidos")

    for idx in range(len(transforma_tuplo(tab))):
        if (idx + 1) == pos:
            return True
        
    return False

#2.2.2:
def eh_posicao_livre(tab, pos):
    """
    Função que define se a posição escolhida está ocupada por uma pedra.
    Utiliza a função eh_tabuleiro(tab), eh_posicao(pos) e\
    eh_posicao_valida(tab, pos).
    Se a posição escolhida for zero, não tem nenhuma pedra. 1 e -1 são pedras.

    >>>eh_posicao_livre(((1,0,0,1),(-1,1,0,1),(-1,0,0,-1)), 2)
    True

    {tuple, int} --> {bool}
    """
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not \
        eh_posicao_valida(tab, pos):
        raise ValueError("eh_posicao_livre: argumentos invalidos")
    
    linha = (pos - 1) // len(tab[0]) #determina a linha onde está inserido pos
    coluna = (pos - 1) % len(tab[0]) #determina a coluna onde está inserido pos

    return tab[linha][coluna] == 0 #True para livre

#2.2.3
def obtem_posicoes_livres(tab):
    """
    Função que determina quais as posições livres (sem pedras).
    Utiliza as funções auxiliares transforma_tuplo(tab) e eh_tabulerio(tab).
    Se o valor de uma determinada posição do tuplo formado pela função auxiliar\
    for 0, ele é acrescentado ao tuplo resultado.

    >>>obtem_posicao_livre((1,0,0,1),(-1,1,0,1),(-1,0,0,-1))
    (2,3,7,10,11)

    {tuple} --> {tuple}
    """
    res = ()
    tuplo = transforma_tuplo(tab)
    if not eh_tabuleiro(tab):
        raise ValueError("obtem_posicoes_livres: argumento invalido")

    for idx in range(len(tuplo)):
        if tuplo[idx] == 0:
            res += (idx+1,)
        
    return res

#2.2.4
def obtem_posicoes_jogador(tab, jog):
    """
    Função que determina quais as posições com pedras brancas(-1) ou pretas(1).
    Utiliza as funções auxiliares transforma_tuplo(tab), obtem_dimensao(tab)\
    e eh_tabulerio(tab).
    Cria um novo tuplo com as posições do tabuleiro mais 1 em que o valor \
    associado é 1 ou -1. 

    >>>obtem_posicoes_jogador(((1,0,0,1),(-1,1,0,1),(-1,0,0,-1)), 1)
    (1, 4, 6, 8)

    {tuple, int} --> {tuple}
    """
    tuplo = transforma_tuplo(tab)
    res = ()
    m, n = obtem_dimensao(tab)

    if type(jog) != int or jog not in (-1, 1) or not eh_tabuleiro(tab):
        raise ValueError("obtem_posicoes_jogador: argumentos invalidos")

    for i in range(1, m * n + 1):
        if obtem_valor(tuplo, i) == jog:
            res += (i,)

    return res

#Função auxiliar 5:
def coordenadas(tab):
    """
    Função auxiliar que devolve as coordenadas de um tuplo.

    >>> coordenadas((1,0,1),(0,1,1))
    ((1,1),(1,2),(1,3),(2,1),(2,2),(2,3))

    {tuple} --> {tuple}
    """
    coordenadas = () 

    for x, valor1 in enumerate(tab):
        nova_linha = ()
        for y, valor2 in enumerate(valor1):
            nova_linha += ((x+1, y+1),) 

        coordenadas += (nova_linha,)
    
    return coordenadas

#2.2.5:
def obtem_posicoes_adjacentes(tab, pos):
    """
    Função que recebe um tabuleiro e uma posição desse tabuleiro e devolve as \
    suas posições adjacentes.
    Utiliza as funções auxiliares eh_tabuleiro(tab), eh_posicao(pos), \
    coordenadas(tab) e coordenadas_elem(tab, pos).
    Determina quais as coordenadas de cada posição. Se a distância entre pos e \
    outra posição for menor ou igual a 1, essa posição é adjacente.

    >>>obtem_posicoes_adjacentes(((1,0,0,1),(-1,1,0,1),(-1,0,0,-1)), 1)
    (2,5,6)

    {tuple, int} --> {tuple}
    """
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not\
        eh_posicao_valida(tab, pos):
        raise ValueError("obtem_posicoes_adjacentes: argumentos invalidos")

    coord = coordenadas(tab)
    pos = coordenada_elem(tab, pos)
    x1, y1 = pos[0], pos[1]
    adjacentes = ()

    for idx in coord:
        for elem in idx:
            x2, y2 = elem[0], elem[1]
            if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1 and (x1, y1) != (x2, y2):
                n = (x2 - 1) * len(tab[0]) + y2
                adjacentes = adjacentes + (n,)

    return tuple(sorted(adjacentes))

#2.2.6:
def ordena_posicoes_tabuleiro(tab, tup):
    """
    Função que recebe um tabuleiro e um tuplo e devolve o tuplo das posições \
    com a ordem ascendente à posição central.
    Utiliza as funções auxiliares eh_tabuleiro(tab) e coordenada_elem(tab, pos).
    Determina as coordenadas da posição central e de todas as coordenadas do \
    tabuleiro, para calcular a distância entre as posições.
    Adiciona as posições a uma lista pela ordem pretendida. Faz return do tuplo\
    correspondente.

    >>> tab = ((1,0,0,1),(-1,1,0,1),(-1,0,0,-1))
    >>> ordena_posicoes_tabuleiro(tab, tuple(range(1,13)))
    (7,2,3,4,6,8,10,11,12,1,5,9)

    {tuple, tuple} --> {tuple}
    """
    if not eh_tabuleiro(tab) or type(tup) != tuple:
        raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")

    for i in tup:
        if not eh_posicao(i) or not eh_posicao_valida(tab, i):
            raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")

    m, n = len(tab), len(tab[0])
    pos_central = (m // 2) * n + n // 2 + 1
    ordem_centro, distancias = [], []
    coord_central = coordenada_elem(tab, pos_central)
    x1, y1 = coord_central

    for pos in tup:
        coord = coordenada_elem(tab, pos)
        x2, y2 = coord
        distancia = max(abs(x1 - x2), abs(y1 - y2))  # fórmula da distância
        distancias.append((distancia, pos))

    distancias.sort()  # ordenar da ordem pretendiada
    # adiciona todas as pos já ordenadas em função da distância ao centro
    ordem_centro.extend(pos for valor, pos in distancias)

    return tuple(ordem_centro)

#2.2.7:
def marca_posicao(tab, pos, jog):
    """
    Função que substitui uma posição livre (representada por 0) por 1 para o \
    jogador de pedras pretas e -1 para o jogador das pedras brancas.
    Utiliza as funções auxiliares eh_tabuleiro(tab), transforma_tuplo(tab), \
    eh_posicao(pos), eh_posicao_valida(tab, pos) e eh_posicao_livre(tab, pos).
    Transforma o tuplo inicial em uma lista para conseguir alterar o valor da \
    posição escolhida e volta a torná-la num tuplo.

    >>> marca_posicao(((1,0,0,1),(-1,1,0,1),(-1,0,0,-1), 11, -1))
    ((1,0,0,1),(-1,1,0,1),(-1,0,-1,-1))

    {tuple, int, int} --> {tuple}
    """
    lista = list(transforma_tuplo(tab)) #obter apenas uma lista sem tuplos
    nova_lista= []

    if not eh_tabuleiro(tab) or type(jog) != int or jog not in (-1, 1)\
        or not eh_posicao(pos) or not eh_posicao_valida(tab, pos)\
            or not eh_posicao_livre(tab, pos):
        raise ValueError("marca_posicao: argumentos invalidos")

    lista[pos-1] = jog

    for idx in range(0, len(lista), len(tab[0])): 
        #voltar a criar tuplos dentro da lista do tamanho de len(tab[0])
        nova_lista.append(tuple(lista[idx:idx+len(tab[0])]))

    return tuple(nova_lista)

#2.2.8:
def verifica_k_linhas(tab, pos, jog, k):
    """
    Função que define se existe pelo menos uma linha que contenha pos com k ou \
    mais pedras consecutivas. Estas podem ter valor 1 para o jogador das pedras\
    pretas, ou -1 para o das brancas.
    Utiliza as funções auxiliares eh_tabuleiro(tab), obtem_valor(tab,pos),\
    obtem_coluna(tab, pos), obtem_linha(tab, pos), obtem_diagonais(tab, pos) e\
    eh_posicao(pos).
    Determina se existe alguma linha, coluna, diagonal ou antidiagonal que \
    contemple o pedido.

    >>> tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1))
    >>> verifica_k_linhas(tab, 4, 1, 2), verifica_k_linhas(tab, 12, 1, 2)
    (True, False) 

    {tup, int, int, int} --> {bool}
    """
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not\
        eh_posicao_valida(tab, pos) or type(k) != int or type(jog) != int\
            or jog not in (-1, 1) or k < 1:
        raise ValueError("verifica_k_linhas: argumentos invalidos")

    if obtem_valor(tab, pos) != jog:
        return False

    tuplo_linhas = (obtem_coluna(tab, pos), obtem_linha(tab, pos),\
                    obtem_diagonais(tab, pos)[0], obtem_diagonais(tab, pos)[1])

    for tuplo in tuplo_linhas:
        idx = tuplo.index(pos)

        contar1 = 1
        contar2 = -1

        for i in range(len(tuplo[idx:]) - 1):
            contar2 += 1
            if obtem_valor(tab, tuplo[idx]) == \
                obtem_valor(tab, tuplo[idx + 1 + contar2]):
                contar1 += 1

            else:
                break

        if contar1 >= k:
            return True

        contar2 = -1
        for i in range(len(tuplo[: idx + 1]) - 1):
            contar2 += 1
            if obtem_valor(tab, tuplo[idx]) == \
                obtem_valor(tab, tuplo[idx - 1 - contar2]):
                contar1 += 1

            else:
                break

        if contar1 >= k:
            return True

    return False

#2.3.1:
def eh_fim_jogo(tab, k):
    """
    Função que recebe um tabuleiro e determina se um jogo já terminou consoante\
    existam ou não k pedras seguidas ou já não existam mais posições livres\
    para jogar. True indica que terminou i False o contrário.
    Utiliza as funções auxiliares eh_tabuleiro(tab),obtem_posicoes_livres(tab),\
    obtem_posicoes_jogador(tab, pos) e verifica_k_linhas(tab, pos, jog, k).

    >>> tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1))
    >>> eh_fim_jogo(tab, 3)
    False

    {tuple, int} --> {bool}
    """
    if not eh_tabuleiro(tab) or type(k) != int or k < 1:
        raise ValueError("eh_fim_jogo: argumentos invalidos")

    if not obtem_posicoes_livres(tab):
        return True

    for jog in (-1, 1):
        for pos in obtem_posicoes_jogador(tab, jog):
            if verifica_k_linhas(tab, pos, jog, k):
                return True
            
    return False

#2.3.2:
def escolhe_posicao_manual(tab):  
    """
    Função que devolve ao jogador uma posição livre.
    Utiliza a função auxiliar eh_tabuleiro(tab) para validar o tabuleiro.
    Pede ao jogador uma posição. Se o seu valor for 0 retorna a posição, se não\
    continua a pedr posições até encontrar uma livre.

    >>> escolhe_posicao_manual((1,0,0,1),(-1,1,0,1), (-1,0,0,-1))
    Turno do jogador. Escolha uma posicao livre: 2
    2

    {tuple} --> {int}
    """
    if not eh_tabuleiro(tab):
        raise ValueError("escolhe_posicao_manual: argumento invalido")

    while True:
        pos = input("Turno do jogador. Escolha uma posicao livre: ")

        #fazer a verificação para poder fazer int(pos)
        if not pos:
            continue
        if not pos.isdigit():
            continue
        pos = int(pos)

        if not eh_posicao(pos) or not eh_posicao_valida(tab, pos)\
            or not eh_posicao_livre(tab, pos):
            continue

        return pos

#2.3.3:
def escolhe_posicao_auto(tab, jog, k, lvl):
    """
    Função que devolve uma posição consoante a estratégia escolhida.

    >>> tab = ((0,0,0),(0,1,0),(-1,0,1))
    >>> escolhe_posicao_auto(tab, -1, 3, 'facil')
    4    

    {tuple, int, int, string} --> {int}
    """
    if not eh_tabuleiro(tab) or type(jog) != int or jog not in (-1, 1)\
        or type(k) != int or k < 1 or type(lvl) != str or lvl not in\
            ("facil", "normal", "dificil"):
        raise ValueError("escolhe_posicao_auto: argumentos invalidos")
    
    def facil(tab, jog, k):
        """
        Função para a estratégia fácil.
        Se existir no tabuleiro pelo menos uma posição livre e adjacente a uma\
        pedra própria, jogar numa dessas posições; Se não, jogar numa posição\
        livre.

        >>> tab = ((0,0,0),(0,1,0),(-1,0,1))
        >>> escolhe_posicao_auto(tab, -1, 3, 'facil')
        4

        {tuple, int, int} --> {int}
        """
        adj_livres = []
        pos_livres = obtem_posicoes_livres(tab)

        for pos in pos_livres:
            adjacentes = obtem_posicoes_adjacentes(tab, pos)

            if any(obtem_valor(tab, adj) == jog for adj in adjacentes):
                adj_livres.append(pos)
        
        #se existirem várias adjacentes livres, ordenar em relação à 
        #distância ao centro
        if adj_livres:
            ordenacao = ordena_posicoes_tabuleiro(tab , tuple(adj_livres))
            return ordenacao[0] #devolver primeiro elemento
        
        #se não existirem adjacentes livres
        else:
            ordenacao = ordena_posicoes_tabuleiro(tab , tuple(pos_livres))
            return ordenacao[0] 

    def normal(tab, jog, k):
        """
        Função para a estratégia normal.
        Determinar o maior valor de L ≤ k tal que o próprio ou o adversário \
        podem conseguir colocar L peçcas consecutivas na próoxima jogada numa \
        linha vertical, horizontal ou diagonal que contenha essa jogada.

        >>> tab = ((0,0,0),(0,1,0),(-1,0,1))
        >>> escolhe_posicao_auto(tab, -1, 3, 'normal')
        1

        {tuple, int, int} --> {int}
        """
        pos_livres = obtem_posicoes_livres(tab)

        for L in range(k, 0, -1): 
            vantagens = []
            bloqueios = []

            #jogador pode ganhar numa jogada
            for pos in pos_livres:
                temp_tab = marca_posicao(tab, pos, jog)
                if verifica_k_linhas(temp_tab, pos, jog, L):
                    vantagens.append(pos)

            if vantagens:
                return ordena_posicoes_tabuleiro(tab, tuple(vantagens))[0]

            #jogador pode bloquear o adversário de ganhar
            for pos in pos_livres:
                temp_tab = marca_posicao(tab, pos, -jog)
                if verifica_k_linhas(temp_tab, pos, -jog, L):
                    bloqueios.append(pos)

            if bloqueios:
                return ordena_posicoes_tabuleiro(tab, tuple(bloqueios))[0]

    def dificil(tab, jog, k):
        pos_livres = obtem_posicoes_livres(tab)
        vantagens = []
        bloqueios = []
        
        def verifica_resultado(tab, jog, k):
            """
            Função auxiliar que devolve uma posição consoante dê para ganhar,
            empatar ou continuar a jogar.
            Usa como funções auxiliares marca_posicao(tab, pos, jog) e 
            verifica_resultado(tem_tab, pos).

            {tuple, int} --> {int}
            """
            jog_atual = -jog

            while not eh_fim_jogo(tab, k):
                pos_livres = obtem_posicoes_livres(tab)

                if not pos_livres:
                    break

                pos = pos_livres[0]
                tab = marca_posicao(tab, pos, jog_atual)

                jog_atual = -jog_atual

            if verifica_k_linhas(tab, pos, jog, k):
                return "VITORIA"
            elif verifica_k_linhas(tab, pos, -jog, k):
                return "DERROTA"
            else: 
                return "EMPATE"    

        #jogador pode ganhar numa jogada
        for pos in pos_livres:
            temp_tab = marca_posicao(tab, pos, jog)
            if verifica_k_linhas(temp_tab, pos, jog, k):
                vantagens.append(pos)

        if vantagens:
            return ordena_posicoes_tabuleiro(tab, tuple(vantagens))[0]

        #jogador pode bloquear o adversário de ganhar
        for pos in pos_livres:
            temp_tab = marca_posicao(tab, pos, -jog)
            if verifica_k_linhas(temp_tab, pos, -jog, k):
                bloqueios.append(pos)

        if bloqueios:
            return ordena_posicoes_tabuleiro(tab, tuple(bloqueios))[0]

        verifica_resultado_ganhar = []
        verifica_resultado_empate = []

        for pos in pos_livres:
            temp_tab = marca_posicao(tab, pos, jog)
            res = verifica_resultado(temp_tab, jog, k)

            if res == "EMPATE":
                verifica_resultado_empate.append(pos) #posições em que o jog ganha

            if res == "VITORIA":
                verifica_resultado_ganhar.append(pos) #posições onde jogo empata
        
        if verifica_resultado_ganhar:
            return ordena_posicoes_tabuleiro(tab, tuple(verifica_resultado_ganhar))[0]
        
        elif verifica_resultado_empate:
            return ordena_posicoes_tabuleiro(tab, tuple(verifica_resultado_empate))[0]
        
        return pos_livres[0]
   
    if lvl == "facil":
        return facil(tab, jog, k)

    if lvl == "normal":
        return normal(tab, jog, k)
    
    if lvl == "dificil":
        return dificil(tab, jog, k)

#2.3.4:
def jogo_mnk(cfg, jog, lvl):
    """
    Função que permite jogar o jogo mnk. 
    Utiliza as funções auxiliares tabuleiro_para_str(tab), marca_posicao(tab),\
    escolhe_posicao_manual(tab), escolhe_posicao_auto(tab, -jog, k, lvl),\
    verifica_k_linhas(tab, pos, quem_joga, k) e eh_fim_jogo(tab, k).
    Analisa os cenários consoante as estratégias e declara vitória, derrota ou\
    empate.
    
    {tuple, int, str} --> {str}
    """
    if type(cfg) != tuple or len(cfg) != 3 or any(type(i) != int for i in cfg)\
        or any(i <= 0 for i in cfg) or type(jog) != int or jog not in (-1, 1)\
            or type(lvl) != str or lvl not in ("facil", "normal", "dificil"):
        raise ValueError("jogo_mnk: argumentos invalidos")

    m, n, k = cfg
    tab = tuple((0,) * n for idx in range(m))  # criar um tabuleiro

    print("Bem-vindo ao JOGO MNK.")

    if jog == 1:
        simbolo = 'X'
    
    else:
        simbolo = 'O'

    print(f"O jogador joga com {simbolo}.")

    quem_joga = 1
    resultado = 0

    while 1:
        print(tabuleiro_para_str(tab))

        if quem_joga == jog:
            pos = escolhe_posicao_manual(tab) #para o jogador

        else:
            print(f"Turno do computador ({lvl}):")
            pos = escolhe_posicao_auto(tab, -jog, k, lvl) #para o computador

        tab = marca_posicao(tab, pos, quem_joga)

        if verifica_k_linhas(tab, pos, quem_joga, k):
            resultado = quem_joga
            break

        elif eh_fim_jogo(tab, k):
            break

        quem_joga = -quem_joga #inverte quem joga

    print(tabuleiro_para_str(tab))

    if resultado == 0:
        print("EMPATE")
    elif resultado == jog:
        print("VITORIA")
    else:
        print("DERROTA")

    return resultado