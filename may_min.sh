read -p "Teclee el directorio que quiere cambiar de mayus a mins: " ruta

echo "ruta : $ruta";

	if [ "$ruta"==" " ]:
	then
     		for i in `ls -1`; do mv $i `echo $i |tr “[:upper:]” “[:lower:]”`; done
	elif [ -d "$ruta" ]:
	then
		cd $ruta;
                for i in `ls -1`; do mv $i `echo $i |tr “[:upper:]” “[:lower:]”`; done
	else
		exit 1;
	fi

