from pyshacl import validate
from rdflib import Graph
import sys

def ruleaza_validarea(data_file, shapes_file):
    print(f"--- Încep validarea: {data_file} folosind {shapes_file} ---")
    
    # Încărcăm grafurile
    data_graph = Graph().parse(data_file, format="turtle")
    shacl_graph = Graph().parse(shapes_file, format="turtle")

    # Validăm
    conforms, results_graph, results_text = validate(
        data_graph,
        shacl_graph=shacl_graph,
        inference='rdfs',
        debug=False
    )

    if conforms:
        print("VALIDARE REUȘITĂ: Datele sunt conforme.")
    else:
        print("VALIDARE EȘUATĂ: S-au găsit următoarele încălcări:")
        print(results_text)
        sys.exit(1) # Cod de ieșire pentru sisteme de CI/CD

if __name__ == "__main__":
    ruleaza_validarea("date_test.ttl", "shapes.ttl")
