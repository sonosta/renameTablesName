from pathlib import Path

p = Path("C:\excelSolution\models")
for x in p.rglob("*"):
    print(x)