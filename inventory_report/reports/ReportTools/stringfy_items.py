

def stringfy_items(dict: dict):
    keys = dict.keys()
    string_list = []

    for key in keys:
        value = dict[f"{key}"]
        string_list.append(f"- {key}: {value}\n")
    return "".join(string_list)
