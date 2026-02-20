import os
import xml.etree.ElementTree as ET
import pandas as pd

def parse_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()

    focus = root.findtext("Focus") or ""
    try:
        cui = root.find("FocusAnnotations/UMLS/CUIs/CUI").text
    except:
        cui = ""

    qa_pairs = []
    for qa in root.findall(".//QAPair"):
        q = qa.findtext("Question") or ""
        a = qa.findtext("Answer") or ""

        if q.strip() == "" or a.strip() == "":
            continue

        qa_pairs.append({
            "focus": focus,
            "cui": cui,
            "question": q.strip(),
            "answer": a.strip()
        })
    return qa_pairs


def load_medquad(root_folder="MedQuAD-master"):
    data = []

    for folder in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder)

        if os.path.isdir(folder_path):
            print(f"\n📁 Reading folder: {folder}")

            for file in os.listdir(folder_path):
                if file.endswith(".xml"):
                    xml_path = os.path.join(folder_path, file)
                    try:
                        records = parse_xml(xml_path)
                        data.extend(records)
                        print(f"  ✔ Loaded {file}")
                    except Exception as e:
                        print(f"  ✖ Error in {file}: {e}")

    df = pd.DataFrame(data)
    df.to_csv("medquad_final.csv", index=False)
    df.to_json("medquad_final.json", orient="records", indent=2)

    print("\n🎉 Done! Extracted:", len(df), "Q&A pairs.")

if __name__ == "__main__":
    load_medquad("MedQuAD-master")
