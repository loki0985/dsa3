class Solution {
public:
    int minMoves(vector<string>& classroom, int energy) {
        int m = classroom.size();
        int n = classroom[0].size();

        int sr = 0, sc = 0;
        vector<vector<int>> id(m, vector<int>(n, -1));

        int L = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (classroom[i][j] == 'S') {
                    sr = i;
                    sc = j;
                }
                else if (classroom[i][j] == 'L') {
                    id[i][j] = L++;
                }
            }
        }

        if (L == 0)
            return 0;

        int fullMask = (1 << L) - 1;

        /*
            best[r][c][mask] =
            maximum energy with which we have reached
            (r,c,mask) at the current/best distance.
        */
        int states = m * n * (1 << L);

        vector<int> best(states, -1);

        auto getId = [&](int r, int c, int mask) {
            return (r * n + c) * (1 << L) + mask;
        };

        struct State {
            int r, c;
            int mask;
            int energy;
        };

        queue<State> q;

        best[getId(sr, sc, 0)] = energy;
        q.push({sr, sc, 0, energy});

        int dr[4] = {1, -1, 0, 0};
        int dc[4] = {0, 0, 1, -1};

        int dist = 0;

        while (!q.empty()) {
            int sz = q.size();

            while (sz--) {
                State cur = q.front();
                q.pop();

                int r = cur.r;
                int c = cur.c;
                int mask = cur.mask;
                int e = cur.energy;

                // This state may have become dominated
                if (e < best[getId(r, c, mask)])
                    continue;

                if (mask == fullMask)
                    return dist;

                // If no energy, cannot make another move.
                if (e == 0)
                    continue;

                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    if (nr < 0 || nr >= m ||
                        nc < 0 || nc >= n)
                        continue;

                    if (classroom[nr][nc] == 'X')
                        continue;

                    int ne = e - 1;
                    int nmask = mask;

                    // Collect litter
                    if (id[nr][nc] != -1) {
                        nmask |= (1 << id[nr][nc]);
                    }

                    // Reset energy
                    if (classroom[nr][nc] == 'R') {
                        ne = energy;
                    }

                    int idx = getId(nr, nc, nmask);

                    /*
                        If we've already reached this exact
                        position + mask with at least as much
                        energy, this new state is useless.
                    */
                    if (ne <= best[idx])
                        continue;

                    best[idx] = ne;

                    q.push({
                        nr,
                        nc,
                        nmask,
                        ne
                    });
                }
            }

            dist++;
        }

        return -1;
    }
};