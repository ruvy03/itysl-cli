import sys
from src.browser import ITYSLBrowser


def main():
    
    browser = ITYSLBrowser()
    try:
        browser.run()
    except KeyboardInterrupt:
        print("\n\nExiting... I don't even want to be around anymore")
        sys.exit(0)


if __name__ == "__main__":
    main()