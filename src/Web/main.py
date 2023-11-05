from src.Web.startup import Startup

startup = Startup().main()

if __name__ == '__main__':
    startup.run(
        port=3000,
        debug=True
    )
