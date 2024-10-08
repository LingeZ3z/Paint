import requests

def getboard():
    board = [["" for j in range(1000)] for i in range(600)]
    res = requests.get("https://pbd.uwuwu.us.kg/paintboard/board").text
    for i in range(1, 1800000, 3):
        x = (i // 3) % 600
        y = (i // 3) // 600
        color = hex(ord(res[i]))[2:].rjust(2,"0")+hex(ord(res[i+1]))[2:].rjust(2,"0")+hex(ord(res[i+2]))[2:].rjust(2,"0")
        board[x][y] = color
    return board

if __name__ == "__main__":
    getboard()