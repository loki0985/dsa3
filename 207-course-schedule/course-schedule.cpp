class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        
        vector<vector<int>> graph(numCourses);
        vector<int> indegree(numCourses, 0);

        // Build graph
        for (auto &p : prerequisites) {
            int course = p[0];
            int pre = p[1];

            graph[pre].push_back(course);
            indegree[course]++;
        }

        // Courses with no prerequisites
        queue<int> q;

        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0)
                q.push(i);
        }

        int completed = 0;

        // BFS Topological Sort
        while (!q.empty()) {
            int curr = q.front();
            q.pop();

            completed++;

            for (int next : graph[curr]) {
                indegree[next]--;

                if (indegree[next] == 0)
                    q.push(next);
            }
        }

        // If all courses are completed, no cycle exists
        return completed == numCourses;
    }
};