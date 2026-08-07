class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Required powers of 2, 3, 5, 7
        req = []
        for p in (2, 3, 5, 7):
            cnt = 0
            while t % p == 0:
                t //= p
                cnt += 1
            req.append(cnt)

        # If t has another prime factor, impossible.
        if t != 1:
            return "-1"

        a, b, c, d = req

        # Prime-factor contribution of digits 1..9
        contrib = [
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        ]

        # Dimensions for flattened DP.
        B = b + 1
        C = c + 1
        D = d + 1

        def idx(x, y, z, w):
            return ((x * B + y) * C + z) * D + w

        total_states = (a + 1) * B * C * D
        INF = 10**9

        # dp[state] = minimum number of digits needed
        # to provide at least the required prime factors.
        dp = [INF] * total_states
        dp[0] = 0

        for x in range(a + 1):
            for y in range(b + 1):
                for z in range(c + 1):
                    for w in range(d + 1):
                        if x == y == z == w == 0:
                            continue

                        cur = INF

                        for digit in range(2, 10):
                            dx, dy, dz, dw = contrib[digit - 1]

                            px = max(0, x - dx)
                            py = max(0, y - dy)
                            pz = max(0, z - dz)
                            pw = max(0, w - dw)

                            prev = dp[idx(px, py, pz, pw)]
                            if prev != INF:
                                cur = min(cur, prev + 1)

                        dp[idx(x, y, z, w)] = cur

        def needed(r):
            return dp[idx(*r)]

        # Check whether a given prefix can be completed
        # with exactly 'slots' remaining digits.
        def can_complete(r, slots):
            return needed(r) <= slots

        # Return the lexicographically smallest string of exactly
        # 'length' digits satisfying the remaining requirements.
        def build_min(r, length):
            ans = []

            for pos in range(length):
                remaining = length - pos - 1

                for digit in range(1, 10):
                    dx, dy, dz, dw = contrib[digit - 1]

                    nr = (
                        max(0, r[0] - dx),
                        max(0, r[1] - dy),
                        max(0, r[2] - dz),
                        max(0, r[3] - dw)
                    )

                    if can_complete(nr, remaining):
                        ans.append(str(digit))
                        r = nr
                        break

            return ''.join(ans)

        n = len(num)

        # If num itself is zero-free, check whether its digit product
        # is divisible by t.
        current = [a, b, c, d]
        zero_free = True

        for ch in num:
            if ch == '0':
                zero_free = False
                break

            dx, dy, dz, dw = contrib[int(ch) - 1]
            current[0] = max(0, current[0] - dx)
            current[1] = max(0, current[1] - dy)
            current[2] = max(0, current[2] - dz)
            current[3] = max(0, current[3] - dw)

        if zero_free and current == [0, 0, 0, 0]:
            return num

        # Find the smallest number of the SAME length that is > num.
        #
        # We want to change the rightmost possible position because
        # changing a later digit produces the smallest number.
        remaining = [a, b, c, d]
        best_pos = -1
        best_digit = -1
        best_req = None

        prefix_valid = True

        for i in range(n):
            if not prefix_valid:
                break

            cur_digit = int(num[i])

            # Try making this position larger.
            for digit in range(max(1, cur_digit + 1), 10):
                dx, dy, dz, dw = contrib[digit - 1]

                nr = (
                    max(0, remaining[0] - dx),
                    max(0, remaining[1] - dy),
                    max(0, remaining[2] - dz),
                    max(0, remaining[3] - dw)
                )

                if can_complete(nr, n - i - 1):
                    best_pos = i
                    best_digit = digit
                    best_req = nr
                    break

            # The equal prefix must itself be zero-free.
            if cur_digit == 0:
                prefix_valid = False
                break

            dx, dy, dz, dw = contrib[cur_digit - 1]

            remaining = [
                max(0, remaining[0] - dx),
                max(0, remaining[1] - dy),
                max(0, remaining[2] - dz),
                max(0, remaining[3] - dw)
            ]

        if best_pos != -1:
            prefix = num[:best_pos]
            suffix = build_min(best_req, n - best_pos - 1)
            return prefix + str(best_digit) + suffix

        # No solution with the same length.
        # The next possible length must be at least n + 1 and
        # at least the minimum number of digits required.
        min_digits = needed((a, b, c, d))

        if min_digits == INF:
            return "-1"

        length = max(n + 1, min_digits)

        return build_min((a, b, c, d), length)