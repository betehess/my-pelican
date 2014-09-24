docker-build:
	docker build -t betehess/pelican .
	mkdir website/content
	mkdir website/output

docker-kill:
	docker stop pelican
	docker rm pelican

docker-run:
	docker run --name="pelican" -d -v $(CURDIR)/website:/srv/pelican-website -p 8000:8000 betehess/pelican

docker-bash:
	docker run --name="pelican" -i -t -v $(CURDIR)/website:/srv/pelican-website -p 8000:8000 betehess/pelican /bin/bash

docker-work:
	docker run --rm -i -t -v $(CURDIR)/website:/srv/pelican-website -u `whoami` -v /etc/passwd:/etc/passwd -v /etc/group:/etc/group -p 8000:8000 betehess/pelican /bin/bash

push-egp:
	rsync -avz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --progress --exclude feed website/output/ betehess@bertails.org:~/www-egp/

push-egp-feed:
	rsync -avz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --progress website/output/feed/ betehess@bertails.org:~/www-egp/feed/

push-www:
	rsync -avz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --progress --exclude feed website/output/ betehess@bertails.org:~/www/

push-feed:
	rsync -avz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --progress website/output/feed/ betehess@bertails.org:~/www/feed/
