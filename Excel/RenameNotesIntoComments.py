import openpyxl

def notizen_in_kommentare_umwandeln(dateipfad):
    # Arbeitsmappe laden
    wb = openpyxl.load_workbook(dateipfad)
    ws = wb.active
    
    # Über alle Zellen im Arbeitsblatt iterieren
    for row in ws.iter_rows():
        for cell in row:
            # Prüfen, ob die Zelle eine Notiz hat
            if cell.comment:
                # Notiztext in Kommentar umwandeln
                text = cell.comment.text
                cell.comment = openpyxl.comments.Comment(text, "Author")
    
    # Änderungen speichern
    wb.save(dateipfad)

# Beispielaufruf
dateipfad = 'Ihre_Datei.xlsx'
notizen_in_kommentare_umwandeln(dateipfad)
