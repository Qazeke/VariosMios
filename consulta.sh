read -p "Teclee el directorio que quiere consultar: " ruta

echo "ruta : $ruta"
if [ -z $ruta ];
	then
	echo "$(pwd)"

	elif [ -d "$ruta" ];
	then
		cd $ruta;
    		for i in `ls *.txt`; 
     		do 
				doing=true;
				while [ "$doing" = true ];
				do 
				read -p "¿Quieres leer el archivo $i? [S/n] " option
				if [ "$option" = "si" ] || [ "$option" = "s" ] || [ "$option" = "SI" ] || [ "$option" = "S" ]; then
					tail $i 
					echo ""
					doing=false
				elif [ "$option" = "no" ] || [ "$option" = "n" ] || [ "$option" = "NO" ] || [ "$option" = "N" ]; then
					doing=false
				elif [ "$option" = "q" ];
					then 
					exit 1;	
				else
					echo "respuesta no reconocida"
				fi
			done	
			doing=false	
		done
		fi		 	      