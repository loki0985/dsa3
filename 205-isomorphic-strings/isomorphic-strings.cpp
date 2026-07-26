class Solution {
public:
    bool isIsomorphic(string s, string t) {
        vector<int> mp1(256, -1);
        vector<int> mp2(256, -1);

        for (int i = 0; i < s.size(); i++) {
            char a = s[i];
            char b = t[i];

            if (mp1[a] != -1 && mp1[a] != b)
                return false;

            if (mp2[b] != -1 && mp2[b] != a)
                return false;

            mp1[a] = b;
            mp2[b] = a;
        }

        return true;
    }
};