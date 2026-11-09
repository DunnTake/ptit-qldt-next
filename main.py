import extract
import parser
import server
from time import sleep

def main():
    try:
        print(extract.main())
        server.run()
        while True:
            print(parser.main())
            sleep(300)
    except Exception as Error:
        print(Error)

if __name__ == "__main__":
    main()