import prettytable

table = prettytable.PrettyTable()
table.field_names = ["Pokemon Name", "Type"]

table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmandar", "Fire"],
    ]
)

table.align = "l"
print(table)