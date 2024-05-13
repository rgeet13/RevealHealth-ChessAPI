from django.shortcuts import render
from .utils import calculate_bishop_moves, calculate_knight_moves, calculate_rook_moves, calculate_queen_moves
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def valid_moves(request, piece):
    if request.method == 'POST':
        data = json.loads(request.body)
        positions = data.get('positions', {})
        if not positions or piece.lower() not in positions:
            return JsonResponse({'error': 'Invalid piece name'})

        valid_moves = []
        if piece.lower() == 'knight':
            valid_moves = calculate_knight_moves(positions, piece)
        elif piece.lower() == 'queen':
            valid_moves = calculate_queen_moves(positions, piece)
        elif piece.lower() == 'rook':
            valid_moves = calculate_rook_moves(positions, piece)
        elif piece.lower() == 'bishop':
            valid_moves = calculate_bishop_moves(positions, piece)

        return JsonResponse({'valid_moves': valid_moves})

