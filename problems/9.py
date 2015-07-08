
# A Pythagorean triplet is a set of three natural numbers,
# a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# 200 375 425
# 31875000


def main():
    for i in list(range(1, 500)):
        for j in list(range(1, 500)):
            for k in list(range(1, 500)):
                if i ** 2 + j ** 2 == k ** 2 and i + j + k == 1000:
                    print(i, j, k)
main()
