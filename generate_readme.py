import json

with open("resources.json", "r") as f:
    data = json.load(f)

with open("README.md", "w", encoding="utf-8") as readme:
    readme.write("# 📚 Competitive Programming Resources\n\n")
    for category, items in data.items():
        readme.write(f"## 🔹 {category}\n\n")
        readme.write("| Topic | Resources | Code |\n")
        readme.write("|-------|-----------|------|\n")
        for item in items:
            res_list = "<br>".join([f"[{r['type']} - {r['title']}]({r['url']})" for r in item["resources"]])
            readme.write(f"| {item['topic']} | {res_list} | [Code]({item['code']}) |\n")
        readme.write("\n---\n\n")
