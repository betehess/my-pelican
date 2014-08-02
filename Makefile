deploy_repo_url = @@@

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

#pelican-github-user-page: 
#	docker run -d -v $(CURDIR)/website:/srv/pelican-website betehess/pelican ghp-import output
#	git push $(deploy_repo_url) gh-pages:master

pelican-github-project-page:
	docker run -i -t -v $(CURDIR)/website:/srv/pelican-website betehess/pelican make github
