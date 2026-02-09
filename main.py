# main.py
from src.processor import get_data, calculate_scores
import os

def run_pipeline(place):
    # 1. Obter dados
    nodes, pois = get_data(place)
    
    # 2. Processar Score
    nodes_with_score = calculate_scores(nodes, pois)
    
    # 3. Salvar Output (GeoJSON)
    if not os.path.exists('output'): os.makedirs('output')
    
    output_name = f"output/{place.replace(',', '').replace(' ', '_').lower()}.geojson"
    nodes_with_score[['walk_score', 'geometry']].to_file(output_name, driver='GeoJSON')
    print(f"✅ Sucesso! Mapa gerado em: {output_name}")

if __name__ == "__main__":
    # Teste com uma área pequena primeiro
    run_pipeline("Urca, Rio de Janeiro, Brazil")
