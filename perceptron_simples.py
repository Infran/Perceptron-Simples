from ast import Return, While
from lib2to3.pytree import convert
from tracemalloc import start
from xmlrpc.client import Boolean, boolean


bias:int = 1;

counter = 0;

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

parametros_iniciais = [6, -4, 1];
parametros_atuais = parametros_iniciais;
parametros_antigos = parametros_atuais;

taxa_aprendizado = 0.9;
objetivos = [0, 1, 0, 0, 1, 1, 1, 0, 0];

S = [0, 0, 0];

tipo_erro = [];
continua:Boolean = True;
while continua == True:
    counter += 1;
    def soma(i):
        return parametros_atuais[0] + parametros_atuais[1] * v[i][1] + parametros_atuais[2] * v[i][2];

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
            print(resultados);
            print(resultados_testados);
            return False;
        else:
            parametros_antigos = parametros_atuais;
            for i in range(len(divergencias)):
                if (tipo_erro[i] == "+"):
                    S[0] += divergencias[i][0];
                    S[1] += divergencias[i][1];
                    S[2] += divergencias[i][2];
                else:
                    S[0] -= divergencias[i][0];
                    S[1] -= divergencias[i][1];
                    S[2] -= divergencias[i][2];
            parametros_atuais[0] = parametros_antigos[0] + taxa_aprendizado * S[0];
            parametros_atuais[1] = parametros_antigos[1] + taxa_aprendizado * S[1];
            parametros_atuais[2] = parametros_antigos[2] + taxa_aprendizado * S[2];
            print("Parametros atuais: " + str(parametros_atuais));
            print("Parametros antigos: " + str(parametros_antigos));
            print("S: " + str(S));
            print("Tipo de erro: " + str(tipo_erro));
            print("Divergências: " + str(divergencias));
            print("\n");
            S.clear();
            tipo_erro.clear();
            return True;
    continua = começaAprendizado();

print(counter);
