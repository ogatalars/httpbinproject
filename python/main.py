from http_requests import get_public_ip

def main():
    result = get_public_ip()
    if 'origin' in result: 
        print(f"Seu IP público é: {result['origin']}")
    else:
        print(result['error'])

if __name__ == '__main__':        
    main()