from rich.console import Console
from scanner.port_scanner import run_scanner
from recon.dns_lookup import dns_lookup
from analyzer.http_headers import analyze_headers
console = Console()

def show_menu(): 
    console.print("\n[bold green]CyberSentinel[/bold green]")
    console.print("Cybersecurity Assessment Toolkit\n")

    console.print("[bold cyan]1.[/bold cyan] Port Scanner")
    console.print("[bold cyan]2.[/bold cyan] DNS Lookup")
    console.print("[bold cyan]3.[/bold cyan] HTTP Header Analyzer")
    console.print("[bold cyan]4.[/bold cyan] Exit")

def main():
    while True:
          show_menu()

          choice = input("\nchoose an option: ")

          if choice == "1":
              run_scanner()
          elif choice =="2":
              dns_lookup()
          elif choice =="3":
              analyze_headers()
          elif choice =="4":
              console.print("[bold green]Goodbye![/bold green]")
              break
          else:
               console.print("[bold red]Invalid option. please try again.[/bold red]")

if __name__ == "__main__":
    main()

