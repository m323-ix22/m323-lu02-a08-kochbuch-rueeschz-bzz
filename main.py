"""
-
"""
import json


# Funktion, um ein Rezept aus einem JSON-String in ein Python-Dictionary zu laden
def load_recipe(json_string):
    return json.loads(json_string)


# Funktion, um die Zutatenmengen basierend auf der Anzahl der Personen anzupassen
def adjust_recipe(recipes, new_serving):
    # Berechne den Skalierungsfaktor
    factor = new_serving / recipes["servings"]
    # Passe die Mengen der Zutaten an
    adjusted_ingredients = {ingredient: amount * factor for ingredient, amount in recipes["ingredients"].items()}
    # Erstelle ein neues Rezept-Dictionary mit den angepassten Mengen und der neuen Anzahl an Portionen
    adjusted_recipes = {
        "title": recipes["title"],
        "ingredients": adjusted_ingredients,
        "servings": new_serving
    }
    return adjusted_recipes


if __name__ == "__main__":
    # Beispiel-Rezept im JSON-Format
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": '
                   '{"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}')

    # Lade das Rezept in ein Python-Dictionary
    recipe = load_recipe(recipe_json)

    # Neue Anzahl an Personen
    new_servings = 2

    # Rezept anpassen
    adjusted_recipe = adjust_recipe(recipe, new_servings)

    # Ausgabe des angepassten Rezepts
    print(json.dumps(adjusted_recipe, indent=4))
