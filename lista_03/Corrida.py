while True:
    try:
        L = int(input())
        velocidades = list(map(int, input().split()))
        velocidade_maxima = max(velocidades)
        if velocidade_maxima < 10:
            print(1)
        elif velocidade_maxima < 20:
            print(2)
        else:
            print(3)
    except EOFError:
        break