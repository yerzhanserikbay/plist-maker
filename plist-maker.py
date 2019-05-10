file_name = '/Users/ys/Documents/BioSDK.xlsx'
sheet = 'Sheet 2'
plist_header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">"

import pandas as pd

image_name_numpy = pd.read_excel(io=file_name, usecols=[0], skiprows=1).to_numpy()

id_numpy = pd.read_excel(io=file_name, usecols=[1], skiprows=1).to_numpy()

model_name_numpy = pd.read_excel(io=file_name, usecols=[2], skiprows=1).to_numpy()

"\n<plist version=\"1.0\">"
dict = "\n</dict>"
key = "<key>"

"\n</plist>"


def key_wrapper(key, space):
    return "\n{}<key>".format(space) + key + "</key>"

def string_wrapper(string, space):
    return "\n{}<string>".format(space) + string + "</string>"

def dict_wrapper(keys_vals, space):
    return "{}<dict>".format(space) + keys_vals + "\n</dict>"

def key_val_wrapper(key, key_name, val, val_name, space, back):
    return "\n{}<{}>".format(space, key_name) + key + "</{}>".format(key_name) + "\n" + "{}<{}>".format(space, val_name) + val + "{}</{}>".format(back, val_name)

def plist_wrapper(dict):
    return plist_header + "\n<plist version=\"1.0\">\n{}\n</plist>".format(dict)

def make_dict(keyObject, valObject):
    i = 0
    dict = ""
    while i < len(image_name_numpy):
        key = keyObject[i][0]
        val = valObject[i][0]

        val.replace('&', '&amp;')

        dict += key_val_wrapper(key, "key", val, "string", "    ", "")
        i += 1

    return dict


inner_dict = key_val_wrapper("Models-ID", "key", make_dict(image_name_numpy, id_numpy), "dict", "  ", "\n  ")

inner_dict2 = key_val_wrapper("Models-Names", "key", make_dict(image_name_numpy, model_name_numpy), "dict", "  ", "\n  ")

main_dict = dict_wrapper(inner_dict + inner_dict2, "")

print(plist_wrapper(main_dict))







