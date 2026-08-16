class Solution {
public:
    bool stoneGameIX(vector<int>& stones) {
        int cnt[3] = {0, 0, 0};

        for (int x : stones) {
            cnt[x % 3]++;
        }

        // If there are no remainder-1 and no remainder-2 stones,
        // Alice cannot make a move that makes the sum divisible by 3.
        // Bob wins after all stones are removed.
        if (cnt[1] == 0 && cnt[2] == 0)
            return false;

        // If cnt[0] is even, Alice wins when both types of
        // non-zero remainders exist.
        if (cnt[0] % 2 == 0) {
            return cnt[1] > 0 && cnt[2] > 0;
        }

        // If cnt[0] is odd, Alice can win if one type has
        // at least 3 more stones than the other.
        return abs(cnt[1] - cnt[2]) > 2;
    }
};