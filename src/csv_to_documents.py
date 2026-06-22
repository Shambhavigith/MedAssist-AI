import pandas as pd
from langchain_core.documents import Document


def load_clinical_documents():

    # Load CSVs
    description_df = pd.read_csv("Data/clinical/description.csv")
    medications_df = pd.read_csv("Data/clinical/medications.csv")
    diets_df = pd.read_csv("Data/clinical/diets.csv")
    workout_df = pd.read_csv("Data/clinical/workout.csv")
    precautions_df = pd.read_csv("Data/clinical/precautions.csv")

    # Merge all datasets
    master_df = description_df

    master_df = master_df.merge(
        medications_df,
        on="Disease",
        how="left"
    )

    master_df = master_df.merge(
        diets_df,
        on="Disease",
        how="left"
    )

    master_df = master_df.merge(
        workout_df,
        on="Disease",
        how="left"
    )

    master_df = master_df.merge(
        precautions_df,
        on="Disease",
        how="left"
    )

    documents = []

    for _, row in master_df.iterrows():

        content = f"""
Disease: {row['Disease']}

Description:
{row['Description']}
"""

        if pd.notna(row["Medication"]):
            content += f"""

Medication:
{row['Medication']}
"""

        if pd.notna(row["Diet"]):
            content += f"""

Diet:
{row['Diet']}
"""

        if pd.notna(row["Workouts"]):
            content += f"""

Workouts:
{row['Workouts']}
"""

        precautions = []

        for col in [
            "Precaution_1",
            "Precaution_2",
            "Precaution_3",
            "Precaution_4"
        ]:
            if pd.notna(row[col]):
                precautions.append(row[col])

        if precautions:
            content += "\n\nPrecautions:\n"
            for precaution in precautions:
                content += f"- {precaution}\n"

        doc = Document(
            page_content=content,
            metadata={
                "disease": row["Disease"],
                "source": "clinical_dataset"
            }
        )

        documents.append(doc)

    return documents


if __name__ == "__main__":

    clinical_docs = load_clinical_documents()

    print(f"Total Clinical Documents: {len(clinical_docs)}")

    print("\nSample Document:\n")
    print(clinical_docs[0].page_content)
