# Local imports
from src import create_app
from src.threading import create_threads
from src.config import HOST_IP, HOST_PORT

def main():
    # Create threads
    create_threads()

    # Create app 
    app = create_app()

    # Start python flask app
    app.run(host=HOST_IP, port=HOST_PORT, threaded=True)

if __name__ == "__main__":
    # Run main
    main()
