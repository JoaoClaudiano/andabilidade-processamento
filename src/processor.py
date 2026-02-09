# src/processor.py
import osmnx as ox
import pandas as pd
from src.config import CATEGORIES, MAX_WALK_DIST

def get_data(place_name):
    print(f"-> Baixando dados para: {place_name}")
    # Baixa a malha viária
    graph = ox.graph_from_place(place_name, network_type="walk")
    nodes, _ = ox.graph_to_gdfs(graph)
    
    # Baixa os Pontos de Interesse (POIs) baseados na config.py
    pois = ox.features_from_place(place_name, tags=CATEGORIES)
    
    # Garante que todos os POIs sejam Pontos (converte polígonos em centroides)
    pois['geometry'] = pois.centroid
    return nodes, pois

def calculate_scores(nodes, pois):
    print("-> Calculando scores...")
    
    # Função de decaimento simples
    def decay_function(distance):
        if distance <= 400: return 100
        if distance > MAX_WALK_DIST: return 0
        # Queda linear entre 400m e 1600m
        return 100 * (1 - (distance - 400) / (MAX_WALK_DIST - 400))

    # Para cada nó da rua, encontra a distância pro POI mais próximo de cada tipo
    # (Simplificação: aqui pegamos o POI mais próximo de QUALQUER categoria)
    for index, node in nodes.iterrows():
        distances = pois.distance(node.geometry) * 111320 # Conv. aprox para metros
        min_dist = distances.min()
        nodes.at[index, 'walk_score'] = round(decay_function(min_dist), 2)
        
    return nodes
