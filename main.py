from os import path, listdir, makedirs, remove

bad_words = ['Balance = 0', 'Solde : 0']

if not path.exists("Removed"):
        makedirs("Removed")
with open('To_remove/hits.txt') as oldfile, open('Removed/pointprize.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)
print(f"""
______                                  _   _ 
| ___ \                                | | | |
| |_/ /___ _ __ ___   _____   _____  __| | | |
|    // _ \ '_ ` _ \ / _ \ \ / / _ \/ _` | | |
| |\ \  __/ | | | | | (_) \ V /  __/ (_| | |_|
\_| \_\___|_| |_| |_|\___/ \_/ \___|\__,_| (_)
                                              
""")
