1. 가상환경을 켜고 requirements.txt를 다운받는다.

2. 강의가 시작한 후, 개발자도구를 켠다.(강의 본 영상 시작 전에는 html이 다름)

2. edit as html을 눌러서 html을 처음부터 끝까지 복사한다.(ctrl a -> ctrl c)

3. data/xinhtml.txt에 붙여넣기 한다. (알고리즘, 자료구조는 data/html.txt에 넣어야함)

4. main.py를 실행한다. (이산수학이면 3입력)

5. 이산수학이면 3을 입력한다. 

6. 몇 월 며칠 강의인지 입력한다.
<!-- # XIN_Picture_Downloader 1.1.1

XIN 강의의 사진과 영상(음성)을 자동으로 다운로드 해주는 프로그램입니다.

음성 다운로드 시에는 오래걸리니 왜 안움직이지? 오류났나? 하고 프로그램 종료하는 불상사가 없길 바랍니다.

질문은 [여기](https://github.com/DetegiCE/XIN_Picture_Downloader/issues) 로 남겨주세요

## 업데이트 내역

* 1.1.1 cp949 오류 업데이트 - 2021. 03. 07.
* 1.1 PDF Conversion 업데이트 - 2020. 05. 26.
* 1.0 Release - 2020. 05. 19.

## 컴알못을 위한 사용법 1.1

0. [파이썬 설치하기](https://wikidocs.net/8)

1. [이 버튼을 눌러 다운로드 하기](https://github.com/DetegiCE/XIN_Picture_Downloader/archive/master.zip)

2. 다운로드 하고 바탕화면으로 옮기자.

3. [이 링크로](https://studyhard24.tistory.com/234)가서 설치까지만 하고, [이 링크](https://kamang-it.tistory.com/entry/PIL-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-%ED%95%98%EA%B8%B0image-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-%ED%95%98%EA%B8%B0)로 가서 하나 더 설치하자.

4. 윈도우+R을 눌러 ``cmd`` 작성 후 엔터

5. 이제 검은 창이 뜨는데 ``cd C:\\Users\\컴퓨터이름\\Desktop\\XIN_Picture_Downloader`` 을 해주자

6. XIN 강의의 html 파일을 가져와야한다.
> 6-1. XIN 강의로 들어가서 F12를 누른다.
>
> 6-2. 왼쪽에 창이 하나 뜨는데 Elements를 누른다.
>
> 6-3. ``<html class=`` 라고 써진데에서 우클릭을 하고 ``Edit as HTML`` 을 눌러준다.
> 
> 6-4. Ctrl+A(전체선택) 후 Ctrl+C(복사) 한다. 
> 
> 6-5. 다운로드한 파일의 data 폴더 아래의 xinhtml.txt 파일에 Ctrl+V(붙여넣기) 한다.

7. 아까 그 검은 창에서 ``python ./main.py`` 를 해주자

잘 모르겠다면 위에 issues를 눌러 질문을 남기거나 컴잘알에게 물어보자.

## 나름 파이썬 다뤄봤다는 사람을 위한 사용법 1.1

0. [Python을 설치](https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe)한다
> Add Python3.x to PATH 는 꼭 클릭한다.

1. 해당 repository를 git으로 clone 또는 [download](https://github.com/DetegiCE/XIN_Picture_Downloader/archive/master.zip)한다

2. 터미널을 이용하여 해당 폴더에 접근한다.
> 혹은 탐색기를 C://xxx/XIN_Picture_Downloader 에 위치시킨 후 주소창을 클릭한 후 "cmd ."을 입력하고 Enter를 입력한다

3. 다음과 같이 라이브러리를 설치한다.
> BeautifulSoup4와 Pillow가 이미 깔려있으신 개발자 분께서는 이 과정을 스킵하셔도 됩니다.

```
pip install -r requirement.txt
```

또는

```
pip3 install -r requirement.txt
```

4. XIN 강의의 html을 긁어오자.

> 4-1. XIN 강의로 들어가서 F12를 누른다.

> 4-2. Elements를 누르고 ``<html class=``에서 우클릭을 하고 ``Edit as HTML``을 누른다.

> 4-3. Ctrl+A(전체선택) 후 Ctrl+C(복사) 한다. 

> 4-4. data 폴더 아래의 xinhtml.txt 파일에 Ctrl+V(붙여넣기) 한다.

5. 다음 명령어를 이용하여 프로그램을 돌린다

```python ./main.py``` -->
