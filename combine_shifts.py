import os
import pandas as pd
from pathlib import Path
from charset_normalizer import from_path

base_dir = Path("shifts_by_day")
all_rows = []

for day_folder in base_dir.iterdir():
    if day_folder.is_dir():
        for file in day_folder.glob("*_shifts.txt"):
            # 🔍 Detect file encoding
            detected = from_path(file).best()
            encoding = detected.encoding if detected else "utf-8"

            with open(file, "r", encoding=encoding, errors="ignore") as f:
                lines = f.readlines()

            data_lines = [line.strip() for line in lines if line.strip().startswith("SH-")]

            for line in data_lines:
                parts = [x.strip() for x in line.split(",")]
                if len(parts) == 3:
                    shift_id, emp_id, hours = parts
                    hours = hours.replace("hrs", "").strip()
                    all_rows.append({
                        "Date": day_folder.name,
                        "ShiftID": shift_id,
                        "EmployeeID": emp_id,
                        "Hours_Worked": hours
                    })

df = pd.DataFrame(all_rows)
df.to_csv("all_shifts.csv", index=False, encoding="utf-8")
print(f"✅ Combined {len(df)} shifts into all_shifts.csv")
