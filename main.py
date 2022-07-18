import os.path


def getFileName(checkexist=False) -> str:
    isExit = False
    fn = ''
    while not isExit:
        print('Enter file name:')
        fn = input('> ')
        if not checkexist:
            return fn
        if os.path.isfile(fn):
            isExit = True
        else:
            print(f'File "{fn}" is not exist')
    return fn


if __name__ == '__main__':
    print('Prefix tree.')
    isExit = False
    while not isExit:
        print('Choose:')
        print('1. Load data from txt file')
        print('2. Save data to txt file')
        print('3. Load tata from binary file')
        print('4. Save data to binary file')
        print('0. Exit')
        choose = input('> ')
        if choose not in ['1', '2', '3', '4', '0']:
            print('Uncorrected choice')
            continue
        if choose == '0':
            isExit = True
            continue
        fn = getFileName(True)
