import argparse
import sys

def init_banner():
    print("=" * 50)
    print("  ORION :: AI-Powered API Security Fuzzer")
    print("=" * 50)

def main():
    init_banner()
    
    parser = argparse.ArgumentParser(
        description="ORION - Automated API Security Pipeline",
        epilog="Example: python orion.py -u https://api.example.com/v1/user?id=1"
    )
    
    parser.add_argument("-u", "--url", help="Target API endpoint URL to test", type=str)
    parser.add_argument("-f", "--file", help="Path to raw HTTP request file", type=str)
    parser.add_argument("--output", help="Output format for report (json/md)", default="json", choices=["json", "md"])

    args = parser.parse_args()

    if not args.url and not args.file:
        parser.print_help()
        sys.exit(1)

    if args.url:
        print(f"[*] Target specified: {args.url}")
        print("[*] Initializing Module 01 (Input & Parameter Parser)...")
    elif args.file:
        print(f"[*] Request file specified: {args.file}")
        print("[*] Initializing Module 01 (HTTP File Parser)...")

if __name__ == "__main__":
    main()
