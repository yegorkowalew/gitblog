import subprocess

def to_git():
    process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return output

if __name__ == '__main__':
    print(to_git())