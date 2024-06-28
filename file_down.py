import requests  # requests 모듈 임포트

def download_file(file_url, save_path):
    with open(save_path, 'wb') as f: # 저장할 파일을 바이너리 쓰기 모드로 열기
        response = requests.get(file_url) # 파일 URL에 GET 요청 보내기
        f.write(response.content) # 응답의 내용을 파일에 쓰기

# URL과 저장 경로 변수를 지정합니다.
url = 'https://apihub.kma.go.kr/api/typ01/url/kma_sfctm2.php?tm=202211300900&stn=201&help=0&authKey='
save_file_path = 'download.csv'

# 파일 다운로드 함수를 호출합니다.
download_file(url, save_file_path)