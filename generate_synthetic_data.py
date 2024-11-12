import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
num_samples = 28
koerpergroesse = np.random.randint(158, 190, size=num_samples)
schuhgroesse = (koerpergroesse - 50) / 3 + np.random.normal(0, 1, size=num_samples)  # Introduce correlation with some noise

data = pd.DataFrame({
    'nr': range(1, num_samples + 1),
    'Koerpergroesse': koerpergroesse,
    'Lieblingsfilm': np.random.choice(['Hangover', 'Top Gun: Maverick', 'Oppenheimer', 'Harry Potter', 'Gefährten', 'Honig im Kopf', 'Mamma Mia!', 'House of Gucci', 'Little Women', 'Inception', 'Pretty Women', 'Coach Carter'], size=num_samples),
    'Sockenfarbe': np.random.choice(['weiß', 'schwarz', 'dunkelgrau', 'grün', 'braun'], size=num_samples),
    'Armlaenge': np.random.uniform(60.0, 75.0, size=num_samples).round(1),
    'Einwohnerzahl': np.random.randint(1, 2000000, size=num_samples),
    'Akku': np.random.choice(['30%', '50%', '70%', '90%'], size=num_samples),
    'Sandkoerner': np.random.choice(['500 000 000 000 000 000', '60 000 000 000 000 000 000', '7 000 000 000 000 000 000', '25 000 000 000 000 000 000', '100 000 000 000 000'], size=num_samples),
    'Distanz_Wohnort': np.random.choice(['24km', '35km', '42km', '50km', '70km'], size=num_samples),
    'letzte_Pizza': pd.date_range(start='2023-12-01', periods=num_samples, freq='D').strftime('%d.%m.%Y'),
    'Statistik': np.random.randint(1, 11, size=num_samples),
    'Schuhgroesse': schuhgroesse.round(0).astype(int),  # Round and convert to integer
    'Mahlzeiten_Mensa': np.random.randint(100, 300, size=num_samples)
})

print(data)

scatter = data.plot.scatter(x='Koerpergroesse', y='Schuhgroesse')

# Save the data to a CSV file
data.to_csv('synthetic_data.csv', index=False)