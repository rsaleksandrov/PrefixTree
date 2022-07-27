import os.path
import prefixtree


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


def checkWords(prefTree):
    print('Enter word to check (enter empty word to exit)')
    isStop = False
    while not isStop:
        word = input('> ')
        if len(word) == 0:
            isStop = True
            continue
        word = word.lower()
        # corr = prefTree.checkWord(word, True)
        # pcorr = prefTree.checkWord(word, False)
        corr, pcorr = prefTree.checkWord(word)

        if not corr and not pcorr:
            print('UNCORRECTED')
        elif corr:
            print('CORRECT')
        else:
            print('PARTIALLY CORRECT')


if __name__ == '__main__':
    print('Prefix tree.')
    isExit = False
    pt = prefixtree.PrefixTree()
    while not isExit:
        print('Choose:')
        print('1. Load data from txt file')
        print('2. Save data to txt file')
        print('3. Load tata from binary file')
        print('4. Save data to binary file')
        print('5. Check word')
        print('0. Exit')
        choose = input('> ')
        if choose not in ['1', '2', '3', '4', '5', '0']:
            print('Uncorrected choice')
            continue
        if choose == '0':
            isExit = True
            continue
        if choose in ['1', '2', '3', '4']:
            fn = getFileName((True if choose in ['1', '3'] else False))
        if choose == '1':
            pt.loadFromTxt(fn)
            print(f'Load OK. Loaded {pt.wordCount} words in {pt.nodeCount} '
                  f'nodes')
        elif choose == '2':
            pt.saveToTxt(fn)
            print('Save OK.')
        elif choose == '3':
            pt.loadFromBin(fn)
            print(f'Load OK. Loaded {pt.wordCount} words in {pt.nodeCount} '
                  f'nodes')
        elif choose == '4':
            pt.saveToBin(fn)
            print('Save OK.')
        elif choose == '5':
            checkWords(pt)

print('END.')
