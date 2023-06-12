import os
import subprocess as sp


def parse_data(data_pair):
    pairing = {}
    for pair in data_pair:
        if pair[0] not in pairing.keys():
            pairing[pair[0]] = []
        pairing[pair[0]].append(pair[1])
    return pairing

def pair_files_by_type(dir, types):
    files = [f"{dir}/{file}" for file in os.listdir(dir) if os.path.isfile(f"{dir}/{file}")]
    folders = [f"{dir}/{folder}" for folder in types.keys() if not os.path.exists(f"{dir}/{folder}")]
    if folders:
        sp.run(["mkdir", *folders])
    for type, extensions in types.items():
        for file in files:
            extension = os.path.splitext(file)[1]
            if extension in extensions:
                sp.run(["mv", file, f"{dir}/{type}/{os.path.basename(file)}"])


