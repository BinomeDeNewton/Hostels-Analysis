import folium
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import pandas as pd
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable


# List of hotels
hotels = [
    {
        "address": "34 avenue de la Grande Armée, Paris, 75017, France",
        "price_for_2_nights": 121.50,
        "overall_rating": 7.5,
        "reviews": 1337,
        "details": {
            "personnel": 7.8,
            "equipements": 7.3,
            "cleanliness": 7.9,
            "comfort": 7.9,
            "value_for_money": 7.5,
            "geographic_location": 9.4,
        }
    },
    {
        "address": "68 Rue De Longchamp, 75016 Paris, France",
        "price_for_2_nights": 183.00,
        "overall_rating": 8.5,
        "reviews": 1058,
        "details": {
            "personnel": 9.4,
            "equipements": 8.3,
            "cleanliness": 8.8,
            "comfort": 8.8,
            "value_for_money": 8.2,
            "geographic_location": 9.6,
        }
    },
    {
        "address": "10 rue Marbeau, 75016 Paris, France",
        "price_for_2_nights": 145.50,
        "overall_rating": 8.1,
        "reviews": 1225,
        "details": {
            "personnel": 9.1,
            "equipements": 8.1,
            "cleanliness": 8.6,
            "comfort": 8.6,
            "value_for_money": 7.9,
            "geographic_location": 8.8,
        }
    },
    {
        "address": "63 Rue Saint-Lazare, 75009 Paris, France",
        "price_for_2_nights": 142.00,
        "overall_rating": 8.4,
        "reviews": 963,
        "details": {
            "personnel": 9.1,
            "equipements": 8.2,
            "cleanliness": 8.7,
            "comfort": 8.7,
            "value_for_money": 8.2,
            "geographic_location": 9.4,
        }
    },
    {
        "address": "45 rue de la Victoire, 75009 Paris, France",
        "price_for_2_nights": 145.50,
        "overall_rating": 8.0,
        "reviews": 1385,
        "details": {
            "personnel": 8.6,
            "equipements": 7.8,
            "cleanliness": 8.5,
            "comfort": 8.5,
            "value_for_money": 7.9,
            "geographic_location": 9.2,
        }
    },
    {
        "address": "12 rue de Richelieu, 75001 Paris, France",
        "price_for_2_nights": 166.00,
        "overall_rating": 8.1,
        "reviews": 2660,
        "details": {
            "personnel": 9.1,
            "equipements": 7.7,
            "cleanliness": 8.2,
            "comfort": 8.2,
            "value_for_money": 8.1,
            "geographic_location": 9.7,
        }
    },
    {
        "address": "11 rue Ravignan, 75018 Paris, France",
        "price_for_2_nights": 141.50,
        "overall_rating": 8.3,
        "reviews": 2314,
        "details": {
            "personnel": 8.9,
            "equipements": 8.0,
            "cleanliness": 8.6,
            "comfort": 8.5,
            "value_for_money": 8.0,
            "geographic_location": 9.6,
        }
    },
    {
        "address": "35, Rue Des Ecoles, 75005 Paris, France",
        "price_for_2_nights": 164.00,
        "overall_rating": 8.4,
        "reviews": 1548,
        "details": {
            "personnel": 9.1,
            "equipements": 8.3,
            "cleanliness": 8.8,
            "comfort": 8.8,
            "value_for_money": 8.0,
            "geographic_location": 9.3,
        }
    },
    {
        "address": "6 Rue Gay Lussac, 75005 Paris, France",
        "price_for_2_nights": 147.50,
        "overall_rating": 8.5,
        "reviews": 2028,
        "details": {
            "personnel": 8.9,
            "equipements": 8.3,
            "cleanliness": 8.8,
            "comfort": 8.9,
            "value_for_money": 8.2,
            "geographic_location": 9.4,
        }
    },
    {
        "address": "9 Rue Saint Jacques, 75005 Paris, France",
        "price_for_2_nights": 169.50,
        "overall_rating": 8.5,
        "reviews": 1908,
        "details": {
            "personnel": 9.1,
            "equipements": 8.3,
            "cleanliness": 8.8,
            "comfort": 8.8,
            "value_for_money": 8.2,
            "geographic_location": 9.6,
        }
    },
    {
        "address": "9 Rue de l'Ancienne Comédie, 75006 Paris, France",
        "price_for_2_nights": 180.50,
        "overall_rating": 8.7,
        "reviews": 1155,
        "details": {
            "personnel": 9.1,
            "equipements": 8.4,
            "cleanliness": 9.0,
            "comfort": 9.0,
            "value_for_money": 8.3,
            "geographic_location": 9.8,
        }
    },
    {
        "address": "38 Rue Poncelet, Paris, 75017, France",
        "price_for_2_nights": 115.50,
        "overall_rating": 7.4,
        "reviews": 1326,
        "details": {
            "personnel": 8.4,
            "equipements": 7.2,
            "cleanliness": 7.7,
            "comfort": 7.7,
            "value_for_money": 7.1,
            "geographic_location": 8.8,
        }
    },
    {
        "address": "74 rue de Provence, Paris, 75009, France",
        "price_for_2_nights": 122.50,
        "overall_rating": 7.0,
        "reviews": 1878,
        "details": {
            "personnel": 8.1,
            "equipements": 6.8,
            "cleanliness": 7.5,
            "comfort": 7.5,
            "value_for_money": 6.9,
            "geographic_location": 9.1,
        }
    }
]


# Points of interest with their coordinates
points_of_interest = {
    "Louvre Pyramid": (48.861017, 2.335848),
    "Sacré Coeur": (48.886705, 2.343104),
    "Arc de Triomphe": (48.873792, 2.295028),
    "Eiffel Tower": (48.858370, 2.294481),
    "Opéra Garnier": (48.871946, 2.331619)
}


# Function to obtain location with error handling
def get_location(address):
    try:
        return geolocator.geocode(address)
    except (GeocoderTimedOut, GeocoderUnavailable):
        return None
    
    
# Initialize the geolocator
geolocator = Nominatim(user_agent="Hotels", timeout=10)
    
    
# Calculate distances and adjust for the top 3
def calculate_distances_and_top3(hotels, points_of_interest):
    distances_per_poi = {poi: [] for poi in points_of_interest.keys()}
    hotel_counts = {hotel['address']: 0 for hotel in hotels}  # Pour compter les apparitions dans le top 3
    
    for hotel in hotels:
        hotel_location = get_location(hotel['address'])
        if hotel_location:
            hotel['latitude'] = hotel_location.latitude
            hotel['longitude'] = hotel_location.longitude
            for poi, coords in points_of_interest.items():
                distance = geodesic((hotel_location.latitude, hotel_location.longitude), coords).kilometers
                distances_per_poi[poi].append((hotel, distance))
                
    for poi, distances in distances_per_poi.items():
        distances.sort(key=lambda x: x[1])
        top_3 = distances[:3]  # Obtient les 3 plus proches
        for hotel, _ in top_3:
            hotel_counts[hotel['address']] += 1  # Incrémente le compteur pour cet hôtel
            
    # Mise à jour des hôtels avec leur compte de top 3
    for hotel in hotels:
        hotel['top_3_count'] = hotel_counts[hotel['address']]
        
    # Maintenant, imprimez le top 3 pour chaque point d'intérêt
    for poi in distances_per_poi:
        print(f"Top 3 closest hotels to {poi}:")
        for hotel, distance in distances_per_poi[poi][:3]:
            print(f"- {hotel['address']} at {distance:.2f} km")
        print("")  # For better formatting
    
    return distances_per_poi


def calculate_score(hotels):
    for hotel in hotels:
        details = hotel['details']
        score = ((details['geographic_location'] / 10 * 0.4) + 
            (details['cleanliness'] / 10 * 0.3) + 
            (details['comfort'] / 10 * 0.3) + 
            (details['personnel'] / 10 * 0.2) +
            (details['value_for_money'] / 10 * 0.1) + 
            (hotel['overall_rating'] / 10 * 0.2)) * 1000 - hotel['price_for_2_nights'] + (hotel['reviews'] / 1000)
        
        # Adds 100 for each appearance in a top 3 (or top 2, adjust as needed)
        score += hotel.get('top_3_count', 0) * 100
        
        hotel['score'] = score
        
        # Imprimer les détails du calcul du score
        print(f"Calculating score for {hotel['address']}:")
        print(f"Final score: {score:.2f}\n")
        

distances_per_poi = calculate_distances_and_top3(hotels, points_of_interest)
calculate_score(hotels)

# Sort hotels by score
hotels_sorted = sorted(hotels, key=lambda x: x['score'], reverse=True)

# Display the results
for hotel in hotels_sorted[:5]:  # Display the top 2 hotels
    print("Ranking of Hotels:")
    print(f"Address: {hotel['address']}, Score: {hotel['score']:.2f}")
    
# Initialisation de la carte
m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

# Palette de couleurs pour les points d'intérêt
colors = ['red', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']

# Ajout des hôtels avec des icônes bleues
for hotel in hotels:
    if 'latitude' in hotel and 'longitude' in hotel:
        folium.Marker(
            [hotel['latitude'], hotel['longitude']],
            popup=f"{hotel['address']}, Score: {hotel.get('score', 0):.2f}",
            icon=folium.Icon(color='blue')
        ).add_to(m)
        
# Itération sur les points d'intérêt
for poi_name, poi_coord in points_of_interest.items():
    # Obtenir le top 3 des hôtels pour ce point d'intérêt spécifique
    top_3_hotels = distances_per_poi[poi_name][:3]  # Assurez-vous de récupérer les bonnes données
    
    # Pour chaque hôtel dans le top 3, ajouter une ligne de la couleur correspondante au POI
    for hotel, distance in top_3_hotels:
        hotel_coords = (hotel['latitude'], hotel['longitude'])
        # Choix de la couleur pour le POI actuel
        poi_color = colors[list(points_of_interest.keys()).index(poi_name) % len(colors)]
        folium.PolyLine(locations=[poi_coord, hotel_coords], color=poi_color, weight=2.5).add_to(m)
        
    # Ajouter également un marqueur pour le POI lui-même
    folium.Marker(
        poi_coord,
        popup=f"{poi_name}",
        icon=folium.Icon(color=poi_color, icon='info-sign')
    ).add_to(m)
    
    # Pour chaque hôtel dans le top 3, tracer une ligne de la couleur du POI
    for hotel, _ in top_3_hotels:
        if 'latitude' in hotel and 'longitude' in hotel:
            line = folium.PolyLine(locations=[poi_coord, [hotel['latitude'], hotel['longitude']]], color=poi_color, weight=2.5, opacity=0.5)
            m.add_child(line)
            
# Sauvegarde de la carte dans un fichier HTML
m.save('hotels_and_points_of_interest.html')