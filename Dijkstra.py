def sssp_dijkstra(self, source):

    total_vertex = len(self.vertex)
    Q = np.array(self.vertex)

    dist = np.zeros(total_vertex)
    dist.fill(np.inf)

    dist[self.vertex == source] = 0

    while len(Q) != 0:

        min = np.inf
        u = 0
        for q in Q:
            if dist[self.vertex == q] <= min:
                min = dist[self.vertex == q]
                u = q

        Q = np.delete(Q, np.argwhere(Q == u))

        for v in self.target[self.source == u]:
            alt = dist[self.vertex == u] + self.get_weight(u, v)
            index_v = self.vertex == v
            if alt < dist[index_v]:
                dist[index_v] = alt
