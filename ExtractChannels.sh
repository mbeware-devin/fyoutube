touch $2
cp $2 $2.$( date +%Y%m%d-%H%M%S ).bak
grep -oP 'https://www\.youtube\.com/@[\w\-]+' $1 | sort -u > $2 
