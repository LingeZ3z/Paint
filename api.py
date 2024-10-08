import requests

url = "https://pbd.uwuwu.us.kg/paintboard"

def getboard():
    board = [["" for j in range(1000)] for i in range(600)]
    res = requests.get(url + "/board").text
    for i in range(1, 1800000, 3):
        x = (i // 3) % 600
        y = (i // 3) // 600
        color = hex(ord(res[i]))[2:].rjust(2,"0")\
              + hex(ord(res[i+1]))[2:].rjust(2,"0")\
              + hex(ord(res[i+2]))[2:].rjust(2,"0")
        board[x][y] = color
    return board

def paint(mx, my, mcolor, muid, mtoken):
    data = {'x': mx, 'y': my, 'color': mcolor, 'uid': muid,  'token': mtoken}
    x = requests.post(url + "/paint", data = data)

if __name__ == "__main__":
    getboard()