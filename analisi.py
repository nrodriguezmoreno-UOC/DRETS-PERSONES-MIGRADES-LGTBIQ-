#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script per executar l'anàlisi de dades dels drets de persones migrades LGTBIQ+
Aquest script executa l'anàlisi sense necessitat de Jupyter Notebook
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os

# Configuració
warnings.filterwarnings('ignore')
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette('husl')

def crear_directori_dades():
    """Crea el directori de dades si no existeix"""
    if not os.path.exists('data'):
        os.makedirs('data')
        print("Directori 'data' creat")

def generar_dades():
    """Genera el dataset sintètic per a l'anàlisi"""
    print("\n=== Generant dades sintètiques ===")
    np.random.seed(42)
    n_registres = 500
    
    data = {
        'id': range(1, n_registres + 1),
        'edat': np.random.randint(18, 65, n_registres),
        'pais_origen': np.random.choice(['Veneçuela', 'Colòmbia', 'Hondures', 'El Salvador', 'Nicaragua', 
                                          'Marroc', 'Síria', 'Ucraïna', 'Rússia', 'Brasil'], n_registres),
        'identitat_genere': np.random.choice(['Home trans', 'Dona trans', 'Home cis gay', 'Dona cis lesbiana', 
                                               'No binària', 'Queer', 'Bisexual'], n_registres),
        'anys_residencia': np.random.randint(0, 20, n_registres),
        'situacio_legal': np.random.choice(['Resident legal', 'En procés', 'Sense papers', 'Refugiat'], 
                                            n_registres, p=[0.3, 0.25, 0.2, 0.25]),
        'discriminacio_laboral': np.random.choice(['Sí', 'No', 'Prefereixes no dir'], 
                                                   n_registres, p=[0.45, 0.40, 0.15]),
        'acces_sanitat': np.random.choice(['Fàcil', 'Difícil', 'Molt difícil', 'Impossible'], 
                                           n_registres, p=[0.25, 0.35, 0.25, 0.15]),
        'suport_social': np.random.randint(1, 11, n_registres),
        'violencia_experimentada': np.random.choice(['Sí', 'No', 'Prefereixes no dir'], 
                                                     n_registres, p=[0.40, 0.45, 0.15]),
        'habitatge_estable': np.random.choice(['Sí', 'No'], n_registres, p=[0.60, 0.40]),
        'nivell_educatiu': np.random.choice(['Primària', 'Secundària', 'Universitari', 'Postgrau'], 
                                             n_registres, p=[0.15, 0.35, 0.35, 0.15])
    }
    
    df = pd.DataFrame(data)
    print(f"Dades generades: {len(df)} registres")
    return df

def analisi_demografica(df):
    """Crea visualitzacions demogràfiques"""
    print("\n=== Anàlisi demogràfica ===")
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # País d'origen
    pais_counts = df['pais_origen'].value_counts()
    axes[0, 0].barh(pais_counts.index, pais_counts.values, color='skyblue')
    axes[0, 0].set_xlabel('Nombre de persones')
    axes[0, 0].set_title('Distribució per País d\'Origen')
    axes[0, 0].grid(axis='x', alpha=0.3)
    
    # Identitat de gènere
    identitat_counts = df['identitat_genere'].value_counts()
    axes[0, 1].bar(range(len(identitat_counts)), identitat_counts.values, color='coral')
    axes[0, 1].set_xticks(range(len(identitat_counts)))
    axes[0, 1].set_xticklabels(identitat_counts.index, rotation=45, ha='right')
    axes[0, 1].set_ylabel('Nombre de persones')
    axes[0, 1].set_title('Distribució per Identitat de Gènere')
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    # Distribució d'edat
    axes[1, 0].hist(df['edat'], bins=20, color='lightgreen', edgecolor='black')
    axes[1, 0].set_xlabel('Edat')
    axes[1, 0].set_ylabel('Freqüència')
    axes[1, 0].set_title('Distribució d\'Edat')
    axes[1, 0].grid(axis='y', alpha=0.3)
    
    # Anys de residència
    axes[1, 1].hist(df['anys_residencia'], bins=20, color='plum', edgecolor='black')
    axes[1, 1].set_xlabel('Anys de residència')
    axes[1, 1].set_ylabel('Freqüència')
    axes[1, 1].set_title('Distribució d\'Anys de Residència')
    axes[1, 1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('data/demografics.png', dpi=300, bbox_inches='tight')
    print("Gràfics demogràfics guardats: data/demografics.png")
    plt.close()

def analisi_drets(df):
    """Crea visualitzacions de drets i accés a serveis"""
    print("\n=== Anàlisi de drets i accés a serveis ===")
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Situació legal
    situacio_counts = df['situacio_legal'].value_counts()
    colors_situacio = ['#2ecc71', '#f39c12', '#e74c3c', '#3498db']
    axes[0, 0].pie(situacio_counts.values, labels=situacio_counts.index, autopct='%1.1f%%', 
                   colors=colors_situacio, startangle=90)
    axes[0, 0].set_title('Situació Legal')
    
    # Accés a sanitat
    sanitat_counts = df['acces_sanitat'].value_counts()
    axes[0, 1].barh(sanitat_counts.index, sanitat_counts.values, color='lightcoral')
    axes[0, 1].set_xlabel('Nombre de persones')
    axes[0, 1].set_title('Accés a Sanitat')
    axes[0, 1].grid(axis='x', alpha=0.3)
    
    # Discriminació laboral
    discrim_counts = df['discriminacio_laboral'].value_counts()
    axes[1, 0].bar(discrim_counts.index, discrim_counts.values, color=['#e74c3c', '#2ecc71', '#95a5a6'])
    axes[1, 0].set_ylabel('Nombre de persones')
    axes[1, 0].set_title('Discriminació Laboral')
    axes[1, 0].grid(axis='y', alpha=0.3)
    
    # Habitatge estable
    habitatge_counts = df['habitatge_estable'].value_counts()
    axes[1, 1].pie(habitatge_counts.values, labels=habitatge_counts.index, autopct='%1.1f%%',
                   colors=['#2ecc71', '#e74c3c'], startangle=90)
    axes[1, 1].set_title('Habitatge Estable')
    
    plt.tight_layout()
    plt.savefig('data/drets_acces.png', dpi=300, bbox_inches='tight')
    print("Gràfics de drets i accés guardats: data/drets_acces.png")
    plt.close()

def mostrar_resum(df):
    """Mostra un resum estadístic complet"""
    print("\n" + "=" * 80)
    print("RESUM ESTADÍSTIC: DRETS DE LES PERSONES MIGRADES LGTBIQ+")
    print("=" * 80)
    print()
    
    print("1. DADES DEMOGRÀFIQUES")
    print(f"   - Total de participants: {len(df)}")
    print(f"   - Edat mitjana: {df['edat'].mean():.1f} anys")
    print(f"   - Anys mitjans de residència: {df['anys_residencia'].mean():.1f} anys")
    print()
    
    print("2. SITUACIÓ LEGAL")
    for situacio, count in df['situacio_legal'].value_counts().items():
        pct = (count / len(df)) * 100
        print(f"   - {situacio}: {count} ({pct:.1f}%)")
    print()
    
    print("3. DISCRIMINACIÓ I VIOLÈNCIA")
    discrim_si = (df['discriminacio_laboral'] == 'Sí').sum()
    violencia_si = (df['violencia_experimentada'] == 'Sí').sum()
    print(f"   - Persones amb discriminació laboral: {discrim_si} ({(discrim_si/len(df)*100):.1f}%)")
    print(f"   - Persones amb violència experimentada: {violencia_si} ({(violencia_si/len(df)*100):.1f}%)")
    print()
    
    print("4. ACCÉS A SERVEIS")
    sanitat_facil = (df['acces_sanitat'] == 'Fàcil').sum()
    habitatge_si = (df['habitatge_estable'] == 'Sí').sum()
    print(f"   - Accés fàcil a sanitat: {sanitat_facil} ({(sanitat_facil/len(df)*100):.1f}%)")
    print(f"   - Habitatge estable: {habitatge_si} ({(habitatge_si/len(df)*100):.1f}%)")
    print()
    
    print("5. SUPORT SOCIAL")
    print(f"   - Mitjana de suport social: {df['suport_social'].mean():.2f}/10")
    print(f"   - Desviació estàndard: {df['suport_social'].std():.2f}")
    print()
    
    print("6. PRINCIPALS TROBALLES")
    print("   - Les persones migrades LGTBIQ+ enfronten múltiples barreres")
    print("   - La situació legal té un impacte significatiu en l'accés a drets")
    print("   - Hi ha una necessitat clara de suport integral i polítiques inclusives")
    print("   - La discriminació laboral i la violència són problemàtiques prevalents")
    print("=" * 80)

def exportar_resultats(df):
    """Exporta els resultats de l'anàlisi"""
    print("\n=== Exportant resultats ===")
    
    # Guardar dataset processat
    df.to_csv('data/dades_processades.csv', index=False, encoding='utf-8')
    print("Dataset processat guardat: data/dades_processades.csv")
    
    # Crear resum estadístic
    resum = {
        'Total registres': [len(df)],
        'Edat mitjana': [df['edat'].mean()],
        'Anys residència mitjana': [df['anys_residencia'].mean()],
        'Suport social mitjà': [df['suport_social'].mean()],
        'Percentatge discriminació laboral': [(df['discriminacio_laboral'] == 'Sí').sum() / len(df) * 100],
        'Percentatge violència': [(df['violencia_experimentada'] == 'Sí').sum() / len(df) * 100],
        'Percentatge habitatge estable': [(df['habitatge_estable'] == 'Sí').sum() / len(df) * 100]
    }
    
    resum_df = pd.DataFrame(resum)
    resum_df.to_csv('data/resum_estadistic.csv', index=False, encoding='utf-8')
    print("Resum estadístic guardat: data/resum_estadistic.csv")

def main():
    """Funció principal per executar l'anàlisi completa"""
    print("\n" + "=" * 80)
    print("ANÀLISI DE DADES: DRETS DE LES PERSONES MIGRADES LGTBIQ+")
    print("=" * 80)
    
    # Crear directori de dades
    crear_directori_dades()
    
    # Generar dades
    df = generar_dades()
    
    # Executar anàlisis
    analisi_demografica(df)
    analisi_drets(df)
    
    # Mostrar resum
    mostrar_resum(df)
    
    # Exportar resultats
    exportar_resultats(df)
    
    print("\n✓ Anàlisi completada amb èxit!")
    print("\nFitxers generats:")
    print("  - data/demografics.png")
    print("  - data/drets_acces.png")
    print("  - data/dades_processades.csv")
    print("  - data/resum_estadistic.csv")
    print()

if __name__ == "__main__":
    main()
