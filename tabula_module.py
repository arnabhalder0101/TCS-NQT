import tabula

# Read pdf into a list of DataFrame
dfs = tabula.read_pdf(r"C:\Users\arnab\OneDrive\Documents\Project\Project\example.pdf", pages='all')
print()