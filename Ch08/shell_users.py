
shell_users = {}

with open("./Ch08/passwd") as f:
    for line in f:
        _, _, _, _, _, _, shell = line.rstrip("\r\n").split(":")
        if shell not in shell_users:
            shell_users[shell] = 0
        shell_users[shell] += 1

for s in shell_users.items():
    shell, count = s
    if len(shell) > 0:
        print(f"{shell:15s} {count}")