

def convert_list_lowercase(list):
    for i in range(len(list)):
        list[i] = list[i].lower()
    return list

def list_substring(list, substring):
    return [string for string in list if substring in string]
