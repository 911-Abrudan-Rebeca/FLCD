from Scanner import Scanner


def run(file_path):
    scanner = Scanner(file_path)
    scanner.scan()
    pif = scanner.get_pif()

    with open(file_path+".pif.txt", 'w') as file:
        for element in pif:
            file.write(str(element) + '\n')

    constST = scanner.get_constantST().toString()
    idST = scanner.get_identifiersST().toString()
    with open(file_path + ".tables.txt", 'w') as file:
        file.write("Constants table:" + '\n')
    with open(file_path+".tables.txt", 'a') as file:
        for element in constST:
            file.write(str(element) + '\n')
    with open(file_path + ".tables.txt", 'a') as file:
        file.write('\n' + "Identifiers table:" + '\n')
    with open(file_path+".tables.txt", 'a') as file:
        for element in idST:
            file.write(str(element) + '\n')


if __name__ == "__main__":
    print("p2:")
    run("p2.txt")
