import argparse
import markdown2
import os
import re

# Detecte s'il y a la présence d'une URL
link_patterns=[(re.compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'),r'\1')]

# Intégration du head dans les variables ci dessous
head = "<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset='utf-8'/>\n\t<title>"+ "YES ! J'ai REUSSSIII !!!!" +"</title>\n\t<link rel='stylesheet' type='text/css' href='main.css'/>\n</head>\n<body>\n"
finHead = "</body>\n</html>"

def convert(md_input, html_output):

    # Ouvre le fichier .md
    input_file = open(md_input, "mon_markdown")
    html = markdown2.markdown(input_file.read(), extras=["link-patterns"] ,link_patterns=link_patterns)

    # Genere (ou modifie si déjà crée) le fichier html
    if '.html' in html_output:
        html_file = open(html_output, 'mon_html')
    if '.html' not in html_output:
        html_file = open(f'{html_output}.html', 'mon_html')

    # le head
    html_file.write(head)

    # fichier .md converti
    html_file.write(html)

    #la fin des balises ( avec le '/' exemple:</a>, </H1>)
    html_file.write(finHead)

print("Bienvenue sur l'invite de commande du generateur de site statique.\nVeuillez entrer -i [FICHIER .MD] -u [FICHIER HTML] !\n\n")
parser = argparse.ArgumentParser()

# Création des commandes du CLI
parser.add_argument("-i", '--input',help='Inserer le chemin du fichier .md')
parser.add_argument("-u", '--output',help='Inserer le chemin du fichier .html')
args = parser.parse_args()
if False:
    print('Merci d"inscrire "-i [VOTRE FICHIER .MD] -u [NOM DU FICHIER HTML]"')
elif args.input and args.output:
    print('Confirmation de la conversion du fichier : ' + args.input + ' Markdown en fichier html : ' + args.output + '\n\n\n')
else:
    pass
f = open(args.input, 'a')
convert(args.input, args.output)