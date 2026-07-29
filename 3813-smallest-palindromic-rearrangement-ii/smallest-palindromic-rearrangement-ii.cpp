class Solution {
public:
    const long long LIM = 1000000LL + 5;

    long long mulCap(long long a, long long b) {
        if (a == 0 || b == 0) return 0;
        if (a > LIM / b) return LIM;
        return min(LIM, a * b);
    }

    long long comb(int n, int r) {
        if (r < 0 || r > n) return 0;
        r = min(r, n - r);
        long long ans = 1;
        for (int i = 1; i <= r; i++) {
            ans = ans * (n - r + i) / i;
            if (ans >= LIM) return LIM;
        }
        return min(ans, LIM);
    }

    long long countWays(vector<int>& cnt) {
        int total = 0;
        for (int x : cnt) total += x;

        long long res = 1;
        int rem = total;

        for (int c : cnt) {
            if (c == 0) continue;
            res = mulCap(res, comb(rem, c));
            rem -= c;
            if (res >= LIM) return LIM;
        }
        return res;
    }

    string smallestPalindrome(string s, int k) {
        vector<int> freq(26, 0);
        for (char c : s) freq[c - 'a']++;

        vector<int> half(26);
        string mid = "";

        for (int i = 0; i < 26; i++) {
            half[i] = freq[i] / 2;
            if (freq[i] % 2)
                mid.push_back(char('a' + i));
        }

        if (countWays(half) < k)
            return "";

        string left = "";
        int len = 0;
        for (int x : half) len += x;

        for (int pos = 0; pos < len; pos++) {
            for (int c = 0; c < 26; c++) {
                if (half[c] == 0) continue;

                half[c]--;
                long long ways = countWays(half);

                if (ways >= k) {
                    left.push_back(char('a' + c));
                    break;
                } else {
                    k -= ways;
                    half[c]++;
                }
            }
        }

        string right = left;
        reverse(right.begin(), right.end());

        return left + mid + right;
    }
};