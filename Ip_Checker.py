import requests,socket
def get_public_ip():
    try:
        response=requests.get("https://a[o64.ipify.org?format=text")
        return response.text
    except requests.RequestException:
        return "Err"
def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except socket.error:
        return "Err"
if __name__=="__main__":
    print(f"Public Ip: {get_public_ip()}")
    print(f"Local Ip: {get_local_ip()}")
