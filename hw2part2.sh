#!/bin/bash
argparser() {
    if [ $# -gt 0 ]; then
        echo "$1"
    else
        return 1
    fi
}

find_sum() {
    local fname="$1"
    local sum=0
    local linecount=0

    while IFS= read -r line || [[ -n "$line" ]]; do
        ((linecount++))
        if ((linecount % 3 != 0)); then
            continue
        fi

        firstdigit=$(echo "$line" | grep -o '[0-9]' | head -n1)
        lastdigit=$(echo "$line" | grep -o '[0-9]' | tail -n1)
        
        if [ -n "$firstdigit" ] && [ -n "$lastdigit" ]; then
            sum=$((sum + 10#${firstdigit}${lastdigit}))
        fi
    done < "$fname"

    echo "$sum"
}
# Main script
filename=$(argparser "$@")
if [ $? -eq 0 ]; then
    result=$(find_sum "$filename")
    echo "Sum: $result"
else
    echo "No arguments provided, please provide a filename to read. Usage: $0 filename"
fi