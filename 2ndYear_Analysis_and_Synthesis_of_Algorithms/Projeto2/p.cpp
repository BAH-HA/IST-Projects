#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

typedef struct {
    int u, v, w;
} edge;

typedef struct {
    int n, e;
    vector<edge> edges;
} graph;

graph createGraph() {
    int n, e;
    scanf("%d%d", &n, &e);
    graph g = {n, e, vector<edge>(e)};
    for (int i = 0; i < e; i++) {
        scanf("%d %d %d", &g.edges[i].u, &g.edges[i].v, &g.edges[i].w);
    }
    return g;
}

int maxKruskal(graph g) {
    // ordenar arestas por peso decrescente
    sort(g.edges.begin(), g.edges.end(), [](edge a, edge b) {
        return a.w > b.w;
    });
    int *parent = new int[g.n];
    for (int i = 0; i < g.n; i++) { // inicializa o vetor de pais
        parent[i] = i;
    }
    int sum = 0; 
    for (int i = 0; i < g.e; i++) {
        int u = g.edges[i].u;
        int v = g.edges[i].v;
        int w = g.edges[i].w;
        while (u != parent[u]) { // procura o pai de u
            u = parent[u];
        }
        while (v != parent[v]) { // procura o pai de v
            v = parent[v];
        }
        if (u != v) {           // se forem diferentes, faz a união
            parent[u] = v; 
            sum += w;           // soma o peso do caminho
        }
    }
    delete[] parent; 
    return sum;
}

int main() {
    graph g = createGraph();
    cout << maxKruskal(g) << endl;
}

