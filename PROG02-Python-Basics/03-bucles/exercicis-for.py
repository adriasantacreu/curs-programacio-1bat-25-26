# 🔄 Unitat 3: Bucles (For i While)

En aquesta unitat aprendrem a automatitzar tasques repetitives. Un bucle ens permet executar el mateix bloc de codi múltiples vegades.

## 1. El Bucle `for`
S'utilitza quan sabem exactament quantes vegades volem repetir una acció o quan volem recórrer una llista d'elements.

### Exemple: Comptador simple
```python
for i in range(1, 6):
    print(f"Estem comptant: {i}")
```

### Exemple: Recórrer una llista
```python
fruites = ["poma", "plàtan", "cirera"]
for f in fruites:
    print(f"M'agrada la {f}")
```

---

## 2. El Bucle `while`
S'utilitza quan volem repetir un codi **mentre** es compleixi una condició, sense saber exactament quantes vegades serà.

### Exemple: Fins que l'usuari digui "prou"
```python
resposta = ""
while resposta.lower() != "prou":
    resposta = input("Escriu alguna cosa (o 'prou' per sortir): ")
```

---

## 3. Exercicis de Pràctica

### 📝 Tasca 1: Taula de multiplicar
Crea un programa que demani un número a l'usuari i mostri la seva taula de multiplicar de l'1 al 10.
* [Veure solució en Python](exercici_taula.py)

### 📝 Tasca 2: Sumatori de números positius
Fes un bucle que vagi demanant números i els sumi fins que l'usuari introdueixi un número negatiu.

---

## 🎄 Projecte del Mòdul: L'Arbre de Nadal
Aquest és l'exercici estrella de la unitat, on combinem bucles, `range()` i probabilitat.

👉 **[Anar al codi de l'Arbre de Nadal](./arbre_nadal.py)**

> [!TIP]
> **Recorda la indentació:** En Python, tot el que va dins del bucle ha d'estar desplaçat a la dreta. Si no, el programa donarà error!