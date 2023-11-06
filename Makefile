up-system:
	docker-compose -f docker-compose.yaml up
	
down-system:
	docker-compose -f docker-compose.yaml down
	
up-system-local:
	docker-compose -f docker-compose-local.yaml up
	
down-system-local:
	docker-compose -f docker-compose-local.yaml down