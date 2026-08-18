from rich.console import Console
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
              console.print("[yellow]Port Scanner selected.[/yellow]")
          elif choice =="2":
              console.print("[yellow]DNS Lookup selected.[/yellow]")
          elif choice =="3":
              console.print("[yellow]HTTP Header Analyzer selected.[/yellow]")
          elif choice =="4":
              console.print("[bold green]Goodbye![/bold green]")
              break
          else:
               console.print("[bold red]Invalid option. please try again.[/bold red]")

if __name__ == "__main__":
    main()

