while True :
   a = int( input(" Entrez un nombre : "));
   b = int( input( "Entrez un autre nombre : "));
   print(" Choisissez parmis ces opération : add, mult, div, sous.");
   type_calcul = input("Quel calcul souhaitez-vous faire : ").lower( )

   # Affichage normal
   if type_calcul == "add" :
      resultat = a + b
      print("Le résultat de l'addition de",a,"avec",b,"est égale à",resultat,);    
   elif type_calcul == "mult" :
      resultat = a * b
      print("Le résultat de la multiplication de",a,"avec",b,"est égale à",resultat); 

   # Affichage avec f-string
   elif type_calcul == "div" :
      if b != 0 :
         resultat = a / b
         print(f"Le résultat de la division de {a} avec {b} est égale à {resultat}");   
      else :
         print("La division de",a,"par",b,"est impossible.")
   elif type_calcul == "sous" :
      resultat = a - b
      print(f" Le résultat de la soustraction de {a} avec {b} est égale à {resultat}");
   else :
      print(" Vous n'avez choisie aucune des opérations mentionnées.");
   
   continuer = input ("Souyaitez vous continuer ? oui/non : ").lower( )
   if continuer == "non" :
      break

