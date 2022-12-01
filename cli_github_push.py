
import os
from colorama import init, Fore, Back
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, required=True)
parser.add_argument("--repo", type=str, required=True)
# parser.add_argument("--commit", type=str, required=False)
args = parser.parse_args()

init()

print("\n")
print(Fore.GREEN + "Pushing Files to Github Repo.." + Fore.RESET)
print(Fore.LIGHTCYAN_EX + "\n")

os.chdir(args.file)

os.system("git add .")
os.system("git init")
os.system(f"git remote add origin https://github.com/BananaApache/{args.repo}.git")
os.system("git commit -m 'Commit'")
# if args.commit != None:
#     os.system(f"git commit -m '{args.commit}'")
# else:
#     os.system("git commit -m 'Commit'")
os.system("git push -f origin master")

print("\n")
print(Fore.GREEN + "Finished Program")
print("\n")
