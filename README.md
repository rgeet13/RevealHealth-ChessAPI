# RevealHealth-ChessAPI

## Overview
API endpoint that determines the valid moves for a given chess piece on a chessboard. The
chessboard contains pieces such as Rook, Queen, Bishop, and Knight, and their positions are provided as input

## Requirements
- Docker
- Docker Compose

## Installation
1. Clone the repository: `git clone https://github.com/rgeet13/RevealHealth-ChessAPI.git`
2. Navigate to the project directory: `cd chess_valid_moves`
3. Build the Docker image: `docker build -t my-django-app .`

## Configuration
- Set environment variables, if any.

## Usage
- Run the Docker container: `docker run -d -p 8000:8000 my-django-app`
- Access the application in a web browser at `http://localhost:8000/`

## API End-points
URL - `http://localhost:8000/app/<piece>`
Method - POST
Payload(example) - {
            "positions": {"Queen": "E7", "Bishop": "B7", "Rook":"G5", "Knight": "C3"}
          }
Response - {
    "valid_moves": ["D1", "B1", "A2", "A4"]
}
- <piece> (string): The name of the chess piece (e.g., "knight", "queen", etc.).
