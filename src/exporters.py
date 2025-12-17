import pandas as pd
import os

def export_results(results):
    df = pd.DataFrame(results)
    os.makedirs("output", exist_ok=True)
    df.to_csv("output/prices.csv", index=False)
    df.to_excel("output/prices.xlsx", index=False)
