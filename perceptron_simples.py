bias = 1;

contador = 0;

v = [
    [bias , 1, 1],
    [bias , 1, 3],
    [bias , 1.5, 2],
    [bias , 2, 1.5],
    [bias , 2, 3.5],
    [bias , 3.5, 3],
    [bias , 2.5, 4],
    [bias , 3, 1],
    [bias , 3.5, 1.5]
];

w = [6, -4, 1];

taxa_aprendizado = 0.9;
objetivos = [0, 1, 0, 0, 1, 1, 1, 0, 0];

continua = True;
while continua == True:
    contador += 1;
    tipo_erro = [];

    def soma(i):
        return w[0] + w[1] * v[i][1] + w[2] * v[i][2];

    resultados = [soma(i)for i in range(len(v))];

    def testaResultado(i):
        if (resultados[i] >= 0):
            return 1;
        else:
            return 0;

    resultados_testados = [testaResultado(i)for i in range(len(v))];

    def verificaEficacia(i):
        return (objetivos[i] == resultados_testados[i]);


    def analisaResultados(i):
        if (verificaEficacia(i) == False):
            if (objetivos[i] > resultados_testados[i]):
                tipo_erro.append("+");
            else:
                tipo_erro.append("-");
            return i;

    divergencias = [v[analisaResultados(i)]for i in range(len(v)) if (verificaEficacia(i) == False)];

    def começaAprendizado():
        S = [0, 0, 0];
        if (len(divergencias) == 0):
            print("Não há mais divergências");
            return False;
        else:
            for i in range(len(divergencias)):
                if (tipo_erro[i] == "+"):
                    S[0] += divergencias[i][0];
                    S[1] += divergencias[i][1];
                    S[2] += divergencias[i][2];
                else:
                    S[0] -= divergencias[i][0];
                    S[1] -= divergencias[i][1];
                    S[2] -= divergencias[i][2];
            w[0] = w[0] + taxa_aprendizado * S[0];
            w[1] = w[1] + taxa_aprendizado * S[1];
            w[2] = w[2] + taxa_aprendizado * S[2];
            print("S: " + str(S));
            print("W: " + str(w));
            print("Tipo de erro: " + str(tipo_erro));
            print("Divergências: " + str(divergencias));
            print("\n");
            return True;
    continua = começaAprendizado();

print("Numero de processos: " + str(contador));