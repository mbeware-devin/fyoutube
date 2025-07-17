cp subscriptions.md subscriptions.md.$( date +%Y%m%d-%H%M%S ).bak
grep -oP 'https://www\.youtube\.com/@[\w\-]+' YouTube.html | sort -u > subscriptions.md 
