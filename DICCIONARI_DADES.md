# Diccionari de Dades

## Descripció General

Aquest document descriu totes les variables incloses en el dataset d'anàlisi dels drets de les persones migrades LGTBIQ+.

## Estructura del Dataset

### Variables d'Identificació

| Variable | Tipus | Descripció | Valors | Notes |
|----------|-------|------------|--------|-------|
| `id` | Numèric | Identificador únic del participant | 1 a N | Clau primària |

### Variables Demogràfiques

| Variable | Tipus | Descripció | Valors | Notes |
|----------|-------|------------|--------|-------|
| `edat` | Numèric | Edat del participant en anys | 18-65 | Variable contínua |
| `pais_origen` | Categòric | País d'origen del participant | Veneçuela, Colòmbia, Hondures, El Salvador, Nicaragua, Marroc, Síria, Ucraïna, Rússia, Brasil | 10 categories |
| `identitat_genere` | Categòric | Identitat de gènere autodeclarada | Home trans, Dona trans, Home cis gay, Dona cis lesbiana, No binària, Queer, Bisexual | 7 categories |
| `anys_residencia` | Numèric | Anys de residència al país d'acollida | 0-20 | Variable contínua |
| `nivell_educatiu` | Ordinal | Màxim nivell educatiu assolit | Primària, Secundària, Universitari, Postgrau | 4 nivells ordenats |

### Variables de Situació Legal

| Variable | Tipus | Descripció | Valors | Notes |
|----------|-------|------------|--------|-------|
| `situacio_legal` | Categòric | Situació legal/administrativa actual | Resident legal, En procés, Sense papers, Refugiat | 4 categories |

### Variables d'Accés a Drets i Serveis

| Variable | Tipus | Descripció | Valors | Notes |
|----------|-------|------------|--------|-------|
| `acces_sanitat` | Ordinal | Nivell d'accés als serveis sanitaris | Fàcil, Difícil, Molt difícil, Impossible | 4 nivells ordenats |
| `habitatge_estable` | Binari | Té habitatge estable | Sí, No | Variable dicotòmica |
| `discriminacio_laboral` | Categòric | Ha experimentat discriminació laboral | Sí, No, Prefereixes no dir | 3 categories |

### Variables de Benestar i Violència

| Variable | Tipus | Descripció | Valors | Notes |
|----------|-------|------------|--------|-------|
| `suport_social` | Numèric | Nivell de suport social percebut | 1-10 | Escala Likert |
| `violencia_experimentada` | Categòric | Ha experimentat violència | Sí, No, Prefereixes no dir | 3 categories |

## Detalls de les Categories

### País d'Origen

Els països inclosos representen les principals regions d'origen de persones migrades LGTBIQ+:

- **Amèrica Llatina**: Veneçuela, Colòmbia, Hondures, El Salvador, Nicaragua, Brasil
- **Nord d'Àfrica**: Marroc
- **Orient Mitjà**: Síria
- **Europa de l'Est**: Ucraïna, Rússia

### Identitat de Gènere

Categories basades en terminologia reconeguda internacionalment:

- **Home trans**: Persona assignada dona al néixer que s'identifica com a home
- **Dona trans**: Persona assignada home al néixer que s'identifica com a dona
- **Home cis gay**: Home cisgènere homosexual
- **Dona cis lesbiana**: Dona cisgènere homosexual
- **No binària**: Persona que no s'identifica exclusivament com a home o dona
- **Queer**: Identitat de gènere/sexual no normativa
- **Bisexual**: Persona atreta per més d'un gènere

### Situació Legal

- **Resident legal**: Té permisos de residència vàlids
- **En procés**: Sol·licitud de residència o asil en tràmit
- **Sense papers**: No té documentació legal de residència
- **Refugiat**: Estatus de refugiat reconegut

### Accés a Sanitat

Escala ordinal que mesura la dificultat d'accés:

1. **Fàcil**: Pot accedir als serveis sense obstacles significatius
2. **Difícil**: Troba barreres però pot accedir amb esforç
3. **Molt difícil**: Accés molt limitat amb moltes barreres
4. **Impossible**: No pot accedir als serveis sanitaris

### Nivell Educatiu

Ordenat de menys a més formació:

1. **Primària**: Educació bàsica
2. **Secundària**: Educació secundària o equivalent
3. **Universitari**: Grau universitari o equivalent
4. **Postgrau**: Màster, doctorat o estudis postuniversitaris

## Codificació per a Anàlisi

### Variables Numèriques

Per a anàlisi de correlació, algunes variables categòriques es codifiquen numèricament:

| Variable Original | Variable Numèrica | Codificació |
|-------------------|-------------------|-------------|
| `discriminacio_laboral` | `discriminacio_laboral_num` | Sí=1, No=0, Prefereixes no dir=0.5 |
| `violencia_experimentada` | `violencia_num` | Sí=1, No=0, Prefereixes no dir=0.5 |
| `habitatge_estable` | `habitatge_num` | Sí=1, No=0 |
| `acces_sanitat` | `acces_sanitat_num` | Fàcil=3, Difícil=2, Molt difícil=1, Impossible=0 |

## Valors Perduts

En aquest dataset sintètic no hi ha valors perduts (NA/null). En un estudi real:

- Els valors perduts han de ser documentats
- S'ha d'indicar si són "Missing at Random" (MAR) o no
- Cal decidir estratègies d'imputació o exclusió

## Consideracions de Privacitat

### Dades Sensibles

Segons el RGPD, aquestes variables són dades sensibles:

- Origen ètnic o racial (inferible del país d'origen)
- Orientació sexual (identitat de gènere)
- Salut (accés a sanitat, violència experimentada)

### Protecció Recomanada

- **Anonimització**: Eliminar identificadors directes
- **Agregació**: Presentar resultats agregats
- **Accés restringit**: Limitar qui pot veure dades individuals
- **Encriptació**: Dades emmagatzemades de forma segura

## Validació de Dades

### Regles de Validació

| Variable | Validació |
|----------|-----------|
| `edat` | 18 ≤ edat ≤ 65 |
| `anys_residencia` | 0 ≤ anys_residencia ≤ edat-18 |
| `suport_social` | 1 ≤ suport_social ≤ 10 |
| Totes les categòriques | Valor dins del conjunt permès |

### Comprovacions de Qualitat

- No duplicats en `id`
- No valors fora de rang
- Coherència entre variables relacionades
- Distribucions esperades per a cada variable

## Actualitzacions del Dataset

**Versió**: 1.0  
**Data**: Desembre 2024  
**Autor**: Anàlisi de Drets LGTBIQ+  

### Historial de Canvis

| Versió | Data | Canvis |
|--------|------|--------|
| 1.0 | 2024-12 | Versió inicial del dataset sintètic |

## Referències

- RGPD: Reglament General de Protecció de Dades (EU) 2016/679
- Principis de Yogyakarta sobre l'aplicació de la legislació internacional de drets humans
- ISO/IEC 27001: Gestió de la seguretat de la informació
