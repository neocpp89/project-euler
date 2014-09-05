./id32.py | grep True | awk '{ print $2 }' | sort | uniq | awk '{sum += $1} END{print sum}'
