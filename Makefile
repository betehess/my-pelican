deploy_repo_url = git@github.com:jderuere/jderuere.github.io.git

docker-build:
	docker build -t jderuere/pelican .
	mkdir website/content
	mkdir website/output
docker-kill:
	docker stop pelican
	docker rm pelican

docker-run:
	docker run --name="pelican" -d -v $(CURDIR)/website:/srv/pelican-website -p 8000:8000 jderuere/pelican

docker-bash:
	docker run --name="pelican" -i -t -v $(CURDIR)/website:/srv/pelican-website -p 8000:8000 jderuere/pelican /bin/bash
 
pelican-github-user-page: 
	docker run -d -v $(CURDIR)/website:/srv/pelican-website jderuere/pelican ghp-import output
	git push $(deploy_repo_url) gh-pages:master

pelican-github-project-page:
	docker run -i -t -v $(CURDIR)/website:/srv/pelican-website jderuere/pelican make github
