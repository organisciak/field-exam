# Convert Google's zipped csv files to year-by-year
# Usage:
# ./ngram.sh IN START END OUT
#	IN - folder where the zip files are kept. This script reads all of them
#	START - First year to process
#	END - Last year to process
# 	OUT - Output folder.
# e.g.
# 	./ngram.sh ~/Downloads 1789 2009 year

IN=$1
START=$2
END=$3
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OUT=$DIR/$4

for z in $(find $IN -name "*.zip") 
do 
	unzip -p $z > $z.temp
	for i in $(seq $START $END) 
	do	
		if [ "$i" = "$START" ] 
		then
			>"$OUT/$i.gz"
		fi
		echo "$z for $i"
		grep -P "\t$i\t" $z.temp | gzip >> "$OUT/$i.gz"
	done
	rm $z.temp
done
