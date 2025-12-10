# Anàlisi de Dades: Drets de les Persones Migrades LGTBIQ+

## Descripció del Projecte

Aquest projecte realitza una anàlisi de dades exhaustiva sobre els drets i la situació de les persones migrades LGTBIQ+. L'objectiu és identificar patrons, tendències i àrees crítiques que requereixen atenció en termes de polítiques públiques i suport social.

## Contingut del Projecte

- **analisi_drets_lgtbiq.ipynb**: Notebook principal de Jupyter amb l'anàlisi completa
- **data/**: Directori per emmagatzemar dades i visualitzacions generades
- **requirements.txt**: Dependències de Python necessàries

## Àrees d'Anàlisi

1. **Anàlisi Demogràfica**
   - Distribució per país d'origen
   - Identitats de gènere
   - Distribució d'edat i temps de residència

2. **Drets i Accés a Serveis**
   - Situació legal
   - Accés a sanitat
   - Habitatge estable
   - Discriminació laboral

3. **Violència i Suport Social**
   - Violència experimentada
   - Nivells de suport social disponible

4. **Anàlisi de Correlacions**
   - Relacions entre diferents variables
   - Impacte de la situació legal en altres aspectes

## Instal·lació

### Prerequisits

- Python 3.8 o superior
- pip (gestor de paquets de Python)

### Passos d'Instal·lació

1. Clonar el repositori:
```bash
git clone https://github.com/nrodriguezmoreno-UOC/DRETS-PERSONES-MIGRADES-LGTBIQ-.git
cd DRETS-PERSONES-MIGRADES-LGTBIQ-
```

2. Crear un entorn virtual (recomanat):
```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
# o
venv\Scripts\activate  # En Windows
```

3. Instal·lar les dependències:
```bash
pip install -r requirements.txt
```

## Ús

### Executar l'Anàlisi

1. Iniciar Jupyter Notebook:
```bash
jupyter notebook
```

2. Obrir el fitxer `analisi_drets_lgtbiq.ipynb` al navegador

3. Executar les cel·les del notebook seqüencialment:
   - Podeu executar totes les cel·les amb: `Cell > Run All`
   - O executar-les una per una amb `Shift + Enter`

### Resultats Generats

L'anàlisi genera:
- **Visualitzacions** guardades al directori `data/`:
  - `demografics.png`: Gràfics demogràfics
  - `drets_acces.png`: Anàlisi de drets i accés a serveis
  - `violencia_suport.png`: Violència i suport social
  - `correlacions.png`: Matriu de correlacions
  - `situacio_legal_analisi.png`: Anàlisi creuada amb situació legal

- **Dades processades**:
  - `dades_processades.csv`: Dataset complet processat
  - `resum_estadistic.csv`: Resum estadístic de les troballes principals

## Estructura de Dades

El dataset sintètic inclou les següents variables:

- `id`: Identificador únic
- `edat`: Edat del participant
- `pais_origen`: País d'origen
- `identitat_genere`: Identitat de gènere
- `anys_residencia`: Anys de residència al país d'acollida
- `situacio_legal`: Situació legal (Resident legal, En procés, Sense papers, Refugiat)
- `discriminacio_laboral`: Experiència de discriminació laboral
- `acces_sanitat`: Nivell d'accés a serveis sanitaris
- `suport_social`: Nivell de suport social (escala 1-10)
- `violencia_experimentada`: Si ha experimentat violència
- `habitatge_estable`: Si té habitatge estable
- `nivell_educatiu`: Nivell d'educació

## Principals Troballes

L'anàlisi revela:

- Les persones migrades LGTBIQ+ enfronten múltiples barreres interseccionals
- La situació legal té un impacte significatiu en l'accés a drets bàsics
- Hi ha nivells preocupants de discriminació laboral i violència
- L'accés a sanitat i habitatge estable varia significativament segons la situació legal
- El suport social és una variable crítica per al benestar

## Contribucions

Les contribucions són benvingudes! Si voleu millorar aquest projecte:

1. Feu un fork del repositori
2. Creeu una branca per a la vostra característica (`git checkout -b feature/nova-caracteristica`)
3. Feu commit dels vostres canvis (`git commit -am 'Afegir nova característica'`)
4. Pugeu la branca (`git push origin feature/nova-caracteristica`)
5. Obriu un Pull Request

## Nota sobre les Dades

**Important**: Aquest projecte utilitza dades sintètiques generades per a propòsits d'exemple i demostració. Per a una anàlisi real, caldrà utilitzar dades reals obtingudes d'enquestes, estudis oficials o altres fonts fiables, complint sempre amb les normatives de protecció de dades i privacitat.

## Llicència

Aquest projecte està disponible per a ús educatiu i de recerca.

## Contacte

Per a preguntes o suggeriments, si us plau obriu un issue al repositori de GitHub.

## Agraïments

Aquest projecte busca contribuir a la visibilització i millora dels drets de les persones migrades LGTBIQ+, reconeixent les seves experiències i necessitats específiques.