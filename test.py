list = ['[0]: hello', '[1]: there']

def f(list):
    for email in list:
        email.replace(email[1], str(int(email[1]) + 1))

print(list)

print(f(list))