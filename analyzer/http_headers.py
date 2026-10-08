import requests
from rich.console import Console

console = Console()

def analyze_headers():
    url = input("Enter URL: ")

    try:
        response = requests.get(url, timeout=5)


        print(f"\nStatus Code: {response.status_code}")
        print("\nResponse Headers:")

        for header, value in response.headers.items():
            print(f"{header}: {value}")

        security_headers = {
            "Content-Security-Policy": "Helps protect against XSS and injection attacks",
            "Strict-Transport-Security": "Forces browsers to use HTTPS",
            "X-Frame-Options": "Helps protect against clickjacking",
            "X-Content-Type-Options": "Helps prevent MIME-type sniffing",
            "Referrer-Policy": "Controls how much referrer information is sent",
        }


        console.print("\n[bold cyan]Security Header Analysis:[/bold cyan]")
        score = 0
        for header, description in security_headers.items():
            if header in response.headers:
                score += 1
                console.print(f"[bold green][+] {header}: PRESENT[/bold green]")
                print(f"    {description}")
            else:
                console.print(f"[bold yellow][-] {header}: MISSING[/bold yellow]")
                print(f"    {description}")      
        console.print(f"\n[bold cyan]Security Score: {score}/{len(security_headers)}[/bold cyan]")

    except requests.RequestException:
        print("Unable to connect to the URL.")

if __name__ == "__main__":
    analyze_headers()

