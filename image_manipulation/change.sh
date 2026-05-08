for file in * ; do
    mv -v "$file" "${file#*_}"
done

