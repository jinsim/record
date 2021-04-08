import getpics
import getvideos

if __name__ == "__main__":
    select = input("강의의 종류를 입력해주세요.  \n알고리즘:1 \t자료구조:2 \t이산수학:3\n").strip()
    if select == '1':
        folder = '알고리즘'
        url = getvideos.getUrl("./data/html.txt", '알고리즘')
    elif select == '2':
        folder = '자료구조'
        url = getvideos.getUrl("./data/html.txt", '자료구조')
    elif select == '3':
        folder = '이산수학'
        th = input("몇 월 며칠 강의인가요?  \nex)3월29일\n" ).strip()
        url = getpics.getUrl("./data/xinhtml.txt", folder, th)
