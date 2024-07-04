import sys
input = sys.stdin.readline

n, m = map(int, input().split())

site_info = list()
password_info = list()

for _ in range(n):
    site, password = map(str, input().split())
    site_info.append(site)
    password_info.append(password)

for _ in range(m):
    site = input().rstrip()
    print(password_info[site_info.index(site)])
