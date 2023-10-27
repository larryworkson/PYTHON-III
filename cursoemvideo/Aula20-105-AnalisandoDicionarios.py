def notas(*n, sit=False):
    """
    ---> função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    result = dict()
    result['Notas'] = n
    result['Total'] = len(result['Notas'])
    result['Maior'] = max(result['Notas'])
    result['Menor'] = min(result['Notas'])
    result['Média'] = sum(result['Notas']) / result['Total']
    if sit:
        if result['Média'] >= 7:
            result['Situação'] = 'Boa'
        elif result['Média'] >= 5:
            result['Situação'] = 'Razoável'
        else:
            result['Situação'] = 'Ruim'
    return result

resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)