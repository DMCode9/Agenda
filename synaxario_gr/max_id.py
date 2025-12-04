import json

# Όνομα του αρχείου JSON
file_name = "synaxari_gr.json"

def find_max_id(file_path):
    """
    Διαβάζει ένα αρχείο JSON, εντοπίζει τη λίστα "data"
    και βρίσκει τη μεγαλύτερη τιμή στο πεδίο "id" των αντικειμένων.
    """
    try:
        # Άνοιγμα και ανάγνωση του αρχείου JSON
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
    except FileNotFoundError:
        print(f"Σφάλμα: Το αρχείο '{file_path}' δεν βρέθηκε.")
        return None
    except json.JSONDecodeError:
        print(f"Σφάλμα: Το αρχείο '{file_path}' δεν είναι έγκυρο JSON.")
        return None
    except Exception as e:
        print(f"Προέκυψε ένα απροσδόκητο σφάλμα: {e}")
        return None

    # Έλεγχος αν υπάρχει το κλειδί "data" και αν είναι λίστα
    if "data" in data and isinstance(data["data"], list):
        
        # Λίστα για αποθήκευση όλων των τιμών "id"
        ids = []
        
        for item in data["data"]:
            # Έλεγχος αν υπάρχει το κλειδί "id" και αν είναι αριθμός
            if "id" in item and (isinstance(item["id"], int) or isinstance(item["id"], float)):
                ids.append(item["id"])
            else:
                print(f"Προειδοποίηση: Ένα αντικείμενο στη λίστα 'data' δεν έχει έγκυρο πεδίο 'id'.")
        
        # Εύρεση της μέγιστης τιμής, αν η λίστα δεν είναι κενή
        if ids:
            max_id = max(ids)
            return max_id
        else:
            print("Δεν βρέθηκαν έγκυρες τιμές 'id' στη λίστα 'data'.")
            return None
    else:
        print("Σφάλμα: Το JSON δεν περιέχει το κλειδί 'data' ή δεν είναι λίστα.")
        return None

# Εκτέλεση της συνάρτησης και εμφάνιση του αποτελέσματος
max_value = find_max_id(file_name)

if max_value is not None:
    print(f"\nΟ μεγαλύτερος αριθμός στο πεδίο 'id' είναι: **{max_value}**")