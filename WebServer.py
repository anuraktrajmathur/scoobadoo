import requests

def upload_file(file_path, group, target, server_url):
    url = f"{server_url}/frame/{group}/{target}"
    with open(file_path, 'rb') as file:
        files = {'file': file}
        try:
            response = requests.post(url, files=files)
            if response.status_code == 200:
                print("Success:", response.text)
            else:
                print(f"Failed with status code {response.status_code}: {response.text}")
        except Exception as e:
            print(f"An error occurred: {e}")
        
# Example usage
if __name__ == "__main__":
    server_url = "http://192.168.1.20"
    group = "ScoobaDoo"
    target = "example_target"
    file_path = "path/to/your/file.png"

    upload_file(file_path, group, target, server_url)
