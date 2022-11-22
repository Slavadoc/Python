import export_data


def delete(id):
    list = export_data.export_data()
    list.pop(int(id) - 1)
    print(list)

# def import_data(data, sep=None):
#     d = open('phone.csv', 'w')
    with open('phone.csv', 'w') as file:
        #     # if sep == None:
        #     #     for i in data:
        #     #         file.write(f"{i}\n")
        #     #     file.write(f"\n")
        #     # else:
        for i in list:
            file.write(','.join(i))
            file.write(f"\n")

    # id = 1
    # if s == '':
    #     id = 1
    # else:
    #     for i in s:
    #         if i == '\n':
    #             id += 1
    # d.close()
