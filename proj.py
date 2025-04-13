import sys
from pulp import *


def readInput():
    data = sys.stdin.read().strip().split("\n")
    n, m, t = map(int, data[0].split())

    factories = []
    for i in range(1, n + 1):
        factoryId, idCountry, factory_stock = map(int, data[i].split())
        factories.append((factoryId, idCountry, factory_stock))

    countries = []
    for i in range(n + 1, n + 1 + m):
        CountryId, exportLimit, minToys = map(int, data[i].split())
        countries.append((CountryId, exportLimit, minToys))

    children_requests = []
    for i in range(n + 1 + m, n + 1 + m + t):
        child_data = list(map(int, data[i].split()))
        idChild = child_data[0]
        country_id = child_data[1]
        requested_factories = child_data[2:]
        children_requests.append((idChild, country_id, requested_factories))

    return n, m, t, factories, countries, children_requests


def solveProblem(n, m, t, factories, countries, children_requests):
    prob = LpProblem("toyProblem", LpMaximize)

    # Criar pares válidos e variáveis
    valid_pairs = set()
    for idChild, _, requested_factories in children_requests:
        for factoryId in requested_factories:
            valid_pairs.add((idChild, factoryId))

    data_dict = {pair: LpVariable(f"y_{pair[0]}_{pair[1]}", lowBound=0, cat="Integer") for pair in valid_pairs}

    # Função objetivo
    prob += lpSum(data_dict.values())

    # Restrição: máximo de 1 brinquedo por criança
    for idChild, _, requested_factories in children_requests:
        prob += lpSum(data_dict[(idChild, factoryId)]
                      for factoryId in requested_factories if (idChild, factoryId) in valid_pairs) <= 1

    # Restrição: estoque das fábricas
    for factoryId, _, factory_stock in factories:
        prob += lpSum(data_dict[(idChild, factoryId)]
                      for idChild, factoryId in valid_pairs if factoryId == factoryId) <= factory_stock

    # Criar lista de fábricas por país
    factories_by_country = [[] for _ in range(m + 1)]
    for factoryId, factoryCountry, _ in factories:
        factories_by_country[factoryCountry].append(factoryId)

    # Restrição: limite de exportação e brinquedos mínimos
    for idCountry, exportLimit, minToys in countries:
        if exportLimit != 0:
            prob += lpSum(data_dict[(idChild, factoryId)]
                          for factoryId in factories_by_country[idCountry]
                          for idChild, _, _ in children_requests
                          if (idChild, factoryId) in valid_pairs) <= exportLimit

        if minToys != 0:
            prob += lpSum(data_dict[(idChild, factoryId)]
                          for idChild, childCountry, requested_factories in children_requests
                          if childCountry == idCountry
                          for factoryId in requested_factories if (idChild, factoryId) in valid_pairs) >= minToys

    # Resolver com GLPK
    prob.solve( GLPK(msg=0) )

    if prob.status != 1:
        print(-1)
        return

    result = prob.objective.value()
    print(int(result))


def main():
    n, m, t, factories, countries, children_requests = readInput()
    solveProblem(n, m, t, factories, countries, children_requests)


if __name__ == "__main__":
    main()
